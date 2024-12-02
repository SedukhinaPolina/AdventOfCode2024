import pytest

from day2.main import solve


@pytest.mark.parametrize(
    "file_input, expected_result",
    [
        ("3 4 1\n4 3 3\n2 5 10\n1 3 5\n3 9 0\n3 3 4", 1),
        ("1 2\n2 2\n3 4", 2),
        ("7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9", 2),
    ]
)
def test_solve_valid(file_input, expected_result, tmp_path):
    input_file = tmp_path / "data.txt"
    input_file.write_text(file_input)
    assert solve(filename=str(input_file)) == expected_result
