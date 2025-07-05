import openai
import pandas as pd
import random
import time
import csv
import asyncio
import aiohttp

# ----------------------------
# 1. Set up your API key
# ----------------------------
OPENAI_API_KEY = "(your API here!)"

# ----------------------------
# 2. Define number of postings
# ----------------------------
n_posting = 10000

# ----------------------------
# 3. Generate job sectors
# ----------------------------
sectors = [
    "data science", "software engineering",
    "marketing", "finance", "legal", "sales",
    "healthcare", "education",
    "hospitality", "public sector", "retail"
]

# ----------------------------
# 4. Prompt builder
# ----------------------------
def build_prompt(sector):
    include_pay = random.choice([True, False])
    pay_note = "Include a realistic pay range if appropriate." if include_pay else "Do not mention pay."

    prompt = f"""
        Generate a realistic and varied U.S. job title for a role in the {sector} sector.
        Then write a corresponding online job posting.
        
        **Job Title Instructions**:
        - Vary the actual seniority level of the role (entry-level, mid-level, senior-level).
        - Some job titles should include a seniority indicator (e.g., "Junior", "Mid-Level", "Senior", "Sr.", "Jr."), but **most titles should not**. Many should just say things like "Data Analyst" or "Marketing Manager".
        - Vary structure and formatting: include tools, certifications, or location (e.g., "Remote", "Hybrid") **occasionally**, not always.
        - Use a mix of clean, formal titles and messier, casual, or acronym-heavy titles to simulate real-world postings on LinkedIn or Indeed.
        
        **Job Posting Instructions**:
        - Ensure the posting matches the implied seniority of the job title:
            - Entry-level: simple duties, minimal requirements.
            - Mid-level: 2–5 years experience, moderate complexity.
            - Senior-level: leadership, decision-making, advanced qualifications.
        - Do not mention seniority unless it is in the title.
        - Vary the format: mix bullet points and paragraphs.
        - Include responsibilities, qualifications, and location.
        - Randomly include or exclude DEI language and benefits.
        - {pay_note}
        
        **Format**:
        ### Job Title
        <your job title>
        
        ### Job Posting
        <your posting>
        
        **Instruction for format**
        Only use the ### Job Title and ### Job Posting headers once — at the top. 
        Do not repeat them or include any footer text.
        """.strip()

    return prompt.strip()

# ----------------------------
# 5. Async GPT call
# ----------------------------
async def generate_posting(session, sector, retries=3):
    prompt = build_prompt(sector)
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a recruiter generating synthetic job titles and realistic job postings for the U.S. market."},
            {"role": "user", "content": prompt}
        ],
        "temperature": round(random.uniform(0.5, 0.8), 2),
        "max_tokens": 550,
    }

    for attempt in range(retries):
        try:
            async with session.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data) as response:
                res = await response.json()

                # Check if response contains choices
                if "choices" in res and res["choices"]:
                    content = res["choices"][0]["message"]["content"].strip()
                    if "### Job Title" in content and "### Job Posting" in content:
                        parts = content.split("### Job Posting")
                        title = parts[0].replace("### Job Title", "").strip()
                        text = parts[1].strip()
                        return title, text
                else:
                    print(f"⚠️ Invalid response (no 'choices'): {res}")
        except Exception as e:
            print(f"❌ Error on attempt {attempt + 1} for sector {sector}: {e}")

        # Exponential backoff
        await asyncio.sleep(2 * (attempt + 1))

    return None, None

# ----------------------------
# 6. Main async runner
# ----------------------------
async def main():
    output_file = "../data/synthetic_job_postings.csv"
    batch_size = 10  # Number of concurrent requests
    await asyncio.sleep(3)  # Increase pause between batches

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["job_title", "posting_text"])

        async with aiohttp.ClientSession() as session:
            for i in range(0, n_posting, batch_size):
                current_batch = [random.choice(sectors) for _ in range(batch_size)]
                tasks = [generate_posting(session, sector) for sector in current_batch]
                results = await asyncio.gather(*tasks)
                for j, (title, text) in enumerate(results):
                    if title and text:
                        writer.writerow([title, text])
                        print(f"✅ {i + j + 1}/{n_posting} - {title}")
                    else:
                        print(f"⚠️ Skipped one due to error or formatting.")
                await asyncio.sleep(1)  # Slight pause between batches

if __name__ == "__main__":
    asyncio.run(main())