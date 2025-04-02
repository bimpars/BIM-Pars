# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_script_manager.py
    
def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Script Manager"
            elif first_line == "deutsch":
                return "Skript-Manager"
            elif first_line == "farsi":
                return "مدیریت اسکریپت"
            elif first_line == "russian":
                return "Менеджер скриптов"
            elif first_line == "spanish":
                return "Administrador de scripts"
            elif first_line == "chinese":
                return "脚本管理器"
            elif first_line == "korean":
                return "스크립트 관리자"
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
                return "Set a directory"
            elif first_line == "deutsch":
                return "Verzeichnis festlegen"
            elif first_line == "farsi":
                return "تنظیم یک دایرکتوری"
            elif first_line == "russian":
                return "Установить директорию"
            elif first_line == "spanish":
                return "Establecer un directorio"
            elif first_line == "chinese":
                return "设置目录"
            elif first_line == "korean":
                return "디렉토리 설정하기"
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
                return "Pick script"
            elif first_line == "deutsch":
                return "Skript auswählen"
            elif first_line == "farsi":
                return "انتخاب اسکریپت"
            elif first_line == "russian":
                return "Выбрать скрипт"
            elif first_line == "spanish":
                return "Elegir un script"
            elif first_line == "chinese":
                return "选择脚本"
            elif first_line == "korean":
                return "스크립트 선택하기"
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
                return "My Scripts"
            elif first_line == "deutsch":
                return "Meine Skripte"
            elif first_line == "farsi":
                return "اسکریپت‌های من"
            elif first_line == "russian":
                return "Мои скрипты"
            elif first_line == "spanish":
                return "Mis scripts"
            elif first_line == "chinese":
                return "我的脚本"
            elif first_line == "korean":
                return "나의 스크립트"
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
                return "Set"
            elif first_line == "deutsch":
                return "Einstellen"
            elif first_line == "farsi":
                return "تنظیم کردن"
            elif first_line == "russian":
                return "Установить"
            elif first_line == "spanish":
                return "Establecer"
            elif first_line == "chinese":
                return "设置"
            elif first_line == "korean":
                return "설정하다"
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
                return "Reset"
            elif first_line == "deutsch":
                return "Zurücksetzen"
            elif first_line == "farsi":
                return "بازنشانی کردن"
            elif first_line == "russian":
                return "Сбросить"
            elif first_line == "spanish":
                return "Restablecer"
            elif first_line == "chinese":
                return "重置"
            elif first_line == "korean":
                return "재설정"
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
                return "PickRun"
            elif first_line == "deutsch":
                return "Auswählen und Ausführen"
            elif first_line == "farsi":
                return "انتخاب و اجرا کردن"
            elif first_line == "russian":
                return "Выбрать и выполнить"
            elif first_line == "spanish":
                return "Seleccionar y ejecutar"
            elif first_line == "chinese":
                return "选择并运行"
            elif first_line == "korean":
                return "선택하고 실행하기"
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
                return "Add"
            elif first_line == "deutsch":
                return "Hinzufügen"
            elif first_line == "farsi":
                return "افزودن"
            elif first_line == "russian":
                return "Добавить"
            elif first_line == "spanish":
                return "Agregar"
            elif first_line == "chinese":
                return "添加"
            elif first_line == "korean":
                return "추가하기"
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
                return "Delete"
            elif first_line == "deutsch":
                return "Löschen"
            elif first_line == "farsi":
                return "حذف کردن"
            elif first_line == "russian":
                return "Удалить"
            elif first_line == "spanish":
                return "Eliminar"
            elif first_line == "chinese":
                return "删除"
            elif first_line == "korean":
                return "삭제하기"
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
                return "Directory: Directory is not set."
            elif first_line == "deutsch":
                return "Verzeichnis: Verzeichnis ist nicht festgelegt."
            elif first_line == "farsi":
                return "دایرکتوری: دایرکتوری تنظیم نشده است"
            elif first_line == "russian":
                return "Директория: Директория не установлена."
            elif first_line == "spanish":
                return "Directorio: El directorio no está establecido."
            elif first_line == "chinese":
                return "目录：目录未设置。"
            elif first_line == "korean":
                return "디렉토리: 디렉토리가 설정되지 않았습니다."
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
                return "Directory: "
            elif first_line == "deutsch":
                return "Verzeichnis: "
            elif first_line == "farsi":
                return "دایرکتوری: "
            elif first_line == "russian":
                return "Директория: "
            elif first_line == "spanish":
                return "Directorio: "
            elif first_line == "chinese":
                return "目录："
            elif first_line == "korean":
                return "디렉토리: "
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
                return "Directory is set"
            elif first_line == "deutsch":
                return "Verzeichnis ist festgelegt"
            elif first_line == "farsi":
                return "دایرکتوری تنظیم شده است"
            elif first_line == "russian":
                return "Директория установлена"
            elif first_line == "spanish":
                return "Directorio está establecido"
            elif first_line == "chinese":
                return "目录已设置"
            elif first_line == "korean":
                return "디렉토리가 설정되었습니다"
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
                return "Select"
            elif first_line == "deutsch":
                return "Auswählen"
            elif first_line == "farsi":
                return "انتخاب کردن"
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
 
def str_14(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Good job! The script has no errors."
            elif first_line == "deutsch":
                return "Gut gemacht! Das Skript enthält keine Fehler."
            elif first_line == "farsi":
                return "کارت عالی بود! این اسکریپت هیچ خطایی ندارد"
            elif first_line == "russian":
                return "Отличная работа! Скрипт не содержит ошибок."
            elif first_line == "spanish":
                return "¡Buen trabajo! El script no tiene errores."
            elif first_line == "chinese":
                return "干得好！脚本没有错误。"
            elif first_line == "korean":
                return "잘했어요! 스크립트에 오류가 없습니다."
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
                return  "Operation canceled."
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

def str_16(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Script added successfully."
            elif first_line == "deutsch":
                return "Skript erfolgreich hinzugefügt."
            elif first_line == "farsi":
                return "اسکریپت با موفقیت اضافه شد"
            elif first_line == "russian":
                return "Скрипт успешно добавлен."
            elif first_line == "spanish":
                return "Script añadido exitosamente."
            elif first_line == "chinese":
                return "脚本添加成功。"
            elif first_line == "korean":
                return "스크립트가 성공적으로 추가되었습니다."
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
                return "No file selected." 
            elif first_line == "deutsch":
                return "Keine Datei ausgewählt."
            elif first_line == "farsi":
                return "هیچ فایلی انتخاب نشده است"
            elif first_line == "russian":
                return "Файл не выбран."
            elif first_line == "spanish":
                return "No se ha seleccionado ningún archivo."
            elif first_line == "chinese":
                return "未选择文件。"
            elif first_line == "korean":
                return "파일이 선택되지 않았습니다."
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
                return "Selected script: {}"
            elif first_line == "deutsch":
                return "Ausgewähltes Skript: {}"
            elif first_line == "farsi":
                return "اسکریپت انتخاب شده: {}"
            elif first_line == "russian":
                return "Выбранный скрипт: {}"
            elif first_line == "spanish":
                return "Script seleccionado: {}"
            elif first_line == "chinese":
                return "已选择的脚本：{}"
            elif first_line == "korean":
                return "선택된 스크립트: {}"
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
                return "Description: {}"
            elif first_line == "deutsch":
                return "Beschreibung: {}"
            elif first_line == "farsi":
                return "توضیحات: {}"
            elif first_line == "russian":
                return "Описание: {}"
            elif first_line == "spanish":
                return "Descripción: {}"
            elif first_line == "chinese":
                return "描述：{}"
            elif first_line == "korean":
                return "설명: {}"
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
                return "scripts"
            elif first_line == "deutsch":
                return "Skripte"
            elif first_line == "farsi":
                return "اسکریپت‌ها"
            elif first_line == "russian":
                return "Скрипты"
            elif first_line == "spanish":
                return "Scripts"
            elif first_line == "chinese":
                return "脚本"
            elif first_line == "korean":
                return "스크립트"
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
                return "My script"
            elif first_line == "deutsch":
                return "Mein Skript"
            elif first_line == "farsi":
                return "اسکریپت من"
            elif first_line == "russian":
                return "Мой скрипт"
            elif first_line == "spanish":
                return "Mi script"
            elif first_line == "chinese":
                return "我的脚本"
            elif first_line == "korean":
                return "내 스크립트"
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
                return "Directory"
            elif first_line == "deutsch":
                return "Verzeichnis"
            elif first_line == "farsi":
                return "دایرکتوری"
            elif first_line == "russian":
                return "Каталог"
            elif first_line == "spanish":
                return "Directorio"
            elif first_line == "chinese":
                return "目录"
            elif first_line == "korean":
                return "디렉터리"
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