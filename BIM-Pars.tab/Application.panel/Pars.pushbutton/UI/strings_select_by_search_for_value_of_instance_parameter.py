# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_select_by_search_for_value_of_instance_parameter.py

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
                return "Parameter Check for all the {}"
            elif first_line == "deutsch":
                return "Parameterüberprüfung für alle {}"
            elif first_line == "farsi":
                return "بررسی پارامتر برای همه {}"
            elif first_line == "russian":
                return "Проверка параметра для всех {}"
            elif first_line == "spanish":
                return "Verificación de parámetros para todos los {}"
            elif first_line == "chinese":
                return "参数检查：所有{}"
            elif first_line == "korean":
                return "모든 에 대한 매개변수 확인{}"
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
        return "An error occurred: {e}"
    
def str_5(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Target Parameter"
            elif first_line == "deutsch":
                return "Zielparameter"
            elif first_line == "farsi":
                return "پارامتر هدف"
            elif first_line == "russian":
                return "Целевой параметр"
            elif first_line == "spanish":
                return "Parámetro objetivo"
            elif first_line == "chinese":
                return "目标参数"
            elif first_line == "korean":
                return "대상 매개변수"
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
    
def str_7(file_path):
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
    
def str_8(file_path):
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
    
def str_9(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Value"
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
    
def str_10(file_path):
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
    
def str_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Search for value of instance parameters"
            elif first_line == "deutsch":
                return "Wert von Instanzparametern suchen"
            elif first_line == "farsi":
                return "جستجوی مقدار پارامترهای نمونه"
            elif first_line == "russian":
                return "Поиск значений параметров экземпляра"
            elif first_line == "spanish":
                return "Buscar valor de los parámetros de la instancia"
            elif first_line == "chinese":
                return "搜索实例参数值"
            elif first_line == "korean":
                return "인스턴스 매개변수 값 검색"
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
        return "An error occurred: {e}"
    
def str_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter"
            elif first_line == "deutsch":
                return "Parameter"
            elif first_line == "farsi":
                return "پارامتر"
            elif first_line == "russian":
                return "Параметр"
            elif first_line == "spanish":
                return "Parámetro"
            elif first_line == "chinese":
                return "参数"
            elif first_line == "korean":
                return "매개변수"
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
                return "Value"
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