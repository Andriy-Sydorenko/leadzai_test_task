import pytest

from pagination import generate_pagination


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (4, 5, 1, 0, "1 ... 4 5"),
        (4, 10, 2, 2, "1 2 3 4 5 6 ... 9 10"),
        (1, 10, 2, 2, "1 2 3 ... 9 10"),
        (10, 10, 2, 2, "1 2 ... 8 9 10"),
        (6, 19, 3, 2, "1 2 3 4 5 6 7 8 ... 17 18 19"),
        (1, 8, 3, 1, "1 2 3 ... 6 7 8"),
        (4, 19, 3, 0, "1 2 3 4 ... 17 18 19"),
        (11, 14, 1, 1, "1 ... 10 11 12 ... 14"),
        (15, 16, 3, 1, "1 2 3 ... 14 15 16"),

        (1, 1, 2, 2, "1"),
        (5, 10, 15, 20, "1 2 3 4 5 6 7 8 9 10"),

        (0, 0, 0, 0, "Invalid input"),
        (-1, 10, 2, 1, "Invalid input"),
        (11, 10, 1, 1, "Invalid input"),
        (0, 5, 1, 1, "Invalid input"),
        (0, 5, 0, 0, "Invalid input"),
    ],
)
def test_pagination_with_valid_parameters(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected
