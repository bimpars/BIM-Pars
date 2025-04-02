# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_select_by_ids_from_excel.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Row-Column" 
            elif first_line == "deutsch":
                return "Zeile-Spalte"
            elif first_line == "farsi":
                return "ردیف-ستون"
            elif first_line == "russian":
                return "Строка-столбец"
            elif first_line == "spanish":
                return "Fila-Columna"
            elif first_line == "chinese":
                return "行-列"
            elif first_line == "korean":
                return "행-열"
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
                return "Row:"
            elif first_line == "deutsch":
                return "Zeile:"
            elif first_line == "farsi":
                return "ردیف:"
            elif first_line == "russian":
                return "Строка:"
            elif first_line == "spanish":
                return "Fila:"
            elif first_line == "chinese":
                return "行:"
            elif first_line == "korean":
                return "행:"
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
                return "Column:"
            elif first_line == "deutsch":
                return "Spalte:"
            elif first_line == "farsi":
                return "ستون:"
            elif first_line == "russian":
                return "Столбец:"
            elif first_line == "spanish":
                return "Columna:"
            elif first_line == "chinese":
                return "列:"
            elif first_line == "korean":
                return "열:"
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
                return "Row"
            elif first_line == "deutsch":
                return "Zeile"
            elif first_line == "farsi":
                return "ردیف"
            elif first_line == "russian":
                return "Строка"
            elif first_line == "spanish":
                return "Fila"
            elif first_line == "chinese":
                return "行"
            elif first_line == "korean":
                return "행"
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
                return "Column"
            elif first_line == "deutsch":
                return "Spalte"
            elif first_line == "farsi":
                return "ستون"
            elif first_line == "russian":
                return "Столбец"
            elif first_line == "spanish":
                return "Columna"
            elif first_line == "chinese":
                return "列"
            elif first_line == "korean":
                return "열"
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
                return "Row {}, Column {}"
            elif first_line == "deutsch":
                return "Zeile {}, Spalte {}"
            elif first_line == "farsi":
                return "ردیف {}، ستون {}"
            elif first_line == "russian":
                return "Строка {}, Столбец {}"
            elif first_line == "spanish":
                return "Fila {}, Columna {}"
            elif first_line == "chinese":
                return "第{}行，第{}列"
            elif first_line == "korean":
                return "{}행, {}열"
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
                return  "Invalid IDs (not found in the document):\n"
            elif first_line == "deutsch":
                return "Ungültige IDs (nicht im Dokument gefunden):\n"
            elif first_line == "farsi":
                return "شناسه‌های نامعتبر (در سند یافت نشدند)\n"
            elif first_line == "russian":
                return "Недопустимые идентификаторы (не найдены в документе):\n"
            elif first_line == "spanish":
                return "IDs inválidos (no encontrados en el documento):\n"
            elif first_line == "chinese":
                return "无效的ID（在文档中未找到）：\n"
            elif first_line == "korean":
                return "잘못된 ID (문서에서 찾을 수 없음):\n"
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
                return  "All IDs are valid."
            elif first_line == "deutsch":
                return "Alle IDs sind gültig."
            elif first_line == "farsi":
                return "تمامی شناسه‌ها معتبر هستند"
            elif first_line == "russian":
                return "Все идентификаторы действительны."
            elif first_line == "spanish":
                return "Todos los IDs son válidos."
            elif first_line == "chinese":
                return "所有ID均有效。"
            elif first_line == "korean":
                return "모든 ID가 유효합니다."
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
                return  "Invalid IDs"
            elif first_line == "deutsch":
                return "Ungültige IDs"
            elif first_line == "farsi":
                return "شناسه‌های نامعتبر"
            elif first_line == "russian":
                return "Недопустимые идентификаторы"
            elif first_line == "spanish":
                return "IDs inválidos"
            elif first_line == "chinese":
                return "无效的ID"
            elif first_line == "korean":
                return "잘못된 ID"
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
                return  "Please enter valid numeric values for row and column numbers."
            elif first_line == "deutsch":
                return "Bitte geben Sie gültige numerische Werte für Zeilen- und Spaltennummern ein."
            elif first_line == "farsi":
                return "لطفاً برای شماره ردیف و ستون مقادیر عددی معتبر وارد کنید"
            elif first_line == "russian":
                return "Пожалуйста, введите действительные числовые значения для номеров строки и столбца."
            elif first_line == "spanish":
                return "Por favor, ingrese valores numéricos válidos para los números de fila y columna."
            elif first_line == "chinese":
                return "请为行号和列号输入有效的数值。"
            elif first_line == "korean":
                return "행 번호와 열 번호에 유효한 숫자 값을 입력해주세요."
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
                return  "Invalid Input"
            elif first_line == "deutsch":
                return "Ungültige Eingabe"
            elif first_line == "farsi":
                return "ورودی نامعتبر"
            elif first_line == "russian":
                return "Неверный ввод"
            elif first_line == "spanish":
                return "Entrada inválida"
            elif first_line == "chinese":
                return "无效输入"
            elif first_line == "korean":
                return "잘못된 입력"
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
                return  "Enter the row number:"
            elif first_line == "deutsch":
                return "Geben Sie die Zeilennummer ein:"
            elif first_line == "farsi":
                return "شماره ردیف را وارد کنید:"
            elif first_line == "russian":
                return "Введите номер строки:"
            elif first_line == "spanish":
                return "Ingrese el número de fila:"
            elif first_line == "chinese":
                return "输入行号："
            elif first_line == "korean":
                return "행 번호를 입력하세요:"
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
                return  "Row Number"
            elif first_line == "deutsch":
                return "Zeilennummer"
            elif first_line == "farsi":
                return "شماره ردیف"
            elif first_line == "russian":
                return "Номер строки"
            elif first_line == "spanish":
                return "Número de fila"
            elif first_line == "chinese":
                return "行号"
            elif first_line == "korean":
                return "행 번호"
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
                return  "Column {}"
            elif first_line == "deutsch":
                return "Spalte {}"
            elif first_line == "farsi":
                return "ستون {}"
            elif first_line == "russian":
                return "Столбец {}"
            elif first_line == "spanish":
                return "Columna {}"
            elif first_line == "chinese":
                return "列 {}"
            elif first_line == "korean":
                return "{}열"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return   "Please enter a positive integer."
            elif first_line == "deutsch":
                return "Bitte geben Sie eine positive ganze Zahl ein."
            elif first_line == "farsi":
                return "لطفاً یک عدد صحیح مثبت وارد کنید"
            elif first_line == "russian":
                return "Пожалуйста, введите положительное целое число."
            elif first_line == "spanish":
                return "Por favor, ingrese un número entero positivo."
            elif first_line == "chinese":
                return "请输入一个正整数。"
            elif first_line == "korean":
                return "양의 정수를 입력하세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_16(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Please enter an integer."
            elif first_line == "deutsch":
                return "Bitte geben Sie eine ganze Zahl ein."
            elif first_line == "farsi":
                return "لطفاً یک عدد صحیح وارد کنید"
            elif first_line == "russian":
                return "Пожалуйста, введите целое число."
            elif first_line == "spanish":
                return "Por favor, ingrese un número entero."
            elif first_line == "chinese":
                return "请输入一个整数。"
            elif first_line == "korean":
                return "정수를 입력하세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_17(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return   "Enter the column number:"
            elif first_line == "deutsch":
                return "Geben Sie die Spaltennummer ein:"
            elif first_line == "farsi":
                return "شماره ستون را وارد کنید:"
            elif first_line == "russian":
                return "Введите номер столбца:"
            elif first_line == "spanish":
                return "Ingrese el número de columna:"
            elif first_line == "chinese":
                return "输入列号："
            elif first_line == "korean":
                return "열 번호를 입력하세요:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Column Number"
            elif first_line == "deutsch":
                return "Spaltennummer"
            elif first_line == "farsi":
                return "شماره ستون"
            elif first_line == "russian":
                return "Номер столбца"
            elif first_line == "spanish":
                return "Número de columna"
            elif first_line == "chinese":
                return "列号"
            elif first_line == "korean":
                return "열 번호"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_19(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Row {}"
            elif first_line == "deutsch":
                return "Zeile {}"
            elif first_line == "farsi":
                return "ردیف {}"
            elif first_line == "russian":
                return "Строка {}"
            elif first_line == "spanish":
                return "Fila {}"
            elif first_line == "chinese":
                return "第{}行"
            elif first_line == "korean":
                return "{}행"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_20(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select IDs from Excel"
            elif first_line == "deutsch":
                return "IDs aus Excel auswählen"
            elif first_line == "farsi":
                return "انتخاب شناسه‌ها از اکسل"
            elif first_line == "russian":
                return "Выбрать идентификаторы из Excel"
            elif first_line == "spanish":
                return "Seleccionar IDs desde Excel"
            elif first_line == "chinese":
                return "从 Excel 中选择 ID"
            elif first_line == "korean":
                return "Excel에서 ID 선택"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_21(file_path):
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
    

def str_22(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "ID"
            elif first_line == "deutsch":
                return "ID"
            elif first_line == "farsi":
                return "شناسه"
            elif first_line == "russian":
                return "ID"
            elif first_line == "spanish":
                return "ID"
            elif first_line == "chinese":
                return "ID"
            elif first_line == "korean":
                return "ID"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    
def str_23(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Name"
            elif first_line == "deutsch":
                return "Name"
            elif first_line == "farsi":
                return "نام"
            elif first_line == "russian":
                return "Имя"
            elif first_line == "spanish":
                return "Nombre"
            elif first_line == "chinese":
                return "名称"
            elif first_line == "korean":
                return "이름"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)

def str_24(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Category"
            elif first_line == "deutsch":
                return "Kategorie"
            elif first_line == "farsi":
                return "دسته‌بندی"
            elif first_line == "russian":
                return "Категория"
            elif first_line == "spanish":
                return "Categoría"
            elif first_line == "chinese":
                return "类别"
            elif first_line == "korean":
                return "카테고리"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)