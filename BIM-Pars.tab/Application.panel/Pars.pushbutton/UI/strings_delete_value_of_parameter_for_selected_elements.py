# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_delete_value_of_parameter_for_selected_elements.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No elements selected. Please select at least one element."
            elif first_line == "deutsch":
                return "Keine Elemente ausgewählt. Bitte wählen Sie mindestens ein Element aus."
            elif first_line == "farsi":
                return "هیچ المانی انتخاب نشده است. لطفاً حداقل یک المان انتخاب کنید"
            elif first_line == "russian":
                return "Не выбрано ни одного элемента. Пожалуйста, выберите хотя бы один элемент."
            elif first_line == "spanish":
                return "No se han seleccionado elementos. Por favor, seleccione al menos un elemento."
            elif first_line == "chinese":
                return "没有选择任何元素。请至少选择一个元素。"
            elif first_line == "korean":
                return "선택된 요소가 없습니다. 최소한 하나의 요소를 선택해주세요."
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
                return "Parameter:"
            elif first_line == "deutsch":
                return "Parameter:"
            elif first_line == "farsi":
                return "پارامتر:"
            elif first_line == "russian":
                return "Параметр:"
            elif first_line == "spanish":
                return "Parámetro:"
            elif first_line == "chinese":
                return "参数："
            elif first_line == "korean":
                return "매개변수:"
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
                return "Parameter value for one or more elements is Read Only and can't be deleted."
            elif first_line == "deutsch":
                return "Der Parameterwert für ein oder mehrere Elemente ist schreibgeschützt und kann nicht gelöscht werden."
            elif first_line == "farsi":
                return "مقدار پارامتر برای یک یا چند المان فقط خواندنی است و قابل حذف نیست"
            elif first_line == "russian":
                return "Значение параметра для одного или нескольких элементов доступно только для чтения и не может быть удалено."
            elif first_line == "spanish":
                return "El valor del parámetro para uno o más elementos es de solo lectura y no se puede eliminar."
            elif first_line == "chinese":
                return "一个或多个元素的参数值为只读，无法删除。"
            elif first_line == "korean":
                return "하나 이상의 요소에 대한 매개변수 값은 읽기 전용이므로 삭제할 수 없습니다."
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
                return "Parameter Values Before and After Deletion"
            elif first_line == "deutsch":
                return "Parameterwerte vor und nach der Löschung"
            elif first_line == "farsi":
                return "مقادیر پارامتر قبل و بعد از حذف"
            elif first_line == "russian":
                return "Значения параметров до и после удаления"
            elif first_line == "spanish":
                return "Valores del parámetro antes y después de la eliminación"
            elif first_line == "chinese":
                return "删除前后的参数值"
            elif first_line == "korean":
                return "삭제 전후 매개변수 값"
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
                return "Element ID"
            elif first_line == "deutsch":
                return "Element-ID"
            elif first_line == "farsi":
                return "شناسه المان"
            elif first_line == "russian":
                return "Идентификатор элемента"
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
        return "An error occurred: {e}"
    
def str_6(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Previous Value"
            elif first_line == "deutsch":
                return "Vorheriger Wert"
            elif first_line == "farsi":
                return "مقدار قبلی"
            elif first_line == "russian":
                return "Предыдущее значение"
            elif first_line == "spanish":
                return "Valor anterior"
            elif first_line == "chinese":
                return "上一个值"
            elif first_line == "korean":
                return "이전 값"
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
                return "Current Value"
            elif first_line == "deutsch":
                return "Aktueller Wert"
            elif first_line == "farsi":
                return "مقدار فعلی"
            elif first_line == "russian":
                return "Текущее значение"
            elif first_line == "spanish":
                return "Valor actual"
            elif first_line == "chinese":
                return "当前值"
            elif first_line == "korean":
                return "현재 값"
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
                return "Deleted values report"
            elif first_line == "deutsch":
                return "Bericht über gelöschte Werte"
            elif first_line == "farsi":
                return "گزارش مقادیر حذف شده"
            elif first_line == "russian":
                return "Отчет об удаленных значениях"
            elif first_line == "spanish":
                return "Informe de valores eliminados"
            elif first_line == "chinese":
                return "已删除值报告"
            elif first_line == "korean":
                return "삭제된 값 보고서"
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
                return "Delete value of parameter"
            elif first_line == "deutsch":
                return "Parameterwert löschen"
            elif first_line == "farsi":
                return "حذف مقدار پارامتر"
            elif first_line == "russian":
                return "Удалить значение параметра"
            elif first_line == "spanish":
                return "Eliminar valor de parámetro"
            elif first_line == "chinese":
                return "删除参数值"
            elif first_line == "korean":
                return "매개 변수 값 삭제"
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
                return "Parameter name : "
            elif first_line == "deutsch":
                return "Parametername : "
            elif first_line == "farsi":
                return "نام پارامتر : "
            elif first_line == "russian":
                return "Имя параметра : "
            elif first_line == "spanish":
                return "Nombre del parámetro : "
            elif first_line == "chinese":
                return "参数名称 : "
            elif first_line == "korean":
                return "매개변수 이름 : "
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
    
def str_12(file_path):
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
    
def str_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter Name"
            elif first_line == "deutsch":
                return "Parameternamen"
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