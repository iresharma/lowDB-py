# LowDB-py

Heavy inspired from lowDb a node package

[typicode/lowdb](https://github.com/typicode/lowdb#api)

## Why ??

Not every project requires a full on database with proper dbm and you requiring to write a db module, sometiems all you want is a basic storage for your Proof of concept or for the project where you are something very new and don't want to focus on database functions.

## Solution

A simple JSON file with a wrapper sdk to handle basic operations locally to a file, which can later be exported to Firestore or mongodb directly.



### To build and install the project
```bash
# Install package building tools
python3 -m pip install setuptools wheel

# Build the project
python3 -m setup.py sdist bdist_wheel

# Install the project to your local machine
python3 -m pip install -e .
```