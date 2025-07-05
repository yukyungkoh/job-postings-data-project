# Job Postings Data Project

This repository contains a collection of Jupyter notebooks and scripts aimed at learning how to apply **natural language processing (NLP)** and **large language models (LLMs)** to extract structured insights from messy, unstructured **job postings**. Using a sample of synthetic job posting, the project explores methods for leveraging job posting data to study the labor market. 


**Why Use Synthetic Job Postings?**

- Access to real job posting data from platforms like LinkedIn is limited due to licensing restrictions and proprietary constraints.
- **Synthetic job postings** generated with LLMs offer a practical alternative: they are safe to use, fully customizable, and scalable—making them ideal for experimentation and learning.
- You can explore how I generated the synthetic data in [this folder](https://github.com/yukyungkoh/job-postings-data-project/tree/main/0_generate-synthetic-job-postings).

The remainder of the project is organized into the following parts:

## 🔷 Part 1: Categorize Job Titles  
This section explores multiple NLP approaches for classifying job titles into categories, including:
- Rule-based methods
- Supervised learning (e.g., logistic regression, Naive Bayes)
- Unsupervised learning (e.g., k-means clustering, LDA topic modeling)

[Browse the notebook folder for Part 1](https://github.com/yukyungkoh/job-postings-data-project/tree/main/1_categorize-job-titles)


## 🔷 Part 2: Extract Job Skills and Tasks  
This section focuses on extracting job skills and task descriptions from job posting text using:
- Keyword matching to a curated skill list (from Lightcast)
- Sentence embeddings
- Large language models (LLMs)

[Browse the notebook folder for Part 2](https://github.com/yukyungkoh/job-postings-data-project/tree/main/2_extract-job-skills-and-tasks)


## 🔷 Part 3: Measure AI Demand Exposure  
This section estimates the **AI exposure** of job tasks -- i.e., how susceptible the listed tasks in job postings are to automation or augmentation by AI tools. It builds on task-level extraction to compute AI relevance scores.

[Browse the notebook folder for Part 3](https://github.com/yukyungkoh/job-postings-data-project/tree/main/3_measure-AI-demand-exposure)


---

**Author:** Yu Kyung Koh 

**Last updated:** July 4, 2025