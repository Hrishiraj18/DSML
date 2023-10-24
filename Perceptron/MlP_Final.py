# Import the NumPy library to work with arrays and mathematical functions
import numpy as np

# Define the sigmoid activation function
def sigmoid(z):
    """
    Compute the sigmoid of the input.

    Args:
    z (float or NumPy array): Input value(s) to calculate the sigmoid function for.

    Returns:
    float or NumPy array: Sigmoid of the input.
    """
    return 1 / (1 + np.exp(-z))

# Initialize neural network parameters
def initializeParameters(inputFeatures, neuronsInHiddenLayers, outputFeatures):
    """
    Initialize the neural network parameters with random values.

    Args:
    inputFeatures (int): Number of input features.
    neuronsInHiddenLayers (int): Number of neurons in the hidden layer.
    outputFeatures (int): Number of output features.

    Returns:
    dict: Dictionary containing initialized parameters, including weights and biases.
    """
    W1 = np.random.randn(neuronsInHiddenLayers, inputFeatures)
    b1 = np.zeros((neuronsInHiddenLayers, 1))
    W2 = np.random.randn(outputFeatures, neuronsInHiddenLayers)
    b2 = np.zeros((outputFeatures, 1))
    
    parameters = {"W1": W1, "b1": b1, "W2": W2, "b2": b2}
    return parameters

# Perform forward propagation through the neural network
def forwardPropagation(X, parameters):
    """
    Perform forward propagation through the neural network.

    Args:
    X (NumPy array): Input data.
    parameters (dict): Dictionary containing network parameters.

    Returns:
    NumPy array: Output of the neural network (predictions).
    dict: Cache containing intermediate values during forward propagation.
    """
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

# Neural network parameters
neuronsInHiddenLayers = 2  # number of hidden layer neurons
inputFeatures = X.shape[0]  # number of input features
outputFeatures = Y.shape[0]  # number of output features
parameters = initializeParameters(inputFeatures, neuronsInHiddenLayers, outputFeatures)

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
    """
    Get input values from the user for testing the trained model.

    Returns:
    NumPy array: User input as a NumPy array.
    """
    input_values = []
    for i in range(inputFeatures):
        value = float(input(f"Enter input value {i+1}: "))
        input_values.append(value)
    X_input = np.array(input_values).reshape(inputFeatures, 1)
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
