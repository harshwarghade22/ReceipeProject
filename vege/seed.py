
from faker import Faker
fake=Faker()

import random
from .models import *

def create_subject_marks(n):
    student_objs=Student.objects.all()
    for student in student_objs:
        subject_obj=Subject.objects.all()
        for subject in subject_obj:
            SubjectMarks.objects.create(
                student=student,
                subject=subject,
                marks=random.randint(0,100)
            )

def seed_db(n)->None:
    for i in range(0,n):
        department_objs=Department.objects.all()
        random_indx=random.randint(1,len(department_objs)-1)
        department=department_objs[random_indx]
        student_id=f'STU-0{random.randint(100,900)}' 
        student_name=fake.name()
        student_email=fake.email()
        student_age=random.randint(20,30)
        student_address=fake.address()


        student_id_objs=StudentId.objects.create(student_id=student_id)

        student_obj=Student.objects.create(
            department=department,
            student_id=student_id_objs,
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_address=student_address,
        )
        
        
