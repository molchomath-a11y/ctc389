# Moshe Molcho Lab 6.

# Creating a list with 5 student names... possibly biblical :)
students = ["Moshe","Arron","Mirriam","Samuel","Sarah"]


# Display menu with 3 options numbered.

print("1. Add student to the list:")
print("2. Modify student name:")
print("3. Remove student:")

# Choice option:

choice = int(input("Choose and option:"))

print(choice)

if choice == 1:
    new_student = input("Enter the new student's name:")
    students.append(new_student)

    print("Updated student list:")
    for student in students:
        print(student)

elif choice ==2:
    print("Student list:")
    for index in range(len(students)):
        print(index,students[index])

    index_number = int(input("Enter the index number to change: "))
    new_name = input("Enter the student's new name: ")
    students[index_number] = new_name

    print("Updated student list:")
    for student in students:
        print(student)

elif choice==3:
    print("Student list:")
    for index in range(len(students)):
        print(index, students[index])

    index_number = int(input("Enter the index number to remove: "))
    students.pop(index_number)
    
    print("Updated student list:")
    for student in students:
        print(student)


       

