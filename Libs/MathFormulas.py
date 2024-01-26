#lets start with the mathematical formulas 
#mean square error method 
import numpy as np

#predictions
predictions = np.array([1,1,1,1,1,1])
# print(predictions)

#labels given for supervised learning 
labels = np.array([1,1,2,3,6,4])
# print(labels)


#formula to check the error between labeled data and the prediction data
error = (1/6) * np.sum(np.square(predictions - labels))
print(error)