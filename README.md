 SQLAlchemy + Alembic Demo Project

Цей проєкт демонструє роботу з SQLAlchemy та Alembic для роботи з базою даних PostgreSQL. Він містить приклади створення моделей, налаштування підключення, міграцій, заповнення бази тестовими даними та виконання SQL-запитів.

//Структура проєкту


├── alembic/               # Міграції Alembic
│   ├── versions/          # Файли міграцій
│   └── env.py             # Конфігурація Alembic
├── models.py              # SQLAlchemy моделі
├── database.py            # Підключення до бази
├── seed.py                # Скрипт заповнення бази тестовими даними
├── print_test_select.py   # Приклади SQL-запитів
├── requirements.txt       # Список залежностей
└── README.md              # Документація проєкту

-- Запуск проєкту
//Клонуйте репозиторій:

git clone <посилання на репозиторій>
cd <назва репозиторію>

Створіть та активуйте віртуальне середовище:

python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

Встановіть залежності:

pip install -r requirements.txt

Налаштуйте файл .env для з'єднання з вашою базою PostgreSQL (або задайте sqlalchemy.url у alembic.ini):

SQLALCHEMY_URL=postgresql+psycopg2://<user>:<password>@localhost:5432/<dbname>
Ініціалізуйте міграції:

alembic upgrade head
Заповніть базу тестовими даними:

python seed.py

Виконайте приклади запитів:

python print_test_select.py

// Опис файлів
models.py - SQLAlchemy моделі: Group, Teacher, Subject, Student, Grade.

database.py - Підключення до бази даних.

alembic/ - Каталог з міграціями Alembic.

seed.py - Скрипт заповнення бази випадковими даними.

print_test_select.py - Приклади складних SQL-запитів до бази даних.


