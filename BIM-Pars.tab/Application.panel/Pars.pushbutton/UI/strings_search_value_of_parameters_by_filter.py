# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_search_value_of_parameter_by_filter.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select Category"
            elif first_line == "deutsch":
                return "Kategorie auswählen"
            elif first_line == "farsi":
                return "انتخاب دسته‌بندی"
            elif first_line == "russian":
                return "Выберите категорию"
            elif first_line == "spanish":
                return "Seleccionar categoría"
            elif first_line == "chinese":
                return "选择类别"
            elif first_line == "korean":
                return "카테고리 선택하기"
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
        return "An error occurred: {e}"
    
def str_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Family"
            elif first_line == "deutsch":
                return "Familie"
            elif first_line == "farsi":
                return "خانواده"
            elif first_line == "russian":
                return "Семья"
            elif first_line == "spanish":
                return "Familia"
            elif first_line == "chinese":
                return "家族"
            elif first_line == "korean":
                return "가족"
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
                return "Select Family"
            elif first_line == "deutsch":
                return "Familie auswählen"
            elif first_line == "farsi":
                return "انتخاب خانواده"
            elif first_line == "russian":
                return "Выберите семью"
            elif first_line == "spanish":
                return "Seleccionar familia"
            elif first_line == "chinese":
                return "选择家族"
            elif first_line == "korean":
                return "가족 선택하기"
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
                return "Type"
            elif first_line == "deutsch":
                return "Typ"
            elif first_line == "farsi":
                return "نوع"
            elif first_line == "russian":
                return "Тип"
            elif first_line == "spanish":
                return "Tipo"
            elif first_line == "chinese":
                return "类型"
            elif first_line == "korean":
                return "유형"
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
                return "Select Type"
            elif first_line == "deutsch":
                return "Typ auswählen"
            elif first_line == "farsi":
                return "انتخاب نوع"
            elif first_line == "russian":
                return "Выберите тип"
            elif first_line == "spanish":
                return "Seleccionar tipo"
            elif first_line == "chinese":
                return "选择类型"
            elif first_line == "korean":
                return "유형 선택하기"
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
                return "Parameters"
            elif first_line == "deutsch":
                return "Parameter"
            elif first_line == "farsi":
                return "پارامترها"
            elif first_line == "russian":
                return "Параметры"
            elif first_line == "spanish":
                return "Parámetros"
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
     
def str_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select parameter"
            elif first_line == "deutsch":
                return "Parameter auswählen"
            elif first_line == "farsi":
                return "انتخاب پارامتر"
            elif first_line == "russian":
                return "Выберите параметр"
            elif first_line == "spanish":
                return "Seleccionar parámetro"
            elif first_line == "chinese":
                return "选择参数"
            elif first_line == "korean":
                return "매개변수 선택하기"
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
                return "Print mode"
            elif first_line == "deutsch":
                return "Druckmodus"
            elif first_line == "farsi":
                return "حالت چاپ"
            elif first_line == "russian":
                return "Режим печати"
            elif first_line == "spanish":
                return "Modo de impresión"
            elif first_line == "chinese":
                return "打印模式"
            elif first_line == "korean":
                return "인쇄 모드"
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
                return "Select one of the options based on your preference."
            elif first_line == "deutsch":
                return "Wählen Sie eine der Optionen entsprechend Ihrer Vorliebe aus."
            elif first_line == "farsi":
                return "براساس ترجیح خود یکی از گزینه‌ها را انتخاب کنید"
            elif first_line == "russian":
                return "Выберите один из вариантов в соответствии с вашими предпочтениями."
            elif first_line == "spanish":
                return "Selecciona una de las opciones según tu preferencia."
            elif first_line == "chinese":
                return "根据您的偏好选择其中一种选项。"
            elif first_line == "korean":
                return "선호에 따라 옵션 중 하나를 선택하세요."
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
                return "All elements in one table"
            elif first_line == "deutsch":
                return "Alle Elemente in einer Tabelle"
            elif first_line == "farsi":
                return "همه المان ها در یک جدول"
            elif first_line == "russian":
                return "Все элементы в одной таблице"
            elif first_line == "spanish":
                return "Todos los elementos en una tabla"
            elif first_line == "chinese":
                return "所有元素都在一个表格中"
            elif first_line == "korean":
                return "모든 요소를 하나의 테이블에 표시"
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
                return "The data will be printed in one single table"
            elif first_line == "deutsch":
                return "Die Daten werden in einer einzigen Tabelle gedruckt"
            elif first_line == "farsi":
                return "داده‌ها در یک جدول واحد چاپ خواهند شد"
            elif first_line == "russian":
                return "Данные будут выведены в одной единственной таблице"
            elif first_line == "spanish":
                return "Los datos se imprimirán en una sola tabla"
            elif first_line == "chinese":
                return "数据将以单个表格形式打印"
            elif first_line == "korean":
                return "데이터는 하나의 테이블에 출력될 것입니다"
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
                return "Each element in a separate table"
            elif first_line == "deutsch":
                return "Jedes Element in einer separaten Tabelle"
            elif first_line == "farsi":
                return "هر المان در یک جدول مجزا"
            elif first_line == "russian":
                return "Каждый элемент в отдельной таблице"
            elif first_line == "spanish":
                return "Cada elemento en una tabla separada"
            elif first_line == "chinese":
                return "每个元素都在单独的表格中"
            elif first_line == "korean":
                return "각 요소는 별도의 테이블에 있습니다"
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
                return "The data of each element will be printed in a separate table."
            elif first_line == "deutsch":
                return "Die Daten jedes Elements werden in einer separaten Tabelle gedruckt."
            elif first_line == "farsi":
                return "داده‌های هر المان در یک جدول مجزا چاپ خواهند شد"
            elif first_line == "russian":
                return "Данные каждого элемента будут выведены в отдельной таблице."
            elif first_line == "spanish":
                return "Los datos de cada elemento se imprimirán en una tabla separada."
            elif first_line == "chinese":
                return "每个元素的数据将打印在单独的表格中。"
            elif first_line == "korean":
                return "각 요소의 데이터는 별도의 테이블에 출력될 것입니다."
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
                return "Parameter Values Table"
            elif first_line == "deutsch":
                return "Parameterwerte-Tabelle"
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
    
def str_16(file_path):
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
    
def str_17(file_path):
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
    
def str_18(file_path):
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
    
def str_19(file_path):
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
    
def str_20(file_path):
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
    
def str_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No type selected."
            elif first_line == "deutsch":
                return "Kein Typ ausgewählt."
            elif first_line == "farsi":
                return "هیچ نوعی انتخاب نشده است."
            elif first_line == "russian":
                return "Не выбран тип."
            elif first_line == "spanish":
                return "No se ha seleccionado ningún tipo."
            elif first_line == "chinese":
                return "未选择类型。"
            elif first_line == "korean":
                return "선택된 유형이 없습니다."
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
                return "No family name selected."
            elif first_line == "deutsch":
                return "Kein Familienname ausgewählt."
            elif first_line == "farsi":
                return "هیچ نام خانواده ای انتخاب نشده است"
            elif first_line == "russian":
                return "Не выбрано фамилии."
            elif first_line == "spanish":
                return "No se ha seleccionado ningún apellido."
            elif first_line == "chinese":
                return "未选择家族名称。"
            elif first_line == "korean":
                return "선택된 가족 이름이 없습니다."
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
                return "The selected category does not have valid families or types."
            elif first_line == "deutsch":
                return "Die ausgewählte Kategorie hat keine gültigen Familien oder Typen."
            elif first_line == "farsi":
                return "دسته‌بندی انتخاب شده دارای خانواده‌ یا انواع معتبری نمی‌باشد"
            elif first_line == "russian":
                return "Выбранная категория не имеет действительных семей или типов."
            elif first_line == "spanish":
                return "La categoría seleccionada no tiene familias o tipos válidos."
            elif first_line == "chinese":
                return "所选类别没有有效的家族或类型。"
            elif first_line == "korean":
                return "선택한 카테고리에 유효한 가족이나 유형이 없습니다."
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
                return "Invalid Category"
            elif first_line == "deutsch":
                return "Ungültige Kategorie"
            elif first_line == "farsi":
                return "دسته‌بندی نامعتبر"
            elif first_line == "russian":
                return "Недопустимая категория"
            elif first_line == "spanish":
                return "Categoría no válida"
            elif first_line == "chinese":
                return "无效的类别"
            elif first_line == "korean":
                return "유효하지 않은 카테고리"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_25(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No category selected."
            elif first_line == "deutsch":
                return "Keine Kategorie ausgewählt."
            elif first_line == "farsi":
                return "هیچ دسته‌بندی انتخاب نشده است"
            elif first_line == "russian":
                return "Категория не выбрана."
            elif first_line == "spanish":
                return "No se ha seleccionado ninguna categoría."
            elif first_line == "chinese":
                return "未选择类别。"
            elif first_line == "korean":
                return "선택된 카테고리가 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_26(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No element found"
            elif first_line == "deutsch":
                return "Kein Element gefunden"
            elif first_line == "farsi":
                return "هیچ المانی یافت نشد"
            elif first_line == "russian":
                return "Элемент не найден"
            elif first_line == "spanish":
                return "No se encontró ningún elemento"
            elif first_line == "chinese":
                return "未找到元素"
            elif first_line == "korean":
                return "요소를 찾을 수 없습니다"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_27(file_path):
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
    
def str_28(file_path):
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

def str_29(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "The category is invalid."
            elif first_line == "deutsch":
                return "Die Kategorie ist ungültig."
            elif first_line == "farsi":
                return "این دسته بندی معتبر نیست"
            elif first_line == "russian":
                return "Категория недействительна."
            elif first_line == "spanish":
                return "La categoría no es válida."
            elif first_line == "chinese":
                return "该类别无效。"
            elif first_line == "korean":
                return "해당 카테고리가 유효하지 않습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_30(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "All"
            elif first_line == "deutsch":
                return "Alle"
            elif first_line == "farsi":
                return "همه"
            elif first_line == "russian":
                return "Все"
            elif first_line == "spanish":
                return "Todos"
            elif first_line == "chinese":
                return "所有"
            elif first_line == "korean":
                return "모든"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_31(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Report mode"
            elif first_line == "deutsch":
                return "Berichtsmodus"
            elif first_line == "farsi":
                return "حالت گزارش"
            elif first_line == "russian":
                return "Режим отчета"
            elif first_line == "spanish":
                return "Modo de informe"
            elif first_line == "chinese":
                return "报告模式"
            elif first_line == "korean":
                return "보고서 모드"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_32(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Value of parameters"
            elif first_line == "deutsch":
                return "Wert der Parameter"
            elif first_line == "farsi":
                return "مقدار پارامترها"
            elif first_line == "russian":
                return "Значение параметров"
            elif first_line == "spanish":
                return "Valor de los parámetros"
            elif first_line == "chinese":
                return "参数的值"
            elif first_line == "korean":
                return "매개변수 값"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_33(file_path):
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