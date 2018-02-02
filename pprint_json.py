
import sys
import json


def load_data(filepath):
    with open(filepath, 'r', encoding='cp1251') as file_reader:
        return file_reader.read()


def pretty_print_json(text_to_print):
    print(json.dumps(json.loads(text_to_print), indent=4, sort_keys=True))


if __name__ == '__main__':
    try:
        text_to_print = load_data(sys.argv[1])
        pretty_print_json(text_to_print)
    except (FileNotFoundError, IndexError, ValueError):
        sys.exit('File not found')
