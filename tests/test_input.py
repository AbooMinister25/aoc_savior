from aoc_savior import fetch_input


def test_input() -> None:
    raw_input = fetch_input(2020, 25)
    assert raw_input == "9033205\n9281649\n"
