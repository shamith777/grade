
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Fail"

def main():
    marks = []
    for i in range(5):
        try:
            mark = float(input(f"Enter marks for subject {i+1}: "))
            marks.append(mark)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return 

    average = sum(marks) / 5
    grade = calculate_grade(average)

    print(f"\nAverage Marks: {average:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
