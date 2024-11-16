 TODO импортировать необходимые молули
import csv, json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as src_csv:
        src_csv = [i for i in csv.DictReader(src_csv, delimiter = ",", lineterminator = '\n')]
        json_data = json.dumps(src_csv, indent = 4)

    with open(OUTPUT_FILENAME, "w") as dst:
        dst_json = dst.write(json_data)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
