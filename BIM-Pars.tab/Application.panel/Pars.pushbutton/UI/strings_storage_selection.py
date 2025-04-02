# -*- coding: utf-8 -*-
#strings_storage_selection.py

def detect_language(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "English"
            elif first_line == "deutsch":
                return "Deutsch"
            elif first_line == "farsi":
                return "فارسی" 
            elif first_line == "russian":
                return "Русский" 
            elif first_line == "spanish":
                return "Español" 
            elif first_line == "chinese":
                return "中文" 
            elif first_line == "korean":
                return "한국어" 
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Memory"
            elif first_line == "deutsch":
                return "Erinnerung"
            elif first_line == "farsi":
                return "حافظه"
            elif first_line == "russian":
                return "Память"
            elif first_line == "spanish":
                return "Memoria"
            elif first_line == "chinese":
                return "记忆"
            elif first_line == "korean":
                return "기억"
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
                return "Store in memory"
            elif first_line == "deutsch":
                return "Im Gedächtnis speichern"
            elif first_line == "farsi":
                return "ذخیره در حافظه"
            elif first_line == "russian":
                return "Сохранить в памяти"
            elif first_line == "spanish":
                return "Guardar en la memoria"
            elif first_line == "chinese":
                return "存储在记忆中"
            elif first_line == "korean":
                return "기억에 저장"
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
                return "Select stored elements"
            elif first_line == "deutsch":
                return "Gespeicherte Elemente auswählen"
            elif first_line == "farsi":
                return "انتخاب المان های ذخیره شده"
            elif first_line == "russian":
                return "Выбрать сохраненные элементы"
            elif first_line == "spanish":
                return "Seleccionar elementos almacenados"
            elif first_line == "chinese":
                return "选择存储的元素"
            elif first_line == "korean":
                return "저장된 요소 선택"
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
                return "Reduce stored selection from current selection"
            elif first_line == "deutsch":
                return "Reduzieren Sie die gespeicherte Auswahl aus der aktuellen Auswahl"
            elif first_line == "farsi":
                return "کاهش انتخاب ذخیره شده از انتخاب فعلی"
            elif first_line == "russian":
                return "Сократить сохраненный выбор из текущего выбора"
            elif first_line == "spanish":
                return "Reducir selección almacenada de la selección actual"
            elif first_line == "chinese":
                return "从当前选择中减少存储的选择"
            elif first_line == "korean":
                return "현재 선택에서 저장된 선택 축소"
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
                return "At least one element must be selected."
            elif first_line == "deutsch":
                return "Mindestens ein Element muss ausgewählt werden."
            elif first_line == "farsi":
                return "حداقل باید یک المان انتخاب شود"
            elif first_line == "russian":
                return "Должен быть выбран хотя бы один элемент."
            elif first_line == "spanish":
                return "Debe seleccionarse al menos un elemento."
            elif first_line == "chinese":
                return "必须选择至少一个元素。"
            elif first_line == "korean":
                return "최소한 하나의 요소가 선택되어야 합니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_6(file_path, model_path, model_name, current_user):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Model Path: " + str(model_path) + "\n" \
                        "Model Name: " + str(model_name) + "\n" \
                        "Stored By: " + str(current_user) + "\n" \
                        "_________________________________________" + "\n" \
                        "Selection stored in memory."
            elif first_line == "deutsch":
                return "Modellpfad: " + str(model_path) + "\n" \
                        "Modellname: " + str(model_name) + "\n" \
                        "Gespeichert von: " + str(current_user) + "\n" \
                        "_________________________________________" + "\n" \
                        "Auswahl wurde im Speicher abgelegt."
            elif first_line == "farsi":
                return "مسیر مدل: " + str(model_path) + "\n" \
                        "نام مدل: " + str(model_name) + "\n" \
                        "ذخیره شده توسط: " + str(current_user) + "\n" \
                        "_________________________________________" + "\n" \
                        "انتخاب در حافظه ذخیره شد"
            elif first_line == "russian":
                return "Путь модели: " + str(model_path) + "\n" \
                        "Название модели: " + str(model_name) + "\n" \
                        "Сохранено пользователем: " + str(current_user) + "\n" \
                        "_________________________________________" + "\n" \
                        "Выбор сохранен в памяти."
            elif first_line == "spanish":
                return "Ruta del modelo: " + str(model_path) + "\n" \
                        "Nombre del modelo: " + str(model_name) + "\n" \
                        "Almacenado por: " + str(current_user) + "\n" \
                        "_________________________________________" + "\n" \
                        "Selección almacenada en la memoria."
            elif first_line == "chinese":
                return "模型路径： " + str(model_path) + "\n" \
                        "模型名称： " + str(model_name) + "\n" \
                        "存储者： " + str(current_user) + "\n" \
                        "_________________________________________" + "\n" \
                        "选择已存储在内存中。"
            elif first_line == "korean":
                return "모델 경로: " + str(model_path) + "\n" \
                        "모델 이름: " + str(model_name) + "\n" \
                        "저장자: " + str(current_user) + "\n" \
                        "_________________________________________" + "\n" \
                        "선택이 메모리에 저장되었습니다."
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
                return  "Multiple files with the model name found. Aborting deletion."
            elif first_line == "deutsch":
                return "Mehrere Dateien mit dem Modellnamen gefunden. Löschen wird abgebrochen."
            elif first_line == "farsi":
                return "چندین فایل با نام مدل یافت شد. حذف متوقف شد"
            elif first_line == "russian":
                return "Обнаружено несколько файлов с именем модели. Отмена удаления."
            elif first_line == "spanish":
                return "Se encontraron varios archivos con el nombre del modelo. Se aborta la eliminación."
            elif first_line == "chinese":
                return "找到多个具有模型名称的文件。中止删除操作。"
            elif first_line == "korean":
                return "모델 이름과 일치하는 여러 파일이 발견되었습니다. 삭제가 중단됩니다."
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
                return "Memory is empty for current model."
            elif first_line == "deutsch":
                return "Der Speicher für dieses Modell ist leer."
            elif first_line == "farsi":
                return "حافظه برای این مدل خالی است"
            elif first_line == "russian":
                return "Память для этой модели пуста."
            elif first_line == "spanish":
                return "La memoria para este modelo está vacía."
            elif first_line == "chinese":
                return "该模型的内存为空。"
            elif first_line == "korean":
                return "현재 모델에 대한 메모리가 비어 있습니다."
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
    
def str_10(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "The selection file does not belong to this model. The file belongs to: {0}"
            elif first_line == "deutsch":
                return "Die Auswahldatei gehört nicht zu diesem Modell. Die Datei gehört zu: {0}"
            elif first_line == "farsi":
                return "فایل انتخاب متعلق به این مدل نیست. این فایل متعلق به است {0}"
            elif first_line == "russian":
                return "Файл выборки не принадлежит данной модели. Файл принадлежит: {0}"
            elif first_line == "spanish":
                return "El archivo de selección no pertenece a este modelo. El archivo pertenece a: {0}"
            elif first_line == "chinese":
                return "选择文件不属于该模型。该文件属于：{0}"
            elif first_line == "korean":
                return "선택 파일이 이 모델에 속하지 않습니다. 해당 파일은 다음에 속합니다: {0}"
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
                return  "Error"
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
    
def str_12(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Memory"
            elif first_line == "deutsch":
                return "Speicher"
            elif first_line == "farsi":
                return "حافظه"
            elif first_line == "russian":
                return "Память"
            elif first_line == "spanish":
                return "Memoria"
            elif first_line == "chinese":
                return "内存"
            elif first_line == "korean":
                return "메모리"
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
                return "Memory Status"
            elif first_line == "deutsch":
                return "Speicherstatus"
            elif first_line == "farsi":
                return "وضعیت حافظه"
            elif first_line == "russian":
                return "Статус памяти"
            elif first_line == "spanish":
                return "Estado de la memoria"
            elif first_line == "chinese":
                return "内存状态"
            elif first_line == "korean":
                return "메모리 상태"
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
                return "Do you want to empty memory?"
            elif first_line == "deutsch":
                return "Möchten Sie den Speicher leeren?"
            elif first_line == "farsi":
                return "آیا میخواهید حافظه را خالی کنید؟"
            elif first_line == "russian":
                return "Хотите опустошить память?"
            elif first_line == "spanish":
                return "¿Deseas vaciar la memoria?"
            elif first_line == "chinese":
                return "您是否想要清空内存？"
            elif first_line == "korean":
                return "메모리를 비우시겠습니까?"
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
                return "Print IDs of selection"
            elif first_line == "deutsch":
                return "Drucken Sie die Auswahl-IDs"
            elif first_line == "farsi":
                return "چاپ شناسه های انتخاب"
            elif first_line == "russian":
                return "Распечатать идентификаторы выбора"
            elif first_line == "spanish":
                return "Imprimir los IDs de la selección"
            elif first_line == "chinese":
                return "打印选择的 ID"
            elif first_line == "korean":
                return "선택 ID 인쇄"
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
                return "Model Path When First Stored: "
            elif first_line == "deutsch":
                return "Modellpfad bei erster Speicherung: "
            elif first_line == "farsi":
                return "مسیر مدل در زمان اولین ذخیره‌سازی: "
            elif first_line == "russian":
                return "Путь модели при первом сохранении: "
            elif first_line == "spanish":
                return "Ruta del modelo al momento de la primera almacenamiento: "
            elif first_line == "chinese":
                return "模型路径（首次存储时）："
            elif first_line == "korean":
                return "첫 저장 시 모델 경로: "
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
                return "Model Name When First Stored: "
            elif first_line == "deutsch":
                return "Modellname bei erster Speicherung: "
            elif first_line == "farsi":
                return "نام مدل در زمان اولین ذخیره‌سازی: "
            elif first_line == "russian":
                return "Название модели при первом сохранении: "
            elif first_line == "spanish":
                return "Nombre del modelo al momento de la primera almacenamiento: "
            elif first_line == "chinese":
                return "模型名称（首次存储时）："
            elif first_line == "korean":
                return "첫 저장 시 모델 이름: "
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
                return "Stored By: "
            elif first_line == "deutsch":
                return "Gespeichert von: "
            elif first_line == "farsi":
                return "ذخیره شده توسط: "
            elif first_line == "russian":
                return "Сохранено: "
            elif first_line == "spanish":
                return "Almacenado por: "
            elif first_line == "chinese":
                return "存储人："
            elif first_line == "korean":
                return "저장자: "
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
                return  ""
            elif first_line == "deutsch":
                return ""
            elif first_line == "farsi":
                return ""
            elif first_line == "russian":
                return ""
            elif first_line == "spanish":
                return ""
            elif first_line == "chinese":
                return ""
            elif first_line == "korean":
                return ""
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
                return "Memory is Empty."
            elif first_line == "deutsch":
                return "Der Speicher ist leer."
            elif first_line == "farsi":
                return "حافظه خالی است"
            elif first_line == "russian":
                return "Память пуста."
            elif first_line == "spanish":
                return "La memoria está vacía."
            elif first_line == "chinese":
                return "内存为空。"
            elif first_line == "korean":
                return "메모리가 비어 있습니다."
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
                return  "No file with the model name found. Aborting deletion."
            elif first_line == "deutsch":
                return "Keine Datei mit dem Modellnamen gefunden. Löschen abgebrochen."
            elif first_line == "farsi":
                return "هیچ فایلی با نام مدل پیدا نشد. حذف لغو شد"
            elif first_line == "russian":
                return "Файл с таким названием модели не найден. Отмена удаления."
            elif first_line == "spanish":
                return "No se encontró ningún archivo con el nombre del modelo. Abortando eliminación."
            elif first_line == "chinese":
                return "未找到与模型名称匹配的文件。取消删除操作。"
            elif first_line == "korean":
                return "모델 이름과 일치하는 파일을 찾을 수 없습니다. 삭제를 중단합니다."
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
                return  "No element selected."
            elif first_line == "deutsch":
                return "Kein Element ausgewählt."
            elif first_line == "farsi":
                return "هیچ المانی انتخاب نشده است"
            elif first_line == "russian":
                return "Не выбрано ни одного элемента."
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
    
def str_23(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Added by selecting elements in memory"
            elif first_line == "deutsch":
                return "Durch Auswahl von Elementen im Speicher hinzugefügt"
            elif first_line == "farsi":
                return "اضافه شده توسط انتخاب المان‌ها در حافظه"
            elif first_line == "russian":
                return "Добавлено при выборе элементов в памяти"
            elif first_line == "spanish":
                return "Agregado por seleccionar elementos en la memoria"
            elif first_line == "chinese":
                return "通过选择内存中的元素添加"
            elif first_line == "korean":
                return "메모리에서 요소를 선택하여 추가됨"
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
                return "Reduced by elements in memory"
            elif first_line == "deutsch":
                return "Durch Elemente im Speicher reduziert"
            elif first_line == "farsi":
                return "کاهش یافته توسط المان‌های موجود در حافظه"
            elif first_line == "russian":
                return "Уменьшено элементами в памяти"
            elif first_line == "spanish":
                return "Reducido por elementos en la memoria"
            elif first_line == "chinese":
                return "通过内存中的元素减少"
            elif first_line == "korean":
                return "메모리의 요소들로 감소됨"
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