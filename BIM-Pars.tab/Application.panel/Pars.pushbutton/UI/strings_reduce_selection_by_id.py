# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_reduce_selection_by_id.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "IDs (separate with comma):"
            elif first_line == "deutsch":
                return "IDs (mit Komma trennen):"
            elif first_line == "farsi":
                return "[شناسه‌ها [با کاما جدا کنید:"
            elif first_line == "russian":
                return "Идентификаторы (разделяйте запятой):"
            elif first_line == "spanish":
                return "IDs (separados por coma):"
            elif first_line == "chinese":
                return "标识符（用逗号分隔）："
            elif first_line == "korean":
                return "ID (쉼표로 구분):"
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
                return "Operation canceled."
            elif first_line == "deutsch":
                return "Vorgang abgebrochen."
            elif first_line == "farsi":
                return "عملیات لغو شد"
            elif first_line == "russian":
                return "Операция отменена."
            elif first_line == "spanish":
                return "Operación cancelada."
            elif first_line == "chinese":
                return "操作已取消。"
            elif first_line == "korean":
                return "작업이 취소되었습니다."
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
                return "Invalid input. Only integers are allowed."
            elif first_line == "deutsch":
                return "Ungültige Eingabe. Nur ganze Zahlen sind erlaubt."
            elif first_line == "farsi":
                return "ورودی نامعتبر. تنها اعداد صحیح مجاز هستند"
            elif first_line == "russian":
                return "Неверный ввод. Разрешены только целые числа."
            elif first_line == "spanish":
                return "Entrada inválida. Solo se permiten números enteros."
            elif first_line == "chinese":
                return "无效输入。仅允许整数。"
            elif first_line == "korean":
                return "잘못된 입력입니다. 정수만 허용됩니다."
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
                return "No element left in selection."
            elif first_line == "deutsch":
                return "Kein Element mehr in der Auswahl."
            elif first_line == "farsi":
                return "هیچ المانی در انتخاب باقی نمانده است"
            elif first_line == "russian":
                return "В выборке нет больше элементов."
            elif first_line == "spanish":
                return "No queda ningún elemento en la selección."
            elif first_line == "chinese":
                return "选择中没有剩余元素。"
            elif first_line == "korean":
                return "선택된 요소가 없습니다."
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
                return "Reduce Selection By ID"
            elif first_line == "deutsch":
                return "Auswahl nach ID reduzieren"
            elif first_line == "farsi":
                return "کاهش انتخاب بر اساس شناسه"
            elif first_line == "russian":
                return "Сократить выделение по идентификатору"
            elif first_line == "spanish":
                return "Reducir selección por ID"
            elif first_line == "chinese":
                return "按 ID 缩小选择"
            elif first_line == "korean":
                return "ID로 선택 영역 축소"
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
    
def str_7(file_path):
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
    
def str_8(file_path):
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

def str_9(file_path):
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