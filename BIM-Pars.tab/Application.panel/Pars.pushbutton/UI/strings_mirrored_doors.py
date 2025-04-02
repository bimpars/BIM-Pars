# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_mirrored_doors.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "of"
            elif first_line == "deutsch":
                return "von"
            elif first_line == "farsi":
                return "از"
            elif first_line == "russian":
                return "из"
            elif first_line == "spanish":
                return "de"
            elif first_line == "chinese":
                return "的"
            elif first_line == "korean":
                return "의"
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
                return " are mirrored in the current view."
            elif first_line == "deutsch":
                return "werden im aktuellen Ansicht gespiegelt."
            elif first_line == "farsi":
                return "در نمای کنونی متقارن هستند"
            elif first_line == "russian":
                return "отражены в текущем виде."
            elif first_line == "spanish":
                return "están reflejados en la vista actual."
            elif first_line == "chinese":
                return "在当前视图中被镜像。"
            elif first_line == "korean":
                return "현재 뷰에서 반전되어 있습니다."
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
                return "Door ID"
            elif first_line == "deutsch":
                return "Tür-ID"
            elif first_line == "farsi":
                return "شناسه درب"
            elif first_line == "russian":
                return "Идентификатор двери"
            elif first_line == "spanish":
                return "ID de puerta"
            elif first_line == "chinese":
                return "门标识"
            elif first_line == "korean":
                return "도어 ID"
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
                return "Door Name"
            elif first_line == "deutsch":
                return "Türname"
            elif first_line == "farsi":
                return "نام درب"
            elif first_line == "russian":
                return "Название двери"
            elif first_line == "spanish":
                return "Nombre de puerta"
            elif first_line == "chinese":
                return "门名称"
            elif first_line == "korean":
                return "도어 이름"
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
                return "symmetric modeled doors"
            elif first_line == "deutsch":
                return "symmetrisch modellierte Türen"
            elif first_line == "farsi":
                return "درب های متقارن"
            elif first_line == "russian":
                return "симметричные моделированные двери"
            elif first_line == "spanish":
                return "puertas modeladas simétricas"
            elif first_line == "chinese":
                return "对称建模的门"
            elif first_line == "korean":
                return "대칭으로 모델링된 문"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_6(file_path):
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
    
def str_h1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "### Date and Time: {}"
            elif first_line == "deutsch":
                return "### Datum und Uhrzeit: {}"
            elif first_line == "farsi":
                return "### تاریخ و زمان: {}"
            elif first_line == "russian":
                return "### Дата и время: {}"
            elif first_line == "spanish":
                return "### Fecha y Hora: {}"
            elif first_line == "chinese":
                return "### 日期和时间：{}"
            elif first_line == "korean":
                return "### 날짜와 시간: {}"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_h2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "### User: {}"
            elif first_line == "deutsch":
                return "### Benutzer: {}"
            elif first_line == "farsi":
                return "### کاربر: {}"
            elif first_line == "russian":
                return "### Пользователь: {}"
            elif first_line == "spanish":
                return "### Usuario: {}"
            elif first_line == "chinese":
                return "### 用户：{}"
            elif first_line == "korean":
                return "### 사용자: {}"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"