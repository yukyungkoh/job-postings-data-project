# Part 1: Categorize Jobs

This part of the project explores multiple approaches to classify jobs extracted from job postings into broader occupational categories. Job classification is a key step in analyzing the labor market. 

Although job category labels are known by design -- assigned during the LLM-based generation of synthetic job postings ([details here](https://github.com/yukyungkoh/job-postings-data-project/tree/main/0_generate-synthetic-job-postings)) -- they are treated as unknown here to demonstrate how the classification techniques can be applied in practice. 

I implement three different methods, each documented in a separate Jupyter notebook within this folder.

## 1: Rule-Based Classification (Regex Matching) - [Click here](https://github.com/yukyungkoh/job-postings-data-project/blob/main/1_categorize-jobs/1_approach1-rule-based.ipynb)

This method relies on manually defined patterns (e.g., keywords or regular expressions) to assign job titles to categories such as "Data-related", "Software Development", or "Finance".

**✅ Advantages:**
- Simple and interpretable
- Easy to customize for specific categories
- Works well when category patterns are clear

**❌ Limitations:**
- Not scalable for large or evolving datasets
- Fragile to typos, variations, and edge cases
- Requires manual tuning of rules

## 2: Supervised Learning - [Click here](https://github.com/yukyungkoh/job-postings-data-project/blob/main/1_categorize-jobs/2_approach2-supervised.ipynb)

I train machine learning classifiers (e.g., logistic regression, Naive Bayes) on labeled examples of jobs to predict categories based on job posting contents.

**✅ Advantages:**
- More flexible than rule-based approaches
- Can generalize to unseen titles if trained well

**❌ Limitations:**
- Requires labeled training data
- May struggle with rare or ambiguous titles

## 3: Unsupervised Learning - [Click here](https://github.com/yukyungkoh/job-postings-data-project/blob/main/1_categorize-jobs/3_approach3-unsupervised.ipynb)

I use clustering and topic modeling (e.g., k-means, LDA) to group similar jobs without predefined labels, again using job posting contents.

**✅ Advantages:**
- No need for labeled data
- Can reveal latent structure or emerging job groups

**❌ Limitations:**
- Clusters may be noisy or hard to interpret
- Results can be sensitive to preprocessing choices

---

Each method provides complementary strengths. In this project, I use them all to compare performance and to better understand how different techniques can be applied to real-world job posting data.

