import numpy as np
#intialising the threshold value 
threshold =float(input("Enter the Threshold value : "))
#Entering the learning rate 
learning_rate = float(input("Enter the learning rate vale :"))
#Entering the value of the weights
w1=float(input("Enter the weight for input 1 : "))
w2=float(input("Enter the weight for input 2 : "))

w=np.array([w1,w2])

# Define the AND gate training data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
expected_outputs = np.array([0, 0, 0, 1])

#Providing step function 

# Define the step function
def step_function(x):
    return 1 if x >= threshold else 0


    # Main training loop
while True:
    all_correct = True
    for i in range(len(X)):
        x = X[i]
        expected_output = expected_outputs[i]
        
        # Calculate the weighted sum
        weighted_sum = np.dot(w, x)
        
        # Calculate the obtained output using the step function
        obtained_output = step_function(weighted_sum)
        
        # Update the weight vector if expected output and obtained output differ
        if expected_output != obtained_output:
            delta_w = learning_rate * (expected_output - obtained_output) * x
            w += delta_w
            all_correct = False
    
    # Break the loop if all training instances are correctly satisfied
    if all_correct:
        break

# Test the trained perceptron
print("Trained weights:", w)

# Test the AND gate with the trained perceptron
while True:
    input_1=int(input("Enter the input 1 : "))
    input_2=int(input("Enter the input 2 : "))
    list=[]
    list.append(input_1)
    list.append(input_2)
    if len(list)!=2:
        break
    x=np.array([input_1,input_2])
    result = step_function(np.dot(w, x))
    print("Output:", result)

