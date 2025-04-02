# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_dictionary_of_element.py

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
                return  "Instance Parameters Dictionary"
            elif first_line == "deutsch":
                return "Instanzparameter-Wörterbuch"
            elif first_line == "farsi":
                return "فهرست پارامترهای نمونه"
            elif first_line == "russian":
                return "Словарь параметров экземпляра"
            elif first_line == "spanish":
                return "Diccionario de parámetros de instancia"
            elif first_line == "chinese":
                return "实例参数字典"
            elif first_line == "korean":
                return "인스턴스 매개변수 사전"
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
                return  "Storage Type"
            elif first_line == "deutsch":
                return "Speichertyp"
            elif first_line == "farsi":
                return "نوع ذخیره‌سازی"
            elif first_line == "russian":
                return "Тип хранения"
            elif first_line == "spanish":
                return "Tipo de almacenamiento"
            elif first_line == "chinese":
                return "存储类型"
            elif first_line == "korean":
                return "저장 유형"
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
                return "Has Value"
            elif first_line == "deutsch":
                return "Besitzt Wert"
            elif first_line == "farsi":
                return "دارای مقدار"
            elif first_line == "russian":
                return "Имеет значение"
            elif first_line == "spanish":
                return "Tiene valor"
            elif first_line == "chinese":
                return "有值"
            elif first_line == "korean":
                return "값이 있는지"
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
                return   "Type Parameters Dictionary"
            elif first_line == "deutsch":
                return "Typ-Parameter-Wörterbuch"
            elif first_line == "farsi":
                return "فهرست پارامترهای نوع"
            elif first_line == "russian":
                return "Словарь параметров типа"
            elif first_line == "spanish":
                return "Diccionario de parámetros de tipo"
            elif first_line == "chinese":
                return "类型参数字典"
            elif first_line == "korean":
                return "타입 매개변수 사전"
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
                return "Element type not found."
            elif first_line == "deutsch":
                return "Elementtyp nicht gefunden."
            elif first_line == "farsi":
                return "نوع المان یافت نشد"
            elif first_line == "russian":
                return "Тип элемента не найден."
            elif first_line == "spanish":
                return "No se encontró el tipo de elemento."
            elif first_line == "chinese":
                return "未找到元素类型。"
            elif first_line == "korean":
                return "요소 유형을 찾을 수 없습니다."
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
    
def str_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Does not have value" 
            elif first_line == "deutsch":
                return "Hat keinen Wert"
            elif first_line == "farsi":
                return "مقدار ندارد"
            elif first_line == "russian":
                return "Не имеет значения"
            elif first_line == "spanish":
                return "No tiene valor"
            elif first_line == "chinese":
                return "没有值"
            elif first_line == "korean":
                return "값이 없음"
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
                return "No value available"
            elif first_line == "deutsch":
                return "Kein Wert verfügbar"
            elif first_line == "farsi":
                return "هیچ مقداری موجود نیست"
            elif first_line == "russian":
                return "Нет доступного значения"
            elif first_line == "spanish":
                return "No hay valor disponible"
            elif first_line == "chinese":
                return "没有可用的值"
            elif first_line == "korean":
                return "값을 사용할 수 없음"
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
                return "Type Parameters"
            elif first_line == "deutsch":
                return "Typ-Parameter"
            elif first_line == "farsi":
                return "پارامترهای نوع"
            elif first_line == "russian":
                return "Параметры типа"
            elif first_line == "spanish":
                return "Parámetros de tipo"
            elif first_line == "chinese":
                return "类型参数"
            elif first_line == "korean":
                return "타입 매개변수"
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

def str_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter Value"
            elif first_line == "deutsch":
                return "Parameterwert"
            elif first_line == "farsi":
                return "مقدار پارامتر"
            elif first_line == "russian":
                return "Значение параметра"
            elif first_line == "spanish":
                return "Valor del parámetro"
            elif first_line == "chinese":
                return "参数值"
            elif first_line == "korean":
                return "매개변수 값"
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
                return "No parameters found for the element type."
            elif first_line == "deutsch":
                return "Keine Parameter für den Elementtyp gefunden."
            elif first_line == "farsi":
                return "پارامتری برای نوع المان یافت نشد"
            elif first_line == "russian":
                return "Для данного типа элемента параметры не найдены."
            elif first_line == "spanish":
                return "No se encontraron parámetros para el tipo de elemento."
            elif first_line == "chinese":
                return "未找到该元素类型的参数。"
            elif first_line == "korean":
                return "해당 요소 유형에 대한 매개변수를 찾을 수 없습니다."
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
                return "Invalid 'specific_param' value."
            elif first_line == "deutsch":
                return "Ungültiger Wert für 'specific_param'."
            elif first_line == "farsi":
                return "مقدار نامعتبر برای 'specific_param'."
            elif first_line == "russian":
                return "Недопустимое значение для 'specific_param'."
            elif first_line == "spanish":
                return "Valor no válido para 'specific_param'."
            elif first_line == "chinese":
                return "'specific_param' 值无效。"
            elif first_line == "korean":
                return "'specific_param'의 값이 잘못되었습니다."
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
                return  "Element dictionary"
            elif first_line == "deutsch":
                return "Element-Wörterbuch"
            elif first_line == "farsi":
                return "دیکشنری المان "
            elif first_line == "russian":
                return "Словарь элементов"
            elif first_line == "spanish":
                return "Diccionario de elementos"
            elif first_line == "chinese":
                return "元素字典"
            elif first_line == "korean":
                return "요소 사전"
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
