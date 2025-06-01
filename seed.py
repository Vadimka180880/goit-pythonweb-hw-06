from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Group, Teacher, Subject, Student, Grade
from faker import Faker
import random       
from datetime import date, timedelta     

DATABASE_URL = "postgresql+psycopg2://postgres:VS010203@localhost:5432/goit_hw_06"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)         
session = Session()

fake = Faker('uk_UA')

with Session() as session:
    
    session.query(Grade).delete()
    session.query(Student).delete()
    session.query(Group).delete()
    session.query(Subject).delete()
    session.query(Teacher).delete()
    session.commit()
 
groups = [Group(name=f"Group {i+1}") for i in range(3)]             
session.add_all(groups)             
session.commit()                  
      
teachers = [Teacher(name=fake.name()) for _ in range(4)]    
session.add_all(teachers)  
session.commit() 

subjects = [Subject(name=fake.word().capitalize(), teacher=random.choice(teachers)) for _ in range(7)]
session.add_all(subjects) 
session.commit()  

students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(40)]      
session.add_all(students)     
session.commit()           

for student in students:
    num_grades = random.randint(10, 20)
    for _ in range(num_grades):
        subject = random.choice(subjects)    
        grade_value = random.randint(60, 100) 
        days_ago = random.randint(0, 180)  
        grade_date = date.today() - timedelta(days=days_ago)
        grade = Grade(student=student, subject=subject, grade=grade_value, grade_date=grade_date)
        session.add(grade)              
        
        session.commit()            
print("The database has been populated with random data!!!")       
session.close()  