import os

try:
    TOKEN = os.environ["AOC_SESSION"]
except KeyError:
    raise
