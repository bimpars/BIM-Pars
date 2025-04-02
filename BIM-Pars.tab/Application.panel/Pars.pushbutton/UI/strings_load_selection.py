# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_load_selection.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Files with Model Name"
            elif first_line == "deutsch":
                return "Dateien mit Modellnamen"
            elif first_line == "farsi":
                return "فایل‌ها با نام مدل"
            elif first_line == "russian":
                return "Файлы с названием модели"
            elif first_line == "spanish":
                return "Archivos con nombre de modelo"
            elif first_line == "chinese":
                return "具有模型名称的文件"
            elif first_line == "korean":
                return "모델 이름을 가진 파일들"
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
                return "Files without Model Name"
            elif first_line == "deutsch":
                return "Dateien ohne Modellnamen"
            elif first_line == "farsi":
                return "فایل‌ها بدون نام مدل"
            elif first_line == "russian":
                return "Файлы без названия модели"
            elif first_line == "spanish":
                return "Archivos sin nombre de modelo"
            elif first_line == "chinese":
                return "没有模型名称的文件"
            elif first_line == "korean":
                return "모델 이름이 없는 파일들"
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
                return "Load list"
            elif first_line == "deutsch":
                return "Ladeliste"
            elif first_line == "farsi":
                return "لیست بارگذاری "
            elif first_line == "russian":
                return "Список загрузки"
            elif first_line == "spanish":
                return "Lista de carga"
            elif first_line == "chinese":
                return "装载列表"
            elif first_line == "korean":
                return "로드 목록"
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
                return "Lists:"
            elif first_line == "deutsch":
                return "Listen:"
            elif first_line == "farsi":
                return "لیست‌ها:"
            elif first_line == "russian":
                return "Списки:"
            elif first_line == "spanish":
                return "Listas:"
            elif first_line == "chinese":
                return "列表："
            elif first_line == "korean":
                return "목록:"
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
    

def str_6(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No file was selected."
            elif first_line == "deutsch":
                return "Es wurde keine Datei ausgewählt."
            elif first_line == "farsi":
                return "هیچ فایلی انتخاب نشده است"
            elif first_line == "russian":
                return "Файл не был выбран."
            elif first_line == "spanish":
                return "No se seleccionó ningún archivo."
            elif first_line == "chinese":
                return "未选择任何文件。"
            elif first_line == "korean":
                return "파일이 선택되지 않았습니다."
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
    
def str_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "The selection file does not belong to this model. The file belongs to: {0}"
            elif first_line == "deutsch":
                return "Die ausgewählte Datei gehört nicht zu diesem Modell. Die Datei gehört zu: {0}"
            elif first_line == "farsi":
                return "فایل انتخاب شده متعلق به این مدل نیست. این فایل متعلق است به \n {0}"
            elif first_line == "russian":
                return "Выбранный файл не принадлежит данной модели. Файл принадлежит: {0}"
            elif first_line == "spanish":
                return "El archivo seleccionado no pertenece a este modelo. El archivo pertenece a: {0}"
            elif first_line == "chinese":
                return "所选文件不属于此模型。该文件属于：{0}"
            elif first_line == "korean":
                return "선택한 파일은 이 모델에 속하지 않습니다. 해당 파일은 다음에 속합니다: {0}"
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
                return "Selection Name: "
            elif first_line == "deutsch":
                return "Auswahlname: "
            elif first_line == "farsi":
                return "نام انتخاب: "
            elif first_line == "russian":
                return "Название выбора: "
            elif first_line == "spanish":
                return "Nombre de la selección: "
            elif first_line == "chinese":
                return "选择名称："
            elif first_line == "korean":
                return "선택 이름: "
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
                return "Model Path When Saved: "
            elif first_line == "deutsch":
                return "Pfad des Modells beim Speichern: "
            elif first_line == "farsi":
                return "مسیر مدل ذخیره شده: "
            elif first_line == "russian":
                return "Путь модели при сохранении: "
            elif first_line == "spanish":
                return "Ruta del modelo al guardarse: "
            elif first_line == "chinese":
                return "保存时的模型路径："
            elif first_line == "korean":
                return "저장 시 모델 경로: "
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
                return "Model Name When Saved: "
            elif first_line == "deutsch":
                return "Modellname beim Speichern: "
            elif first_line == "farsi":
                return "نام مدل در زمان ذخیره سازی: "
            elif first_line == "russian":
                return "Имя модели при сохранении: "
            elif first_line == "spanish":
                return "Nombre del modelo al guardarse: "
            elif first_line == "chinese":
                return "保存时的模型名称："
            elif first_line == "korean":
                return "저장 시 모델 이름: "
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
                return "Saved By: "
            elif first_line == "deutsch":
                return "Gespeichert von: "
            elif first_line == "farsi":
                return "ذخیره شده توسط: "
            elif first_line == "russian":
                return "Сохранено пользователем: "
            elif first_line == "spanish":
                return "Guardado por: "
            elif first_line == "chinese":
                return "由谁保存："
            elif first_line == "korean":
                return "저장한 사람: "
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
                return "Added Note: " 
            elif first_line == "deutsch":
                return "Hinzugefügte Notiz: "
            elif first_line == "farsi":
                return "یادداشت اضافه شده: "
            elif first_line == "russian":
                return "Добавленное примечание: "
            elif first_line == "spanish":
                return "Nota agregada: "
            elif first_line == "chinese":
                return "添加的备注："
            elif first_line == "korean":
                return "추가된 노트: "
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
                return "File"
            elif first_line == "deutsch":
                return "Datei"
            elif first_line == "farsi":
                return "فایل"
            elif first_line == "russian":
                return "Файл"
            elif first_line == "spanish":
                return "Archivo"
            elif first_line == "chinese":
                return "文件"
            elif first_line == "korean":
                return "파일"
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
                return "Do you want to keep this saved selection?"
            elif first_line == "deutsch":
                return "Möchten Sie diese gespeicherte Auswahl behalten?"
            elif first_line == "farsi":
                return "آیا می‌خواهید این انتخاب ذخیره شده را نگه دارید؟"
            elif first_line == "russian":
                return "Хотите сохранить этот сохраненный выбор?"
            elif first_line == "spanish":
                return "¿Quieres mantener esta selección guardada?"
            elif first_line == "chinese":
                return "您是否要保留此保存的选择？"
            elif first_line == "korean":
                return "이 저장된 선택을 유지하시겠습니까?"
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
                return "Saved selection removed."
            elif first_line == "deutsch":
                return "Gespeicherte Auswahl entfernt."
            elif first_line == "farsi":
                return "انتخاب ذخیره شده حذف شد"
            elif first_line == "russian":
                return "Сохраненный выбор удален."
            elif first_line == "spanish":
                return "Selección guardada eliminada."
            elif first_line == "chinese":
                return "已删除保存的选择。"
            elif first_line == "korean":
                return "저장된 선택이 제거되었습니다."
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
                return "Load"
            elif first_line == "deutsch":
                return "Laden"
            elif first_line == "farsi":
                return "بارگذاری"
            elif first_line == "russian":
                return "Загрузить"
            elif first_line == "spanish":
                return "Cargar"
            elif first_line == "chinese":
                return "加载"
            elif first_line == "korean":
                return "로드"
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
    
def str_19(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Selection Info"
            elif first_line == "deutsch":
                return "Auswahlinformationen"
            elif first_line == "farsi":
                return "اطلاعات انتخاب"
            elif first_line == "russian":
                return "Информация о выборе"
            elif first_line == "spanish":
                return "Información de selección"
            elif first_line == "chinese":
                return "选择信息"
            elif first_line == "korean":
                return "선택 정보"
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

def str_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "The selection file does not belong to this model."
            elif first_line == "deutsch":
                return "Die Auswahldatei gehört nicht zu diesem Modell."
            elif first_line == "farsi":
                return ".فایل انتخاب شده به این مدل تعلق ندارد"
            elif first_line == "russian":
                return "Файл выбора не принадлежит этой модели."
            elif first_line == "spanish":
                return "El archivo de selección no pertenece a este modelo."
            elif first_line == "chinese":
                return "选择的文件不属于此模型。"
            elif first_line == "korean":
                return "선택한 파일이 이 모델에 속하지 않습니다."
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