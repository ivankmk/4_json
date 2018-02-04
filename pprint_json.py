
import sys
import json


def load_data(filepath):
    with open(filepath, 'r', encoding='cp1251') as file_reader:
        return file_reader.read()


def pretty_print_json(read_json):
    print(json.dumps(json.loads(read_json), indent=4, sort_keys=True))


if __name__ == '__main__':
    try:
        read_json = load_data(sys.argv[1])
        pretty_print_json(read_json)
    except (FileNotFoundError, IndexError):
        sys.exit('File not found')
    except (ValueError):
        sys.exit('Your file not in JSON format')
