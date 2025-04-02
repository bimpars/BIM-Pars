# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_reduce_selection_based_on_existance_of_parameter_value.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Reduce Selection By Parameter value for exist"
            elif first_line == "deutsch":
                return "Reduziere Auswahl um Parameterwert für Vorhandenes"
            elif first_line == "farsi":
                return "کاهش انتخاب با مقدار پارامتر برای موجودیت"
            elif first_line == "russian":
                return "Уменьшить выборку на величину параметра для существующих"
            elif first_line == "spanish":
                return "Reducir selección por el valor del parámetro para existentes"
            elif first_line == "chinese":
                return "按参数值减少现有选择"
            elif first_line == "korean":
                return "기존의 매개변수 값에 따른 선택 감소"
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
                return "Please select at least one element."
            elif first_line == "deutsch":
                return "Bitte wähle mindestens ein Element aus."
            elif first_line == "farsi":
                return "لطفاً حداقل یک المان را انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, выберите хотя бы один элемент."
            elif first_line == "spanish":
                return "Por favor, selecciona al menos un elemento."
            elif first_line == "chinese":
                return "请至少选择一个元素。"
            elif first_line == "korean":
                return "최소한 하나의 요소를 선택해주세요."
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
                return "Both with value and with no value"
            elif first_line == "deutsch":
                return "Sowohl mit Wert als auch ohne Wert"
            elif first_line == "farsi":
                return "با مقدار و بدون مقدار"
            elif first_line == "russian":
                return "И с значением, и без значения"
            elif first_line == "spanish":
                return "Ambos con valor y sin valor"
            elif first_line == "chinese":
                return "既有值又无值"
            elif first_line == "korean":
                return "값이 있는 것과 값이 없는 것 모두"
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
                return "Reduces from selection all elements that have the inserted parameter"
            elif first_line == "deutsch":
                return "Reduziert aus der Auswahl alle Elemente, die den eingefügten Parameter haben"
            elif first_line == "farsi":
                return "از انتخاب تمام المان هایی که پارامتر وارد شده را دارند، کاهش می‌دهد"
            elif first_line == "russian":
                return "Удаляет из выборки все элементы, имеющие вставленный параметр"
            elif first_line == "spanish":
                return "Reduce de la selección todos los elementos que tienen el parámetro insertado"
            elif first_line == "chinese":
                return "从选择中减去具有插入参数的所有元素"
            elif first_line == "korean":
                return "삽입된 매개변수를 갖는 모든 요소를 선택에서 제거합니다"
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
                return "Reduces from selection only the elements that inserted parameter has value"
            elif first_line == "deutsch":
                return "Reduziert aus der Auswahl nur die Elemente, bei denen der eingefügte Parameter einen Wert hat"
            elif first_line == "farsi":
                return "تنها المان هایی را کاهش می‌دهد که پارامتر وارد شده مقدار دارد"
            elif first_line == "russian":
                return "Уменьшает выборку только элементов, у которых вставленный параметр имеет значение"
            elif first_line == "spanish":
                return "Reduce de la selección solo los elementos que el parámetro insertado tiene valor"
            elif first_line == "chinese":
                return "只从选择中减少插入参数具有值的元素"
            elif first_line == "korean":
                return "삽입된 매개변수가 값을 갖는 요소만 선택에서 제거합니다"
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
                return "Reduces from selection only the elements that inserted parameter has no value"
            elif first_line == "deutsch":
                return "Reduziert aus der Auswahl nur die Elemente, bei denen der eingefügte Parameter keinen Wert hat"
            elif first_line == "farsi":
                return "تنها المان هایی را کاهش می‌دهد که پارامتر وارد شده مقدار ندارد"
            elif first_line == "russian":
                return "Уменьшает выборку только элементов, у которых вставленный параметр не имеет значения"
            elif first_line == "spanish":
                return "Reduce de la selección solo los elementos que el parámetro insertado no tiene valor"
            elif first_line == "chinese":
                return "只从选择中减少插入参数没有值的元素"
            elif first_line == "korean":
                return "삽입된 매개변수가 값을 갖지 않는 요소만 선택에서 제거합니다"
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
    
def str_14(file_path):
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
    
def str_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No elements found for the selected categories."
            elif first_line == "deutsch":
                return "Keine Elemente für die ausgewählten Kategorien gefunden."
            elif first_line == "farsi":
                return "هیچ المانی برای دسته‌بندی‌های انتخاب شده یافت نشد"
            elif first_line == "russian":
                return "Не найдено элементов для выбранных категорий."
            elif first_line == "spanish":
                return "No se encontraron elementos para las categorías seleccionadas."
            elif first_line == "chinese":
                return "未找到所选分类的任何元素。"
            elif first_line == "korean":
                return "선택한 카테고리에 대한 요소를 찾을 수 없습니다."
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
                return "No element left in selection."
            elif first_line == "deutsch":
                return "In der Auswahl sind keine Elemente mehr verfügbar."
            elif first_line == "farsi":
                return "هیچ المانی در انتخاب باقی نمانده است"
            elif first_line == "russian":
                return "В выборке больше нет элементов."
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
    
def str_17(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No parameter inserted."
            elif first_line == "deutsch":
                return "Kein Parameter eingefügt."
            elif first_line == "farsi":
                return "هیچ پارامتری وارد نشده است"
            elif first_line == "russian":
                return "Не вставлено ни одного параметра."
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
    
def str_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Existence of parameter's values"
            elif first_line == "deutsch":
                return "Vorhandensein von Parameterwerten"
            elif first_line == "farsi":
                return "وجود مقادیر پارامترها"
            elif first_line == "russian":
                return "Наличие значений параметров"
            elif first_line == "spanish":
                return "Existencia de valores de parámetros"
            elif first_line == "chinese":
                return "参数值的存在"
            elif first_line == "korean":
                return "매개변수 값의 존재"
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
    
def str_20(file_path):
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
    
def str_21(file_path):
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

def str_22(file_path):
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