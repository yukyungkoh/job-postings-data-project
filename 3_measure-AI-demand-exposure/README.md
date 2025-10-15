# Part 3: Construct AI Demand Exposure for Job Tasks

This part of the project measures how susceptible job tasks listed in new postings are to augmentation or replacement by AI.

Below are the steps to construct the AI Demand Exposure Score. 

## Step 1: Extract tasks from job postings 
Currently, I use a **large language model** (specifically, Mistral via Ollama) to extract task statements from the job descriptions. While LLM does a good job in extracting tasks, there is an important caveat.

#### ⚠️ Caveats
- Task extraction using LLMs is **time-consuming** (e.g., ~5 hours for 2,000 postings).
- To scale to **millions of postings**, we need a more efficient approach.

#### ✅ Alternative: Rule-Based and ML-Based Task Parsing (No LLM) - ‼️Future To-Do‼️
Alternative methods for task extraction include:

* **Section-based parsing**  
   - Use regex to extract content under headers like "Responsibilities", "Duties", "Tasks".
   - Note that this only works for job postings without clear headers
   
* **Sentence segmentation and filtering**  
   - Split into sentences or bullet points using `nltk` or `spaCy`.  
   - Filter likely tasks using rules (e.g., starts with a verb) and a list of task-related verbs (from O*NET or curated sources).

* **Sentence-level classification**  
   - Use a classifier trained on LLM-labeled training data to identify whether a sentence describes a task.


## Step 2: Map tasks to standardized activities 
* Auto-cluster the extracted tasks, using sentence embeddings and clustering
* Each cluster represents a generalized **activity type**.

## Step 3: Classify Activities as AI-Augmentable or Not
* Use GPT to label whether each activity is AI-exposed.
* For example, ask:  
  *“Can this task be automated or enhanced by artificial intelligence?”*
  
## Step 4: Compute the AI Demand Exposure Score
* Compute the score per job posting

$$
\text{AI Demand Exposure Score} = \frac{\text{Number of AI-exposed tasks}}{\text{Total number of tasks}}
$$