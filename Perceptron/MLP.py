import numpy as np

# Sigmoid Function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Initialization of the neural network parameters
def initializeParameters(inputFeatures, neuronsInHiddenLayers, outputFeatures):
    W1 = np.random.randn(neuronsInHiddenLayers, inputFeatures)
    b1 = np.zeros((neuronsInHiddenLayers, 1))
    W2 = np.random.randn(outputFeatures, neuronsInHiddenLayers)
    b2 = np.zeros((outputFeatures, 1))
    
    parameters = {"W1": W1, "b1": b1, "W2": W2, "b2": b2}
    return parameters

# Forward Propagation
def forwardPropagation(X, parameters):
    W1, b1, W2, b2 = parameters["W1"], parameters["b1"], parameters["W2"], parameters["b2"]

    Z1 = np.dot(W1, X) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)

    cache = (Z1, A1, W1, b1, Z2, A2, W2, b2)
    return A2, cache

# Model to learn the XOR truth table 
X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]]) # XOR input
Y = np.array([[0, 1, 1, 0]]) # XOR output

# Define model parameters
neuronsInHiddenLayers = 2 # number of hidden layer neurons (2)
inputFeatures = X.shape[0] # number of input features (2)
outputFeatures = Y.shape[0] # number of output features (1)
parameters = initializeParameters(inputFeatures, neuronsInHiddenLayers, outputFeatures)
epoch = 100000
learningRate = 0.01

losses = np.zeros((epoch, 1))

for i in range(epoch):
    A2, cache = forwardPropagation(X, parameters)
    
    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, cache[1].T) / X.shape[1]
    db2 = np.sum(dZ2, axis=1, keepdims=True) / X.shape[1]

    dZ1 = np.dot(parameters["W2"].T, dZ2) * (cache[1] * (1 - cache[1]))
    dW1 = np.dot(dZ1, X.T) / X.shape[1]
    db1 = np.sum(dZ1, axis=1, keepdims=True) / X.shape[1]
    
    parameters["W1"] -= learningRate * dW1
    parameters["b1"] -= learningRate * db1
    parameters["W2"] -= learningRate * dW2
    parameters["b2"] -= learningRate * db2
    
    loss = -np.sum(np.multiply(Y, np.log(A2)) + np.multiply(1 - Y, np.log(1 - A2)))/X.shape[1]
    losses[i, 0] = loss

# Testing
X_test = X  # Use the same input for testing
A2, _ = forwardPropagation(X_test, parameters)
predictions = (A2 > 0.5) * 1
print("Predicted XOR Output:", predictions)
