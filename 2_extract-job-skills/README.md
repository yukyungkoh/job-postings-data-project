# Part 2: Extract job skills

This part of the project explores different approaches for extracting job-relevant skills from job posting texts. 

Each method is implemented in a separate Jupyter notebook and described below.


## 1: Explore Most Common Words in Job Postings

- This notebook conducts an **exploratory analysis** of the most frequently appearing words in job descriptions, grouped by job sector.
- The goal is to get a high-level sense of the language used across different types of postings.


## 2: Skill Extraction Using a Curated Skill List

- This notebook extracts job-relevant skills using a **curated list of standardized skills** provided by [Lightcast](https://lightcast.io/).
- The skill list includes thousands of technical, soft, and domain-specific skills.
- By matching the job description text to the predefined list, we can identify which skills are most frequently requested in each job category.


## 3: Skill Extraction Using LLMs

- This notebook applies a **large language model (LLM)** to extract skill mentions directly from job posting text.
- Specifically, I use the **Mistral model via Ollama**, a free and high-performing local LLM.
- To reduce redundancy and ensure consistency across extracted terms (e.g., “Microsoft Office” vs. “Microsoft Office Suite”), I apply a **harmonization process** that clusters semantically similar skills using:
  - **Sentence embeddings**
  - **Unsupervised clustering**
