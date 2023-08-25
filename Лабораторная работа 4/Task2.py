# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open('input.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if row[0]:
                data = {}
                for column_name in row:
                    data[column_name] = row[column_name]
                json_string = json.dumps(list(data), indent=4)
                print(json_string)
            else:
                print("{}".format(row[0]))

    # TODO считать содержимое csv файла
    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open('output.json') as output_f:
        for line in output_f:
            print(line, end="")