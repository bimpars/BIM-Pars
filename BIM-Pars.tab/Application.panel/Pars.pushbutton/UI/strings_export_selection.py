# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_export_selection.py

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
                return "Export"
            elif first_line == "deutsch":
                return "Exportieren"
            elif first_line == "farsi":
                return "اکسپورت "
            elif first_line == "russian":
                return "Экспорт"
            elif first_line == "spanish":
                return "Exportar"
            elif first_line == "chinese":
                return "导出"
            elif first_line == "korean":
                return "내보내기"
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

def str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Native plugin's export format which includes clickable ids and note."
            elif first_line == "deutsch":
                return "Exportformat des nativen Plugins, das anklickbare IDs und Notizen enthält."
            elif first_line == "farsi":
                return " خروجی گرفتن با فرمت بومی پلاگین  که شامل شناسه‌های قابل کلیک و یادداشت است"
            elif first_line == "russian":
                return "Формат экспорта нативного плагина, включающий кликабельные идентификаторы и заметку."
            elif first_line == "spanish":
                return "Formato de exportación del plugin nativo que incluye identificadores clicables y nota."
            elif first_line == "chinese":
                return "包括可点击的标识和注释的本机插件导出格式。"
            elif first_line == "korean":
                return "클릭 가능한 ID와 노트가 포함된 네이티브 플러그인의 내보내기 형식."
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
                return "only the ids will be stored."
            elif first_line == "deutsch":
                return "Es werden nur die IDs gespeichert."
            elif first_line == "farsi":
                return "تنها شناسه‌ها ذخیره خواهند شد"
            elif first_line == "russian":
                return "Будут сохранены только идентификаторы."
            elif first_line == "spanish":
                return "Solo se almacenarán los identificadores."
            elif first_line == "chinese":
                return "只会存储标识。"
            elif first_line == "korean":
                return "ID만 저장됩니다."
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
                return "Name of the file:"
            elif first_line == "deutsch":
                return "Name der Datei:"
            elif first_line == "farsi":
                return "نام فایل:"
            elif first_line == "russian":
                return "Имя файла:"
            elif first_line == "spanish":
                return "Nombre del archivo:"
            elif first_line == "chinese":
                return "文件名："
            elif first_line == "korean":
                return "파일 이름:"
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
                return "Exported File path: "
            elif first_line == "deutsch":
                return "Exportierter Dateipfad: "
            elif first_line == "farsi":
                return "مسیر فایل خروجی: "
            elif first_line == "russian":
                return "Путь экспортированного файла: "
            elif first_line == "spanish":
                return "Ruta del archivo exportado: "
            elif first_line == "chinese":
                return "导出文件路径："
            elif first_line == "korean":
                return "내보낸 파일 경로: "
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
                return "Added Note: "
            elif first_line == "deutsch":
                return "Hinzugefügte Notiz: "
            elif first_line == "farsi":
                return "یادداشت افزوده شده: "
            elif first_line == "russian":
                return "Добавленная заметка: "
            elif first_line == "spanish":
                return "Nota agregada: "
            elif first_line == "chinese":
                return "添加的注释："
            elif first_line == "korean":
                return "추가된 노트: "
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

def str_12(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "file exported by:"
            elif first_line == "deutsch":
                return "Datei exportiert von:"
            elif first_line == "farsi":
                return "فایل خروجی گرفته شده توسط:"
            elif first_line == "russian":
                return "Файл экспортирован:"
            elif first_line == "spanish":
                return "Archivo exportado por:"
            elif first_line == "chinese":
                return "文件导出者："
            elif first_line == "korean":
                return "파일을 내보낸 사람:"
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
                return "File created successfully."
            elif first_line == "deutsch":
                return "Datei erfolgreich erstellt."
            elif first_line == "farsi":
                return "فایل با موفقیت ایجاد شد"
            elif first_line == "russian":
                return "Файл успешно создан."
            elif first_line == "spanish":
                return "Archivo creado exitosamente."
            elif first_line == "chinese":
                return "文件创建成功。"
            elif first_line == "korean":
                return "파일이 성공적으로 생성되었습니다."
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
                return "Export CSV"
            elif first_line == "deutsch":
                return "CSV exportieren"
            elif first_line == "farsi":
                return "خروجی گرفتن CSV"
            elif first_line == "russian":
                return "Экспорт в CSV"
            elif first_line == "spanish":
                return "Exportar a CSV"
            elif first_line == "chinese":
                return "导出为CSV"
            elif first_line == "korean":
                return "CSV로 내보내기"
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