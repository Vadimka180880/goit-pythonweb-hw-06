from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, desc
from models import Student, Grade, Subject, Group, Teacher
from database import engine
from database import Session
from models import Subject

Session = sessionmaker(bind=engine)
session = Session()

def select_all_subjects():
    with Session() as session:
        result = session.query(Subject).all()
        return [(sub.id, sub.name) for sub in result]


def select_1():
    return session.query(
        Student.name, func.round(func.avg(Grade.grade), 2).label('average_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    
def select_2(subject_name):
    return session.query(
        Student.name, func.round(func.avg(Grade.grade), 2).label('average_grade')
    ).join(Grade).join(Subject).filter(Subject.name == subject_name)\
    .group_by(Student.id).order_by(desc('average_grade')).first()
    
def select_3(subject_name):
    return session.query(
        Group.name,
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ).select_from(Group)\
    .join(Group.students)\
    .join(Student.grades)\
    .join(Grade.subject)\
    .filter(Subject.name == subject_name)\
    .group_by(Group.id).all() 

    
def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2)).scalar()

def select_5(teacher_name):
    return session.query(Subject.name).join(Teacher)\
    .filter(Teacher.name == teacher_name).all()   
    
def select_6(group_name):
    return session.query(Student.name).join(Group).filter(Group.name == group_name).all()     

def select_7(group_name, subject_name): 
    return session.query(Student.name, Grade.grade).join(Group).join(Grade).join(Subject)\
    .filter(Group.name == group_name, Subject.name == subject_name).all()      

def select_8(teacher_name):   
    return session.query(func.round(func.avg(Grade.grade), 2)).join(Subject).join(Teacher)\
    .filter(Teacher.name == teacher_name).scalar()   
    
def select_9(student_name):
    return session.query(Subject.name).join(Grade).join(Student)\
    .filter(Student.name == student_name).group_by(Subject.id).all()  
    
def select_10(student_name, teacher_name):  
    return session.query(Subject.name).join(Teacher).join(Grade).join(Student)\
    .filter(Student.name == student_name, Teacher.name == teacher_name).all()  
    
    
    session.close()