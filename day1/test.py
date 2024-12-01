import pytest

from day1.main import calculate_distance, solve


@pytest.mark.parametrize(
    "list_1, list_2, expected_result",
    [
        ([2], [3], 1),
        ([2, 1], [3, 4], 4),
        ([2, 1, 3], [3, 4, 5], 6),
        ([], [], 0),
        ([10, -5], [5, 10], 10),
        ([0, 0, 0], [0, 0, 0], 0),
        ([5, 8, 3], [2, 5, 10], 3),
        ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3], 11),
    ]
)
def test_calculate_distance(list_1, list_2, expected_result):
    assert calculate_distance(list_1, list_2) == expected_result


@pytest.mark.parametrize(
    "list_1, list_2",
    [
        ([1, 2], [1]),
        ([], [1, 2]),
    ]
)
def test_calculate_distance_invalid(list_1, list_2):
    with pytest.raises(ValueError):
        calculate_distance(list_1, list_2)


@pytest.mark.parametrize(
    "file_input, expected_result",
    [
        ("3 4\n4 3\n2 5\n1 3\n3 9\n3 3", 11),
        ("1 1\n2 2\n3 3", 0),
        ("10 20\n30 40", 20),
    ]
)
def test_solve_valid(file_input, expected_result, tmp_path):
    input_file = tmp_path / "data.txt"
    input_file.write_text(file_input)
    assert solve(filename=str(input_file)) == expected_result


@pytest.mark.parametrize(
    "file_input, expected_result",
    [
        ("3 4\n4 3\n2 5\n1 3\n3 9\n3", 11),
    ]
)
def test_solve_valid(file_input, expected_result, tmp_path):
    input_file = tmp_path / "data.txt"
    input_file.write_text(file_input)
    with pytest.raises(ValueError):
        solve(filename=str(input_file))