# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_active_view.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "View Name: "
            elif first_line == "deutsch":
                return "Ansichtsname: "
            elif first_line == "farsi":
                return " نام :  "
            elif first_line == "russian":
                return "Имя представления: "
            elif first_line == "spanish":
                return "Nombre de vista: "
            elif first_line == "chinese":
                return "视图名称："
            elif first_line == "korean":
                return "보기 이름: "
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
                return "ID: "
            elif first_line == "deutsch":
                return "ID: "
            elif first_line == "farsi":
                return "شناسه: "
            elif first_line == "russian":
                return "ID: "
            elif first_line == "spanish":
                return "ID: "
            elif first_line == "chinese":
                return "ID："
            elif first_line == "korean":
                return "ID: "
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
                return "Creator: "
            elif first_line == "deutsch":
                return "Ersteller: "
            elif first_line == "farsi":
                return "ایجاد کننده: "
            elif first_line == "russian":
                return "Создатель: "
            elif first_line == "spanish":
                return "Creador: "
            elif first_line == "chinese":
                return "创建者："
            elif first_line == "korean":
                return "생성자: "
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
                return "Information about active view :"
            elif first_line == "deutsch":
                return "Informationen über die aktive Ansicht :"
            elif first_line == "farsi":
                return ": اطلاعات درباره نمای فعال"
            elif first_line == "russian":
                return "Информация об активном представлении :"
            elif first_line == "spanish":
                return "Información sobre la vista activa :"
            elif first_line == "chinese":
                return "关于活动视图的信息 :"
            elif first_line == "korean":
                return "활성 뷰에 대한 정보 :"
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
                return "Active view"
            elif first_line == "deutsch":
                return "Aktive Ansicht"
            elif first_line == "farsi":
                return "نمای فعال"
            elif first_line == "russian":
                return "Активное представление"
            elif first_line == "spanish":
                return "Vista activa"
            elif first_line == "chinese":
                return "活动视图"
            elif first_line == "korean":
                return "활성 뷰"
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
    
def str_7(file_path):
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
                return "Имя"
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
    
def str_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Creator"
            elif first_line == "deutsch":
                return "Ersteller"
            elif first_line == "farsi":
                return "ایجادکننده"
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
        return "An error occurred: {}".format(e)
    
def str_9(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Last Changed By"
            elif first_line == "deutsch":
                return "Zuletzt geändert von"
            elif first_line == "farsi":
                return "آخرین تغییر توسط"
            elif first_line == "russian":
                return "Последнее изменение от"
            elif first_line == "spanish":
                return "Último cambiado por"
            elif first_line == "chinese":
                return "最后修改者"
            elif first_line == "korean":
                return "마지막 수정자"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    
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