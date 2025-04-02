# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_all_elements_in_selected_views.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select Views"
            elif first_line == "deutsch":
                return "Auswahl der Ansichten"
            elif first_line == "farsi":
                return "انتخاب نماها"
            elif first_line == "russian":
                return "Выберите виды"
            elif first_line == "spanish":
                return "Seleccionar vistas"
            elif first_line == "chinese":
                return "选择视图"
            elif first_line == "korean":
                return "보기 선택"
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
                return "Select"
            elif first_line == "deutsch":
                return "Auswählen"
            elif first_line == "farsi":
                return "انتخاب "
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
    
def str_3(file_path):
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
    
def str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Zoom to selection" 
            elif first_line == "deutsch":
                return "Auf Auswahl zoomen"
            elif first_line == "farsi":
                return "بزرگنمایی انتخاب"
            elif first_line == "russian":
                return "Увеличить для выбора"
            elif first_line == "spanish":
                return "Acercar a la selección"
            elif first_line == "chinese":
                return "缩放至选择区域"
            elif first_line == "korean":
                return "선택 영역 확대"
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
                return "Do you want to zoom to selection?" 
            elif first_line == "deutsch":
                return "Möchten Sie zur Auswahl zoomen?"
            elif first_line == "farsi":
                return "آیا می‌خواهید انتخاب رابزرگنمایی کنید؟"
            elif first_line == "russian":
                return "Вы хотите увеличить для выбора?"
            elif first_line == "spanish":
                return "¿Quieres acercarte a la selección?"
            elif first_line == "chinese":
                return "您是否要缩放至选择区域？"
            elif first_line == "korean":
                return "선택 영역으로 확대하시겠습니까?"
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
                return "Not recommended for scattered views since the camera will be positioned far from selection."
            elif first_line == "deutsch":
                return "Nicht empfohlen für zerstreute Ansichten, da die Kamera weit von der Auswahl entfernt positioniert wird."
            elif first_line == "farsi":
                return "برای نماهای پراکنده توصیه نمی‌شود زیرا دوربین از انتخاب دورتر قرار خواهد گرفت"
            elif first_line == "russian":
                return "Не рекомендуется для разбросанных видов, так как камера будет находиться далеко от выбора."
            elif first_line == "spanish":
                return "No recomendado para vistas dispersas, ya que la cámara estará posicionada lejos de la selección."
            elif first_line == "chinese":
                return "不推荐用于分散的视图，因为摄像机将远离选择区域。"
            elif first_line == "korean":
                return "분산된 보기에는 권장되지 않으며, 선택 영역으로부터 카메라가 멀리 위치됩니다."
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
    
def str_8(file_path):
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
    
def str_9(file_path):
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
    
def str_10(file_path):
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
    
def str_11(file_path):
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