# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_creator_finder.py

def str_1(file_path):
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
                return "Por favor, seleccione al menos un elemento."
            elif first_line == "chinese":
                return "请至少选择一个元素。"
            elif first_line == "korean":
                return "적어도 하나의 요소를 선택하세요."
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
    
def str_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "At least one element must be selected."
            elif first_line == "deutsch":
                return "Mindestens ein Element muss ausgewählt werden."
            elif first_line == "farsi":
                return "حداقل باید یک المان انتخاب شود"
            elif first_line == "russian":
                return "Необходимо выбрать хотя бы один элемент."
            elif first_line == "spanish":
                return "Debe seleccionarse al menos un elemento."
            elif first_line == "chinese":
                return "至少需要选择一个元素。"
            elif first_line == "korean":
                return "적어도 하나의 요소를 선택해야 합니다."
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
                return "Model is not workshared."
            elif first_line == "deutsch":
                return "Das Modell ist nicht freigegeben."
            elif first_line == "farsi":
                return "مدل به اشتراک گذاشته نشده است"
            elif first_line == "russian":
                return "Модель не является совместно используемой."
            elif first_line == "spanish":
                return "El modelo no está compartido en colaboración."
            elif first_line == "chinese":
                return "模型未共享。"
            elif first_line == "korean":
                return "모델이 공유되지 않았습니다."
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
                return "Element information"
            elif first_line == "deutsch":
                return "Elementinformationen"
            elif first_line == "farsi":
                return "اطلاعات المان"
            elif first_line == "russian":
                return "Информация об элементе"
            elif first_line == "spanish":
                return "Información del elemento"
            elif first_line == "chinese":
                return "元素信息"
            elif first_line == "korean":
                return "요소 정보"
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
                return "Information about selected elements:"
            elif first_line == "deutsch":
                return "Informationen über ausgewählte Elemente:"
            elif first_line == "farsi":
                return ": اطلاعات درباره المان های انتخاب شده"
            elif first_line == "russian":
                return "Информация об выбранных элементах:"
            elif first_line == "spanish":
                return "Información sobre los elementos seleccionados:"
            elif first_line == "chinese":
                return "关于所选元素的信息:"
            elif first_line == "korean":
                return "선택한 요소에 대한 정보:"
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
                return "Print Information"
            elif first_line == "deutsch":
                return "Informationen drucken"
            elif first_line == "farsi":
                return "چاپ اطلاعات"
            elif first_line == "russian":
                return "Распечатать информацию"
            elif first_line == "spanish":
                return "Imprimir Información"
            elif first_line == "chinese":
                return "打印信息"
            elif first_line == "korean":
                return "정보 인쇄"
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
                return "The information will be printed in the Output window in a tabular format."
            elif first_line == "deutsch":
                return "Die Informationen werden in einem tabellarischen Format im Ausgabefenster ausgedruckt."
            elif first_line == "farsi":
                return  "اطلاعات در قالب یک جدول در پنجره خروجی چاپ خواهد شد"
            elif first_line == "russian":
                return "Информация будет распечатана в окне вывода в табличном формате."
            elif first_line == "spanish":
                return "La información se imprimirá en la ventana de Salida en formato tabular."
            elif first_line == "chinese":
                return "信息将以表格格式打印在输出窗口中。"
            elif first_line == "korean":
                return "정보가 출력 창에 표 형식으로 인쇄될 것입니다."
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
        return "An error occurred: {e}"
    
def str_10(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Allow you to add a comment on the information and print them."
            elif first_line == "deutsch":
                return "Erlaubt es Ihnen, einen Kommentar zu den Informationen hinzuzufügen und sie auszudrucken."
            elif first_line == "farsi":
                return "به شما امکان می دهد که بر روی اطلاعات یک نظر بگذاریدوسپس آن را چاپ کنید"
            elif first_line == "russian":
                return "Позволит вам добавить комментарий к информации и распечатать её."
            elif first_line == "spanish":
                return "Le permite agregar un comentario a la información e imprimirla."
            elif first_line == "chinese":
                return "允许您对信息添加注释并打印。"
            elif first_line == "korean":
                return "정보에 코멘트를 추가하고 그것들을 인쇄할 수 있게 해줍니다."
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
                return "Element Information"
            elif first_line == "deutsch":
                return "Elementinformation"
            elif first_line == "farsi":
                return "اطلاعات المان"
            elif first_line == "russian":
                return "Информация об элементе"
            elif first_line == "spanish":
                return "Información del elemento"
            elif first_line == "chinese":
                return "元素信息"
            elif first_line == "korean":
                return "요소 정보"
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
                return "Идентификатор элемента"
            elif first_line == "spanish":
                return "ID del elemento"
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
    
def str_13(file_path):
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
    
def str_14(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Current Owner"
            elif first_line == "deutsch":
                return "Aktueller Besitzer"
            elif first_line == "farsi":
                return "مالک فعلی"
            elif first_line == "russian":
                return "Текущий владелец"
            elif first_line == "spanish":
                return "Propietario actual"
            elif first_line == "chinese":
                return "当前所有者"
            elif first_line == "korean":
                return "현재 소유자"
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
                return "Last Changed By"
            elif first_line == "deutsch":
                return "Zuletzt geändert von"
            elif first_line == "farsi":
                return "آخرین تغییر دهنده"
            elif first_line == "russian":
                return "Последний измененный"
            elif first_line == "spanish":
                return "Última modificación por"
            elif first_line == "chinese":
                return "最后修改者"
            elif first_line == "korean":
                return "최종 변경자"
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
                return "Comment"
            elif first_line == "deutsch":
                return "Kommentar"
            elif first_line == "farsi":
                return "نظر"
            elif first_line == "russian":
                return "Комментарий"
            elif first_line == "spanish":
                return "Comentario"
            elif first_line == "chinese":
                return "评论"
            elif first_line == "korean":
                return "댓글"
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
                return "Comment: "
            elif first_line == "deutsch":
                return "Kommentar: "
            elif first_line == "farsi":
                return ": نظر "
            elif first_line == "russian":
                return "Комментарий: "
            elif first_line == "spanish":
                return "Comentario: "
            elif first_line == "chinese":
                return "评论："
            elif first_line == "korean":
                return "댓글: "
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
                return 'Element ID: {}\n\n''Creator: {}\n''Current Owner: {}\n''Last Changed By: {}\n\n\n'
            elif first_line == "deutsch":
                return 'Element-ID: {}\n\n''Ersteller: {}\n''Aktueller Besitzer: {}\n''Zuletzt geändert von: {}\n\n\n'
            elif first_line == "farsi":
                return 'شناسه المان: {}\n\n''ایجاد کننده: {}\n''مالک فعلی: {}\n''آخرین تغییر دهنده: {}\n\n\n'
            elif first_line == "russian":
                return 'Идентификатор элемента: {}\n\n''Создатель: {}\n''Текущий владелец: {}\n''Последнее изменение сделано: {}\n\n\n'
            elif first_line == "spanish":
                return 'ID de elemento: {}\n\n''Creador: {}\n''Propietario actual: {}\n''Última modificación por: {}\n\n\n'
            elif first_line == "chinese":
                return '元素 ID: {}\n\n''创建者: {}\n''当前所有者: {}\n''最后修改者: {}\n\n\n'
            elif first_line == "korean":
                return '요소 ID: {}\n\n''작성자: {}\n''현재 소유자: {}\n''최종 수정자: {}\n\n\n'
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