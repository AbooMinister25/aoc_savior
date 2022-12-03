"""A helper library for writing advent of code solutions in Python."""

from aoc_savior.constants import TOKEN
from aoc_savior.errors import NoToken, PuzzleLocked
from aoc_savior.input import fetch_input

__VERSION__ = "0.0.0"
__all__ = ("TOKEN", "NoToken", "PuzzleLocked", "fetch_input")
