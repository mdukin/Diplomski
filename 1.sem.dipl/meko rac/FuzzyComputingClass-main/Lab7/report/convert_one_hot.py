import sys


def convert_input(input_file, output_file):
    with open(input_file) as f:
        lines = f.readlines()

    class_mapping = {'class1': 1, 'class2': 2, 'class3': 3}
    converted_lines = []
    for line in lines:
        x, y, class1, class2, class3 = line.strip().split()
        class_label = class_mapping['class1'] if class1 == '1' else (
            class_mapping['class2'] if class2 == '1' else class_mapping['class3'])
        converted_lines.append(f'{x} {y} {class_label}\n')

    with open(output_file, 'w') as f:
        f.writelines(converted_lines)

    print(f'File converted successfully. Output written to {output_file}')


input_file = sys.argv[1]
output_file = sys.argv[2]
convert_input(input_file, output_file)
