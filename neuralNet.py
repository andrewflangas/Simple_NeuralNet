import numpy as np 

def sigmoid(x):
	return 1/(1 + np.exp(-x))

def sigmoid_derivative(x):
	return x*(1 - x)

class NeuralNetwork:
	def __init__(self, x, y):
		self.input = x 
		self.weights1 = np.random.rand(self.input.shape[1], 4)
		self.weights2 = np.random.rand(4,1)
		self.y = y
		self.output = np.zeros(y.shape)

	def feedforward(self):
		self.layer1 = sigmoid(np.dot(self.input, self.weights1))
		self.output = sigmoid(np.dot(self.layer1, self.weights2))

	def backprop(self):
		# error calculation
		error = self.y - self.output

		# multiply error by the slope of the sigmoid at the values in layer1
		d_weights2 = np.dot(self.layer1.T, (2*error*sigmoid_derivative(self.output)))
		d_weights1 = np.dot(self.input.T, (np.dot(2 * error * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

    	# update the weights with the derivative (slope) of the loss function
		self.weights1 += d_weights1
		self.weights2 += d_weights2

if __name__ == "__main__":
	X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
	y = np.array([[0], [1], [1], [0]])
	nn = NeuralNetwork(X, y)

	# Train the neural network
	for i in range(1500):
		nn.feedforward()
		nn.backprop()

	# Test the neural network with a new input
	test = np.array([1, 0, 0])
	test = test.reshape(1, 3)
	nn.input = test
	nn.feedforward()
	print("Output: ", nn.output)