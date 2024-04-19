# schema demo

Small demo to validate a python dict, json, yaml, xml and ini with the same schema.

## Usage

Run `./validate.py`:  

```bash
validated dict: {'foo': {'version': 1, 'blocks': {'block1': {'data': 'abcd'}}}}
validated json: {'foo': {'version': 1, 'blocks': {'block1': {'data': 'abcd'}}}}
validated yaml: {'foo': {'version': 1, 'blocks': {'block1': {'data': 'abcd'}}}}
validated  xml: {'foo': {'version': 1, 'blocks': {'block1': {'data': 'abcd'}}}}
validated  ini: {'foo': {'version': 1, 'blocks': {'block1': {'data': 'abcd'}}}}
```

## Links

* https://github.com/keleshev/schema
* https://github.com/martinblech/xmltodict
