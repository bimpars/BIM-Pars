# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_all_elements_on_selected_levels.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "All elements on selected levels"
            elif first_line == "deutsch":
                return "Alle Elemente auf ausgewählten Ebenen"
            elif first_line == "farsi":
                return "همه المان ها در سطوح انتخاب شده"
            elif first_line == "russian":
                return "Все элементы на выбранных уровнях"
            elif first_line == "spanish":
                return "Todos los elementos en los niveles seleccionados"
            elif first_line == "chinese":
                return "所有选定层级上的元素"
            elif first_line == "korean":
                return "선택된 수준의 모든 요소들"
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
                return "Current view"
            elif first_line == "deutsch":
                return "Aktuelle Ansicht"
            elif first_line == "farsi":
                return "نمای کنونی"
            elif first_line == "russian":
                return "Текущий вид"
            elif first_line == "spanish":
                return "Vista actual"
            elif first_line == "chinese":
                return "当前视图"
            elif first_line == "korean":
                return "현재 보기"
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
                return "Consider other views"
            elif first_line == "deutsch":
                return "Andere Ansichten in Betracht ziehen"
            elif first_line == "farsi":
                return "نماهای دیگر را در نظر بگیرد"
            elif first_line == "russian":
                return "Учтите другие виды"
            elif first_line == "spanish":
                return "Considerar otras vistas"
            elif first_line == "chinese":
                return "考虑其他视图"
            elif first_line == "korean":
                return "다른 보기를 고려하세요"
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
                return "No level available for the selected view."
            elif first_line == "deutsch":
                return "Keine Ebene für die ausgewählte Ansicht verfügbar."
            elif first_line == "farsi":
                return "هیچ سطحی برای نمای انتخاب شده وجود ندارد"
            elif first_line == "russian":
                return "Для выбранного вида нет доступных уровней."
            elif first_line == "spanish":
                return "No hay niveles disponibles para la vista seleccionada."
            elif first_line == "chinese":
                return "选择的视图没有可用的层级。"
            elif first_line == "korean":
                return "선택한 보기에 대해 사용 가능한 레벨이 없습니다."
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
                return "Levels"
            elif first_line == "deutsch":
                return "Ebenen"
            elif first_line == "farsi":
                return "سطوح"
            elif first_line == "russian":
                return "Уровни"
            elif first_line == "spanish":
                return "Niveles"
            elif first_line == "chinese":
                return "层级"
            elif first_line == "korean":
                return "레벨"
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
                return "Select"
            elif first_line == "deutsch":
                return "Auswählen"
            elif first_line == "farsi":
                return "انتخاب کنید"
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

def str_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "No element found."
            elif first_line == "deutsch":
                return "Kein Element gefunden."
            elif first_line == "farsi":
                return "هیچ المانی یافت نشد"
            elif first_line == "russian":
                return "Элемент не найден."
            elif first_line == "spanish":
                return "No se encontró ningún elemento."
            elif first_line == "chinese":
                return "未找到元素。"
            elif first_line == "korean":
                return "요소를 찾을 수 없습니다."
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
                return  "No level selected."
            elif first_line == "deutsch":
                return "Keine Ebene ausgewählt."
            elif first_line == "farsi":
                return "سطحی انتخاب نشده است"
            elif first_line == "russian":
                return "Уровень не выбран."
            elif first_line == "spanish":
                return "No se ha seleccionado ningún nivel."
            elif first_line == "chinese":
                return "未选择层级。"
            elif first_line == "korean":
                return "선택된 레벨이 없습니다."
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
                return  "Views" 
            elif first_line == "deutsch":
                return "Ansichten"
            elif first_line == "farsi":
                return "نماها"
            elif first_line == "russian":
                return "Виды"
            elif first_line == "spanish":
                return "Vistas"
            elif first_line == "chinese":
                return "视图"
            elif first_line == "korean":
                return "보기"
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
                return  "No elements available to select in the level '{level.Name}'."
            elif first_line == "deutsch":
                return "Keine Elemente zum Auswählen in der Ebene '{level.Name}' verfügbar."
            elif first_line == "farsi":
                return "'{level.Name}'هیچ المانی برای سطح انتخاب شده یافت نشد"
            elif first_line == "russian":
                return "Нет доступных элементов для выбора в уровне '{level.Name}'."
            elif first_line == "spanish":
                return "No hay elementos disponibles para seleccionar en el nivel '{level.Name}'."
            elif first_line == "chinese":
                return "在层级 '{level.Name}' 中没有可供选择的元素。"
            elif first_line == "korean":
                return "'{level.Name}' 레벨에서 선택할 수 있는 요소가 없습니다."
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
                return  "No elements available to select in the selected levels."
            elif first_line == "deutsch":
                return "Keine Elemente zum Auswählen in den ausgewählten Ebenen verfügbar."
            elif first_line == "farsi":
                return "هیچ المانی برای انتخاب در سطوح انتخاب شده وجود ندارد"
            elif first_line == "russian":
                return "Нет доступных элементов для выбора в выбранных уровнях."
            elif first_line == "spanish":
                return "No hay elementos disponibles para seleccionar en los niveles seleccionados."
            elif first_line == "chinese":
                return "在所选层级中没有可供选择的元素。"
            elif first_line == "korean":
                return "선택된 레벨에서 선택할 수 있는 요소가 없습니다."
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
                return  "No levels selected or all selected levels have no elements."
            elif first_line == "deutsch":
                return "Keine Ebenen ausgewählt oder alle ausgewählten Ebenen enthalten keine Elemente."
            elif first_line == "farsi":
                return "هیچ سطحی انتخاب نشده است یا تمام سطوح انتخاب شده دارای هیچ المانی نیستند"
            elif first_line == "russian":
                return "Не выбрано ни одного уровня или все выбранные уровни не содержат элементов."
            elif first_line == "spanish":
                return "No se han seleccionado niveles o todos los niveles seleccionados no tienen elementos."
            elif first_line == "chinese":
                return "未选择层级或所有选择的层级均无元素。"
            elif first_line == "korean":
                return "선택된 레벨이 없거나 모든 선택된 레벨에 요소가 없습니다."
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
                return  "No views selected."
            elif first_line == "deutsch":
                return "Keine Ansichten ausgewählt."
            elif first_line == "farsi":
                return "هیچ نمایی انتخاب نشده است"
            elif first_line == "russian":
                return "Не выбрано ни одного вида."
            elif first_line == "spanish":
                return "No se han seleccionado vistas."
            elif first_line == "chinese":
                return "未选择视图。"
            elif first_line == "korean":
                return "선택된 보기가 없습니다."
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
    
def str_15(file_path):
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
    
def str_16(file_path):
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
        return "An error occurred: {}".format(e)
    
def str_17(file_path):
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
    
def str_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "View"
            elif first_line == "deutsch":
                return "Ansicht"
            elif first_line == "farsi":
                return "نما"
            elif first_line == "russian":
                return "Просмотр"
            elif first_line == "spanish":
                return "Vista"
            elif first_line == "chinese":
                return "视图"
            elif first_line == "korean":
                return "보기"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    
def str_19(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Level"
            elif first_line == "deutsch":
                return "Ebene"
            elif first_line == "farsi":
                return "سطح"
            elif first_line == "russian":
                return "Уровень"
            elif first_line == "spanish":
                return "Nivel"
            elif first_line == "chinese":
                return "级别"
            elif first_line == "korean":
                return "수준"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    
def str_20(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No Level"
            elif first_line == "deutsch":
                return "Keine Ebene"
            elif first_line == "farsi":
                return "بدون سطح"
            elif first_line == "russian":
                return "Нет уровня"
            elif first_line == "spanish":
                return "Sin nivel"
            elif first_line == "chinese":
                return "没有层"
            elif first_line == "korean":
                return "레벨 없음"
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
                return "No Category"
            elif first_line == "deutsch":
                return "Keine Kategorie"
            elif first_line == "farsi":
                return "بدون دسته‌بندی"
            elif first_line == "russian":
                return "Нет категории"
            elif first_line == "spanish":
                return "Sin categoría"
            elif first_line == "chinese":
                return "没有类别"
            elif first_line == "korean":
                return "카테고리 없음"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    

    



