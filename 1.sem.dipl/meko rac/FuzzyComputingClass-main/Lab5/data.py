import math
import os
import re
from enum import Enum
from statistics import mean

symbols_path = './symbols'


def clear_symbols():
    files = os.listdir(symbols_path)

    for file in files:
        os.remove(os.path.join(symbols_path, file))

    print('All stored symbols cleared.')


def save_symbol(title, characters: list[list[tuple]]):
    with open(f'{symbols_path}/{title}.txt', 'w') as file:
        for character in characters:
            file.write(', '.join([str(item) for item in character]) + '\n')


def read_raw_symbols():
    symbols = {}

    files = os.listdir(symbols_path)
    for file in files:
        title = file.split('.')[0]
        symbols[title] = []

        with open(os.path.join(symbols_path, file), 'r') as f:
            lines = f.readlines()

            for line in lines:
                if line.strip():
                    symbols[title].append(
                        [tuple(map(int, re.sub(r'[() ]+', '', x).split(','))) for x in line.strip().split('), ')])

    return symbols


def center_character(character: list[tuple]):
    xs, ys = zip(*character)
    x_mean = mean(xs)
    y_mean = mean(ys)

    return [(x[0] - x_mean, x[1] - y_mean) for x in character]


def center_data(symbols: dict[str, list[list[tuple]]]):
    centered_symbols = {}

    for name, characters in symbols.items():
        centered_characters = []
        for character in characters:
            centered_characters.append(center_character(character))

        centered_symbols[name] = centered_characters

    return centered_symbols


def scale_character(character: list[tuple]):
    xs, ys = zip(*character)
    x_max = max(math.fabs(x) for x in xs)
    y_max = max(math.fabs(y) for y in ys)

    m = max(x_max, y_max)

    return [(x[0] / m, x[1] / m) for x in character]


def scale_data(symbols: dict[str, list[list[tuple]]]):
    scaled_symbols = {}

    for name, characters in symbols.items():
        scaled_characters = []
        for character in characters:
            scaled_characters.append(scale_character(character))

        scaled_symbols[name] = scaled_characters

    return scaled_symbols


def distance(point1: tuple, point2: tuple):
    (x1, y1) = point1
    (x2, y2) = point2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_gesture_length(points: list[tuple]):
    total_distance = 0
    for i in range(1, len(points)):
        point_distance = distance(points[i - 1], points[i])
        total_distance += point_distance
    return total_distance


def get_m_representative_points_of_character(m: int, points: list[tuple]):
    total_distance = get_gesture_length(points)
    distance_step = total_distance / (m - 1)

    representative_points = [points[0]]

    for i in range(1, m):
        prev_point = representative_points[-1]

        point_distance_to_last = [(math.fabs(distance(prev_point, x) - distance_step), x) for x in points[i:]]
        point_distance_to_last.sort(key=lambda x: x[0])

        if len(point_distance_to_last) == 0:
            new_point = representative_points[-1]
        else:
            new_point = point_distance_to_last[0][1]

        representative_points.append(new_point)

    return representative_points


def sample_data(m: int, symbols: dict[str, list[list[tuple]]]):
    sampled_data = {}

    for name, characters in symbols.items():
        sampled_character = []
        for character in characters:
            sampled_character.append(get_m_representative_points_of_character(m, character))

        sampled_data[name] = sampled_character

    return sampled_data


def prepare_dict_data(dataset: dict):
    dataset_array = []

    for key, array in dataset.items():
        for value in array:
            dataset_array.append((key, value))

    return dataset_array


class BatchSelection(Enum):
    BACKPROPAGATION = 1
    STOCHASTIC_BACKPROPAGATION = 2
    MINI_GROUP_BACKPROPAGATION = 3
