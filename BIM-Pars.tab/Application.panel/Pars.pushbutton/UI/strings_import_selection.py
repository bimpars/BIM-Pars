# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_import_selection.py

def str_1(file_path):
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
    
def str_2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "The selected file does not belong to this model. The file belongs to: {0}"
            elif first_line == "deutsch":
                return "Die ausgewählte Datei gehört nicht zu diesem Modell. Die Datei gehört zu: {0}"
            elif first_line == "farsi":
                return "فایل انتخاب شده متعلق به این مدل نمی‌باشد. این فایل متعلق به \n{0} است"
            elif first_line == "russian":
                return "Выбранный файл не принадлежит этой модели. Файл принадлежит: {0}"
            elif first_line == "spanish":
                return "El archivo seleccionado no pertenece a este modelo. El archivo pertenece a: {0}"
            elif first_line == "chinese":
                return "所选文件不属于此模型。该文件属于：{0}"
            elif first_line == "korean":
                return "선택한 파일은 이 모델에 속하지 않습니다. 이 파일은 {0}에 속합니다."
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
    
def str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Model Path while exported: "
            elif first_line == "deutsch":
                return "Exportierter Modellpfad: "
            elif first_line == "farsi":
                return "مسیر مدل در هنگام دریافت خروجی: "
            elif first_line == "russian":
                return "Путь модели при экспорте: "
            elif first_line == "spanish":
                return "Ruta del modelo durante la exportación: "
            elif first_line == "chinese":
                return "导出时的模型路径："
            elif first_line == "korean":
                return "내보낼 때 모델 경로: "
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
                return "Model Name while exported: "
            elif first_line == "deutsch":
                return "Modellname während des Exports: "
            elif first_line == "farsi":
                return "نام مدل در هنگام دریافت خروجی: "
            elif first_line == "russian":
                return "Имя модели при экспорте: "
            elif first_line == "spanish":
                return "Nombre del modelo durante la exportación: "
            elif first_line == "chinese":
                return "导出时的模型名称："
            elif first_line == "korean":
                return "내보낼 때 모델 이름: "
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
                return "Exported By: "
            elif first_line == "deutsch":
                return "Exportiert von: "
            elif first_line == "farsi":
                return "خروجی توسط: "
            elif first_line == "russian":
                return "Экспортировано пользователем: "
            elif first_line == "spanish":
                return "Exportado por: "
            elif first_line == "chinese":
                return "导出者："
            elif first_line == "korean":
                return "내보낸 사람: "
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
                return "Added Note: "
            elif first_line == "deutsch":
                return "Hinzugefügter Hinweis: "
            elif first_line == "farsi":
                return "یادداشت افزوده شده: "
            elif first_line == "russian":
                return "Добавленное примечание: "
            elif first_line == "spanish":
                return "Nota agregada: "
            elif first_line == "chinese":
                return "添加备注："
            elif first_line == "korean":
                return "추가된 노트: "
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
                return "Import plugin's native format"
            elif first_line == "deutsch":
                return "Plugin-eigenes Format importieren"
            elif first_line == "farsi":
                return "فرمت بومی پلاگین را وارد کنید"
            elif first_line == "russian":
                return "Импортировать родной формат плагина"
            elif first_line == "spanish":
                return "Importar formato nativo del complemento"
            elif first_line == "chinese":
                return "导入插件的原生格式"
            elif first_line == "korean":
                return "플러그인의 기본 형식 가져오기"
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
                return "Open html file."
            elif first_line == "deutsch":
                return "HTML-Datei öffnen."
            elif first_line == "farsi":
                return "HTML بازکردن فایل "
            elif first_line == "russian":
                return "Открыть HTML-файл."
            elif first_line == "spanish":
                return "Abrir archivo HTML."
            elif first_line == "chinese":
                return "打开 HTML 文件。"
            elif first_line == "korean":
                return "HTML 파일 열기."
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
                return "Import"
            elif first_line == "deutsch":
                return "Importieren"
            elif first_line == "farsi":
                return "ایمپورت "
            elif first_line == "russian":
                return "Импортировать"
            elif first_line == "spanish":
                return "Importar"
            elif first_line == "chinese":
                return "导入"
            elif first_line == "korean":
                return "가져오기"
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
                return "XML Import Information"
            elif first_line == "deutsch":
                return "XML-Importinformationen"
            elif first_line == "farsi":
                return "اطلاعات ٰایکس ام ال ٰ ایمپورت شده"
            elif first_line == "russian":
                return "Информация о импорте XML"
            elif first_line == "spanish":
                return "Información de importación XML"
            elif first_line == "chinese":
                return "XML导入信息"
            elif first_line == "korean":
                return "XML 가져오기 정보"
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