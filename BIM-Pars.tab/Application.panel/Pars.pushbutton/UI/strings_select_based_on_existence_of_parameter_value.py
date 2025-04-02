# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_select_based_on_existance_of_parameter_value.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select By Parameter value based on existence"
            elif first_line == "deutsch":
                return "Auswahl basierend auf dem Vorhandensein des Parameterwerts"
            elif first_line == "farsi":
                return "انتخاب بر اساس مقدار پارامتر بر اساس وجود"
            elif first_line == "russian":
                return "Выбор по значению параметра на основе наличия"
            elif first_line == "spanish":
                return "Seleccionar por valor de parámetro basado en la existencia"
            elif first_line == "chinese":
                return "根据存在性选择的参数值进行选择"
            elif first_line == "korean":
                return "존재에 따른 매개변수 값에 따라 선택"
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
                return "Parameter value for exist"
            elif first_line == "deutsch":
                return "Parameterwert für Existenz"
            elif first_line == "farsi":
                return "وجود مقدار پارامتر "
            elif first_line == "russian":
                return "Значение параметра для существования"
            elif first_line == "spanish":
                return "Valor del parámetro para la existencia"
            elif first_line == "chinese":
                return "存在的参数值"
            elif first_line == "korean":
                return "존재하는 매개변수 값"
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
                return "Select one of the options based on your need."
            elif first_line == "deutsch":
                return "Wählen Sie eine der Optionen basierend auf Ihrem Bedarf aus."
            elif first_line == "farsi":
                return "با توجه به نیاز خود یکی از گزینه‌ها را انتخاب کنید"
            elif first_line == "russian":
                return "Выберите один из вариантов в зависимости от ваших потребностей."
            elif first_line == "spanish":
                return "Selecciona una de las opciones según tus necesidades."
            elif first_line == "chinese":
                return "根据您的需求选择其中一项选项。"
            elif first_line == "korean":
                return "필요에 따라 옵션 중 하나를 선택하세요."
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
                return "Select both with value and with no value"
            elif first_line == "deutsch":
                return "Auswahl sowohl mit Wert als auch ohne Wert"
            elif first_line == "farsi":
                return "انتخاب با مقدار و بدون مقدار"
            elif first_line == "russian":
                return "Выбрать и с значением, и без значения"
            elif first_line == "spanish":
                return "Seleccionar tanto con valor como sin valor"
            elif first_line == "chinese":
                return "选择具有值和没有值的项"
            elif first_line == "korean":
                return "값과 값이 없는 항목 모두 선택"
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
                return "Selects all elements that have the inserted parameter"
            elif first_line == "deutsch":
                return "Wählt alle Elemente aus, die den eingefügten Parameter haben"
            elif first_line == "farsi":
                return "تمام المان هایی که پارامتر وارد شده را دارند را انتخاب می کند"
            elif first_line == "russian":
                return "Выбирает все элементы, у которых есть вставленный параметр"
            elif first_line == "spanish":
                return "Selecciona todos los elementos que tienen el parámetro insertado"
            elif first_line == "chinese":
                return "选择所有具有插入参数的元素"
            elif first_line == "korean":
                return "삽입된 매개변수를 가진 모든 요소를 선택합니다"
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
                return "Only with value."
            elif first_line == "deutsch":
                return "Nur mit Wert."
            elif first_line == "farsi":
                return "فقط با مقدار."
            elif first_line == "russian":
                return "Только со значением."
            elif first_line == "spanish":
                return "Solo con valor."
            elif first_line == "chinese":
                return "仅显示有值的选项。"
            elif first_line == "korean":
                return "값이 있는 항목만 표시하기"
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
                return "Selects only the elements that inserted parameter has value"
            elif first_line == "deutsch":
                return "Wählt nur die Elemente aus, bei denen der eingefügte Parameter einen Wert hat."
            elif first_line == "farsi":
                return "فقط المان هایی را انتخاب می‌کند که پارامتر وارد شده دارای مقدار است"
            elif first_line == "russian":
                return "Выбирает только элементы, у которых есть значение вставленного параметра."
            elif first_line == "spanish":
                return "Selecciona solo los elementos que tienen valor en el parámetro insertado."
            elif first_line == "chinese":
                return "仅选择具有插入参数值的元素。"
            elif first_line == "korean":
                return "삽입된 매개변수에 값이 있는 요소만 선택합니다."
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
                return "Only with no value."
            elif first_line == "deutsch":
                return "Nur ohne Wert."
            elif first_line == "farsi":
                return "فقط بدون مقدار"
            elif first_line == "russian":
                return "Только без значения."
            elif first_line == "spanish":
                return "Solo sin valor."
            elif first_line == "chinese":
                return "仅显示无值的选项。"
            elif first_line == "korean":
                return "값이 없는 항목만 표시하기"
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
                return "Selects only the elements that inserted parameter has no value"
            elif first_line == "deutsch":
                return "Wählt nur die Elemente aus, bei denen der eingefügte Parameter keinen Wert hat."
            elif first_line == "farsi":
                return "فقط المان هایی را انتخاب می‌کند که پارامتر وارد شده بدون مقدار است"
            elif first_line == "russian":
                return "Выбирает только элементы, у которых нет значения вставленного параметра."
            elif first_line == "spanish":
                return "Selecciona solo los elementos que no tienen valor en el parámetro insertado."
            elif first_line == "chinese":
                return "仅选择插入参数没有值的元素。"
            elif first_line == "korean":
                return "삽입된 매개변수에 값이 없는 요소만 선택합니다."
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
                return "Operation canceled."
            elif first_line == "deutsch":
                return "Operation abgebrochen."
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
    
def str_11(file_path):
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
                return "매개변수: "
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
                return "Select Categories"
            elif first_line == "deutsch":
                return "Kategorien auswählen"
            elif first_line == "farsi":
                return "انتخاب دسته‌بندی‌ها"
            elif first_line == "russian":
                return "Выберите категории"
            elif first_line == "spanish":
                return "Seleccionar Categorías"
            elif first_line == "chinese":
                return "选择类别"
            elif first_line == "korean":
                return "카테고리 선택"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_12_(file_path):
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
                return "선택하기"
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
                return "Does not have value."
            elif first_line == "deutsch":
                return "Hat keinen Wert."
            elif first_line == "farsi":
                return "مقدار ندارد"
            elif first_line == "russian":
                return "Не имеет значения."
            elif first_line == "spanish":
                return "No tiene valor."
            elif first_line == "chinese":
                return "没有值。"
            elif first_line == "korean":
                return "값이 없습니다."
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
                return "Parameter Check for all the {}"
            elif first_line == "deutsch":
                return "Parameterprüfung für alle {}"
            elif first_line == "farsi":
                return "بررسی پارامتر برای همه {}"
            elif first_line == "russian":
                return "Проверка параметра для всех {}"
            elif first_line == "spanish":
                return "Verificación de parámetros para todos los {}"
            elif first_line == "chinese":
                return "所有的参数检查{}"
            elif first_line == "korean":
                return "모든 에 대한 매개변수 확인{}"
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
    
def str_16(file_path):
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
    
def str_17(file_path):
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
    
def str_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Invalid Parameter"
            elif first_line == "deutsch":
                return "Ungültiger Parameter"
            elif first_line == "farsi":
                return "پارامتر نامعتبر"
            elif first_line == "russian":
                return "Неверный параметр"
            elif first_line == "spanish":
                return "Parámetro inválido"
            elif first_line == "chinese":
                return "无效参数"
            elif first_line == "korean":
                return "잘못된 매개변수"
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
                return "No parameter inserted"
            elif first_line == "deutsch":
                return "Kein Parameter eingegeben"
            elif first_line == "farsi":
                return "پارامتری وارد نشده است"
            elif first_line == "russian":
                return "Параметр не введен"
            elif first_line == "spanish":
                return "No se ha insertado ningún parámetro"
            elif first_line == "chinese":
                return "未插入参数"
            elif first_line == "korean":
                return "매개변수가 입력되지 않았습니다"
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
                return "Method"
            elif first_line == "deutsch":
                return "Methode"
            elif first_line == "farsi":
                return "روش"
            elif first_line == "russian":
                return "Метод"
            elif first_line == "spanish":
                return "Método"
            elif first_line == "chinese":
                return "方法"
            elif first_line == "korean":
                return "방법"
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
    
def str_22(file_path):
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
    
def str_23(file_path):
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
    
def str_24(file_path):
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