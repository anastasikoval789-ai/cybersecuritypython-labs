"""
Лабораторна робота №1. Завдання 2
Модуль реалізації матриці контролю доступу для Варіанту 8.
"""

import os
import sys

# Надійно додаємо корінь проєкту до шляхів Python
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../.."))
if root_dir not in sys.path:
  sys.path.insert(0, root_dir)

from shared.student import GROUP_NAME, STUDENT_NAME, VARIANT_NUMBER


def check_access():
  """Моделює систему контролю доступу на основі ролей,

  рівнів безпеки та статусу користувачів.
  """
  # Матриця доступу: ролі та їхні дозволені ресурси
  access_matrix = {
      "Administrator": [
          "System_Configs",
          "Security_Logs",
          "User_Database",
          "Public_Reports",
      ],
      "Security_Analyst": [
          "Security_Logs",
          "Incident_Reports",
          "Public_Reports",
      ],
      "User": ["Public_Reports"],
  }

  # Список користувачів із їхніми ролями та статусом
  users = [
      {"name": "Олександр", "role": "Administrator", "active": True},
      {"name": "Вікторія", "role": "Security_Analyst", "active": True},
      {"name": "Максим", "role": "User", "active": False},
      {"name": "Ірина", "role": "User", "active": True},
  ]

  print(
      f"--- Звіт системи контролю доступу ({STUDENT_NAME}, Група:"
      f" {GROUP_NAME}, Варіант {VARIANT_NUMBER}) ---"
  )
  print(
      f"{'Користувач':<15} | {'Роль':<18} | {'Статус':<10} |"
      f" {'Доступні ресурси'}"
  )
  print("-" * 75)

  for u in users:
    status_str = "Активний" if u["active"] else "Заблокований"
    if not u["active"]:
      allowed = "Доступ заборонено (обліковий запис неактивний)"
    else:
      allowed = ", ".join(access_matrix.get(u["role"], []))

    print(f"{u['name']:<15} | {u['role']:<18} | {status_str:<10} | {allowed}")


if __name__ == "__main__":
  check_access()