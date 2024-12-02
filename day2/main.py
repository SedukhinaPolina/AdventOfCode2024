import sys


def _is_report_safe(report: list[int]) -> bool:
    if len(report) < 2:
        return False

    if report[0] == report[1]:
        return False

    is_increasing = report[0] < report[1]
    for i in range(1, len(report)):
        if abs(report[i - 1] - report[i]) > 3 or report[i - 1] == report[i]:
            return False

        if (is_increasing and report[i - 1] >= report[i]) or (not is_increasing and report[i - 1] <= report[i]):
            return False

    return True


def check_report(report: list[int], with_dampener: bool) -> bool:
    is_report_safe = _is_report_safe(report=report)
    if is_report_safe:
        return True

    if with_dampener:
        for i in range(len(report)):
            is_report_safe = _is_report_safe(report[:i] + report[i + 1:])
            if is_report_safe:
                return True


def solve(filename: str, with_dampener: bool) -> (int, int):
    num_of_safe_reports = 0
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.split()
            if check_report(report=list(map(int, numbers)), with_dampener=with_dampener):
                num_of_safe_reports += 1

    return num_of_safe_reports


def main() -> None:
    filename = "data.txt" if len(sys.argv) == 1 else sys.argv[1]
    try:
        num_of_safe_reports = solve(filename=filename, with_dampener=True)
        print(f"# or safe reports: {num_of_safe_reports}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
