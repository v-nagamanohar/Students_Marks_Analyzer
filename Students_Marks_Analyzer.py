def collect_student_data():
    students = {}

    while True:
        name = input("Enter the student name or done to exit: ").strip()
        
        if name.lower() == "done":
            break
        if name in students:
            print("Student already exists")
            continue

        try:
            marks = float(input(f"Enter marks for {name}: "))
            students[name] = marks
        except ValueError:
            print("Please enter a valid number for marks")

    return students

def student_report(students):
    if not students:
        print("No Student Data")
        return
    
    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks)/len(marks)

    topper = [name for name,score in students.items() if score == max_score ]
    duller = [name for name,score in students.items() if score == min_score ]

    print("\n Students marks report")
    print("*"*30)
    print(f"Total Students: {len(students)}")
    print(f"Average Marks for Students: {average:.2f}") #.2f acts as round function for formatting the number
    print(f"Highest Marks: {max_score} by {"".join(topper)}")
    print(f"Lowest Marks: {min_score} by {"".join(duller)}")

    print("*"*30)
    print("Detailed Marks ")
    for name, score in students.items():
        print(f" - {name}:{score}")


students = collect_student_data()
student_report(students)

  



    
