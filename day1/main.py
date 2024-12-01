import sys


def calculate_distance(list_1: list[int], list_2: list[int]) -> int:
    # Distance is a sum of absolute differences between elements of two sorted lists
    list_1.sort()
    list_2.sort()
    return sum(abs(a - b) for a, b in zip(list_1, list_2))


def calculate_similarity_score(list_1: list[int], list_2: list[int]) -> int:
    # Similarity score is a sum a number of the first list
    # multiplied by number of its occurrence in the second list
    score = 0
    for number in list_1:
        score += list_2.count(number) * number

    return score


def solve(filename: str) -> (int, int):
    list_1, list_2 = [], []
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.split()
            if len(numbers) != 2:
                raise ValueError(f"Invalid line format: {line.strip()}")

            a, b = map(int, numbers)
            list_1.append(a)
            list_2.append(b)

    if len(list_1) != len(list_2):
        raise ValueError("Lists must have the same length")

    return calculate_distance(list_1, list_2), calculate_similarity_score(list_1, list_2)


def main() -> None:
    filename = "data.txt" if len(sys.argv) == 1 else sys.argv[1]
    try:
        distance, similarity_score = solve(filename=filename)
        print(f"Distance: {distance}")
        print(f"Similarity score: {similarity_score}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
