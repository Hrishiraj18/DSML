# Import the NumPy library to work with arrays and mathematical functions
import numpy as np

# Define the sigmoid activation function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Initialize neural network parameters manually
def initializeParameters():
    inputFeatures = int(input("Enter the number of input features: "))
    neuronsInHiddenLayers = int(input("Enter the number of neurons in the hidden layer: "))
    outputFeatures = int(input("Enter the number of output features: "))

    W1 = np.array([[float(input(f"Enter W1[{i}][{j}]: ")) for j in range(inputFeatures)] for i in range(neuronsInHiddenLayers)])
    b1 = np.array([[float(input(f"Enter b1[{i}][0]: ")) for i in range(neuronsInHiddenLayers)]])
    W2 = np.array([[float(input(f"Enter W2[{i}][{j}]: ")) for j in range(neuronsInHiddenLayers)] for i in range(outputFeatures)])
    b2 = np.array([[float(input(f"Enter b2[{i}][0]: ")) for i in range(outputFeatures)]])

    parameters = {"W1": W1, "b1": b1, "W2": W2, "b2": b2}
    return parameters

# Perform forward propagation through the neural network
def forwardPropagation(X, parameters):
    W1, b1, W2, b2 = parameters["W1"], parameters["b1"], parameters["W2"], parameters["b2"]

    Z1 = np.dot(W1, X) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)

    cache = {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}
    return A2, cache

# XOR input and output data
X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])  # XOR input
Y = np.array([[0, 1, 1, 0]])  # XOR output

# Manually initialize neural network parameters
parameters = initializeParameters()

# Training parameters
epoch = 100000
learningRate = 0.01

# Create an array to store the loss values during training
losses = np.zeros((epoch, 1))

# Training the neural network
for i in range(epoch):
    A2, cache = forwardPropagation(X, parameters)

    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, cache["A1"].T) / X.shape[1]
    db2 = np.sum(dZ2, axis=1, keepdims=True) / X.shape[1]

    dZ1 = np.dot(parameters["W2"].T, dZ2) * (cache["A1"] * (1 - cache["A1"]))
    dW1 = np.dot(dZ1, X.T) / X.shape[1]
    db1 = np.sum(dZ1, axis=1, keepdims=True) / X.shape[1]

    # Update the network parameters using gradient descent
    parameters["W1"] -= learningRate * dW1
    parameters["b1"] -= learningRate * db1
    parameters["W2"] -= learningRate * dW2
    parameters["b2"] -= learningRate * db2

    # Compute and store the loss
    loss = -np.sum(np.multiply(Y, np.log(A2)) + np.multiply(1 - Y, np.log(1 - A2)))/X.shape[1]
    losses[i, 0] = loss

# Function to get user input
def get_user_input():
    input_values = []
    for i in range(X.shape[0]):
        value = float(input(f"Enter input value {i+1}: "))
        input_values.append(value)
    X_input = np.array(input_values).reshape(X.shape[0], 1)
    return X_input

# Testing the trained model with manual input
while True:
    X_test = get_user_input()
    A2, _ = forwardPropagation(X_test, parameters)
    prediction = (A2 > 0.5).astype(int)[0, 0]
    print("Predicted Output:", prediction)

    cont = input("Do you want to continue (yes/no)? ").lower()
    if cont != "yes":
        break
