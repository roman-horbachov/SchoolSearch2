
# Система Пошуку Учнів

Цей проект є системою пошуку учнів, яка дозволяє користувачу зчитувати дані зі структурованих текстових файлів, виконувати пошук за різними критеріями, такими як клас, номер автобуса або прізвище, та відображати отриману інформацію у відповідному форматі. Система також підтримує збереження даних у форматах JSON та XML, забезпечуючи можливість роботи з даними без використання сторонніх бібліотек або баз даних.

## Мета
Метою роботи є демонстрація основних можливостей об'єктно-орієнтованого програмування та забезпечення точності й ефективності пошуку та обробки даних.

## Функції
Додаток підтримує наступні функції:
1. Додавання студента.
2. Додавання вчителя.
3. Відображення статистики про кількість студентів та вчителів.
4. Пошук студентів за прізвищем, класом, номером автобуса або вчителем.
5. Пошук вчителів за номером класу або оцінкою, яку вони викладають.
6. Збереження даних у форматах JSON та XML.

## Демонстрація команд та функцій

### 1. Додавання студента
**Команда:** `add student`

### 2. Додавання вчителя
**Команда:** `add teacher`

### 3. Відображення статистики
**Команда:** `statistics`

### 4. Пошук студентів за прізвищем
**Команда:** `S:<LastName>`

### 5. Пошук студентів за номером автобуса
**Команда:** `B:<BusNumber>`

### 6. Пошук студентів за вчителем
**Команда:** `T:<TeacherLastName>`

### 7. Пошук студентів за класом
**Команда:** `C:<Classroom>`

### 8. Пошук вчителів за класом
**Команда:** `C:<Classroom> T`

### 9. Пошук студентів за оцінкою
**Команда:** `G:<Grade>`

### 10. Пошук вчителів за оцінкою
**Команда:** `G:<Grade> T`

### 11. Збереження даних у форматі JSON
**Команда:** `save json`

### 12. Збереження даних у форматі XML
**Команда:** `save xml`

### 13. Завершення роботи програми
**Команда:** `quit` або `exit`

## Висновки
Розроблена програма успішно виконує поставлені завдання зчитуючи дані з файлів і надаючи інструменти для пошуку студентів та вчителів за різними критеріями. Під час реалізації було застосовано об’єктно-орієнтований підхід, що дозволило забезпечити чітку структуру коду та легку модифікацію функціоналу. Програма демонструє високу продуктивність під час обробки запитів, забезпечуючи мінімальний час виконання. Усі функціональні та нефункціональні вимоги були успішно виконані, що свідчить про надійність і зручність використання системи.
