# Synthetic U.S. Job Posting Data Generation

This folder contains code and documentation for generating large-scale **synthetic job posting data** using OpenAI's **GPT-4o** model. The goal is to simulate realistic job titles and descriptions across a wide range of industries, with variation in job content, seniority, formatting, and style — mimicking the richness and messiness of real-world job postings.


## Why Generate Synthetic Job Postings?

* Accessing representative job posting data from platforms like LinkedIn is difficult due to strict licensing restrictions and proprietary limitations. 
* In contrast, **synthetic** job postings generated using **large language models (LLMs)** are safe to use, fully customizable, and easily scalable -making them an ideal resource for learning and experimentation with job posting data.

✅ **Advantages:**

* Legal to use and share publicly
* Scalable to as many postings as I want 
* Customizable for various sectors, structures, or use cases
* Useful for building and testing NLP pipelines and job classification models

❌ **Limitations:**

* Synthetic data — not suitable for labor market research or policy analysis
* Requires API usage, which incurs generation **costs**
    * 💰 Cost depends on model choice, prompt length, and volume
* May contain repetitive or overly clean language
* Lacks the noise, inconsistency, and variability of real-world postings

## How I Generated Synthetic Job Postings

I use OpenAI’s **GPT-4o-mini** to generate synthetic job postings that include several features that mimic real-world job postings:
- **Diverse job sectors** (e.g. healthcare, tech, education, retail)
- **Natural variation in job titles**: includes/omits seniority, certifications, tools, location, and abbreviations (e.g., “Sr.” vs. “Senior”)
- **Structured and unstructured content**: mix of paragraphs and bullet points
- **Realistic seniority-based job content**:
  - Entry-level: minimal experience, welcoming tone
  - Mid-level: 2–5 years experience, broader responsibilities
  - Senior-level: leadership duties, advanced qualifications
- **Random inclusion of**: DEI language, compensation info, and benefits
