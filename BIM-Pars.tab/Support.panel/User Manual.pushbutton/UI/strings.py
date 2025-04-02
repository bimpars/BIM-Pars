# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings.py

def detect_language(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "index_en.html"
            elif first_line == "deutsch":
                return "index_de.html"
            elif first_line == "farsi":
                return "index_fa.html"
            elif first_line == "russian":
                return "index_ru.html"
            elif first_line == "spanish":
                return "index_sp.html"
            elif first_line == "chinese":
                return "index_ch.html"
            elif first_line == "korean":
                return "index_ko.html" 
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "User Manual"
            elif first_line == "deutsch":
                return "Benutzerhandbuch"
            elif first_line == "farsi":
                return "راهنمای کاربر"
            elif first_line == "russian":
                return "Руководство пользователя"
            elif first_line == "spanish":
                return "Manual de usuario"
            elif first_line == "chinese":
                return "用户手册"
            elif first_line == "korean":
                return "사용자 매뉴얼"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

