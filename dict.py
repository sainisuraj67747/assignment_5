
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95
}


search_name = input("Enter student's name: ")


if search_name in student_marks:
    print(f"{search_name}'s marks: {student_marks[search_name]}")
else:
    print(f" Student '{search_name}' not found in the records.")