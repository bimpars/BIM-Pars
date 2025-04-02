# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_run_directory.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please set a directory first."
            elif first_line == "deutsch":
                return "Bitte legen Sie zuerst ein Verzeichnis fest."
            elif first_line == "farsi":
                return "لطفاً ابتدا یک دایرکتوری تنظیم کنید"
            elif first_line == "russian":
                return "Пожалуйста, сначала установите директорию."
            elif first_line == "spanish":
                return "Por favor, establezca un directorio primero."
            elif first_line == "chinese":
                return "请先设置一个目录。"
            elif first_line == "korean":
                return "먼저 디렉토리를 설정해주세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Your directory is empty."
            elif first_line == "deutsch":
                return "Ihr Verzeichnis ist leer."
            elif first_line == "farsi":
                return "دایرکتوری شما خالی است"
            elif first_line == "russian":
                return "Ваша директория пуста."
            elif first_line == "spanish":
                return "Tu directorio está vacío."
            elif first_line == "chinese":
                return "您的目录为空。"
            elif first_line == "korean":
                return "디렉토리가 비어 있습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select"
            elif first_line == "deutsch":
                return "Auswählen"
            elif first_line == "farsi":
                return "انتخاب کردن"
            elif first_line == "russian":
                return "Выбрать"
            elif first_line == "spanish":
                return "Seleccionar"
            elif first_line == "chinese":
                return "选择"
            elif first_line == "korean":
                return "선택"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
 
def str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "scripts"
            elif first_line == "deutsch":
                return "Skripte"
            elif first_line == "farsi":
                return "اسکریپت‌ها"
            elif first_line == "russian":
                return "Скрипты"
            elif first_line == "spanish":
                return "Scripts"
            elif first_line == "chinese":
                return "脚本"
            elif first_line == "korean":
                return "스크립트"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
 
def str_5(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error"
            elif first_line == "deutsch":
                return "Fehler"
            elif first_line == "farsi":
                return "خطا"
            elif first_line == "russian":
                return "Ошибка"
            elif first_line == "spanish":
                return "Error"
            elif first_line == "chinese":
                return "错误"
            elif first_line == "korean":
                return "오류"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
 