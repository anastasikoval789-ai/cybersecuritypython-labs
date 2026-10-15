"""
Лабораторна робота №1. Завдання 1
Модуль для аналізу та перевірки складності паролів за критеріями безпеки
для Варіанту 8.
"""

import os
import sys

# Надійно додаємо корінь проєкту до шляхів Python
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../.."))
if root_dir not in sys.path:
  sys.path.insert(0, root_dir)

import random

from shared.student import GROUP_NAME, STUDENT_NAME, VARIANT_NUMBER


def analyze_passwords():
  """Аналізує заданий список паролів згідно з критеріями безпеки Варіанту 8,

  визначає їхній статус (Заборонений, Слабкий, Сильний, Дуже сильний)
  та виводить результати у вигляді таблиці.
  """
  # Вхідні дані для Варіанту 8
  passwords = [
      "ThreatH@nt3r",
      "weak123",
      "P3n3trat10n@Test",
      "visitor",
      "Cyber@Defense2023",
      "normal",
      "Incident@R3sp0nse",
      "standard",
      "Risk@Analys1s",
      "typical",
  ]

  criteria = {
      "min_length": 10,
      "require_digits": True,
      "require_upper": True,
      "require_special": True,
  }

  forbidden_passwords = {
      "weak123",
      "visitor",
      "normal",
      "standard",
      "typical",
      "admin",
  }

  # Фіксуємо seed для відтворюваності випадкового вибору індексів
  random.seed(42)
  random_indices = [random.randint(0, len(passwords) - 1) for _ in range(3)]

  # Дублюємо випадково обрані паролі в кінець списку для перевірки унікальності
  for idx in random_indices:
    passwords.append(passwords[idx])

  results = []
  for pwd in passwords:
    # Перевірка на заборонені паролі або невідповідність мінімальній довжині
    if pwd in forbidden_passwords or len(pwd) < criteria["min_length"]:
      status = "Заборонений"
    else:
      # Перевірка наявності цифр, великих літер та спецсимволів
      has_digit = any(c.isdigit() for c in pwd)
      has_upper = any(c.isupper() for c in pwd)
      has_special = any(not c.isalnum() for c in pwd)

      if not (has_digit and has_upper and has_special):
        status = "Слабкий"
      elif len(pwd) < criteria["min_length"] + 4:
        status = "Сильний"
      else:
        # Перевірка на унікальність у списку (якщо зустрічається більше одного разу)
        is_unique = passwords.count(pwd) == 1
        status = "Дуже сильний" if is_unique else "Сильний"

    results.append((pwd, status))

  # Виведення результатів у вигляді таблиці з урахуванням даних студента
  print(
      f"--- Звіт аналізатора паролів ({STUDENT_NAME}, Група: {GROUP_NAME},"
      f" Варіант {VARIANT_NUMBER}) ---"
  )
  print(f"{'Пароль':<20} | {'Статус':<15}")
  print("-" * 38)
  for pwd, status in results:
    print(f"{pwd:<20} | {status:<15}")


if __name__ == "__main__":
  analyze_passwords()