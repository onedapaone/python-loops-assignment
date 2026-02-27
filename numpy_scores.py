#Numpy Arrays & Operations
import numpy as np

# Task 1: Generate and Inspect the Data
np.random.seed(42)

scores = np.random.randint(50,101, size=(5,4))

print(scores)

print("3rd Student's 2nd Subject score: ", scores[2][1])
print("All scores of last 2 students:\n", scores[-2:])
print("First 3 students' 2nd and 3rd subject scores:\n", scores[:3,1:3])


#Task-2: Aalyze with Broadacasting
subjects_mean = scores.mean(axis=0).round(2)
print(f"Average score for each subject: {subjects_mean}")

curve = ([5,3,7,2])
curved_scores = (scores + curve).clip(max=100)
print("Curved Scores:\n", curved_scores)

highest_scores = curved_scores.max(axis=1)
print("Best subject score for each student: ", highest_scores)

#Task-3: Normalize and Identify
normalized_scores = (curved_scores - curved_scores.min()) / (curved_scores.max() - curved_scores.min())
print("Normalized Scores:\n", normalized_scores)

highest_value = normalized_scores.max()
Index_of_highest = np.where(normalized_scores == highest_value)

print(f"Highest value: {highest_value:.2f}")
print(f"Highest value student index: {Index_of_highest[0]}")
print(f"Highest value subject index: {Index_of_highest[1]}")

#Extracting curved scores above 90 into 1D array using boolean masking
high_scores_mask = curved_scores > 90
high_scores = curved_scores[high_scores_mask]
#print(high_scores_mask)
print("Curved scores above 90: ", high_scores)