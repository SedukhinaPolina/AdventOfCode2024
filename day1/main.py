import sys


def calculate_distance(list_1: list[int], list_2: list[int]) -> int:
    if len(list_1) != len(list_2):
        raise ValueError("Lists must have the same length")

    list_1.sort()
    list_2.sort()
    return sum(abs(a - b) for a, b in zip(list_1, list_2))


def solve(filename: str) -> int:
    list_1, list_2 = [], []
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.split()
            if len(numbers) != 2:
                raise ValueError(f"Invalid line format: {line.strip()}")

            a, b = map(int, numbers)
            list_1.append(a)
            list_2.append(b)

    return calculate_distance(list_1, list_2)


def main() -> None:
    filename = "data.txt" if len(sys.argv) == 1 else sys.argv[1]
    try:
        result = solve(filename=filename)
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
