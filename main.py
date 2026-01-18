def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"


students = []

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    name = input("Enter student name: ")

    marks = []
    for j in range(3):
        mark = float(input(f"Enter mark {j + 1}: "))
        marks.append(mark)

    average = calculate_average(marks)
    grade = assign_grade(average)

    students.append({
        "name": name,
        "average": average,
        "grade": grade
    })

print("\n--- Student Results ---")
for student in students:
    print(f"Student: {student['name']}")
    print(f"Average: {student['average']:.2f}")
    print(f"Grade: {student['grade']}")
    print("-" * 20)
