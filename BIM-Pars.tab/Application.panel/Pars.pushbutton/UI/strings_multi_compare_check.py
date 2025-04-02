# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_multi_compare_check.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Properties Comparison"
            elif first_line == "deutsch":
                return "Eigenschaftsvergleich"
            elif first_line == "farsi":
                return "مقایسه خصوصیات"
            elif first_line == "russian":
                return "Сравнение свойств"
            elif first_line == "spanish":
                return "Comparación de propiedades"
            elif first_line == "chinese":
                return "属性比较"
            elif first_line == "korean":
                return "속성 비교"
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
                return "Passed"
            elif first_line == "deutsch":
                return "Bestanden"
            elif first_line == "farsi":
                return "قبول"
            elif first_line == "russian":
                return "Пройдено"
            elif first_line == "spanish":
                return "Aprobado"
            elif first_line == "chinese":
                return "通过"
            elif first_line == "korean":
                return "통과"
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
                return  "Failed"
            elif first_line == "deutsch":
                return "Fehlgeschlagen"
            elif first_line == "farsi":
                return "ناموفق"
            elif first_line == "russian":
                return "Неудача"
            elif first_line == "spanish":
                return "Fallido"
            elif first_line == "chinese":
                return "失败"
            elif first_line == "korean":
                return "실패"
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
                return "Parameter Name"
            elif first_line == "deutsch":
                return "Parametername"
            elif first_line == "farsi":
                return "نام پارامتر"
            elif first_line == "russian":
                return "Имя параметра"
            elif first_line == "spanish":
                return "Nombre del parámetro"
            elif first_line == "chinese":
                return "参数名称"
            elif first_line == "korean":
                return "매개변수 이름"
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
                return  "Please select minimum two elements for comparison."
            elif first_line == "deutsch":
                return "Bitte wählen Sie mindestens zwei Elemente zur Vergleich aus."
            elif first_line == "farsi":
                return "لطفا حداقل دو المان را برای مقایسه انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, выберите как минимум два элемента для сравнения."
            elif first_line == "spanish":
                return "Por favor, seleccione al menos dos elementos para comparar."
            elif first_line == "chinese":
                return "请至少选择两个元素进行比较。"
            elif first_line == "korean":
                return "비교를 위해 최소한 두 개의 요소를 선택해주세요."
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
                return "Status"
            elif first_line == "deutsch":
                return "Status"
            elif first_line == "farsi":
                return "وضعیت"
            elif first_line == "russian":
                return "Статус"
            elif first_line == "spanish":
                return "Estado"
            elif first_line == "chinese":
                return "状态"
            elif first_line == "korean":
                return "상태"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Comparer of multiple elements"
            elif first_line == "deutsch":
                return "Vergleicher für mehrere Elemente"
            elif first_line == "farsi":
                return "مقایسه کننده چندین المان"
            elif first_line == "russian":
                return "Сравниватель множественных элементов"
            elif first_line == "spanish":
                return "Comparador de múltiples elementos"
            elif first_line == "chinese":
                return "多元素比较器"
            elif first_line == "korean":
                return "다중 요소 비교기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_8(file_path):
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