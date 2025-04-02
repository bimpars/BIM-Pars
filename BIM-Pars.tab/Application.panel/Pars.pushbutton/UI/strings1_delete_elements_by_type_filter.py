# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings1_delete_element_by_type_filter.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select Category"
            elif first_line == "deutsch":
                return "Kategorie auswählen"
            elif first_line == "farsi":
                return "دسته بندی را انتخاب کنید"
            elif first_line == "russian":
                return "Выберите категорию"
            elif first_line == "spanish":
                return "Seleccionar categoría"
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
    
def str_2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Category" 
            elif first_line == "deutsch":
                return "Kategorie"
            elif first_line == "farsi":
                return "دسته بندی"
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
                return  "Select Family"
            elif first_line == "deutsch":
                return "Familie auswählen"
            elif first_line == "farsi":
                return "انتخاب خانواده"
            elif first_line == "russian":
                return "Выберите семейство"
            elif first_line == "spanish":
                return "Seleccionar familia"
            elif first_line == "chinese":
                return "选择家族"
            elif first_line == "korean":
                return "가족 선택"
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
    
def str_5(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "All"
            elif first_line == "deutsch":
                return "Alle"
            elif first_line == "farsi":
                return "همه"
            elif first_line == "russian":
                return "Все"
            elif first_line == "spanish":
                return "Todos"
            elif first_line == "chinese":
                return "全部"
            elif first_line == "korean":
                return "모두"
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
                return  "Family Names, Types, and Element IDs:"
            elif first_line == "deutsch":
                return "Familiennamen, Typen und Element-IDs:"
            elif first_line == "farsi":
                return "نام‌های خانواده، انواع و شناسه المان ها:"
            elif first_line == "russian":
                return "Имена семейств, типы и идентификаторы элементов:"
            elif first_line == "spanish":
                return "Nombres de familia, tipos e IDs de elementos:"
            elif first_line == "chinese":
                return "族名、类型和元素ID:"
            elif first_line == "korean":
                return "패밀리 이름, 타입 및 요소 ID:"
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
                return  "- Family Name: "
            elif first_line == "deutsch":
                return "- Familienname: "
            elif first_line == "farsi":
                return "- نام خانواده: "
            elif first_line == "russian":
                return "- Фамилия: "
            elif first_line == "spanish":
                return "- Apellido familiar: "
            elif first_line == "chinese":
                return "- 族名: "
            elif first_line == "korean":
                return "- 가족 이름: "
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
                return  " - Type Name: "
            elif first_line == "deutsch":
                return " - Typname: "
            elif first_line == "farsi":
                return " - نام نوع: "
            elif first_line == "russian":
                return " - Название типа: "
            elif first_line == "spanish":
                return " - Nombre del tipo: "
            elif first_line == "chinese":
                return " - 类型名称: "
            elif first_line == "korean":
                return " - 타입 이름: "
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
                return  "Select Type"
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
                return "유형 선택"
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
                return  "Type"
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
    
def str_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Selected Family Name: " 
            elif first_line == "deutsch":
                return "Ausgewählter Familienname: "
            elif first_line == "farsi":
                return "نام خانواده انتخاب شده: "
            elif first_line == "russian":
                return "Выбранное имя семейства: "
            elif first_line == "spanish":
                return "Nombre de familia seleccionado: "
            elif first_line == "chinese":
                return "选定的族名: "
            elif first_line == "korean":
                return "선택한 가족 이름: "
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
                return  "Selected Type Name: "
            elif first_line == "deutsch":
                return "Ausgewählter Typname: "
            elif first_line == "farsi":
                return "نام نوع انتخاب شده: "
            elif first_line == "russian":
                return "Выбранное название типа: "
            elif first_line == "spanish":
                return "Nombre de tipo seleccionado: "
            elif first_line == "chinese":
                return "选定的类型名称: "
            elif first_line == "korean":
                return "선택한 타입 이름: "
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
                return  "Element IDs:"
            elif first_line == "deutsch":
                return "Element-IDs:"
            elif first_line == "farsi":
                return "شناسه المان ها:"
            elif first_line == "russian":
                return "Идентификаторы элементов:"
            elif first_line == "spanish":
                return "IDs de elementos:"
            elif first_line == "chinese":
                return "元素ID:"
            elif first_line == "korean":
                return "요소 ID:"
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
                return  "No type selected."
            elif first_line == "deutsch":
                return "Kein Typ ausgewählt."
            elif first_line == "farsi":
                return "هیچ نوعی انتخاب نشده است"
            elif first_line == "russian":
                return "Ningún tipo seleccionado."
            elif first_line == "spanish":
                return "Nombre de tipo seleccionado: "
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
    
def str_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "No family selected."
            elif first_line == "deutsch":
                return "Keine Familie ausgewählt."
            elif first_line == "farsi":
                return "هیچ خانواده‌ای انتخاب نشده است"
            elif first_line == "russian":
                return "Семья не выбрана."
            elif first_line == "spanish":
                return "Ninguna familia seleccionada."
            elif first_line == "chinese":
                return "未选择家族。"
            elif first_line == "korean":
                return "선택된 가족이 없습니다."
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
                return  "The selected category does not have valid families or types."
            elif first_line == "deutsch":
                return "Die ausgewählte Kategorie enthält keine gültigen Familien oder Typen."
            elif first_line == "farsi":
                return "دسته بندی انتخاب شده شامل خانواده‌ها یا انواع معتبری نمی‌باشد"
            elif first_line == "russian":
                return "Выбранная категория не содержит действительных семейств или типов."
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
    
def str_17(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Invalid Category"
            elif first_line == "deutsch":
                return "Ungültige Kategorie"
            elif first_line == "farsi":
                return "دسته بندی نامعتبر"
            elif first_line == "russian":
                return "Недопустимая категория"
            elif first_line == "spanish":
                return "Categoría inválida"
            elif first_line == "chinese":
                return "无效类别"
            elif first_line == "korean":
                return "유효하지 않은 카테고리"
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
                return  "Failed to iterate. It might be due to selecting an invalid category or disturbing the process during iteration."
            elif first_line == "deutsch":
                return "Fehler beim Iterieren. Dies könnte auf die Auswahl einer ungültigen Kategorie oder auf eine Störung des Vorgangs während der Iteration zurückzuführen sein."
            elif first_line == "farsi":
                return "خطا در تکرار. این ممکن است به دلیل انتخاب دسته بندی نامعتبر یا مزاحمت در فرآیند تکرار باشد"
            elif first_line == "russian":
                return "Не удалось выполнить итерацию. Это может быть связано с выбором недопустимой категории или нарушением процесса во время итерации."
            elif first_line == "spanish":
                return "No se pudo iterar. Esto podría ser debido a la selección de una categoría inválida o a interrumpir el proceso durante la iteración."
            elif first_line == "chinese":
                return "迭代失败。可能是因为选择了无效的类别或在迭代过程中干扰了该过程。"
            elif first_line == "korean":
                return "반복에 실패했습니다. 이는 유효하지 않은 카테고리를 선택하거나 반복 중에 프로세스가 중단되었을 수 있습니다."
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
                return  "Error"
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
                return  "No category selected."
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