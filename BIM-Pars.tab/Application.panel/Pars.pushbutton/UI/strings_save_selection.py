# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_save_selection.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "No element is selected."
            elif first_line == "deutsch":
                return "Es wurde kein Element ausgewählt."
            elif first_line == "farsi":
                return "هیچ المانی انتخاب نشده است"
            elif first_line == "russian":
                return "Ни один элемент не выбран."
            elif first_line == "spanish":
                return "No se ha seleccionado ningún elemento."
            elif first_line == "chinese":
                return "未选择任何元素。"
            elif first_line == "korean":
                return "선택된 요소가 없습니다."
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
                return "Add a Note:"
            elif first_line == "deutsch":
                return "Füge eine Notiz hinzu:"
            elif first_line == "farsi":
                return "یک یادداشت اضافه کنید:"
            elif first_line == "russian":
                return "Добавить заметку:"
            elif first_line == "spanish":
                return "Agregar una nota:"
            elif first_line == "chinese":
                return "添加备注："
            elif first_line == "korean":
                return "노트 추가:"
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
                return "Name for selection:"
            elif first_line == "deutsch":
                return "Name für Auswahl:"
            elif first_line == "farsi":
                return "نام برای انتخاب:"
            elif first_line == "russian":
                return "Имя выбора:"
            elif first_line == "spanish":
                return "Nombre para la selección:"
            elif first_line == "chinese":
                return "选择名称："
            elif first_line == "korean":
                return "선택의 이름:"
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
                return "Save"
            elif first_line == "deutsch":
                return "Speichern"
            elif first_line == "farsi":
                return "ذخیره کردن"
            elif first_line == "russian":
                return "Сохранить"
            elif first_line == "spanish":
                return "Guardar"
            elif first_line == "chinese":
                return "保存"
            elif first_line == "korean":
                return "저장"
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
                return "Saved File Name: "
            elif first_line == "deutsch":
                return "Gespeicherter Dateiname: "
            elif first_line == "farsi":
                return "نام فایل ذخیره شده: "
            elif first_line == "russian":
                return "Имя сохраненного файла: "
            elif first_line == "spanish":
                return "Nombre del archivo guardado: "
            elif first_line == "chinese":
                return "保存的文件名："
            elif first_line == "korean":
                return "저장된 파일 이름: "
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
    
def str_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Model Path: "
            elif first_line == "deutsch":
                return "Modellpfad: "
            elif first_line == "farsi":
                return "مسیر مدل: "
            elif first_line == "russian":
                return "Путь модели: "
            elif first_line == "spanish":
                return "Ruta del modelo: "
            elif first_line == "chinese":
                return "模型路径："
            elif first_line == "korean":
                return "모델 경로: "
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
                return "Model Name: "
            elif first_line == "deutsch":
                return "Modellname: "
            elif first_line == "farsi":
                return "نام مدل: "
            elif first_line == "russian":
                return "Имя модели: "
            elif first_line == "spanish":
                return "Nombre del modelo: "
            elif first_line == "chinese":
                return "模型名称："
            elif first_line == "korean":
                return "모델 이름: "
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
                return "保存者："
            elif first_line == "korean":
                return "저장한 사람: "
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
                return "File Saved successfully."
            elif first_line == "deutsch":
                return "Datei erfolgreich gespeichert."
            elif first_line == "farsi":
                return "فایل با موفقیت ذخیره شد"
            elif first_line == "russian":
                return "Файл успешно сохранен."
            elif first_line == "spanish":
                return "Archivo guardado exitosamente."
            elif first_line == "chinese":
                return "文件保存成功。"
            elif first_line == "korean":
                return "파일이 성공적으로 저장되었습니다."
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
    
def str_12(file_path):
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