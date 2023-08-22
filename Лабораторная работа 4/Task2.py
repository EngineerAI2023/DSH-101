# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open('INPUT_FILENAME', 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if row[0]:
                data = {}
                for column_name in row:
                    data[column_name] = row[column_name]
                json_string = json.dumps(data, ensure_ascii=False)
                json_string += '\n' * 4
                print(json_string)
            else:
                print("{}".format(row[0]))

    # TODO считать содержимое csv файла
    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
