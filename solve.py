from itertools import product


def find_solutions() -> list[str]:
    digits: str = "9876543210"
    solutions: list[str] = []

    for operators in product(("+", "-", ""), repeat=len(digits) - 1):
        expression = digits[0]
        total = 0
        number = digits[0]
        sign = 1

        for operator, digit in zip(operators, digits[1:]):
            expression += operator + digit

            if operator:
                total += sign * int(number)
                number = digit
                sign = 1 if operator == "+" else -1
            else:
                number += digit

        if total + sign * int(number) == 200:
            solutions.append(expression)

    return solutions


if __name__ == "__main__":
    for solution in find_solutions():
        print(f"{solution}=200")
