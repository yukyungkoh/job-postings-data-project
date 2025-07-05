# Job Postings Data Project

This repository contains a collection of Jupyter notebooks and scripts aimed at learning how to apply **natural language processing (NLP)** and **large language models (LLMs)** to extract structured insights from messy, unstructured **job postings**. Using a sample of ~100,000 LinkedIn job ads, the project explores methods for leveraging job posting data to study labor market dynamics in real time


## 📁 Project Structure

This project is structured into following sections: 

### 🔷 Part 1: Categorize job titles 
I explore various NLP methods to classify job titles into categories, including:
* Rule-based approach
* Supervised learning methods (e.g., logistic regression, Naive Bayes)
* Unsupervised learning methods (e.g., k-means clustering and LDA)
  
Check out [here](https://github.com/yukyungkoh/job-postings-data-project/tree/main/1_categorize-job-titles). 

### 🔷 Part 2: Extract job skills and tasks
I extract job skills and tasks from each job posting text using various approaches, including:
* Matching to the list of job skills compiled by [Lightcast](https://lightcast.io/open-skills)
* Sentence embeddings
* LLM

Check out [here](https://github.com/yukyungkoh/job-postings-data-project/tree/main/2_extract-job-skills)

### 🔷 Part 3: Measure AI demand exposure using extracted tasks 
I measure AI demand exposure for each job task, how susceptible job tasks listed in new postings are to augmentation or replacement by AI

Check out [here](https://github.com/yukyungkoh/job-postings-data-project/tree/main/3_measure-AI-demand-exposure)