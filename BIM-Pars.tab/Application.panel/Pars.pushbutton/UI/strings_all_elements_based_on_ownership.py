# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_all_elements_based_on_ownership.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Ownership (Only workshared)"
            elif first_line == "deutsch":
                return "Eigentum (Nur gemeinsam genutzt)"
            elif first_line == "farsi":
                return "مالکیت (تنها به اشتراک گذاشته شده)"
            elif first_line == "russian":
                return "Собственность (Только совместное использование)"
            elif first_line == "spanish":
                return "Propiedad (Solo compartido)"
            elif first_line == "chinese":
                return "所有权（仅限共享）"
            elif first_line == "korean":
                return "소유권 (공유 전용)"
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
                return "Owned by me"
            elif first_line == "deutsch":
                return "Von mir besessen"
            elif first_line == "farsi":
                return "متعلق به من"
            elif first_line == "russian":
                return "Мое владение"
            elif first_line == "spanish":
                return "Perteneciente a mí"
            elif first_line == "chinese":
                return "我拥有的"
            elif first_line == "korean":
                return "나의 소유"
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
                return "Owned by X person"
            elif first_line == "deutsch":
                return "Im Besitz von X Person"
            elif first_line == "farsi":
                return "X  متعلق به شخص"
            elif first_line == "russian":
                return "Принадлежит лицу X"
            elif first_line == "spanish":
                return "Perteneciente a la persona X"
            elif first_line == "chinese":
                return "属于X人的所有"
            elif first_line == "korean":
                return "X인이 소유한"
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
                return "No elements found owned by you."
            elif first_line == "deutsch":
                return "Keine von dir besessenen Elemente gefunden."
            elif first_line == "farsi":
                return "هیچ المانی که متعلق به شما باشد یافت نشد"
            elif first_line == "russian":
                return "Не найдено элементов, принадлежащих вам."
            elif first_line == "spanish":
                return "No se encontraron elementos de tu propiedad."
            elif first_line == "chinese":
                return "未找到你拥有的元素。"
            elif first_line == "korean":
                return "당신이 소유한 요소를 찾을 수 없습니다."
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
                return "Model is not shared, you own everything." 
            elif first_line == "deutsch":
                return "Das Modell ist nicht geteilt, du besitzt alles."
            elif first_line == "farsi":
                return "مدل به اشتراک گذاشته نشده است، همه چیز متعلق به شماست"
            elif first_line == "russian":
                return "Модель не разделена, вы владеете всем."
            elif first_line == "spanish":
                return "El modelo no está compartido, tú lo posees todo."
            elif first_line == "chinese":
                return "模型未共享，您拥有全部权利。"
            elif first_line == "korean":
                return "모델이 공유되지 않았으며, 모든 것이 당신의 소유입니다."
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
                return  "Owners"
            elif first_line == "deutsch":
                return "Eigentümer"
            elif first_line == "farsi":
                return "مالکان"
            elif first_line == "russian":
                return "Владельцы"
            elif first_line == "spanish":
                return "Propietarios"
            elif first_line == "chinese":
                return "所有者"
            elif first_line == "korean":
                return "소유자"
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
                return  "No elements found with the specified owner."
            elif first_line == "deutsch":
                return "Keine Elemente mit dem angegebenen Besitzer gefunden."
            elif first_line == "farsi":
                return "هیچ المانی با مالک مشخص شده یافت نشد"
            elif first_line == "russian":
                return "Не найдено элементов с указанным владельцем."
            elif first_line == "spanish":
                return "No se encontraron elementos con el propietario especificado."
            elif first_line == "chinese":
                return "找不到指定所有者的元素。"
            elif first_line == "korean":
                return "지정된 소유자와 관련된 요소를 찾을 수 없습니다."
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
                return  "No owner names found."
            elif first_line == "deutsch":
                return "Keine Namen des Eigentümers gefunden."
            elif first_line == "farsi":
                return "هیچ نام مالکی یافت نشد"
            elif first_line == "russian":
                return "Не найдено имен владельцев."
            elif first_line == "spanish":
                return "No se encontraron nombres de propietarios."
            elif first_line == "chinese":
                return "未找到所有者名称。"
            elif first_line == "korean":
                return "소유자 이름을 찾을 수 없습니다."
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
                return  "No owner selected."
            elif first_line == "deutsch":
                return "Kein Eigentümer ausgewählt."
            elif first_line == "farsi":
                return "هیچ مالکی انتخاب نشده است"
            elif first_line == "russian":
                return "Не выбран владелец."
            elif first_line == "spanish":
                return "No se ha seleccionado propietario."
            elif first_line == "chinese":
                return "未选择所有者。"
            elif first_line == "korean":
                return "소유자가 선택되지 않았습니다."
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
    
def str_14(file_path):
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
    
def str_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Owner"
            elif first_line == "deutsch":
                return "Besitzer"
            elif first_line == "farsi":
                return "مالک"
            elif first_line == "russian":
                return "Владелец"
            elif first_line == "spanish":
                return "Propietario"
            elif first_line == "chinese":
                return "所有者"
            elif first_line == "korean":
                return "소유자"
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
    


