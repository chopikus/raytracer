#!/bin/bash
mypy src/test.py --check-untyped-defs && python3 -m unittest discover -s src/
