from result import calculate_grade
def generate_report(student, subjects_marks):
    print(f"\nResult Report for {student.name}")
    total = 0
    for sub, marks in subjects_marks.items():
        grade = calculate_grade(marks)
        print(f"{sub}: {marks} ({grade})")
        total += marks
    avg = total / len(subjects_marks)
    print(f"Average: {avg:.2f} | Overall Grade: {calculate_grade(avg)}")