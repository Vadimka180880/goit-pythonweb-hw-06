from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10
from database import Session
from models import Subject, Group, Teacher, Student

if __name__ == "__main__":
    with Session() as session:
    # Номер елементів, які хочемо вибрати, можна змінити номер і відповідно результат також  зміниться
        subject_index = 1  # Другий предмет  
        group_index = 2    # Третя група  
        teacher_index = 0  # Перший викладач
        student_index = 4  # П'ятий студент  

    # Отримуємо відповідні дані з бази 
        subject = session.query(Subject).offset(subject_index).limit(1).first() 
        group = session.query(Group).offset(group_index).limit(1).first() 
        teacher = session.query(Teacher).offset(teacher_index).limit(1).first() 
        student = session.query(Student).offset(student_index).limit(1).first()  

        subject_name = subject.name if subject else "Немає предметів"   
        group_name = group.name if group else "Немає груп" 
        teacher_name = teacher.name if teacher else "Немає  викладачів"  
        student_name = student.name if student else "Немає студентів"   

    print(f"Список предметів: {subject_name}")
    print(f"Список груп: {group_name}")
    print(f"Список викладачів: {teacher_name}")
    print(f"Список студентів: {student_name}")

    print("\n1. 5 студентів з найбільшим середнім балом:")
    print(select_1())

    print(f"\n2. Студент із найвищим середнім балом з предмета {subject_name}:")
    print(select_2(subject_name=subject_name))

    print(f"\n3. Середній бал у групах з предмета {subject_name}:")
    print(select_3(subject_name=subject_name))

    print(f"\n4. Середній бал на потоці:")
    print(select_4())

    print(f"\n5. Курси, які читає викладач {teacher_name}:")
    print(select_5(teacher_name=teacher_name))

    print(f"\n6. Список студентів у групі {group_name}:")
    print(select_6(group_name=group_name))

    print(f"\n7. Оцінки студентів у групі {group_name} з предмета {subject_name}:")
    print(select_7(group_name=group_name, subject_name=subject_name))

    print(f"\n8. Середній бал викладача {teacher_name} зі своїх предметів:")
    print(select_8(teacher_name=teacher_name))

    print(f"\n9. Курси, які відвідує студент {student_name}:")
    print(select_9(student_name=student_name))

    print(f"\n10. Курси, які студент {student_name} відвідує у викладача {teacher_name}:")
    print(select_10(student_name=student_name, teacher_name=teacher_name))
