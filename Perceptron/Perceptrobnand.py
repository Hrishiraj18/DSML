import numpy as np

threshold = 1
learning_rate = 0.5

# Initialize the weight vector
w = np.array([1.2, 0.6])

# Define the AND gate training data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
expected_outputs = np.array([0, 0, 0, 1])

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
    user_input = input("Enter input values (e.g., 0 1): ").split()
    if len(user_input) != 2:
        break
    x = np.array([int(user_input[0]), int(user_input[1])])
    result = step_function(np.dot(w, x))
    print("Output:", result)