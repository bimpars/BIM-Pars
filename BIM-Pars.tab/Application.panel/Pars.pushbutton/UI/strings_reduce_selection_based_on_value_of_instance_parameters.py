# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_reduce_selection_based_on_value_of_instance_parameters.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Instance Parameter:"
            elif first_line == "deutsch":
                return "Instanzparameter:"
            elif first_line == "farsi":
                return "پارامتر نمونه:"
            elif first_line == "russian":
                return "Параметр экземпляра:"
            elif first_line == "spanish":
                return "Parámetro de instancia:"
            elif first_line == "chinese":
                return "实例参数："
            elif first_line == "korean":
                return "인스턴스 매개변수:"
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
                return "Desired Value:"
            elif first_line == "deutsch":
                return "Gewünschter Wert:"
            elif first_line == "farsi":
                return "مقدار:"
            elif first_line == "russian":
                return "Желаемое значение:"
            elif first_line == "spanish":
                return "Valor deseado:"
            elif first_line == "chinese":
                return "期望值："
            elif first_line == "korean":
                return "원하는 값:"
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
                return "No element left in selection."
            elif first_line == "deutsch":
                return "Es sind keine Elemente mehr in der Auswahl vorhanden."
            elif first_line == "farsi":
                return "در انتخاب هیچ المانی باقی نمانده است"
            elif first_line == "russian":
                return "В выборке не осталось элементов."
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
    
def str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No elements found for the specified value and parameter."
            elif first_line == "deutsch":
                return "Keine Elemente für den angegebenen Wert und Parameter gefunden."
            elif first_line == "farsi":
                return "هیچ المانی برای مقدار و پارامتر مشخص شده یافت نشد"
            elif first_line == "russian":
                return "Не найдено элементов для указанного значения и параметра."
            elif first_line == "spanish":
                return "No se encontraron elementos para el valor y parámetro especificados."
            elif first_line == "chinese":
                return "未找到指定值和参数的元素。"
            elif first_line == "korean":
                return "지정된 값과 매개변수에 해당하는 요소를 찾을 수 없습니다."
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
                return "No specific value inserted."
            elif first_line == "deutsch":
                return "Es wurde kein spezifischer Wert eingegeben."
            elif first_line == "farsi":
                return "مقدار وارد نشده است"
            elif first_line == "russian":
                return "Не указано конкретное значение."
            elif first_line == "spanish":
                return "No se ha insertado un valor específico."
            elif first_line == "chinese":
                return "未插入特定值。"
            elif first_line == "korean":
                return "특정 값이 입력되지 않았습니다."
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
                return "No parameter inserted."
            elif first_line == "deutsch":
                return "Kein Parameter eingegeben."
            elif first_line == "farsi":
                return "هیچ پارامتری وارد نشده است"
            elif first_line == "russian":
                return "Параметр не введен."
            elif first_line == "spanish":
                return "No se ha insertado ningún parámetro."
            elif first_line == "chinese":
                return "未插入参数。"
            elif first_line == "korean":
                return "매개변수가 입력되지 않았습니다."
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
                return "For Boolean insert Yes or No start with capital letter depend on the language of your Revit. \nRevit language ENG: Yes-No \nRevit language DEU: Ja-Nein"
            elif first_line == "deutsch":
                return "Für boolesche Werte geben Sie Ja oder Nein in Großbuchstaben ein, abhängig von der Sprache Ihres Revit. \nRevit language ENG: Yes-No \nRevit language DEU: Ja-Nein"
            elif first_line == "farsi":
                return "برای مقادیر بولین، بسته به زبان رویت خود، بله یا خیر را با حرف بزرگ وارد کنید. \nRevit language ENG: Yes-No \nRevit language DEU: Ja-Nein"
            elif first_line == "russian":
                return "Для логического значения введите Да или Нет с заглавной буквы, в зависимости от языка вашего Revit. \nRevit language ENG: Yes-No \nRevit language DEU: Ja-Nein"
            elif first_line == "spanish":
                return "Para los valores booleanos, ingrese Sí o No con mayúscula al inicio según el idioma de su Revit. \nRevit language ENG: Yes-No \nRevit language DEU: Ja-Nein"
            elif first_line == "chinese":
                return "布尔值请根据您的 Revit 语言，以大写字母输入是或否。 \nRevit language ENG: Yes-No \nRevit language DEU: Ja-Nein"
            elif first_line == "korean":
                return "Revit 언어에 따라 대문자로 시작하는 예 또는 아니오를 입력하십시오. \nRevit language ENG: Yes-No \nRevit language DEU: Ja-Nein"
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
                return "Value of instance parameter"
            elif first_line == "deutsch":
                return "Wert des Instanzparameters"
            elif first_line == "farsi":
                return "مقدار پارامتر نمونه"
            elif first_line == "russian":
                return "Значение параметра экземпляра"
            elif first_line == "spanish":
                return "Valor del parámetro de instancia"
            elif first_line == "chinese":
                return "实例参数值"
            elif first_line == "korean":
                return "인스턴스 매개변수 값"
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
    
def str_10(file_path):
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
    
def str_11(file_path):
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

def str_12(file_path):
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