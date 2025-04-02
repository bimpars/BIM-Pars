# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_snipe_parameter_value.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please select exactly one element."
            elif first_line == "deutsch":
                return "Bitte wählen Sie genau ein Element aus."
            elif first_line == "farsi":
                return "لطفاً دقیقاً یک المان را انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, выберите ровно один элемент."
            elif first_line == "spanish":
                return "Por favor, seleccione exactamente un elemento."
            elif first_line == "chinese":
                return "请选择一个元素。"
            elif first_line == "korean":
                return "정확히 하나의 요소를 선택하십시오."
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
                return "Information"
            elif first_line == "deutsch":
                return "Information"
            elif first_line == "farsi":
                return "اطلاعات"
            elif first_line == "russian":
                return "Информация"
            elif first_line == "spanish":
                return "Información"
            elif first_line == "chinese":
                return "信息"
            elif first_line == "korean":
                return "정보"
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
                return  "This tool cannot be used in a family document."
            elif first_line == "deutsch":
                return "Dieses Tool kann nicht in einem Familien-Dokument verwendet werden."
            elif first_line == "farsi":
                return "امکان استفاده از این ابزار در یک سند خانواده وجود ندارد"
            elif first_line == "russian":
                return "Этот инструмент не может быть использован в документе семейства."
            elif first_line == "spanish":
                return "Esta herramienta no se puede utilizar en un documento de familia."
            elif first_line == "chinese":
                return "此工具无法在族文件中使用。"
            elif first_line == "korean":
                return "이 도구는 가족 문서에서 사용할 수 없습니다."
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
                return 'Select Parameters'
            elif first_line == "deutsch":
                return "Parameter auswählen"
            elif first_line == "farsi":
                return "انتخاب پارامترها"
            elif first_line == "russian":
                return "Выберите параметры"
            elif first_line == "spanish":
                return "Seleccionar parámetros"
            elif first_line == "chinese":
                return "选择参数"
            elif first_line == "korean":
                return "매개변수 선택"
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
                return  "Select"
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
                return "선택하기"
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
                return "No Value"
            elif first_line == "deutsch":
                return "Kein Wert"
            elif first_line == "farsi":
                return "بدون مقدار"
            elif first_line == "russian":
                return "Нет значения"
            elif first_line == "spanish":
                return "Sin valor"
            elif first_line == "chinese":
                return "无值"
            elif first_line == "korean":
                return "값 없음"
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
                return  "Value"
            elif first_line == "deutsch":
                return "Wert"
            elif first_line == "farsi":
                return "مقدار"
            elif first_line == "russian":
                return "Значение"
            elif first_line == "spanish":
                return "Valor"
            elif first_line == "chinese":
                return "值"
            elif first_line == "korean":
                return "값"
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
    
def str_9(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter Values Table"
            elif first_line == "deutsch":
                return "Parameterwertetabelle"
            elif first_line == "farsi":
                return "جدول مقادیر پارامتر"
            elif first_line == "russian":
                return "Таблица значений параметров"
            elif first_line == "spanish":
                return "Tabla de valores de parámetros"
            elif first_line == "chinese":
                return "参数值表"
            elif first_line == "korean":
                return "매개변수 값 테이블"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_10(file_path):
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
    
def str_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No parameters selected."
            elif first_line == "deutsch":
                return "Keine Parameter ausgewählt."
            elif first_line == "farsi":
                return "پارامتری انتخاب نشده است"
            elif first_line == "russian":
                return "Не выбраны параметры."
            elif first_line == "spanish":
                return "No se han seleccionado parámetros."
            elif first_line == "chinese":
                return "未选择参数。"
            elif first_line == "korean":
                return "선택된 매개변수가 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_12(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameters values"
            elif first_line == "deutsch":
                return "Parameterswerte"
            elif first_line == "farsi":
                return "مقادیر پارامترها"
            elif first_line == "russian":
                return "Значения параметров"
            elif first_line == "spanish":
                return "Valores de parámetros"
            elif first_line == "chinese":
                return "参数值"
            elif first_line == "korean":
                return "매개변수 값들"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_13(file_path):
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
    
def str_14(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Element ID"
            elif first_line == "deutsch":
                return "Element-ID"
            elif first_line == "farsi":
                return "شناسه المان"
            elif first_line == "russian":
                return "ID элемента"
            elif first_line == "spanish":
                return "ID del elemento"
            elif first_line == "chinese":
                return "元素ID"
            elif first_line == "korean":
                return "요소 ID"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    
def str_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Element Name"
            elif first_line == "deutsch":
                return "Elementname"
            elif first_line == "farsi":
                return "نام المان"
            elif first_line == "russian":
                return "Имя элемента"
            elif first_line == "spanish":
                return "Nombre del elemento"
            elif first_line == "chinese":
                return "元素名称"
            elif first_line == "korean":
                return "요소 이름"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    
def str_16(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No Name"
            elif first_line == "deutsch":
                return "Kein Name"
            elif first_line == "farsi":
                return "بدون نام"
            elif first_line == "russian":
                return "Без имени"
            elif first_line == "spanish":
                return "Sin nombre"
            elif first_line == "chinese":
                return "没有名称"
            elif first_line == "korean":
                return "이름 없음"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    
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
