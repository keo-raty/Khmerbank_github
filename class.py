class Student:
    def __init__(self,name,gender,room):
        self.name =name
        self.gender=gender
        self.room=room
    def check_attendance(self):
        print(f'{self.name},{self.gender},{self.room} is present')

Student_list=[]

while True:
    name=input("Student Name: ")
    if name.lower() == 'exit':
        break
    gender=input("Student gender: ")
    room=input("Student room: ")



New_Student = Student(name,gender,room)
Student_list.append(New_Student)

print("\n the results")
for s in Student_list:
    s.check_attendance()
print("\n")