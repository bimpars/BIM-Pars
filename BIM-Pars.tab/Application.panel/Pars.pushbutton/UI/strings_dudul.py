# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_dudul.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "DUDUL"
            elif first_line == "deutsch":
                return "DUDUL"
            elif first_line == "farsi":
                return "دودول"
            elif first_line == "russian":
                return "DUDUL"
            elif first_line == "spanish":
                return "DUDUL"
            elif first_line == "chinese":
                return "DUDUL"
            elif first_line == "korean":
                return "DUDUL"
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
                return "View"
            elif first_line == "deutsch":
                return "Ansicht"
            elif first_line == "farsi":
                return "نما"
            elif first_line == "russian":
                return "Вид"
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
        return "An error occurred: {e}"
    
def str_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Any View"
            elif first_line == "deutsch":
                return "Beliebige Ansicht"
            elif first_line == "farsi":
                return "هر نمایی"
            elif first_line == "russian":
                return "Любой вид"
            elif first_line == "spanish":
                return "Cualquier vista"
            elif first_line == "chinese":
                return "任意视图"
            elif first_line == "korean":
                return "임의의 보기"
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
                return "레벨"
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
    
def str_6(file_path):
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
                return "家庭"
            elif first_line == "korean":
                return "가족"
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
    
def str_8(file_path): 
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Existence of parameter"
            elif first_line == "deutsch":
                return "Existenz des Parameters"
            elif first_line == "farsi":
                return "وجود پارامتر"
            elif first_line == "russian":
                return "Существование параметра"
            elif first_line == "spanish":
                return "Existencia del parámetro"
            elif first_line == "chinese":
                return "参数的存在"
            elif first_line == "korean":
                return "매개변수의 존재"
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
                return "Parameter value"
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
    
def str_10(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Ownership"
            elif first_line == "deutsch":
                return "Eigentum"
            elif first_line == "farsi":
                return "مالکیت"
            elif first_line == "russian":
                return "Собственность"
            elif first_line == "spanish":
                return "Propiedad"
            elif first_line == "chinese":
                return "所有权"
            elif first_line == "korean":
                return "소유권"
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
                return "Modified by"
            elif first_line == "deutsch":
                return "Geändert von"
            elif first_line == "farsi":
                return "تغییر داده شده توسط"
            elif first_line == "russian":
                return "Изменено пользователем"
            elif first_line == "spanish":
                return "Modificado por"
            elif first_line == "chinese":
                return "修改者"
            elif first_line == "korean":
                return "수정자"
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
                return "Creator"
            elif first_line == "deutsch":
                return "Ersteller"
            elif first_line == "farsi":
                return "ایجاد کننده"
            elif first_line == "russian":
                return "Создатель"
            elif first_line == "spanish":
                return "Creador"
            elif first_line == "chinese":
                return "创建者"
            elif first_line == "korean":
                return "생성자"
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
                return "Root"
            elif first_line == "deutsch":
                return "Wurzel"
            elif first_line == "farsi":
                return "ریشه"
            elif first_line == "russian":
                return "Корень"
            elif first_line == "spanish":
                return "Raíz"
            elif first_line == "chinese":
                return "根"
            elif first_line == "korean":
                return "루트"
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
                return  "String In parameter Value"
            elif first_line == "deutsch":
                return "Zeichenkette im Parameterwert"
            elif first_line == "farsi":
                return "رشته در مقدار پارامتر"
            elif first_line == "russian":
                return "Строка в значении параметра"
            elif first_line == "spanish":
                return "Cadena en el valor del parámetro"
            elif first_line == "chinese":
                return "字符串在参数值中"
            elif first_line == "korean":
                return "매개변수 값에 있는 문자열"
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
                return  "Number In parameter Value"
            elif first_line == "deutsch":
                return "Zahl im Parameterwert"
            elif first_line == "farsi":
                return "عدد در مقدار پارامتر"
            elif first_line == "russian":
                return "Число в значении параметра"
            elif first_line == "spanish":
                return "Número en el valor del parámetro"
            elif first_line == "chinese":
                return "数字在参数值中"
            elif first_line == "korean":
                return "매개변수 값에 있는 숫자"
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
                return  "Elements:"
            elif first_line == "deutsch":
                return "Elemente:"
            elif first_line == "farsi":
                return "المانها:"
            elif first_line == "russian":
                return "Элементы:"
            elif first_line == "spanish":
                return "Elementos:"
            elif first_line == "chinese":
                return "元素："
            elif first_line == "korean":
                return "요소:"
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
                return "-> View|"
            elif first_line == "deutsch":
                return "-> Ansicht|"
            elif first_line == "farsi":
                return "-> نما|"
            elif first_line == "russian":
                return "-> Вид|"
            elif first_line == "spanish":
                return "-> Vista|"
            elif first_line == "chinese":
                return "-> 视图|"
            elif first_line == "korean":
                return "-> 보기|"
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
                return "Views"
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
 
def str_19(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Operation Canceled."
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
 
def str_20(file_path):
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
 
def str_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  " -> Level|"
            elif first_line == "deutsch":
                return " -> Ebene|"
            elif first_line == "farsi":
                return " -> سطح|"
            elif first_line == "russian":
                return " -> Уровень|"
            elif first_line == "spanish":
                return " -> Nivel|"
            elif first_line == "chinese":
                return " -> 层级|"
            elif first_line == "korean":
                return " -> 레벨|"
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
    
def str_23(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return " -> Category|"
            elif first_line == "deutsch":
                return " -> Kategorie|"
            elif first_line == "farsi":
                return " -> دسته بندی|"
            elif first_line == "russian":
                return " -> Категория|"
            elif first_line == "spanish":
                return " -> Categoría|"
            elif first_line == "chinese":
                return " -> 类别|"
            elif first_line == "korean":
                return " -> 카테고리|"
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
    
def str_25(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Categories"
            elif first_line == "deutsch":
                return "Kategorien"
            elif first_line == "farsi":
                return "دسته‌بندها"
            elif first_line == "russian":
                return "Категории"
            elif first_line == "spanish":
                return "Categorías"
            elif first_line == "chinese":
                return "分类"
            elif first_line == "korean":
                return "카테고리"
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
                return "No elements with the selected category found."
            elif first_line == "deutsch":
                return "Es wurden keine Elemente mit der ausgewählten Kategorie gefunden."
            elif first_line == "farsi":
                return "هیچ المانی با دسته بندی انتخاب شده یافت نشد"
            elif first_line == "russian":
                return "Элементы с выбранной категорией не найдены."
            elif first_line == "spanish":
                return "No se encontraron elementos con la categoría seleccionada."
            elif first_line == "chinese":
                return "未找到具有所选类别的元素。"
            elif first_line == "korean":
                return "선택한 카테고리의 요소를 찾을 수 없습니다."
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
                return " -> Ownership|"
            elif first_line == "deutsch":
                return " -> Besitz|"
            elif first_line == "farsi":
                return " -> مالکیت|"
            elif first_line == "russian":
                return " -> Владение|"
            elif first_line == "spanish":
                return " -> Propiedad|"
            elif first_line == "chinese":
                return " -> 所有权|"
            elif first_line == "korean":
                return " -> 소유권|"
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
                return "Selection is empty."
            elif first_line == "deutsch":
                return "Auswahl ist leer."
            elif first_line == "farsi":
                return "انتخاب خالی است"
            elif first_line == "russian":
                return "Выбор пуст."
            elif first_line == "spanish":
                return "La selección está vacía."
            elif first_line == "chinese":
                return "选择为空。"
            elif first_line == "korean":
                return "선택이 비어 있습니다."
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
                return "Owners"
            elif first_line == "deutsch":
                return "Besitzer"
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
    
def str_30(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No elements found with the specified owner."
            elif first_line == "deutsch":
                return "Es wurden keine Elemente mit dem angegebenen Besitzer gefunden."
            elif first_line == "farsi":
                return "هیچ المانی با مالک مشخص شده یافت نشد"
            elif first_line == "russian":
                return "Элементы с указанным владельцем не найдены."
            elif first_line == "spanish":
                return "No se encontraron elementos con el propietario especificado."
            elif first_line == "chinese":
                return "未找到具有指定所有者的元素。"
            elif first_line == "korean":
                return "지정된 소유자로 찾을 수 있는 요소가 없습니다."
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
                return  "No owner selected."
            elif first_line == "deutsch":
                return "Kein Besitzer ausgewählt."
            elif first_line == "farsi":
                return "هیچ مالکی انتخاب نشده است"
            elif first_line == "russian":
                return "Не выбран владелец."
            elif first_line == "spanish":
                return "No se ha seleccionado propietario."
            elif first_line == "chinese":
                return "未选择所有者。"
            elif first_line == "korean":
                return "선택된 소유자가 없습니다."
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
                return "No owner names found."
            elif first_line == "deutsch":
                return "Keine Besitzernamen gefunden."
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
 
def str_33(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return " -> Modified by|"
            elif first_line == "deutsch":
                return " -> Geändert von|"
            elif first_line == "farsi":
                return " -> تغییر داده شده توسط|"
            elif first_line == "russian":
                return " -> Изменено|"
            elif first_line == "spanish":
                return " -> Modificado por|"
            elif first_line == "chinese":
                return " -> 修改者|"
            elif first_line == "korean":
                return " -> 수정자|"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
 
def str_34(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Users"
            elif first_line == "deutsch":
                return "Benutzer"
            elif first_line == "farsi":
                return "کاربران"
            elif first_line == "russian":
                return "Пользователи"
            elif first_line == "spanish":
                return "Usuarios"
            elif first_line == "chinese":
                return "用户"
            elif first_line == "korean":
                return "사용자"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_35(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No elements found."
            elif first_line == "deutsch":
                return "Keine Elemente gefunden."
            elif first_line == "farsi":
                return "هیچ المانی یافت نشد"
            elif first_line == "russian":
                return "Элементы не найдены."
            elif first_line == "spanish":
                return "No se encontraron elementos."
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
    
def str_36(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No user selected."
            elif first_line == "deutsch":
                return "Kein Benutzer ausgewählt."
            elif first_line == "farsi":
                return "هیچ کاربری انتخاب نشده است"
            elif first_line == "russian":
                return "Пользователь не выбран."
            elif first_line == "spanish":
                return "No se ha seleccionado ningún usuario."
            elif first_line == "chinese":
                return "未选择用户。"
            elif first_line == "korean":
                return "선택된 사용자가 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_37(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No names found."
            elif first_line == "deutsch":
                return "Keine Namen gefunden."
            elif first_line == "farsi":
                return "هیچ نامی یافت نشد"
            elif first_line == "russian":
                return "Имена не найдены."
            elif first_line == "spanish":
                return "No se encontraron nombres."
            elif first_line == "chinese":
                return "未找到名称。"
            elif first_line == "korean":
                return "이름을 찾을 수 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_38(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return " -> Family|"
            elif first_line == "deutsch":
                return " -> Familie|"
            elif first_line == "farsi":
                return " -> خانواده|"
            elif first_line == "russian":
                return " -> Семья|"
            elif first_line == "spanish":
                return " -> Familia|"
            elif first_line == "chinese":
                return " -> 家庭|"
            elif first_line == "korean":
                return " -> 가족|"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_39(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Families"
            elif first_line == "deutsch":
                return "Familien"
            elif first_line == "farsi":
                return "خانواده‌ها"
            elif first_line == "russian":
                return "Семьи"
            elif first_line == "spanish":
                return "Familias"
            elif first_line == "chinese":
                return "家庭"
            elif first_line == "korean":
                return "가족들"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_40(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No elements with the selected family found."
            elif first_line == "deutsch":
                return "Es wurden keine Elemente mit der ausgewählten Familie gefunden."
            elif first_line == "farsi":
                return "هیچ المانی با خانواده انتخاب شده یافت نشد"
            elif first_line == "russian":
                return "Элементы с выбранной семьей не найдены."
            elif first_line == "spanish":
                return "No se encontraron elementos con la familia seleccionada."
            elif first_line == "chinese":
                return "未找到具有所选家庭的元素。"
            elif first_line == "korean":
                return "未找到具有所选家庭的元素。"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_41(file_path): 
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return " -> Existance of parameter|"
            elif first_line == "deutsch":
                return " -> Vorhandensein des Parameters|"
            elif first_line == "farsi":
                return " -> وجود پارامتر|"
            elif first_line == "russian":
                return " -> Наличие параметра|"
            elif first_line == "spanish":
                return " -> Existencia del parámetro|"
            elif first_line == "chinese":
                return " -> 参数存在|"
            elif first_line == "korean":
                return " -> 매개변수의 존재|"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_42(file_path):
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
                return "参数:"
            elif first_line == "korean":
                return "매개변수:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_43(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No Element found. Parameter is invalid or type parameter." 
            elif first_line == "deutsch":
                return "Kein Element gefunden. Parameter ist ungültig oder vom falschen Typ."
            elif first_line == "farsi":
                return "هیچ المانی یافت نشد. پارامتر نامعتبر است یا پارامتر نوع نادرستی است"
            elif first_line == "russian":
                return "Элемент не найден. Параметр недействителен или имеет неверный тип."
            elif first_line == "spanish":
                return "No se encontró ningún elemento. El parámetro es inválido o tiene un tipo incorrecto."
            elif first_line == "chinese":
                return "未找到元素。参数无效或参数类型错误。"
            elif first_line == "korean":
                return "요소를 찾을 수 없습니다. 매개변수가 잘못되었거나 유형이 잘못되었습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_44(file_path):
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
    
def str_45(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "No elements found with the specified value for the selected parameter."
            elif first_line == "deutsch":
                return "Es wurden keine Elemente mit dem angegebenen Wert für den ausgewählten Parameter gefunden."
            elif first_line == "farsi":
                return "هیچ المانی با مقدار مشخص شده برای پارامتر انتخاب شده یافت نشد"
            elif first_line == "russian":
                return "Элементы с указанным значением для выбранного параметра не найдены."
            elif first_line == "spanish":
                return "No se encontraron elementos con el valor especificado para el parámetro seleccionado."
            elif first_line == "chinese":
                return "未找到具有所选参数指定值的元素。"
            elif first_line == "korean":
                return "선택한 매개변수에 지정된 값으로 요소를 찾을 수 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_46(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Value:"
            elif first_line == "deutsch":
                return "Wert:"
            elif first_line == "farsi":
                return "مقدار:"
            elif first_line == "russian":
                return "Значение:"
            elif first_line == "spanish":
                return "Valor:"
            elif first_line == "chinese":
                return "值:"
            elif first_line == "korean":
                return "값:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_47(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No specific value inserted."
            elif first_line == "deutsch":
                return "Kein bestimmter Wert eingegeben."
            elif first_line == "farsi":
                return "هیچ مقدار مشخصی وارد نشده است"
            elif first_line == "russian":
                return "Не введено конкретное значение."
            elif first_line == "spanish":
                return "No se ha insertado un valor específico."
            elif first_line == "chinese":
                return "未插入特定值。"
            elif first_line == "korean":
                return "특정한 값이 입력되지 않았습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_48(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "  Parameter:  "
            elif first_line == "deutsch":
                return "  Parameter:  "
            elif first_line == "farsi":
                return "  پارامتر:  "
            elif first_line == "russian":
                return "  Параметр:  "
            elif first_line == "spanish":
                return "  Parámetro:  "
            elif first_line == "chinese":
                return "  参数:  "
            elif first_line == "korean":
                return "  매개변수:  "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_49(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "  and Value:  "
            elif first_line == "deutsch":
                return "  und Wert:  "
            elif first_line == "farsi":
                return "  و مقدار:  "
            elif first_line == "russian":
                return "  и Значение:  "
            elif first_line == "spanish":
                return "  y Valor:  "
            elif first_line == "chinese":
                return "  和 值:  "
            elif first_line == "korean":
                return "  와 값:  "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_50(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return " -> Type|"
            elif first_line == "deutsch":
                return " -> Typ|"
            elif first_line == "farsi":
                return " -> نوع|"
            elif first_line == "russian":
                return " -> Тип|"
            elif first_line == "spanish":
                return " -> Tipo|"
            elif first_line == "chinese":
                return " -> 类型|"
            elif first_line == "korean":
                return " -> 유형|"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_51(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No elements with the selected type found."
            elif first_line == "deutsch":
                return "Es wurden keine Elemente mit dem ausgewählten Typ gefunden."
            elif first_line == "farsi":
                return "هیچ المانی با نوع انتخاب شده یافت نشد"
            elif first_line == "russian":
                return "Элементы с выбранным типом не найдены."
            elif first_line == "spanish":
                return "No se encontraron elementos con el tipo seleccionado."
            elif first_line == "chinese":
                return "未找到具有所选类型的元素。"
            elif first_line == "korean":
                return "선택한 유형의 요소를 찾을 수 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_52(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Types"
            elif first_line == "deutsch":
                return "Typen"
            elif first_line == "farsi":
                return "انواع"
            elif first_line == "russian":
                return "Типы"
            elif first_line == "spanish":
                return "Tipos"
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
    
def str_53(file_path):  
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return " -> Creator|"
            elif first_line == "deutsch":
                return " -> Ersteller|"
            elif first_line == "farsi":
                return " -> سازنده|"
            elif first_line == "russian":
                return " -> Создатель|"
            elif first_line == "spanish":
                return " -> Creador|"
            elif first_line == "chinese":
                return " -> 创建者|"
            elif first_line == "korean":
                return " -> 생성자|"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_54(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Creators"
            elif first_line == "deutsch":
                return "Ersteller"
            elif first_line == "farsi":
                return "سازندگان"
            elif first_line == "russian":
                return "Создатели"
            elif first_line == "spanish":
                return "Creadores"
            elif first_line == "chinese":
                return "创建者"
            elif first_line == "korean":
                return "생성자들"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_55(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No elements found with the specified creator."
            elif first_line == "deutsch":
                return "Es wurden keine Elemente mit dem angegebenen Ersteller gefunden."
            elif first_line == "farsi":
                return "هیچ المانی با سازنده مشخص شده یافت نشد"
            elif first_line == "russian":
                return "Элементы с указанным создателем не найдены."
            elif first_line == "spanish":
                return "No se encontraron elementos con el creador especificado."
            elif first_line == "chinese":
                return "未找到具有指定创建者的元素。"
            elif first_line == "korean":
                return "지정된 생성자를 가진 요소를 찾을 수 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_56(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No creator selected."
            elif first_line == "deutsch":
                return "Kein Ersteller ausgewählt."
            elif first_line == "farsi":
                return "هیچ سازنده‌ای انتخاب نشده است"
            elif first_line == "russian":
                return "Не выбран создатель."
            elif first_line == "spanish":
                return "No se ha seleccionado un creador."
            elif first_line == "chinese":
                return "未选择创建者。"
            elif first_line == "korean":
                return "선택된 생성자가 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_57(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please try again: An error happened in one of the stages and broke the root."
            elif first_line == "deutsch":
                return "Bitte versuchen Sie es erneut: Es ist ein Fehler in einem der Schritte aufgetreten und hat den Vorgang unterbrochen."
            elif first_line == "farsi":
                return "لطفا مجددا تلاش کنید: در یکی از مراحل خطا رخ داده است و ریشه را شکسته است"
            elif first_line == "russian":
                return "Пожалуйста, попробуйте еще раз: Произошла ошибка на одной из стадий, что привело к нарушению корневого элемента."
            elif first_line == "spanish":
                return "Por favor, inténtelo de nuevo: Se produjo un error en una de las etapas y rompió el proceso principal."
            elif first_line == "chinese":
                return "请重试：在其中一个阶段发生了错误，破坏了根部。"
            elif first_line == "korean":
                return "다시 시도해주세요: 단계 중 하나에서 오류가 발생하여 루트가 손상되었습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_58(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "It happens if you insert wrong data or cancel any of the stages during filter."
            elif first_line == "deutsch":
                return "Das passiert, wenn Sie falsche Daten eingeben oder eine der Stufen während des Filters abbrechen."
            elif first_line == "farsi":
                return "این اتفاق می افتد اگر شما داده های نادرستی وارد کنید یا در هر یک از مراحل در حین فیلتر کردن انصراف دهید"
            elif first_line == "russian":
                return "Это происходит, если вы вводите неправильные данные или отменяете любую из стадий во время фильтрации."
            elif first_line == "spanish":
                return "Esto sucede si insertas datos incorrectos o cancelas alguna de las etapas durante el filtro."
            elif first_line == "chinese":
                return "如果您插入了错误的数据或在过滤过程中取消了任何阶段，就会发生这种情况。"
            elif first_line == "korean":
                return "잘못된 데이터를 입력하거나 필터 중에 단계를 취소하면 이런 일이 발생합니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_59(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No element is in filter"
            elif first_line == "deutsch":
                return "Kein Element befindet sich im Filter."
            elif first_line == "farsi":
                return "هیچ المانی در فیلتر وجود ندارد"
            elif first_line == "russian":
                return "В фильтре нет элементов."
            elif first_line == "spanish":
                return "No hay ningún elemento en el filtro."
            elif first_line == "chinese":
                return "过滤器中没有元素。"
            elif first_line == "korean":
                return "필터에 요소가 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_60(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "- Filter Root: "
            elif first_line == "deutsch":
                return "- Filterstamm: "
            elif first_line == "farsi":
                return "- ریشه فیلتر: "
            elif first_line == "russian":
                return "- Фильтр корневой элемент: "
            elif first_line == "spanish":
                return "- Raíz del filtro: "
            elif first_line == "chinese":
                return "- 过滤器根："
            elif first_line == "korean":
                return "- 필터 루트: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_61(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return " -> Parameter value|"
            elif first_line == "deutsch":
                return " -> Parameterwert|"
            elif first_line == "farsi":
                return " -> مقدار پارامتر|"
            elif first_line == "russian":
                return " -> Значение параметра|"
            elif first_line == "spanish":
                return " -> Valor del parámetro|"
            elif first_line == "chinese":
                return " -> 参数值|"
            elif first_line == "korean":
                return " -> 매개변수 값|"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_62(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "-> String In parameter Value|"
            elif first_line == "deutsch":
                return "-> Zeichenkette im Parameterwert|"
            elif first_line == "farsi":
                return "-> رشته در مقدار پارامتر|"
            elif first_line == "russian":
                return "-> Строка в значении параметра|"
            elif first_line == "spanish":
                return "-> Cadena en el valor del parámetro|"
            elif first_line == "chinese":
                return "-> 字符串在参数值中|"
            elif first_line == "korean":
                return "-> 매개변수 값에 있는 문자열|"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_63(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "-> Number In parameter Value|"
            elif first_line == "deutsch":
                return "-> Zahl im Parameterwert|"
            elif first_line == "farsi":
                return "-> عدد در مقدار پارامتر|"
            elif first_line == "russian":
                return "-> Число в значении параметра|"
            elif first_line == "spanish":
                return "-> Número en el valor del parámetro|"
            elif first_line == "chinese":
                return "-> 数字在参数值中|"
            elif first_line == "korean":
                return "-> 매개변수 값에 있는 숫자|"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_64(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "number"
            elif first_line == "deutsch":
                return "Nummer"
            elif first_line == "farsi":
                return "عدد"
            elif first_line == "russian":
                return "число"
            elif first_line == "spanish":
                return "número"
            elif first_line == "chinese":
                return "数字"
            elif first_line == "korean":
                return "숫자"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_65(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Filtered elements"
            elif first_line == "deutsch":
                return "Gefilterte Elemente"
            elif first_line == "farsi":
                return "المان های فیلتر شده"
            elif first_line == "russian":
                return "Отфильтрованные элементы"
            elif first_line == "spanish":
                return "Elementos filtrados"
            elif first_line == "chinese":
                return "筛选后的元素"
            elif first_line == "korean":
                return "필터링된 요소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_66(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "elements"
            elif first_line == "deutsch":
                return "Elemente"
            elif first_line == "farsi":
                return "المان ها"
            elif first_line == "russian":
                return "элементы"
            elif first_line == "spanish":
                return "elementos"
            elif first_line == "chinese":
                return "元素"
            elif first_line == "korean":
                return "요소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_67(file_path):
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
    
def str_68(file_path):
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
    
def str_69(file_path):
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