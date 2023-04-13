def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.
    ""
    if not numbers:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    return average


def main():
    numbers = [2, 4, 6, 8, 10]
    average = calculate_average(numbers)
    print(f"The average of {numbers} is {average}")


if __name__ == "__main__":
    main() 
