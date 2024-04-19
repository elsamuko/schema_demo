#!/usr/bin/env python3
# schema demo
# python3 -m pip install schema xmltodict

import json
import yaml
import xmltodict
import configparser

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

a_ini = """
[foo]
version=1

[foo.blocks.block1]
data=abcd
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


class IniParser(configparser.ConfigParser):
    """ parse ini as nested dict """

    def to_dict(self, s, v):
        if "." in s:
            k, r = s.split(".", maxsplit=1)
            return {k: self.to_dict(r, v)}
        else:
            return {s: v}

    def as_dict(self):
        d = {}
        for k, v in self._sections.items():
            sub = self.to_dict(k, v)
            first = list(sub.keys())[0]
            if first in d:
                d[first] |= sub[first]
            else:
                d |= sub
        return d


ini_parser = IniParser()
ini_parser.read_string(a_ini)
data = ini_parser.as_dict()
validated = schema.validate(data)
print(f"validated  ini: {validated}")
