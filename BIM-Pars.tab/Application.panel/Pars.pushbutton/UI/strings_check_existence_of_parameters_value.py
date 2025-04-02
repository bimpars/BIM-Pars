# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_check_existance_of_parameters_value.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter Check"
            elif first_line == "deutsch":
                return "Parameterprüfung"
            elif first_line == "farsi":
                return "بررسی پارامتر"
            elif first_line == "russian":
                return "Проверка параметров"
            elif first_line == "spanish":
                return "Verificación de parámetros"
            elif first_line == "chinese":
                return "参数检查"
            elif first_line == "korean":
                return "매개변수 확인"
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
                return "Show both with value and with no value."
            elif first_line == "deutsch":
                return "Zeige sowohl mit Wert als auch ohne Wert."
            elif first_line == "farsi":
                return "نمایش هر دوی دارای مقدار و بدون مقدار"
            elif first_line == "russian":
                return "Показать и с значением, и без значения."
            elif first_line == "spanish":
                return "Mostrar tanto con valor como sin valor."
            elif first_line == "chinese":
                return "同时显示有值和无值的选项。"
            elif first_line == "korean":
                return "값과 값이 없는 것을 모두 보여주세요."
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
                return "Displays all elements that have the inserted parameter."
            elif first_line == "deutsch":
                return "Zeigt alle Elemente an, die den eingegebenen Parameter besitzen."
            elif first_line == "farsi":
                return "تمام المان هایی را که پارامتر وارد شده را دارند نمایش می‌دهد"
            elif first_line == "russian":
                return "Отображает все элементы, которые имеют вставленный параметр."
            elif first_line == "spanish":
                return "Muestra todos los elementos que tienen el parámetro insertado."
            elif first_line == "chinese":
                return "显示具有插入参数的所有元素。"
            elif first_line == "korean":
                return "삽입된 매개변수를 가진 모든 요소를 표시합니다."
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
                return "Displays only the elements that the inserted parameter has a value."
            elif first_line == "deutsch":
                return "Zeigt nur die Elemente an, bei denen der eingegebene Parameter einen Wert hat."
            elif first_line == "farsi":
                return "تنها المان هایی را نمایش می‌دهد که پارامتر وارد شده دارای مقدار است"
            elif first_line == "russian":
                return "Отображает только элементы, у которых вставленный параметр имеет значение."
            elif first_line == "spanish":
                return "Muestra solo los elementos que el parámetro insertado tiene un valor."
            elif first_line == "chinese":
                return "仅显示具有插入参数值的元素。"
            elif first_line == "korean":
                return "삽입된 매개변수에 값이 있는 요소만 표시합니다."
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
                return "Displays only the elements that the inserted parameter has no value."
            elif first_line == "deutsch":
                return "Zeigt nur die Elemente an, bei denen der eingegebene Parameter keinen Wert hat."
            elif first_line == "farsi":
                return "تنها المان هایی را نمایش می‌دهد که پارامتر وارد شده دارای مقدار نیست"
            elif first_line == "russian":
                return "Отображает только элементы, у которых вставленный параметр не имеет значения."
            elif first_line == "spanish":
                return "Muestra solo los elementos que el parámetro insertado no tiene valor."
            elif first_line == "chinese":
                return "仅显示插入参数没有值的元素。"
            elif first_line == "korean":
                return "삽입된 매개변수에 값이 없는 요소만 표시합니다."
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
                return "Result of check for existance of parameter"
            elif first_line == "deutsch":
                return "Ergebnis der Überprüfung auf Vorhandensein des Parameters"
            elif first_line == "farsi":
                return "نتیجه بررسی برای وجود پارامتر"
            elif first_line == "russian":
                return "Результат проверки на наличие параметра"
            elif first_line == "spanish":
                return "Resultado de la comprobación de la existencia del parámetro"
            elif first_line == "chinese":
                return "参数存在性检查结果"
            elif first_line == "korean":
                return "매개변수 존재 여부 확인 결과"
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
                return "### Check: {}"
            elif first_line == "deutsch":
                return "### Prüfen: {}"
            elif first_line == "farsi":
                return "### بررسی: {}"
            elif first_line == "russian":
                return "### Проверка: {}"
            elif first_line == "spanish":
                return "### Comprobar: {}"
            elif first_line == "chinese":
                return "### 检查: {}"
            elif first_line == "korean":
                return "### 확인: {}"
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
                return "Existence of parameter values in categories"
            elif first_line == "deutsch":
                return "Vorhandensein von Parameterwerten in Kategorien"
            elif first_line == "farsi":
                return "وجود مقادیر پارامترها در دسته‌ بندی ها"
            elif first_line == "russian":
                return "Наличие значений параметров в категориях"
            elif first_line == "spanish":
                return "Existencia de valores de parámetros en categorías"
            elif first_line == "chinese":
                return "参数值在类别中的存在性"
            elif first_line == "korean":
                return "카테고리 내 매개변수 값의 존재"
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
                return "Select"
            elif first_line == "deutsch":
                return "Auswählen"
            elif first_line == "farsi":
                return "انتخاب"
            elif first_line == "russian":
                return "Выбрать"
            elif first_line == "spanish":
                return "Seleccionar"
            elif first_line == "chinese":
                return "选择"
            elif first_line == "korean":
                return "선택"
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
    
def str_25(file_path):
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
    
def str_26(file_path):
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
    
def str_27(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Storage Type"
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