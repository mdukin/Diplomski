import tkinter as tk
from tkinter import ttk

import data
from data import BatchSelection
from nn import NeuralNetwork

histogram_height = 200
histogram_width = 500


def draw_submit(event):
    # Get the current mouse position
    x, y = event.x, event.y

    # Add a point to the array of points
    points.append((x, y))

    # Draw a line from the previous point to the current point
    if len(points) > 1:
        canvas.create_line(points[-2], points[-1], fill="black")


def release_submit(event):
    # Save the current array of points
    characters.append(points.copy())

    # Clear the array of points
    points.clear()
    # Clear the canvas
    canvas.delete("all")


def draw_test(event):
    # Get the current mouse position
    x, y = event.x, event.y

    # Add a point to the array of points
    points_testing.append((x, y))

    # Draw a line from the previous point to the current point
    if len(points_testing) > 1:
        canvas_testing.create_line(points_testing[-2], points_testing[-1], fill="black")


def pair_predictions_labels(predictions):
    result = {}
    for label, value in zip(labels, predictions):
        result[label] = value
    return result


def clear_histogram():
    histogram.delete("all")


def release_test(event):
    if neural_network:

        centered_character = data.center_character(points_testing)
        scaled_character = data.scale_character(centered_character)
        m = int(m_field.get())

        final_character = data.get_m_representative_points_of_character(m, scaled_character)

        # noinspection PyUnresolvedReferences
        predictions = neural_network.predict_single_value(final_character)
        results = pair_predictions_labels(predictions)

        print(f'Predictions: {results}')
        clear_histogram()
        draw_histogram(results)
    else:
        print("Neural network not trained. Please train before testing.")

    # Clear the array of points
    points_testing.clear()
    # Clear the canvas
    canvas_testing.delete("all")


def check_symbol_text_entered(event):
    if submit_text_field.get():
        submit_button.config(state="normal")
    else:
        submit_button.config(state="disabled")


def submit_symbol():
    symbol_name = submit_text_field.get()

    data.save_symbol(symbol_name, characters)

    submit_button.config(state="disabled")
    submit_text_field.delete(0, tk.END)
    characters.clear()

    print(f'Submitted symbol {symbol_name}.')


def insert_default_values_properties():
    m_field.insert(0, "10")
    structure_field.insert(0, "20,10,5")
    learning_rate_field.insert(0, "0.01")
    iterations_field.insert(0, "10000")
    radio_selection.set(3)


def train_network():
    structure = structure_field.get()
    batch_selection = radio_selection.get()
    iterations = int(iterations_field.get())
    lr = float(learning_rate_field.get())

    structure = [int(x) for x in structure.split(',')]

    global neural_network
    neural_network = NeuralNetwork(structure, batch_selection)

    stored_data = data.read_raw_symbols()
    if not stored_data:
        print('No stored data please create some symbols')
        return

    centered_data = data.center_data(stored_data)
    scaled_data = data.scale_data(centered_data)
    m = int(m_field.get())

    final_dataset = data.sample_data(m, scaled_data)

    global labels
    labels = final_dataset.keys()

    neural_network.train(lr, iterations, final_dataset)
    print('Network trained.')


def draw_histogram(predictions: dict):
    # Calculate the width and height of each bar in the histogram
    bar_width = histogram_width / len(predictions)
    max_height = histogram_height - 20

    # Draw the histogram
    for i, (key, value) in enumerate(predictions.items()):
        x1 = i * bar_width
        y1 = max_height - (value * max_height)
        x2 = x1 + bar_width
        y2 = max_height
        histogram.create_rectangle(x1, y1, x2, y2, fill="blue")

        # Add a label below each bar
        x = x1 + (bar_width / 2)
        y = max_height + 10
        histogram.create_text(x, y, text=key, anchor="n")


if __name__ == '__main__':
    # Create the main window
    root = tk.Tk()
    root.title("NN Network")

    # Create a tabbed interface
    notebook = ttk.Notebook(root)

    # Create a tab called Input Data
    input_data_tab = ttk.Frame(notebook)
    notebook.add(input_data_tab, text="Input Data")

    # Create fields
    canvas = tk.Canvas(input_data_tab, width=500, height=500)
    submit_button = tk.Button(input_data_tab, text="Submit Symbol", state="disabled", command=submit_symbol)
    clear_symbols_button = tk.Button(input_data_tab, text="Clear Symbols", command=data.clear_symbols)
    submit_text_field = tk.Entry(input_data_tab)
    submit_text_field.bind("<Key>", check_symbol_text_entered)

    # Use the grid layout to arrange the widgets
    clear_symbols_button.grid(row=0, columnspan=2)
    canvas.grid(row=1, columnspan=2)
    submit_text_field.grid(row=2, column=0)
    submit_button.grid(row=2, column=1)

    # Bind the draw function to the left mouse button click and drag event
    canvas.bind("<B1-Motion>", draw_submit)
    # Bind the release function to the left mouse button release event
    canvas.bind("<ButtonRelease-1>", release_submit)

    # Create a tab called NN Properties
    nn_properties_tab = ttk.Frame(notebook)
    notebook.add(nn_properties_tab, text="NN Properties")

    # Create the fields
    m_field = tk.Entry(nn_properties_tab)
    m_title = tk.Label(nn_properties_tab, text="Significant points M:")
    structure_field = tk.Entry(nn_properties_tab)
    structure_title = tk.Label(nn_properties_tab, text="NN Structure:")
    learning_rate_field = tk.Entry(nn_properties_tab)
    learning_rate_title = tk.Label(nn_properties_tab, text="Learning rate:")
    iterations_field = tk.Entry(nn_properties_tab)
    iterations_title = tk.Label(nn_properties_tab, text="Iterations")

    radio_selection = tk.IntVar()
    tk.Radiobutton(nn_properties_tab, text="Backpropagation", variable=radio_selection,
                   value=BatchSelection.BACKPROPAGATION.value).grid(row=4)
    tk.Radiobutton(nn_properties_tab, text="Stochastic Backpropagation", variable=radio_selection,
                   value=BatchSelection.STOCHASTIC_BACKPROPAGATION.value).grid(row=5)
    tk.Radiobutton(nn_properties_tab, text="Mini-Batch Backpropagation", variable=radio_selection,
                   value=BatchSelection.MINI_GROUP_BACKPROPAGATION.value).grid(row=6)

    # Create train button
    train_button = tk.Button(nn_properties_tab, text="Train Neural Network", command=train_network)

    # Use the grid layout to arrange the widgets
    m_field.grid(row=0, column=1)
    m_title.grid(row=0, column=0)
    structure_field.grid(row=1, column=1)
    structure_title.grid(row=1, column=0)
    learning_rate_field.grid(row=2, column=1)
    learning_rate_title.grid(row=2, column=0)
    iterations_field.grid(row=3, column=1)
    iterations_title.grid(row=3, column=0)
    train_button.grid(row=7, columnspan=2)

    insert_default_values_properties()

    # Create a tab called NN Testing
    nn_testing_tab = ttk.Frame(notebook)
    notebook.add(nn_testing_tab, text="NN Testing")

    # Create fields
    canvas_testing = tk.Canvas(nn_testing_tab, width=500, height=300)
    histogram = tk.Canvas(nn_testing_tab, width=histogram_width, height=histogram_height)

    separator = ttk.Separator(nn_testing_tab, orient="horizontal")
    separator.place(x=0, y=300 + 2, width=histogram_width)

    # Use the grid layout to arrange the widgets
    canvas_testing.grid(row=0)
    histogram.grid(row=1)

    # Bind the draw function to the left mouse button click and drag event
    canvas_testing.bind("<B1-Motion>", draw_test)
    # Bind the release function to the left mouse button release event
    canvas_testing.bind("<ButtonRelease-1>", release_test)

    # Add the tabbed interface to the main window
    notebook.pack()

    # Create data fields
    points = []
    characters = []
    points_testing = []

    # Neural Network
    neural_network = None
    labels = []

    # Start the main event loop
    root.mainloop()
