"""
Лабораторна робота №1. Завдання 3 (Варіант 8)
"""

import csv
import hashlib
import json
import os
import sys
from datetime import datetime

# Надійно додаємо корінь проєкту до шляхів Python
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../.."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from shared.student import VARIANT_NUMBER


# 1. Власний виняток
class ValidationError(Exception):
    pass


# 1 та 2. Генерація хешу (SHA-256, мін. довжина 11, сіль з варіанта)
def generate_hash(password: str, salt: str = "00008") -> str:
    if not password or not salt:
        raise ValueError("Пароль або сіль порожні.")
    if len(password) < 11:
        raise ValidationError("Пароль занадто короткий (мінімум 11 символів).")
    return hashlib.sha256((salt + password).encode("utf-8")).hexdigest()


# 6. Декоратор для логування з захистом від некоректного формату JSON
def log_event(func):
    def wrapper(username, password, *args, **kwargs):
        result = "failure"
        try:
            res = func(username, password, *args, **kwargs)
            if res:
                result = "success"
            return res
        finally:
            data_dir = os.path.join(current_dir, "data")
            os.makedirs(data_dir, exist_ok=True)
            log_path = os.path.join(data_dir, "log.json")

            logs = []
            if os.path.exists(log_path):
                try:
                    with open(log_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            logs = data
                        elif isinstance(data, dict):
                            logs = [data]
                except Exception:
                    logs = []

            logs.append(
                {
                    "event": "login",
                    "user": username,
                    "result": result,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "args": list(args),
                    "kwargs": kwargs,
                }
            )
            with open(log_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, ensure_ascii=False, indent=4)

    return wrapper


# 3. Реєстрація користувачів
def create_user(username: str, password: str) -> tuple[str, str]:
    salt = f"{VARIANT_NUMBER:05d}"
    return (username, generate_hash(password, salt))


def create_users(users_list: tuple):
    data_dir = os.path.join(current_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    csv_path = os.path.join(data_dir, "users.csv")
    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for user in users_list:
            writer.writerow(create_user(*user))


# 4. Читання бази даних
def read_users_db() -> list:
    users_db = []
    csv_path = os.path.join(current_dir, "data", "users.csv")
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                users_db.append({"username": row[0], "password_hash": row[1]})
    return users_db


# 5. Автентифікація
@log_event
def login(username: str, password: str) -> bool:
    if not username or not password:
        raise ValueError("Порожній логін або пароль.")
    salt = f"{VARIANT_NUMBER:05d}"
    input_hash = generate_hash(password, salt)
    for user in read_users_db():
        if user["username"] == username and user["password_hash"] == input_hash:
            return True
    return False


# 7 та 8. Головна функція main() з обробкою винятків
def main():
    users_to_register = (
        ("admin_koval", "ThreatH@nt3r"),
        ("analyst_viktoriia", "P3n3trat10n@Test"),
        ("security_lead", "Cyber@Defense2023"),
        ("soc_analyst_01", "Incident@R3sp0nse"),
        ("risk_officer", "Risk@Analys1s_2026"),
        ("crypto_user_01", "Secur3Passw0rd!"),
        ("auditor_ivan", "Audit0r_Pr0t3ct!"),
        ("engineer_petro", "Netw0rk_S3cur3!"),
        ("guest_analyst", "Gu3st_P@ssw0rd!"),
        ("test_operator", "T3st_Op3rat0r!"),
    )

    try:
        create_users(users_to_register)
        db = read_users_db()
        print("База даних користувачів:")
        for u in db:
            print(u)

        # Перевірка входу
        login("admin_koval", "ThreatH@nt3r")
        print("[OK] Автентифікація пройдена успішно і залогінена у log.json!")
    except (
        FileNotFoundError,
        PermissionError,
        IOError,
        ValidationError,
        ValueError,
    ) as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()