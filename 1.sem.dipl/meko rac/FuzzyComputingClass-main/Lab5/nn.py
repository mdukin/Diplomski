import numpy as np

import data

zero_error = 1E-6
minibatch_size = 5


def single_sample_to_numpy(sample):
    return np.array(sample).flatten().reshape((1, -1))


def dataset_to_numpy(dataset: dict):
    labels, X = zip(*data.prepare_dict_data(dataset))

    y = one_hot_encode_labels(labels)

    return y, np.array(X).reshape(len(X), -1)


def one_hot_encode_labels(labels):
    # Get the unique set of labels
    unique_labels = list(dict.fromkeys(labels))

    # Create a dictionary mapping each label to a unique integer
    label_dict = {label: i for i, label in enumerate(unique_labels)}

    # Initialize the one-hot encoded array with all zeros
    one_hot = np.zeros((len(labels), len(unique_labels)))

    # Set the appropriate elements to 1
    for i, label in enumerate(labels):
        one_hot[i, label_dict[label]] = 1

    return one_hot


def convert_single_result_from_numpy(numpy_result):
    return numpy_result.flatten().tolist()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class NeuralNetwork:
    def __init__(self, layer_sizes, batch_selection: data.BatchSelection):
        self.num_layers = len(layer_sizes)
        self.layer_sizes = layer_sizes
        self.batch_selection = batch_selection

        self.weights = [np.random.randn(y, x) for x, y in zip(layer_sizes[:-1], layer_sizes[1:])]
        self.biases = [np.random.randn(y, 1) for y in layer_sizes[1:]]

    def train(self, learning_rate, num_epochs, dataset):
        y, X = dataset_to_numpy(dataset)

        num_batches = self.get_number_of_batches(len(y))
        input_batches = np.array_split(X, num_batches)
        target_batches = np.array_split(y, num_batches)

        for epoch in range(num_epochs):
            # Shuffle batches
            shuffle_indices = np.random.permutation(num_batches)
            input_batches = np.take(input_batches, shuffle_indices, axis=0)
            target_batches = np.take(target_batches, shuffle_indices, axis=0)

            for input_batch, target_batch in zip(input_batches, target_batches):
                self.backward_pass(input_batch, target_batch, learning_rate)

            mse_loss = np.mean((self.predict(X) - y.T) ** 2)
            print("Epoch {}: MSE loss = {}".format(epoch, mse_loss))

            if mse_loss < zero_error:
                break

    def predict_single_value(self, input_sample):
        input_sample = single_sample_to_numpy(input_sample)
        y_pred = self.forward_pass(input_sample)[-1]
        return convert_single_result_from_numpy(y_pred)

    def predict(self, input_batch):
        activations = self.forward_pass(input_batch)
        return activations[-1]

    def forward_pass(self, input_batch):
        activations = [input_batch.T]
        for i in range(self.num_layers - 1):
            z = np.dot(self.weights[i], activations[-1]) + self.biases[i]
            a = sigmoid(z)
            activations.append(a)
        return activations

    def backward_pass(self, X, y, learning_rate):
        activations = self.forward_pass(X)

        output_error = activations[-1] - y.T

        weight_errors = [output_error]
        for i in range(self.num_layers - 2, 0, -1):
            error = np.dot(self.weights[i].T, weight_errors[-1])
            weight_errors.append(error)

        weight_errors = weight_errors[::-1]

        for i in range(self.num_layers - 1):
            self.weights[i] -= learning_rate * np.dot(weight_errors[i], activations[i].T)
            self.biases[i] -= learning_rate * np.sum(weight_errors[i], axis=1, keepdims=True)

    def get_number_of_batches(self, size):
        if self.batch_selection == data.BatchSelection.BACKPROPAGATION.value:
            return 1
        elif self.batch_selection == data.BatchSelection.STOCHASTIC_BACKPROPAGATION.value:
            return size
        else:
            return
