from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School("ABC", "Dhaka")

# Adding Classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Adding Student
rahim = Student("Rahim", eight)
karim = Student("Karim", nine)
fahim = Student("Fahim", ten)
hamim = Student("Hamim", ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)

# Adding Teachers
abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
kabul = Teacher("Kabul Khan")

# Adding Subjects
bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", kabul)
biology = Subject("Biology", kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)
