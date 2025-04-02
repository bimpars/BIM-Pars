# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_element_id.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Category and ID of selected elements:"
            elif first_line == "deutsch":
                return "Kategorie und ID der ausgewählten Elemente:"
            elif first_line == "farsi":
                return ":دسته بندی و شناسه المان های انتخاب شده "
            elif first_line == "russian":
                return "Категория и идентификатор выбранных элементов:"
            elif first_line == "spanish":
                return "Categoría e ID de los elementos seleccionados:"
            elif first_line == "chinese":
                return "所选元素的类别和ID："
            elif first_line == "korean":
                return "선택된 요소의 범주 및 ID:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
 
def str_2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No element selected"
            elif first_line == "deutsch":
                return "Kein Element ausgewählt"
            elif first_line == "farsi":
                return "هیچ المانی انتخاب نشده است"
            elif first_line == "russian":
                return "Не выбрано ни одного элемента"
            elif first_line == "spanish":
                return "No se ha seleccionado ningún elemento"
            elif first_line == "chinese":
                return "未选择任何元素"
            elif first_line == "korean":
                return "선택된 요소가 없습니다"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    
def str_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please select at least one element."
            elif first_line == "deutsch":
                return "Bitte wählen Sie mindestens ein Element aus."
            elif first_line == "farsi":
                return "لطفاً حداقل یک المان را انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, выберите хотя бы один элемент."
            elif first_line == "spanish":
                return "Por favor, selecciona al menos un elemento."
            elif first_line == "chinese":
                return "请至少选择一个元素。"
            elif first_line == "korean":
                return "최소한 하나의 요소를 선택하세요."
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    
def str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Print Raw Data"
            elif first_line == "deutsch":
                return "Rohdaten drucken"
            elif first_line == "farsi":
                return "چاپ داده های خام"
            elif first_line == "russian":
                return "Распечатать исходные данные"
            elif first_line == "spanish":
                return "Imprimir datos sin procesar"
            elif first_line == "chinese":
                return "打印原始数据"
            elif first_line == "korean":
                return "원시 데이터 인쇄"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    
def str_5(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Displayed information will be printed as raw data in the output window."
            elif first_line == "deutsch":
                return "Die angezeigten Informationen werden als Rohdaten im Ausgabefenster ausgegeben."
            elif first_line == "farsi":
                return  "اطلاعات نمایش داده شده به عنوان داده های خام در پنجره خروجی چاپ خواهد شد"
            elif first_line == "russian":
                return "Отображаемая информация будет распечатана в виде исходных данных в окне вывода."
            elif first_line == "spanish":
                return "La información mostrada se imprimirá como datos sin procesar en la ventana de salida."
            elif first_line == "chinese":
                return "显示的信息将以原始数据的形式打印在输出窗口中。"
            elif first_line == "korean":
                return "표시된 정보는 출력 창에서 원시 데이터로 인쇄됩니다."
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)
    
def str_6(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Comment and Print"
            elif first_line == "deutsch":
                return "Kommentieren und drucken"
            elif first_line == "farsi":
                return "نظردادن و چاپ"
            elif first_line == "russian":
                return "Добавить комментарий и распечатать"
            elif first_line == "spanish":
                return "Comentar e Imprimir"
            elif first_line == "chinese":
                return "添加注释并打印"
            elif first_line == "korean":
                return "코멘트 작성 및 인쇄"
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
                return "You can have the info in a table and assign a comment on them."
            elif first_line == "deutsch":
                return "Sie können die Informationen in einer Tabelle haben und einen Kommentar dazu schreiben."
            elif first_line == "farsi":
                return "می توانید اطلاعات را در قالب یک جدول داشته باشید و برای آنها یک نظراختصاص دهید"
            elif first_line == "russian":
                return "Вы можете представить информацию в виде таблицы и добавить к ней комментарий."
            elif first_line == "spanish":
                return "Puedes tener la información en una tabla y asignar un comentario a ellos."
            elif first_line == "chinese":
                return "您可以将信息以表格形式呈现,并为其添加注释。"
            elif first_line == "korean":
                return  "정보를 테이블로 표시하고 각각에 대한 코멘트를 달 수 있습니다."
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
                return "Comment on the selected elemnts"
            elif first_line == "deutsch":
                return "Kommentiere die ausgewählten Elemente"
            elif first_line == "farsi":
                return "درباره ی المان های انتخاب شده نظر دهید"
            elif first_line == "russian":
                return "Прокомментируйте выбранные элементы"
            elif first_line == "spanish":
                return "Comenta sobre los elementos seleccionados"
            elif first_line == "chinese":
                return "对所选元素进行评论"
            elif first_line == "korean":
                return "선택한 요소에 대해 코멘트하기"
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
    
def str_10(file_path):
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

def str_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Comment"
            elif first_line == "deutsch":
                return "Kommentar"
            elif first_line == "farsi":
                return "نظر"
            elif first_line == "russian":
                return "Комментарий"
            elif first_line == "spanish":
                return  "Comentario"
            elif first_line == "chinese":
                return "评论"
            elif first_line == "korean":
                return "코멘트"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)

def str_12(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Date and Time"
            elif first_line == "deutsch":
                return "Datum und Uhrzeit"
            elif first_line == "farsi":
                return "تاریخ و زمان"  
            elif first_line == "russian":
                return "Дата и время"  
            elif first_line == "spanish":
                return "Fecha y hora"  
            elif first_line == "chinese":
                return "日期和时间"  
            elif first_line == "korean":
                return "날짜와 시간"  
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
                return "User"
            elif first_line == "deutsch":
                return "Benutzer"
            elif first_line == "farsi":
                return "کاربر"  
            elif first_line == "russian":
                return "Пользователь"  
            elif first_line == "spanish":
                return "Usuario"  
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
    
def str_14(file_path):
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
                return "ID de elemento"  
            elif first_line == "chinese":
                return "元素 ID"  
            elif first_line == "korean":
                return "요소 ID"  
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
                return "Category: {0}"
            elif first_line == "deutsch":
                return "Kategorie: {0}"
            elif first_line == "farsi":
                return "دسته بندی: {0}"
            elif first_line == "russian":
                return "Категория: {0}"
            elif first_line == "spanish":
                return "Categoría: {0}" 
            elif first_line == "chinese":
                return "类别: {0}"
            elif first_line == "korean":
                return "카테고리: {0}"
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
                return "ID: {0}"
            elif first_line == "deutsch":
                return "ID: {0}"
            elif first_line == "farsi":
                return "شناسه: {0}"
            elif first_line == "russian":
                return "ID: {0}"
            elif first_line == "spanish":
                return "ID: {0}"
            elif first_line == "chinese":
                return "ID: {0}"
            elif first_line == "korean":
                return "ID: {0}"
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
                return "Category: "
            elif first_line == "deutsch":
                return "Kategorie: "
            elif first_line == "farsi":
                return "دسته بندی: "
            elif first_line == "russian":
                return "Категория: "
            elif first_line == "spanish":
                return "Categoría: " 
            elif first_line == "chinese":
                return "类别: "
            elif first_line == "korean":
                return "카테고리: "
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
                return "ID: "
            elif first_line == "korean":
                return "ID: "
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
                return "Unnamed Element"
            elif first_line == "deutsch":
                return "Unbenanntes Element"
            elif first_line == "farsi":
                return "المان بدون نام"
            elif first_line == "russian":
                return "Безымянный элемент"
            elif first_line == "spanish":
                return "Elemento sin nombre"
            elif first_line == "chinese":
                return "未命名元素"
            elif first_line == "korean":
                return "이름 없는 요소"
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
                return "Element Not Found"
            elif first_line == "deutsch":
                return "Element Nicht Gefunden"
            elif first_line == "farsi":
                return "المان پیدا نشد"
            elif first_line == "russian":
                return "Элемент Не Найден"
            elif first_line == "spanish":
                return "Elemento No Encontrado"
            elif first_line == "chinese":
                return "未找到元素"
            elif first_line == "korean":
                return "요소를 찾을 수 없습니다."
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
                return "Error getting name for ID {0}: {1}"
            elif first_line == "deutsch":
                return "Fehler beim Abrufen des Namens für die ID {0}: {1}"
            elif first_line == "farsi":
                return "خطا در دریافت نام برای شناسه {0}: {1}"
            elif first_line == "russian":
                return "Ошибка при получении имени для ID {0}: {1}"
            elif first_line == "spanish":
                return "Error al obtener el nombre para el ID {0}: {1}"
            elif first_line == "chinese":
                return "获取ID {0}的名称时出错：{1}"
            elif first_line == "korean":
                return "ID {0}의 이름을 가져오는 중 오류가 발생했습니다: {1}"
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