# Prettify JSON

A simple JSON pretty printer.

# How to launch


Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>

{
    "$schema": "http://json-schema.org/draft-06/schema#",
    "title": "Product",
    "description": "A product from Acme's catalog",
    "type": "object",
    "properties": {
        "id": {
            "description": "The unique identifier for a product",
            "type": "integer"
        },
        "name": {
            "description": "Name of the product",
            "type": "string"
        },
        "price": {
            "type": "number",
            "exclusiveMinimum": 0
        }
    },
    "required": ["id", "name", "price"]
}
```

# Requirements

 - Python 3.5
 - Text data file with utf-8 encoding;

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
