import threading
import time

# Количество студентов и инициализация семафоров для каждой ложки
num_students = 14
spoons = [threading.Semaphore(1) for _ in range(num_students)]


# Функция, определяющая поведение каждого студента
def student_behavior(student_id):
    left_spoon = spoons[student_id]  # Левая ложка
    right_spoon = spoons[(student_id + 1) % num_students]  # Правая ложка

    while True:
        print(f"Студент {student_id + 1} ожидает ложки.")

        # Захват левой и правой ложек
        left_spoon.acquire()
        right_spoon.acquire()

        # Симуляция трапезы
        print(f"Студент {student_id + 1} кушает.")
        time.sleep(5)

        # Освобождение ложек после еды
        left_spoon.release()
        right_spoon.release()

        # Студент отдыхает после еды
        print(f"Студент {student_id + 1} закончил есть и отдыхает.")
        time.sleep(3)


# Создание и запуск потоков для каждого студента
students = []
for i in range(num_students):
    student_thread = threading.Thread(target=student_behavior, args=(i,))
    students.append(student_thread)
    student_thread.start()

# Поддерживаем потоки активными
for student_thread in students:
    student_thread.join()
