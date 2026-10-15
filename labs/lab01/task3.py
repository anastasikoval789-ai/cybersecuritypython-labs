"""
Лабораторна робота №1. Завдання 3
Модуль генерації хешів, збереження бази даних у CSV та логування у JSON
для Варіанту 8.
"""

import csv
import hashlib
import json
import os
import sys

# Надійно додаємо корінь проєкту до шляхів Python
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../.."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from shared.student import GROUP_NAME, STUDENT_NAME, VARIANT_NUMBER


def hash_password(password: str, salt: str = "00008") -> str:
    """Генерує SHA-256 хеш пароля з додаванням солі для Варіанту 8."""
    combined = salt + password
    return hashlib.sha256(combined.encode("utf-8")).hexdigest()


def process_security_data():
    """Створює директорію data, генерує базу даних користувачів у CSV

    з хешованими паролями та записує лог операцій у JSON.
    """
    # Створюємо папку data, якщо вона ще не існує
    data_dir = os.path.join(current_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    csv_path = os.path.join(data_dir, "users.csv")
    json_path = os.path.join(data_dir, "log.json")

    # Вихідні дані користувачів для збереження
    users_data = [
        {"username": "admin_koval", "password": "ThreatH@nt3r", "role": "Admin"},
        {
            "username": "analyst_viktoriia",
            "password": "P3n3trat10n@Test",
            "role": "Analyst",
        },
        {"username": "user_guest", "password": "Cyber@Defense2023", "role": "User"},
    ]

    # Запис даних у CSV файл із хешуванням паролів
    csv_rows = []
    for user in users_data:
        hashed_pwd = hash_password(user["password"])
        csv_rows.append(
            {
                "username": user["username"],
                "password_hash": hashed_pwd,
                "role": user["role"],
            }
        )

    with open(csv_path, mode="w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["username", "password_hash", "role"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in csv_rows:
            writer.writerow(row)

    # Створення логу у форматі JSON
    log_data = {
        "student": STUDENT_NAME,
        "group": GROUP_NAME,
        "variant": VARIANT_NUMBER,
        "status": "Success",
        "actions_logged": len(users_data),
        "files_created": ["users.csv", "log.json"],
    }

    with open(json_path, mode="w", encoding="utf-8") as json_file:
        json.dump(log_data, json_file, ensure_ascii=False, indent=4)

    print(
        f"--- Звіт генератора хешів та логів ({STUDENT_NAME}, Група:"
        f" {GROUP_NAME}, Варіант {VARIANT_NUMBER}) ---"
    )
    print(f"[OK] Базу даних збережено у: {csv_path}")
    print(f"[OK] Лог операцій збережено у: {json_path}")
    print("Сформовані хеші паролів:")
    for row in csv_rows:
        print(f" - {row['username']} ({row['role']}): {row['password_hash']}")


if __name__ == "__main__":
    process_security_data()
