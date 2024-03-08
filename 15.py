import numpy as np
import matplotlib.pyplot as plt

exam_scores = np.random.normal(loc=75, scale=10, size=50)  # size is no of student 50 ,Mean=75, Standard Deviation=10

plt.hist(exam_scores, bins=15, edgecolor='black', alpha=0.7)
plt.title('Histogram of Exam Scores')
plt.xlabel('Exam Scores')
plt.ylabel('Frequency')
plt.show()
