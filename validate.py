#!/usr/bin/env python3
# schema demo
# python3 -m pip install schema xmltodict

import json
import yaml
import xmltodict

from schema import Schema, And, Regex, Use

schema = Schema(
    {
        "foo":
        {
            "version": And(Use(int), lambda x: x > 0),
            "blocks": {
                Regex("^block\d+$"): {
                    "data": str
                }
            },
        }
    }
)

data = {
    "foo":
        {
            "version": 1,
            "blocks": {"block1": {"data": "abcd"}}
        }
}
a_json = """
{
    "foo": {
        "version": 1,
        "blocks": {
            "block1": {
                "data": "abcd"
            }
        }
    }
}
"""
a_yaml = """
foo:
  version: 1
  blocks:
    block1:
      data:
        abcd
"""
a_xml = """
<foo>
  <version>1</version>
  <blocks>
    <block1>
      <data>abcd</data>
    </block1>
  </blocks>
</foo>
"""

validated = schema.validate(data)
print(f"validated dict: {validated}")

data = json.loads(a_json)
validated = schema.validate(data)
print(f"validated json: {validated}")

data = yaml.safe_load(a_yaml)
validated = schema.validate(data)
print(f"validated yaml: {validated}")

data = xmltodict.parse(a_xml, dict_constructor=dict)
validated = schema.validate(data)
print(f"validated  xml: {validated}")
