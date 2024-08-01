#!/bin/bash
mypy src/test.py --enable-incomplete-feature=NewGenericSyntax --check-untyped-defs && python3 -m unittest discover -s src/
