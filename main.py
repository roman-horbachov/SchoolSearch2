import time
import json
import xml.etree.ElementTree as ET

# Клас для представлення студента
class Student:
    def __init__(self, last_name, first_name, grade, classroom, bus):
        self.last_name = last_name
        self.first_name = first_name
        self.grade = int(grade)
        self.classroom = int(classroom)
        self.bus = int(bus)

    # Метод для перетворення об'єкта в словник (для збереження)
    def to_dict(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'grade': self.grade,
            'classroom': self.classroom,
            'bus': self.bus
        }

# Клас для представлення вчителя
class Teacher:
    def __init__(self, last_name, first_name, classroom):
        self.last_name = last_name
        self.first_name = first_name
        self.classroom = int(classroom)

    # Метод для перетворення об'єкта в словник (для збереження)
    def to_dict(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'classroom': self.classroom
        }

# Основний клас програми
class SchoolSearch:
    def __init__(self):
        self.students = []  # Список студентів
        self.teachers = []  # Список вчителів
        self.load_data()    # Завантаження даних з файлів

    # Метод для завантаження даних з файлів
    def load_data(self):
        try:
            # Завантаження студентів з list.txt
            with open('list.txt', 'r') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 5:
                        # Створення об'єкта Student та додавання до списку
                        student = Student(*[part.strip() for part in parts])
                        self.students.append(student)
            # Завантаження вчителів з teachers.txt
            with open('teachers.txt', 'r') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        # Створення об'єкта Teacher та додавання до списку
                        teacher = Teacher(*[part.strip() for part in parts])
                        self.teachers.append(teacher)
        except FileNotFoundError:
            print("Помилка: Файли даних не знайдено.")

    # Метод для збереження даних у заданому форматі
    def save_data(self, format):
        if format.lower() == 'json':
            # Підготовка даних для збереження у форматі JSON
            data = {
                'students': [s.to_dict() for s in self.students],
                'teachers': [t.to_dict() for t in self.teachers]
            }
            # Запис даних у файл data.json
            with open('data.json', 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("Дані збережено у форматі JSON.")
        elif format.lower() == 'xml':
            # Створення кореневого елемента XML
            root = ET.Element('school')
            # Додавання студентів до XML
            students_el = ET.SubElement(root, 'students')
            for s in self.students:
                student_el = ET.SubElement(students_el, 'student')
                for key, value in s.to_dict().items():
                    ET.SubElement(student_el, key).text = str(value)
            # Додавання вчителів до XML
            teachers_el = ET.SubElement(root, 'teachers')
            for t in self.teachers:
                teacher_el = ET.SubElement(teachers_el, 'teacher')
                for key, value in t.to_dict().items():
                    ET.SubElement(teacher_el, key).text = str(value)
            # Запис даних у файл data.xml
            tree = ET.ElementTree(root)
            tree.write('data.xml', encoding='utf-8', xml_declaration=True)
            print("Дані збережено у форматі XML.")
        else:
            print("Невідомий формат збереження.")

    # Метод для додавання нового студента
    def add_student(self):
        # Введення даних від користувача
        last_name = input("Прізвище студента: ").strip()
        first_name = input("Ім'я студента: ").strip()
        grade = input("Клас: ").strip()
        classroom = input("Класна кімната: ").strip()
        bus = input("Номер автобуса: ").strip()
        # Створення та додавання об'єкта Student
        student = Student(last_name, first_name, grade, classroom, bus)
        self.students.append(student)
        print("Студента додано.")

    # Метод для додавання нового вчителя
    def add_teacher(self):
        # Введення даних від користувача
        last_name = input("Прізвище вчителя: ").strip()
        first_name = input("Ім'я вчителя: ").strip()
        classroom = input("Класна кімната: ").strip()
        # Створення та додавання об'єкта Teacher
        teacher = Teacher(last_name, first_name, classroom)
        self.teachers.append(teacher)
        print("Вчителя додано.")

    # Метод для відображення статистики
    def display_statistics(self):
        print(f"Загальна кількість студентів: {len(self.students)}")
        print(f"Загальна кількість вчителів: {len(self.teachers)}")

    # Метод для пошуку студентів за прізвищем
    def find_students_by_last_name(self, last_name):
        results = []
        for s in self.students:
            if s.last_name == last_name:
                results.append(s)
        return results

    # Метод для пошуку студентів за номером автобуса
    def find_students_by_bus(self, bus_number):
        results = []
        for s in self.students:
            if s.bus == bus_number:
                results.append(s)
        return results

    # Метод для пошуку студентів за прізвищем вчителя
    def find_students_by_teacher(self, teacher_last_name):
        results = []
        # Знаходимо всі класні кімнати, де викладає вчитель
        teacher_classrooms = [
            t.classroom for t in self.teachers if t.last_name == teacher_last_name
        ]
        for s in self.students:
            if s.classroom in teacher_classrooms:
                results.append(s)
        return results

    # Метод для пошуку студентів за номером класної кімнати
    def find_students_by_classroom(self, classroom_number):
        results = []
        for s in self.students:
            if s.classroom == classroom_number:
                results.append(s)
        return results

    # Метод для пошуку вчителів за номером класної кімнати
    def find_teachers_by_classroom(self, classroom_number):
        results = []
        for t in self.teachers:
            if t.classroom == classroom_number:
                results.append(t)
        return results

    # Метод для пошуку студентів за класом
    def find_students_by_grade(self, grade_number):
        results = []
        for s in self.students:
            if s.grade == grade_number:
                results.append(s)
        return results

    # Метод для пошуку вчителів, які викладають у заданому класі
    def find_teachers_by_grade(self, grade_number):
        # Знаходимо всі класні кімнати для заданого класу
        classrooms = set(
            s.classroom for s in self.students if s.grade == grade_number
        )
        results = []
        for t in self.teachers:
            if t.classroom in classrooms:
                results.append(t)
        return results

    # Основний цикл програми для прийняття команд від користувача
    def command_loop(self):
        while True:
            command = input("Введіть команду: ").strip()
            if not command:
                continue
            start_time = time.time()  # Початок вимірювання часу
            if command.lower() == 'add student':
                self.add_student()
            elif command.lower() == 'add teacher':
                self.add_teacher()
            elif command.lower() == 'statistics':
                self.display_statistics()
            elif command.lower().startswith('s:'):
                # Пошук студентів за прізвищем
                last_name = command[2:].strip()
                results = self.find_students_by_last_name(last_name)
                for s in results:
                    print(f"{s.last_name}, {s.first_name}, {s.grade}, "
                          f"{s.classroom}, {s.bus}")
            elif command.lower().startswith('b:'):
                # Пошук студентів за номером автобуса
                bus_number = int(command[2:].strip())
                results = self.find_students_by_bus(bus_number)
                for s in results:
                    print(f"{s.last_name}, {s.first_name}, {s.grade}, "
                          f"{s.classroom}")
            elif command.lower().startswith('t:'):
                # Пошук студентів за прізвищем вчителя
                teacher_last_name = command[2:].strip()
                results = self.find_students_by_teacher(teacher_last_name)
                for s in results:
                    print(f"{s.last_name}, {s.first_name}")
            elif command.lower().startswith('c:'):
                # Пошук за класною кімнатою
                parts = command[2:].strip().split()
                if len(parts) == 1:
                    # Пошук студентів за номером класної кімнати
                    classroom_number = int(parts[0])
                    results = self.find_students_by_classroom(classroom_number)
                    for s in results:
                        print(f"{s.last_name}, {s.first_name}")
                elif len(parts) == 2 and parts[1].lower() == 't':
                    # Пошук вчителів за номером класної кімнати
                    classroom_number = int(parts[0])
                    results = self.find_teachers_by_classroom(classroom_number)
                    for t in results:
                        print(f"{t.last_name}, {t.first_name}")
            elif command.lower().startswith('g:'):
                # Пошук за класом
                parts = command[2:].strip().split()
                if len(parts) == 1:
                    # Пошук студентів за класом
                    grade_number = int(parts[0])
                    results = self.find_students_by_grade(grade_number)
                    for s in results:
                        print(f"{s.last_name}, {s.first_name}")
                elif len(parts) == 2 and parts[1].lower() == 't':
                    # Пошук вчителів, які викладають у заданому класі
                    grade_number = int(parts[0])
                    results = self.find_teachers_by_grade(grade_number)
                    for t in results:
                        print(f"{t.last_name}, {t.first_name}")
            elif command.lower() == 'save json':
                # Збереження даних у форматі JSON
                self.save_data('json')
            elif command.lower() == 'save xml':
                # Збереження даних у форматі XML
                self.save_data('xml')
            elif command.lower() in ['exit', 'quit']:
                # Завершення роботи програми
                print("До побачення!")
                break
            else:
                print("Невідома команда.")
            end_time = time.time()  # Кінець вимірювання часу
            elapsed_ms = (end_time - start_time) * 1000
            # Виведення часу виконання команди
            print(f"Час виконання: {elapsed_ms:.2f} мс\n")

# Точка входу в програму
if __name__ == "__main__":
    app = SchoolSearch()
    app.command_loop()