import os
import json
from dev_utils.data_ops import read_file, read_json

def test_read_file(tmpdir):
    p = tmpdir.join("test.txt")
    p.write("hello world")
    assert read_file(str(p)) == "hello world"

def test_read_json(tmpdir):
    p = tmpdir.join("test.json")
    p.write('{"key": "value"}')
    assert read_json(str(p)) == {"key": "value"}
