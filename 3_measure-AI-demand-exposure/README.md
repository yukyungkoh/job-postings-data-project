# Part 3: Construct AI Demand Exposure for Job Tasks

This part of the project measures how susceptible job tasks listed in new postings are to augmentation or replacement by AI (Called "AI Demand Exposure Score" in Revelio Labs' report "AI at Work: The State of AI Adoption in 2025") 

Below are the steps to construct the AI Demand Exposure Score. 

## 1: Extract tasks from job postings 
* Use a large language model (e.g., GPT-4 or Mistral via Ollama) to extract concise task statements from the job descriptions.
* Tasks should be action-oriented and exclude qualifications, benefits, or company information.

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
       \text{AI Demand Exposure Score} = \frac{\text{\# of tasks in posting that are AI-exposed}}{\text{Total \# of tasks in posting}}
   $$
  