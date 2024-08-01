#!/bin/bash
mypy --enable-incomplete-feature=NewGenericSyntax . && python3 src/main.py
