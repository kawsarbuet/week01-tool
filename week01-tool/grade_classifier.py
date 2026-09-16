

def classify_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


def main():
    user_input = input("Enter a mark out of 100: ")

    # Validate numeric input
    if not user_input.isdigit():
        print("Invalid input: please enter a number between 0 and 100.")
        return

    mark = int(user_input)

    # Validate range
    if mark < 0 or mark > 100:
        print("Out of range: mark must be between 0 and 100.")
        return

    # Compute result
    letter = classify_grade(mark)
    print(f"The letter grade for {mark} is: {letter}")


if __name__ == "__main__":
    main()
