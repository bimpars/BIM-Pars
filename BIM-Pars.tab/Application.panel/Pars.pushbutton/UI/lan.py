# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#lan.py

def detect_language(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()
            if first_line == "english":
                return "English"
            elif first_line == "deutsch":
                return "Deutsch"
            elif first_line == "farsi":
                return "فارسی"  
            elif first_line == "russian":
                return "Русский" 
            elif first_line == "spanish":
                return "Español" 
            elif first_line == "chinese":
                return "中文"  
            elif first_line == "korean":
                return "한국어" 
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"