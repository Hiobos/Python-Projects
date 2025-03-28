import os
import tkinter as tk

class Save:
    def __init__(self):
        pass

    def to_file(self, website, email, password):
        if not os.path.exists('passwords.txt'):  # Sprawdza, czy plik istnieje
            with open('passwords.txt', "w") as file:  # Tworzy pusty plik
                file.write(f"{website}| {email} | {password}\n")
        else:
            with open('passwords.txt', "a") as file:  # Tworzy pusty plik
                file.write(f"{website}| {email} | {password}\n")