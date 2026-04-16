class Student:
    def __init__(self, name, srn, cgpa):
        self.name = name
        self.srn = srn
        self.cgpa = cgpa
    def display(self):
        print("Name:", self.name)
        print("SRN:", self.srn)
        print("CGPA:", self.cgpa)
student1 = Student("Nitya Borkar", "SRN12345", 9.2)
student1.display()
file_name = "student_details.txt"

with open(file_name, "w") as file:
    file.write("Student Details\n")
    file.write("Name: " + student1.name + "\n")
    file.write("SRN: " + student1.srn + "\n")
    file.write("CGPA: " + str(student1.cgpa) + "\n")

print("\nStudent details saved in", file_name)
