import requests

from aoc_savior.constants import TOKEN
from aoc_savior.errors import PuzzleLocked


def fetch_input(year: int, day: int) -> str:
    """Fetch the input for the given year and day.

    Args:
        year (int): The year to fetch the puzzle from.
        day (int): The day for the puzzle.

    Returns:
        str: The raw input.
    """
    cookies = {"session": TOKEN}
    res = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies)

    if res.status_code == 404:
        raise PuzzleLocked("This puzzle is locked, or doesn't exist for the provided year and day.")
    else:
        res.raise_for_status()

    return res.content.decode()
