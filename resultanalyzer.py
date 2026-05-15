
def analyze_result(name, roll, marks):

    total = sum(marks)
    average = total / len(marks)
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")

    print("Subjects below 40:")

    found = False

    for i in range(len(marks)):
        if marks[i] < 40:
            print(f"Subject {i+1}")
            found = True

    if found == False:
        print("None")


name = "sadhika"
roll = 14
marks = [88.5, 90.0, 76.0, 92.5, 89.0]

analyze_result(name, roll, marks)