# 📝 Student Marks Report Generator

A simple Python script to collect student marks, store them, and generate a detailed report including average, highest, and lowest scores. Great for beginners practicing input handling, dictionaries, and basic statistics.

---

## 🚀 Features

- 📥 Collects student names and marks via user input  
- 📛 Prevents duplicate entries  
- 📊 Calculates:
  - Total number of students  
  - Average marks  
  - Highest & lowest scores with student names  
- 📋 Displays a detailed report of all entries

---

## 🧠 Concepts Used

- Dictionaries (`dict`) for storing student name–mark pairs  
- `try-except` for input validation  
- List comprehensions  
- `max()`, `min()`, `sum()` functions  
- String formatting with `f-strings`

---

## 💡 Sample Input

```
Enter the student name or 'done' to exit: Alice
Enter marks for Alice: 87
Enter the student name or 'done' to exit: Bob
Enter marks for Bob: 92
Enter the student name or 'done' to exit: Alice
Student already exists
Enter the student name or 'done' to exit: Charlie
Enter marks for Charlie: 56
Enter the student name or 'done' to exit: done
```

---

## 📊 Sample Output

```
Students Marks Report

Total Students: 3
Average Marks: 78.33
Highest Marks: 92.0 by Bob
Lowest Marks: 56.0 by Charlie

Detailed Marks:
 - Alice: 87.0
 - Bob: 92.0
 - Charlie: 56.0
```

---

## 🛠 How to Run

1. Save the script as `student_report.py`.
2. Open terminal or command prompt.
3. Run:
   ```bash
   python student_report.py
   ```

---


