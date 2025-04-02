# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_batch_parameter_set_using_dataset.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Batch Parameter Set using Dataset"
            elif first_line == "deutsch":
                return "Batch-Parametersatz mit Datensatz"
            elif first_line == "farsi":
                return "تنظیم پارامتر دسته‌ای با استفاده از مجموعه داده"
            elif first_line == "russian":
                return "Пакетный набор параметров с использованием набора данных"
            elif first_line == "spanish":
                return "Conjunto de parámetros por lotes utilizando el conjunto de datos"
            elif first_line == "chinese":
                return "使用数据集的批量参数集"
            elif first_line == "korean":
                return "데이터 세트를 사용한 배치 매개변수 집합"
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
                return "File: "
            elif first_line == "deutsch":
                return "Datei: "
            elif first_line == "farsi":
                return "فایل: "
            elif first_line == "russian":
                return "Файл: "
            elif first_line == "spanish":
                return "Archivo: "
            elif first_line == "chinese":
                return "文件："
            elif first_line == "korean":
                return "파일: "
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
    
def str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter"
            elif first_line == "deutsch":
                return "Parameter"
            elif first_line == "farsi":
                return "پارامتر"
            elif first_line == "russian":
                return "Параметр"
            elif first_line == "spanish":
                return "Parámetro"
            elif first_line == "chinese":
                return "参数"
            elif first_line == "korean":
                return "매개변수"
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
                return "Alert: "
            elif first_line == "deutsch":
                return "Warnung: "
            elif first_line == "farsi":
                return "هشدار: "
            elif first_line == "russian":
                return "Внимание: "
            elif first_line == "spanish":
                return "Alerta: "
            elif first_line == "chinese":
                return "警告: "
            elif first_line == "korean":
                return "경고: "
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
    
def str_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Failed to set parameter '{0}' for element ID {1}: {2}"
            elif first_line == "deutsch":
                return "Fehler beim Setzen des Parameters '{0}' für die Element-ID {1}: {2}"
            elif first_line == "farsi":
                return "تنظیم پارامتر '{0}' برای شناسه المان {1} ناموفق بود: {2}"
            elif first_line == "russian":
                return "Не удалось установить параметр '{0}' для идентификатора элемента {1}: {2}"
            elif first_line == "spanish":
                return "Error al establecer el parámetro '{0}' para el ID de elemento {1}: {2}"
            elif first_line == "chinese":
                return "设置元素 ID {1} 的参数 '{0}' 失败: {2}"
            elif first_line == "korean":
                return "'{0}' 매개변수를 요소 ID {1}에 설정하지 못했습니다: {2}"
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
                return "Storage type"
            elif first_line == "deutsch":
                return "Speichertyp"
            elif first_line == "farsi":
                return "نوع ذخیره سازی"
            elif first_line == "russian":
                return "Тип хранилища"
            elif first_line == "spanish":
                return "Tipo de almacenamiento"
            elif first_line == "chinese":
                return "存储类型"
            elif first_line == "korean":
                return "저장 유형"
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
                return "An error occurred: {0}"
            elif first_line == "deutsch":
                return "Ein Fehler ist aufgetreten: {0}"
            elif first_line == "farsi":
                return "یک خطا رخ داد: {0}"
            elif first_line == "russian":
                return "Произошла ошибка: {0}"
            elif first_line == "spanish":
                return "Ocurrió un error: {0}"
            elif first_line == "chinese":
                return "发生错误: {0}"
            elif first_line == "korean":
                return "오류가 발생했습니다: {0}"
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
                return "Filter"
            elif first_line == "deutsch":
                return "Filter"
            elif first_line == "farsi":
                return "فیلتر"
            elif first_line == "russian":
                return "Фильтр"
            elif first_line == "spanish":
                return "Filtro"
            elif first_line == "chinese":
                return "过滤器"
            elif first_line == "korean":
                return "필터"
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
                return "Column:"
            elif first_line == "deutsch":
                return "Spalte:"
            elif first_line == "farsi":
                return "ستون:"
            elif first_line == "russian":
                return "Столбец:"
            elif first_line == "spanish":
                return "Columna:"
            elif first_line == "chinese":
                return "列:"
            elif first_line == "korean":
                return "열:"
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
                return "An error occurred while applying the filter: {}"
            elif first_line == "deutsch":
                return "Ein Fehler ist beim Anwenden des Filters aufgetreten: {}"
            elif first_line == "farsi":
                return "در حین اعمال فیلتر خطایی رخ داد: {}"
            elif first_line == "russian":
                return "Произошла ошибка при применении фильтра: {}"
            elif first_line == "spanish":
                return "Ocurrió un error al aplicar el filtro: {}"
            elif first_line == "chinese":
                return "应用过滤器时发生错误: {}"
            elif first_line == "korean":
                return "필터를 적용하는 동안 오류가 발생했습니다: {}"
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
                return "Parameter value setting report"
            elif first_line == "deutsch":
                return "Bericht zur Parameterwertsetzung"
            elif first_line == "farsi":
                return "گزارش تنظیم مقدار پارامتر"
            elif first_line == "russian":
                return "Отчет о настройке значения параметра"
            elif first_line == "spanish":
                return "Informe de configuración del valor del parámetro"
            elif first_line == "chinese":
                return "参数值设置报告"
            elif first_line == "korean":
                return "매개변수 값 설정 보고서"
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
                return "Previous value"
            elif first_line == "deutsch":
                return "Vorheriger Wert"
            elif first_line == "farsi":
                return "مقدار قبلی"
            elif first_line == "russian":
                return "Предыдущее значение"
            elif first_line == "spanish":
                return "Valor anterior"
            elif first_line == "chinese":
                return "先前的值"
            elif first_line == "korean":
                return "이전 값"
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
                return "New value"
            elif first_line == "deutsch":
                return "Neuer Wert"
            elif first_line == "farsi":
                return "مقدار جدید"
            elif first_line == "russian":
                return "Новое значение"
            elif first_line == "spanish":
                return "Nuevo valor"
            elif first_line == "chinese":
                return "新值"
            elif first_line == "korean":
                return "새 값"
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
                return "File name:"
            elif first_line == "deutsch":
                return "Dateiname:"
            elif first_line == "farsi":
                return "نام فایل:"
            elif first_line == "russian":
                return "Имя файла:"
            elif first_line == "spanish":
                return "Nombre del archivo:"
            elif first_line == "chinese":
                return "文件名:"
            elif first_line == "korean":
                return "파일 이름:"
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
                return "Save as Excel"
            elif first_line == "deutsch":
                return "Als Excel speichern"
            elif first_line == "farsi":
                return "ذخیره به عنوان اکسل"
            elif first_line == "russian":
                return "Сохранить как Excel"
            elif first_line == "spanish":
                return "Guardar como Excel"
            elif first_line == "chinese":
                return "另存为 Excel"
            elif first_line == "korean":
                return "Excel로 저장"
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
                return "Excel file saved successfully at "
            elif first_line == "deutsch":
                return "Excel-Datei erfolgreich gespeichert unter "
            elif first_line == "farsi":
                return "فایل اکسل با موفقیت در آدرس ذخیره شد "
            elif first_line == "russian":
                return "Файл Excel успешно сохранён по адресу "
            elif first_line == "spanish":
                return "Archivo de Excel guardado con éxito en "
            elif first_line == "chinese":
                return "Excel 文件成功保存于 "
            elif first_line == "korean":
                return "Excel 파일이 성공적으로 저장되었습니다 "
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
                return "Save operation canceled."
            elif first_line == "deutsch":
                return "Speichervorgang abgebrochen."
            elif first_line == "farsi":
                return "عملیات ذخیره سازی لغو شد"
            elif first_line == "russian":
                return "Операция сохранения отменена."
            elif first_line == "spanish":
                return "Operación de guardado cancelada."
            elif first_line == "chinese":
                return "保存操作已取消。"
            elif first_line == "korean":
                return "저장 작업이 취소되었습니다."
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
                return "An error occurred while saving the Excel file: "
            elif first_line == "deutsch":
                return "Ein Fehler ist beim Speichern der Excel-Datei aufgetreten: "
            elif first_line == "farsi":
                return "در حین ذخیره فایل اکسل خطایی رخ داد: "
            elif first_line == "russian":
                return "Произошла ошибка при сохранении файла Excel: "
            elif first_line == "spanish":
                return "Ocurrió un error al guardar el archivo de Excel: "
            elif first_line == "chinese":
                return "保存 Excel 文件时发生错误: "
            elif first_line == "korean":
                return "Excel 파일을 저장하는 동안 오류가 발생했습니다: "
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
                return "An error occurred while deleting rows: "
            elif first_line == "deutsch":
                return "Ein Fehler ist beim Löschen der Zeilen aufgetreten: "
            elif first_line == "farsi":
                return "در حین حذف ردیف‌ها خطایی رخ داد: "
            elif first_line == "russian":
                return "Произошла ошибка при удалении строк: "
            elif first_line == "spanish":
                return "Ocurrió un error al eliminar filas: "
            elif first_line == "chinese":
                return "删除行时发生错误: "
            elif first_line == "korean":
                return "행을 삭제하는 동안 오류가 발생했습니다: "
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
                return "Unsupported file format."
            elif first_line == "deutsch":
                return "Nicht unterstütztes Dateiformat."
            elif first_line == "farsi":
                return "فرمت فایل پشتیبانی نمی‌شود"
            elif first_line == "russian":
                return "Неподдерживаемый формат файла."
            elif first_line == "spanish":
                return "Formato de archivo no soportado."
            elif first_line == "chinese":
                return "不支持的文件格式。"
            elif first_line == "korean":
                return "지원되지 않는 파일 형식입니다."
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
                return "An error occurred: "
            elif first_line == "deutsch":
                return "Ein Fehler ist aufgetreten: "
            elif first_line == "farsi":
                return "یک خطا رخ داد: "
            elif first_line == "russian":
                return "Произошла ошибка: "
            elif first_line == "spanish":
                return "Ocurrió un error: "
            elif first_line == "chinese":
                return "发生错误: "
            elif first_line == "korean":
                return "오류가 발생했습니다: "
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
                return "Invalid element ID"
            elif first_line == "deutsch":
                return "Ungültige Element-ID"
            elif first_line == "farsi":
                return "شناسه المان نامعتبر"
            elif first_line == "russian":
                return "Недействительный идентификатор элемента"
            elif first_line == "spanish":
                return "ID de elemento no válido"
            elif first_line == "chinese":
                return "无效的元素 ID"
            elif first_line == "korean":
                return "잘못된 요소 ID"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_26(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter not found"
            elif first_line == "deutsch":
                return "Parameter nicht gefunden"
            elif first_line == "farsi":
                return "پارامتر یافت نشد"
            elif first_line == "russian":
                return "Параметр не найден"
            elif first_line == "spanish":
                return "Parámetro no encontrado"
            elif first_line == "chinese":
                return "未找到参数"
            elif first_line == "korean":
                return "매개변수를 찾을 수 없습니다"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_27(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Element not found"
            elif first_line == "deutsch":
                return "Element nicht gefunden"
            elif first_line == "farsi":
                return "المان یافت نشد"
            elif first_line == "russian":
                return "Элемент не найден"
            elif first_line == "spanish":
                return "Elemento no encontrado"
            elif first_line == "chinese":
                return "未找到元素"
            elif first_line == "korean":
                return "요소를 찾을 수 없습니다"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_28(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter name missing"
            elif first_line == "deutsch":
                return "Parametername fehlt"
            elif first_line == "farsi":
                return "نام پارامترواردنشده"
            elif first_line == "russian":
                return "Отсутствует имя параметра"
            elif first_line == "spanish":
                return "Nombre del parámetro faltante"
            elif first_line == "chinese":
                return "参数名称缺失"
            elif first_line == "korean":
                return "매개변수 이름이 없습니다"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_29(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Element ID missing"
            elif first_line == "deutsch":
                return "Element-ID fehlt""Element-ID fehlt"
            elif first_line == "farsi":
                return "شناسه ی المان واردنشده"
            elif first_line == "russian":
                return "Отсутствует идентификатор элемента"
            elif first_line == "spanish":
                return "ID de elemento faltante"
            elif first_line == "chinese":
                return "元素 ID 缺失"
            elif first_line == "korean":
                return "요소 ID가 없습니다"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_30(file_path):
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
    
def str_31(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Invalid Element ID: "
            elif first_line == "deutsch":
                return "Ungültige Element-ID: "
            elif first_line == "farsi":
                return "شناسه المان نامعتبر: "
            elif first_line == "russian":
                return "Недействительный идентификатор элемента: "
            elif first_line == "spanish":
                return "ID de elemento no válido: "
            elif first_line == "chinese":
                return "无效的元素 ID: "
            elif first_line == "korean":
                return "잘못된 요소 ID: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_32(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No element selected"
            elif first_line == "deutsch":
                return "Kein Element ausgewählt"
            elif first_line == "farsi":
                return "هیچ المانی انتخاب نشده"
            elif first_line == "russian":
                return "Элемент не выбран"
            elif first_line == "spanish":
                return "Ningún elemento seleccionado"
            elif first_line == "chinese":
                return "未选择任何元素"
            elif first_line == "korean":
                return "선택된 요소가 없습니다"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_33(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "select"
            elif first_line == "deutsch":
                return "auswählen"
            elif first_line == "farsi":
                return "انتخاب کنید"
            elif first_line == "russian":
                return "выбрать"
            elif first_line == "spanish":
                return "seleccionar"
            elif first_line == "chinese":
                return "选择"
            elif first_line == "korean":
                return "선택하다"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_34(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unsupported file type."
            elif first_line == "deutsch":
                return "Nicht unterstützter Dateityp."
            elif first_line == "farsi":
                return "نوع فایل پشتیبانی نمی‌شود"
            elif first_line == "russian":
                return "Неподдерживаемый тип файла."
            elif first_line == "spanish":
                return "Tipo de archivo no soportado."
            elif first_line == "chinese":
                return "不支持的文件类型。"
            elif first_line == "korean":
                return "지원되지 않는 파일 형식입니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_35(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error during file processing: "
            elif first_line == "deutsch":
                return "Fehler beim Verarbeiten der Datei: "
            elif first_line == "farsi":
                return "خطا در حین پردازش فایل: "
            elif first_line == "russian":
                return "Ошибка при обработке файла: "
            elif first_line == "spanish":
                return "Error durante el procesamiento del archivo: "
            elif first_line == "chinese":
                return "文件处理期间发生错误: "
            elif first_line == "korean":
                return "파일 처리 중 오류 발생: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_36(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Element ID List"
            elif first_line == "deutsch":
                return "Element-ID-Liste"
            elif first_line == "farsi":
                return "لیست شناسه المان"
            elif first_line == "russian":
                return "Список идентификаторов элементов"
            elif first_line == "spanish":
                return "Lista de ID de elementos"
            elif first_line == "chinese":
                return "元素 ID 列表"
            elif first_line == "korean":
                return "요소 ID 목록"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_37(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Data Converter"
            elif first_line == "deutsch":
                return "Datenkonverter"
            elif first_line == "farsi":
                return "تبدیل کننده داده"
            elif first_line == "russian":
                return "Конвертер данных"
            elif first_line == "spanish":
                return "Convertidor de datos"
            elif first_line == "chinese":
                return "数据转换器"
            elif first_line == "korean":
                return "데이터 변환기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_38(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Convert XLSX to TXT format"
            elif first_line == "deutsch":
                return "XLSX in TXT-Format konvertieren"
            elif first_line == "farsi":
                return "[TXT] به [XLSX] تبدیل فرمت "
            elif first_line == "russian":
                return "Конвертировать XLSX в формат TXT"
            elif first_line == "spanish":
                return "Convertir XLSX a formato TXT"
            elif first_line == "chinese":
                return "将 XLSX 转换为 TXT 格式"
            elif first_line == "korean":
                return "XLSX를 TXT 형식으로 변환"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_39(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Convert CSV to TXT format"
            elif first_line == "deutsch":
                return "CSV in TXT-Format konvertieren"
            elif first_line == "farsi":
                return "[TXT] به [CSV] تبدیل فرمت "
            elif first_line == "russian":
                return "Конвертировать CSV в формат TXT"
            elif first_line == "spanish":
                return "Convertir CSV a formato TXT"
            elif first_line == "chinese":
                return "将 CSV 转换为 TXT 格式"
            elif first_line == "korean":
                return "CSV를 TXT 형식으로 변환"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_40(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "If your data set contains illegal characters and after importing CSV or XLSX you are encountering encoding problems, you might solve the problem simply by converting your file to TXT format."
            elif first_line == "deutsch":
                return "Wenn Ihr Datensatz ungültige Zeichen enthält und Sie nach dem Importieren von CSV oder XLSX auf Kodierungsprobleme stoßen, können Sie das Problem einfach lösen, indem Sie Ihre Datei in das TXT-Format konvertieren, das das native Format des Plugins ist."
            elif first_line == "farsi":
                return " .اگر مجموعه داده شما شامل کاراکترهای غیرمجاز است و پس از وارد کردن [سی اس وی] یا [اکسل] با مشکلات حروف نامربوط مواجه می‌شوید، می‌توانید به سادگی با تبدیل فایل خود به فرمت [تکست] مشکل را حل کنید"
            elif first_line == "russian":
                return "Если ваш набор данных содержит недопустимые символы и после импорта CSV или XLSX вы сталкиваетесь с проблемами кодировки, вы можете просто решить проблему, конвертировав файл в формат TXT, который является родным форматом плагина."
            elif first_line == "spanish":
                return "Si su conjunto de datos contiene caracteres ilegales y después de importar CSV o XLSX está encontrando problemas de codificación, puede resolver el problema simplemente convirtiendo su archivo al formato TXT, que es el formato nativo del plugin."
            elif first_line == "chinese":
                return "如果您的数据集包含非法字符，并且在导入 CSV 或 XLSX 后遇到编码问题，您可以通过将文件转换为 TXT 格式来简单解决问题，TXT 格式是插件的本地格式。"
            elif first_line == "korean":
                return "데이터 세트에 잘못된 문자가 포함되어 있고 CSV 또는 XLSX를 가져온 후 인코딩 문제가 발생하는 경우, 파일을 플러그인의 기본 형식인 TXT 형식으로 변환하면 문제가 간단히 해결될 수 있습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
 
def str_41(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please select an option.\n"
            elif first_line == "deutsch":
                return "Bitte wählen Sie eine Option.\n"
            elif first_line == "farsi":
                return "لطفاً یک گزینه را انتخاب کنید\n"
            elif first_line == "russian":
                return "Пожалуйста, выберите вариант.\n"
            elif first_line == "spanish":
                return "Por favor, seleccione una opción.\n"
            elif first_line == "chinese":
                return "请选择一个选项。\n"
            elif first_line == "korean":
                return "옵션을 선택해 주세요.\n"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_42(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No data was written to the file. Check if the CSV file has data.\n"
            elif first_line == "deutsch":
                return "Es wurden keine Daten in die Datei geschrieben. Überprüfen Sie, ob die CSV-Datei Daten enthält.\n"
            elif first_line == "farsi":
                return "هیچ داده‌ای به فایل نوشته نشد. بررسی کنید که آیا فایل CSV داده دارد\n"
            elif first_line == "russian":
                return "Данные в файл не записаны. Проверьте, есть ли данные в файле CSV.\n"
            elif first_line == "spanish":
                return "No se escribieron datos en el archivo. Verifique si el archivo CSV tiene datos.\n"
            elif first_line == "chinese":
                return "没有数据写入文件。请检查 CSV 文件是否有数据。\n"
            elif first_line == "korean":
                return "파일에 데이터가 작성되지 않았습니다. CSV 파일에 데이터가 있는지 확인하세요.\n"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_43(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Conversion was successful.     \n"
            elif first_line == "deutsch":
                return "Die Konvertierung war erfolgreich.     \n"
            elif first_line == "farsi":
                return "تبدیل با موفقیت انجام شد     \n"
            elif first_line == "russian":
                return "Конвертация прошла успешно.     \n"
            elif first_line == "spanish":
                return "La conversión fue exitosa.     \n"
            elif first_line == "chinese":
                return "转换成功。     \n"
            elif first_line == "korean":
                return "변환이 성공했습니다.     \n"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_44(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error during conversion: "
            elif first_line == "deutsch":
                return "Fehler bei der Konvertierung: "
            elif first_line == "farsi":
                return "خطا در حین تبدیل: "
            elif first_line == "russian":
                return "Ошибка при конвертации: "
            elif first_line == "spanish":
                return "Error durante la conversión: "
            elif first_line == "chinese":
                return "转换期间发生错误: "
            elif first_line == "korean":
                return "변환 중 오류 발생: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_45(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "File selection canceled.\n"
            elif first_line == "deutsch":
                return "Dateiauswahl abgebrochen.\n"
            elif first_line == "farsi":
                return "انتخاب فایل لغو شد\n"
            elif first_line == "russian":
                return "Выбор файла отменён.\n"
            elif first_line == "spanish":
                return "Selección de archivo cancelada.\n"
            elif first_line == "chinese":
                return "文件选择已取消。\n"
            elif first_line == "korean":
                return "파일 선택이 취소되었습니다.\n"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_46(file_path):
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
        return "An error occurred: {e}"
    
def str_47(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Elements"
            elif first_line == "deutsch":
                return "Elemente"
            elif first_line == "farsi":
                return "المان ها"
            elif first_line == "russian":
                return "Элементы"
            elif first_line == "spanish":
                return "Elementos"
            elif first_line == "chinese":
                return "元素"
            elif first_line == "korean":
                return "요소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_48(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Category List"
            elif first_line == "deutsch":
                return "Kategorieliste"
            elif first_line == "farsi":
                return "لیست دسته‌بندی"
            elif first_line == "russian":
                return "Список категорий"
            elif first_line == "spanish":
                return "Lista de categorías"
            elif first_line == "chinese":
                return "类别列表"
            elif first_line == "korean":
                return "카테고리 목록"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_49(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error setting parameter '{0}' for element '{1}': {2}"
            elif first_line == "deutsch":
                return "Fehler beim Setzen des Parameters '{0}' für das Element '{1}': {2}"
            elif first_line == "farsi":
                return "خطا در تنظیم پارامتر '{0}' برای المان '{1}': {2}"
            elif first_line == "russian":
                return "Ошибка при установке параметра '{0}' для элемента '{1}': {2}"
            elif first_line == "spanish":
                return "Error al establecer el parámetro '{0}' para el elemento '{1}': {2}"
            elif first_line == "chinese":
                return "设置元素 '{1}' 的参数 '{0}' 时出错：{2}"
            elif first_line == "korean":
                return "요소 '{1}'의 매개변수 '{0}'를 설정하는 중 오류 발생: {2}"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_50(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Operation failed: {0}"
            elif first_line == "deutsch":
                return "Operation fehlgeschlagen: {0}"
            elif first_line == "farsi":
                return "عملیات ناموفق بود: {0}"
            elif first_line == "russian":
                return "Операция не удалась: {0}"
            elif first_line == "spanish":
                return "Operación fallida: {0}"
            elif first_line == "chinese":
                return "操作失败：{0}"
            elif first_line == "korean":
                return "작업 실패: {0}"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_51(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Wait till report gets generated..."
            elif first_line == "deutsch":
                return "Warten, bis der Bericht erstellt wird..."
            elif first_line == "farsi":
                return "صبرکنید تا گزارش ایجادشود ..."
            elif first_line == "russian":
                return "Подождите, пока отчет будет сгенерирован..."
            elif first_line == "spanish":
                return "Espere hasta que se genere el informe..."
            elif first_line == "chinese":
                return "请等待报告生成..."
            elif first_line == "korean":
                return "보고서가 생성될 때까지 기다려 주세요..."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_52(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Report"
            elif first_line == "deutsch":
                return "Bericht"
            elif first_line == "farsi":
                return "گزارش"
            elif first_line == "russian":
                return "Отчет"
            elif first_line == "spanish":
                return "Informe"
            elif first_line == "chinese":
                return "报告"
            elif first_line == "korean":
                return "보고서"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_53(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Simple report"
            elif first_line == "deutsch":
                return "Einfacher Bericht"
            elif first_line == "farsi":
                return "گزارش ساده"
            elif first_line == "russian":
                return "Простой отчет"
            elif first_line == "spanish":
                return "Informe sencillo"
            elif first_line == "chinese":
                return "简单报告"
            elif first_line == "korean":
                return "간단한 보고서"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_54(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Does not include element IDs."
            elif first_line == "deutsch":
                return "Enthält keine Element-IDs."
            elif first_line == "farsi":
                return "شامل شناسه‌های المان نمی شود"
            elif first_line == "russian":
                return "Не включает идентификаторы элементов."
            elif first_line == "spanish":
                return "No incluye IDs de elementos."
            elif first_line == "chinese":
                return "不包括元素 ID。"
            elif first_line == "korean":
                return "요소 ID를 포함하지 않습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_55(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Detailed report"
            elif first_line == "deutsch":
                return "Detaillierter Bericht"
            elif first_line == "farsi":
                return "گزارش دقیق"
            elif first_line == "russian":
                return "Подробный отчет"
            elif first_line == "spanish":
                return "Informe detallado"
            elif first_line == "chinese":
                return "详细报告"
            elif first_line == "korean":
                return "자세한 보고서"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_56(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Includes elements of each category. Depending on the number of elements, the process might take some time."
            elif first_line == "deutsch":
                return "Enthält Elemente jeder Kategorie. Je nach Anzahl der Elemente kann der Prozess einige Zeit in Anspruch nehmen."
            elif first_line == "farsi":
                return ".شامل المان های هر دسته است. بسته به تعداد المان ها، این فرآیند ممکن است مدتی طول بکشد"
            elif first_line == "russian":
                return "Включает элементы каждой категории. В зависимости от количества элементов процесс может занять некоторое время."
            elif first_line == "spanish":
                return "Incluye elementos de cada categoría. Dependiendo del número de elementos, el proceso puede tardar un tiempo."
            elif first_line == "chinese":
                return "包括每个类别的元素。根据元素的数量，过程可能需要一些时间。"
            elif first_line == "korean":
                return "각 카테고리의 요소를 포함합니다. 요소 수에 따라 프로세스가 다소 시간이 걸릴 수 있습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_57(file_path):
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
        return "An error occurred: {e}"
    
def str_58(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Generating report was successful."
            elif first_line == "deutsch":
                return "Die Berichtserstellung war erfolgreich."
            elif first_line == "farsi":
                return ".ایجاد گزارش با موفقیت انجام شد"
            elif first_line == "russian":
                return "Создание отчета прошло успешно."
            elif first_line == "spanish":
                return "La generación del informe fue exitosa."
            elif first_line == "chinese":
                return "报告生成成功。"
            elif first_line == "korean":
                return "보고서 생성이 성공했습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_59(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Value of elements in category"
            elif first_line == "deutsch":
                return "Wert der Elemente in der Kategorie"
            elif first_line == "farsi":
                return "مقدار المان ها در دسته بندی"
            elif first_line == "russian":
                return "Значение элементов в категории"
            elif first_line == "spanish":
                return "Valor de elementos en la categoría"
            elif first_line == "chinese":
                return "类别中元素的值"
            elif first_line == "korean":
                return "카테고리의 요소 값"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_60(file_path):
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
        return "An error occurred: {e}"
    
def str_61(file_path):
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
    
def str_62(file_path):
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
    
def str_63(file_path):
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
        return "An error occurred: {e}"
    
def str_64(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter"
            elif first_line == "deutsch":
                return "Parameter"
            elif first_line == "farsi":
                return "پارامتر"
            elif first_line == "russian":
                return "Параметр"
            elif first_line == "spanish":
                return "Parámetro"
            elif first_line == "chinese":
                return "参数"
            elif first_line == "korean":
                return "매개변수"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_65(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Storage Type"
            elif first_line == "deutsch":
                return "Speichertyp"
            elif first_line == "farsi":
                return "نوع ذخیره‌سازی"
            elif first_line == "russian":
                return "Тип хранения"
            elif first_line == "spanish":
                return "Tipo de almacenamiento"
            elif first_line == "chinese":
                return "存储类型"
            elif first_line == "korean":
                return "저장 유형"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_66(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Previous Value"
            elif first_line == "deutsch":
                return "Vorheriger Wert"
            elif first_line == "farsi":
                return "مقدار قبلی"
            elif first_line == "russian":
                return "Предыдущее значение"
            elif first_line == "spanish":
                return "Valor anterior"
            elif first_line == "chinese":
                return "先前的值"
            elif first_line == "korean":
                return "이전 값"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_67(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "New Value"
            elif first_line == "deutsch":
                return "Neuer Wert"
            elif first_line == "farsi":
                return "مقدار جدید"
            elif first_line == "russian":
                return "Новое значение"
            elif first_line == "spanish":
                return "Nuevo valor"
            elif first_line == "chinese":
                return "新值"
            elif first_line == "korean":
                return "새로운 값"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_68(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Convert Excel file to Text file for Element ID List"
            elif first_line == "deutsch":
                return "Excel-Datei in Textdatei für Element-ID-Liste konvertieren"
            elif first_line == "farsi":
                return "تبدیل فایل اکسل به فایل متنی برای لیست شناسه المان"
            elif first_line == "russian":
                return "Преобразовать файл Excel в текстовый файл для списка идентификаторов элементов"
            elif first_line == "spanish":
                return "Convertir archivo de Excel a archivo de texto para la lista de ID de elementos"
            elif first_line == "chinese":
                return "将Excel文件转换为元素ID列表的文本文件"
            elif first_line == "korean":
                return "요소 ID 목록을 위한 Excel 파일을 텍스트 파일로 변환"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_69(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Convert Excel file to Text file for Category List"
            elif first_line == "deutsch":
                return "Excel-Datei in Textdatei für Kategorienliste konvertieren"
            elif first_line == "farsi":
                return "تبدیل فایل اکسل به فایل متنی برای لیست دسته‌بندی"
            elif first_line == "russian":
                return "Преобразовать файл Excel в текстовый файл для списка категорий"
            elif first_line == "spanish":
                return "Convertir archivo de Excel a archivo de texto para la lista de categorías"
            elif first_line == "chinese":
                return "将Excel文件转换为类别列表的文本文件"
            elif first_line == "korean":
                return "카테고리 목록을 위한 Excel 파일을 텍스트 파일로 변환"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_70(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Convert CSV file to Text file for Element ID List"
            elif first_line == "deutsch":
                return "CSV-Datei in Textdatei für Element-ID-Liste konvertieren"
            elif first_line == "farsi":
                return "تبدیل فایل 'سی اس وی' به فایل متنی برای لیست شناسه المان"
            elif first_line == "russian":
                return "Преобразовать файл CSV в текстовый файл для списка идентификаторов элементов"
            elif first_line == "spanish":
                return "Convertir archivo CSV a archivo de texto para la lista de ID de elementos"
            elif first_line == "chinese":
                return "将CSV文件转换为元素ID列表的文本文件"
            elif first_line == "korean":
                return "요소 ID 목록을 위한 CSV 파일을 텍스트 파일로 변환"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_71(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Convert CSV file to Text file for Category List"
            elif first_line == "deutsch":
                return "CSV-Datei in Textdatei für Kategorienliste konvertieren"
            elif first_line == "farsi":
                return "تبدیل فایل 'سی اس وی' به فایل متنی برای لیست دسته‌بندی"
            elif first_line == "russian":
                return "Преобразовать файл CSV в текстовый файл для списка категорий"
            elif first_line == "spanish":
                return "Convertir archivo CSV a archivo de texto para la lista de categorías"
            elif first_line == "chinese":
                return "将CSV文件转换为类别列表的文本文件"
            elif first_line == "korean":
                return "카테고리 목록을 위한 CSV 파일을 텍스트 파일로 변환"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_72(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No category"
            elif first_line == "deutsch":
                return "Keine Kategorie"
            elif first_line == "farsi":
                return "بدون دسته‌بندی"
            elif first_line == "russian":
                return "Без категории"
            elif first_line == "spanish":
                return "Sin categoría"
            elif first_line == "chinese":
                return "没有类别"
            elif first_line == "korean":
                return "카테고리 없음"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_73(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter not found"
            elif first_line == "deutsch":
                return "Parameter nicht gefunden"
            elif first_line == "farsi":
                return "پارامتر پیدا نشد"
            elif first_line == "russian":
                return "Параметр не найден"
            elif first_line == "spanish":
                return "Parámetro no encontrado"
            elif first_line == "chinese":
                return "未找到参数"
            elif first_line == "korean":
                return "매개변수가 발견되지 않음"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_74(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Element not found"
            elif first_line == "deutsch":
                return "Element nicht gefunden"
            elif first_line == "farsi":
                return "المان پیدا نشد"
            elif first_line == "russian":
                return "Элемент не найден"
            elif first_line == "spanish":
                return "Elemento no encontrado"
            elif first_line == "chinese":
                return "未找到元素"
            elif first_line == "korean":
                return "요소를 찾을 수 없음"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_75(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error retrieving element with ID"
            elif first_line == "deutsch":
                return "Fehler beim Abrufen des Elements mit der ID"
            elif first_line == "farsi":
                return "خطا در بازیابی  المان با شناسه"
            elif first_line == "russian":
                return "Ошибка при извлечении элемента с ID"
            elif first_line == "spanish":
                return "Error al recuperar el elemento con ID"
            elif first_line == "chinese":
                return "获取元素时出错，ID"
            elif first_line == "korean":
                return "ID로 요소를 검색하는 중 오류"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_76(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error retrieving category"
            elif first_line == "deutsch":
                return "Fehler beim Abrufen der Kategorie"
            elif first_line == "farsi":
                return "خطا در بازیابی دسته‌بندی"
            elif first_line == "russian":
                return "Ошибка при извлечении категории"
            elif first_line == "spanish":
                return "Error al recuperar la categoría"
            elif first_line == "chinese":
                return "获取类别时出错"
            elif first_line == "korean":
                return "카테고리 검색 중 오류"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_77(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error retrieving parameter type"
            elif first_line == "deutsch":
                return "Fehler beim Abrufen des Parametertyps"
            elif first_line == "farsi":
                return "خطا در بازیابی نوع پارامتر"
            elif first_line == "russian":
                return "Ошибка при извлечении типа параметра"
            elif first_line == "spanish":
                return "Error al recuperar el tipo de parámetro"
            elif first_line == "chinese":
                return "获取参数类型时出错"
            elif first_line == "korean":
                return "매개변수 유형 검색 중 오류"
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
    