# Part 3: Construct AI Demand Exposure for Job Tasks

This part of the project measures how susceptible job tasks listed in new postings are to augmentation or replacement by AI (Called "AI Demand Exposure Score" in Revelio Labs' report "AI at Work: The State of AI Adoption in 2025") 

Below are the steps to construct the AI Demand Exposure Score. 

## 1: Extract tasks from job postings 
* Use a **large language model** (here, Mistral via Ollama) to extract concise task statements from the job descriptions.
* Tasks should be action-oriented and exclude qualifications, benefits, or company information.

#### ⚠️ Caveats
- Task extraction using LLMs is **time-consuming** (e.g., ~5 hours for 2,000 postings).
- To scale to **millions of postings**, we need a more efficient approach.

#### ✅ Alternative: Rule-Based and ML-Based Task Parsing (No LLM)
Consider using:

1. **Section-based parsing**  
   - Use regex to extract content under headers like "Responsibilities", "Duties", "Tasks".
   
2. **Sentence segmentation and filtering**  
   - Split into sentences or bullet points using `nltk` or `spaCy`.  
   - Filter likely tasks using rules (e.g., starts with a verb) and a list of task-related verbs (from O*NET or curated sources).

3. **Sentence-level classification**  
   - Use a classifier trained on LLM-labeled training data to identify whether a sentence describes a task.

This is one of my future to-do's. 

## 2: Map tasks to a taxonomy 
* Auto-cluster the extracted tasks, using sentence embeddings and clustering
* Each cluster represents a generalized **activity type**.

## 3: Classify Activities as AI-Augmentable or Not
* Use GPT to label whether each activity is AI-exposed.
* For example, ask:  
  *“Can this task be automated or enhanced by artificial intelligence?”*
  
## 4: Compute the AI Demand Exposure Score
* Compute the score per job posting

$$
\text{AI Demand Exposure Score} = \frac{\text{Number of AI-exposed tasks}}{\text{Total number of tasks}}
$$