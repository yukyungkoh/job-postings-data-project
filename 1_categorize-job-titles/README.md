# Part 1: Categorize Job Titles

This part of the project explores multiple approaches to classify job titles extracted from job postings into broader occupational categories. Accurate title classification is a key step in analyzing labor market patterns, skill demands, and exposure to automation or AI.

I apply three different methods:


## 1: Rule-Based Classification (Regex Matching)

This method relies on manually defined patterns (e.g., keywords or regular expressions) to assign job titles to categories such as "Data-related", "Software Development", or "Finance".

**✅ Advantages:**
- Simple and interpretable
- Easy to customize for specific categories
- Works well when category patterns are clear

**❌ Limitations:**
- Not scalable for large or evolving datasets
- Fragile to typos, variations, and edge cases
- Requires manual tuning of rules

---

## 2: Supervised Learning

I train machine learning classifiers (e.g., logistic regression, Naive Bayes) on labeled examples of job titles to predict categories.

**✅ Advantages:**
- More flexible than rule-based approaches
- Can generalize to unseen titles if trained well
- Supports probabilistic classification

**❌ Limitations:**
- Requires labeled training data
- Performance depends heavily on feature engineering
- May struggle with rare or ambiguous titles

---

## 3: Unsupervised Learning

I use clustering and topic modeling (e.g., k-means, LDA) to group similar job titles without predefined labels.

**✅ Advantages:**
- No need for labeled data
- Can reveal latent structure or emerging job groups
- Useful for exploratory analysis

**❌ Limitations:**
- Hard to validate without ground truth
- Clusters may be noisy or hard to interpret
- Results can be sensitive to preprocessing choices

---

Each method provides complementary strengths. In this project, I use them all to compare performance and to better understand how different techniques can be applied to real-world job posting data.

