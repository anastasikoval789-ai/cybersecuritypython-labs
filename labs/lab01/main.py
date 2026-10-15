"""
Головний виконуваний файл Лабораторної роботи №1
для Варіанту 8. Запускає всі завдання послідовно.
"""

import os
import sys

# Надійно додаємо корінь проєкту до шляхів Python на самому початку
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../.."))
if root_dir not in sys.path:
  sys.path.insert(0, root_dir)

# Імпорти модулів завдань після налаштування sys.path
from labs.lab01.task1 import analyze_passwords
from labs.lab01.task2 import check_access
from labs.lab01.task3 import process_security_data
from shared.student import GROUP_NAME, STUDENT_NAME, VARIANT_NUMBER


def main():
  print("=" * 70)
  print(f" ПОЧАТОК ВИКОНАННЯ ЛАБОРАТОРНОЇ РОБОТИ №1")
  print(f" Студент: {STUDENT_NAME} | Група: {GROUP_NAME} | Варіант: {VARIANT_NUMBER}")
  print("=" * 70 + "\n")

  print("[ЗАВДАННЯ 1] Аналіз та перевірка складності паролів:")
  analyze_passwords()
  print("\n" + "-" * 70 + "\n")

  print("[ЗАВДАННЯ 2] Моделювання матриці контролю доступу:")
  check_access()
  print("\n" + "-" * 70 + "\n")

  print("[ЗАВДАННЯ 3] Генерація хешів, CSV та JSON логування:")
  process_security_data()

  print("\n" + "=" * 70)
  print(" ВСІ ЗАВДАННЯ ЛАБОРАТОРНОЇ РОБОТИ УСПІШНО ВИКОНАНО!")
  print("=" * 70)


if __name__ == "__main__":
  main()