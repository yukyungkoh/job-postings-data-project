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
OPENAI_API_KEY = "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"
#OPENAI_API_KEY = "(your API here!)"

# ---------------------------------------------------
# 2. Define number of postings, trial number, etc.
# ---------------------------------------------------
n_trial = 2
    # Due to OpenAI's daily request limits, it's not feasible to generate a large dataset
    # (e.g., 100,000 postings) in a single run. Instead, this script is executed daily
    # to generate a batch of 2,000 job postings at a time.

n_posting = 5000

# ----------------------------
# 3. Generate job sectors
# ----------------------------
sectors = [
    "data science", "software engineering",
    "consulting", "marketing", "finance", "legal",
    "sales", "healthcare", "education",
    "public sector", "retail"
]

# ----------------------------
# 4. Prompt builder
# ----------------------------
def build_prompt(sector):
    include_pay = random.choice([True, False])
    pay_note = "Include a realistic pay range if appropriate." if include_pay else "Do not mention pay."

    prompt = f"""
            Generate a realistic and varied U.S. job title for a role in the {sector} sector.
    	    For example, in the "{sector}" sector, consider a wide range of job types—e.g., client-facing, operational, strategy, support, compliance, leadership, and technical roles.
            Then write a corresponding online job posting.

            **Job Title Instructions**:
            - Most titles should **not** have seniority indicator. Many should just say things like "Data Analyst" or "Marketing Manager".
            - Vary structure and formatting: include tools, certifications, or location (e.g., "Remote", "Hybrid") **occasionally**, not always.
            - Use a mix of clean, formal titles and messier, casual, or acronym-heavy titles to simulate real-world postings on LinkedIn or Indeed.
    	    - Cover a wide range of functional areas within the sector. For example:
        		- In **finance**, don't just generate analyst roles—include investment banking, private equity, compliance, treasury, portfolio management, FP&A, controller, and client-facing finance roles.
       		     - In **software engineering**, vary between front-end, back-end, DevOps, infrastructure, QA, and managerial positions.
       		     - In **marketing**, include brand, growth, digital, product marketing, PR, and communications roles.
    	    Examples of varied titles in the {sector} sector might include:
    		  - Finance: Investment Banking Associate, M&A Analyst, Financial Analyst, Wealth Strategy Consultant, Financial Modeling Lead
    		  - Data Science: Data Scientist, AI Research Associate, ML Ops Engineer, Data Strategy Consultant, Predictive Analytics Specialist
    		  - Software Engineering: Software Engineer, SDE, SDE II, Software Development Manager

            **Job Posting Instructions**:
            - Vary the format: mix bullet points and paragraphs.
    	    - Vary the opening sentence structure. Avoid repeating phrases like "We are seeking" or "We are looking for." Use a mix of tones and openings, such as:
      		   - Describe the team or mission first.
      		   - Begin with a bold statement or challenge ("Ready to shape the future of...?")
      		   - Start with a benefit, opportunity, or company vision.
     		   - Use varied verbs (e.g., "Join", "Collaborate", "Help lead", "Support", "Drive", etc.).
            - Include responsibilities, qualifications, and location.
            - Randomly include or exclude DEI language and benefits.
            - {pay_note}
            - Introduce light "real-world noise": occasional grammatical quirks, inconsistent punctuation, typos, or abbreviation use (e.g., "exp." for experience, "req." for requirements). Not in every post — just enough to make the data look realistic.
            - Do not explicitly repeat the job title or sector name within the job description body. Instead, describe tasks and qualifications more naturally.

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
# 5. Async GPT call (Modified)
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
            {
                "role": "system",
                "content": (
                    "You are a recruiter generating synthetic U.S. job postings across varied roles within each job sector, "
                    "simulating the diversity found on real job boards like LinkedIn or Indeed. "
                    "Your outputs should reflect different job types, seniority levels, and tone variations commonly seen online."
                )
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": round(random.uniform(0.5, 0.8), 2),
        "max_tokens": 1500,
    }

    for attempt in range(retries):
        try:
            async with session.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data) as response:
                res = await response.json()
                if "choices" in res and res["choices"]:
                    content = res["choices"][0]["message"]["content"].strip()
                    if "### Job Title" in content and "### Job Posting" in content:
                        parts = content.split("### Job Posting")
                        title = parts[0].replace("### Job Title", "").strip()
                        text = parts[1].strip()
                        return title, text, sector
                else:
                    print(f"⚠️ Invalid response (no 'choices'): {res}")
        except Exception as e:
            print(f"❌ Error on attempt {attempt + 1} for sector {sector}: {e}")

        await asyncio.sleep(2 * (attempt + 1))

    return None, None, sector

# ----------------------------
# 6. Main async runner (Modified)
# ----------------------------
async def main():
    output_file = f"../data/synthetic_job_postings_{n_trial}.csv"
    batch_size = 10
    await asyncio.sleep(3)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["job_title", "posting_text", "sector"])  # ← Added "sector"

        async with aiohttp.ClientSession() as session:
            for i in range(0, n_posting, batch_size):
                current_batch = [random.choice(sectors) for _ in range(batch_size)]
                tasks = [generate_posting(session, sector) for sector in current_batch]
                results = await asyncio.gather(*tasks)

                for j, (title, text, sector) in enumerate(results):
                    if title and text:
                        writer.writerow([title, text, sector])  # ← Include sector
                        print(f"✅ {i + j + 1}/{n_posting} - {title}")
                    else:
                        print(f"⚠️ Skipped one due to error or formatting.")
                await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())