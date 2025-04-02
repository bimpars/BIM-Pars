# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_delete_by_id.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "IDs (separate with comma):"
            elif first_line == "deutsch":
                return "IDs (mit Komma trennen):"
            elif first_line == "farsi":
                return "[شناسه‌ها [با کاما جدا کنید:"
            elif first_line == "russian":
                return "Идентификаторы (разделите запятой):"
            elif first_line == "spanish":
                return "IDs (separados por coma):"
            elif first_line == "chinese":
                return "标识符（用逗号分隔）："
            elif first_line == "korean":
                return "ID (쉼표로 구분):"
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
                return "Delete By IDs"
            elif first_line == "deutsch":
                return "Löschen nach IDs"
            elif first_line == "farsi":
                return "حذف بر اساس شناسه‌ها"
            elif first_line == "russian":
                return "Удалить по идентификаторам"
            elif first_line == "spanish":
                return "Eliminar por IDs"
            elif first_line == "chinese":
                return "按标识符删除"
            elif first_line == "korean":
                return "ID로 삭제"
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
                return "Note that only the selected elements will be deleted and the invalid ids will be ignored."
            elif first_line == "deutsch":
                return "Beachten Sie, dass nur die ausgewählten Elemente gelöscht werden und ungültige IDs ignoriert werden."
            elif first_line == "farsi":
                return "توجه کنید که تنها المان های انتخاب شده حذف خواهند شد و شناسه‌های نامعتبر نادیده گرفته خواهند شد"
            elif first_line == "russian":
                return "Обратите внимание, что будут удалены только выбранные элементы, а недопустимые идентификаторы будут проигнорированы."
            elif first_line == "spanish":
                return "Tenga en cuenta que solo se eliminarán los elementos seleccionados y se ignorarán los identificadores inválidos."
            elif first_line == "chinese":
                return "请注意，只有选定的元素将被删除，无效的标识符将被忽略。"
            elif first_line == "korean":
                return "선택한 요소만 삭제되며 잘못된 ID는 무시됩니다."
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
                return "Invalid IDs"
            elif first_line == "deutsch":
                return "Ungültige IDs"
            elif first_line == "farsi":
                return "شناسه‌های نامعتبر"
            elif first_line == "russian":
                return "Недопустимые идентификаторы"
            elif first_line == "spanish":
                return "IDs inválidos"
            elif first_line == "chinese":
                return "无效的标识符"
            elif first_line == "korean":
                return "잘못된 ID"
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
                return "All IDs are invalid."
            elif first_line == "deutsch":
                return "Alle IDs sind ungültig."
            elif first_line == "farsi":
                return "تمامی شناسه‌ها نامعتبر هستند"
            elif first_line == "russian":
                return "Все идентификаторы недопустимы."
            elif first_line == "spanish":
                return "Todos los IDs son inválidos."
            elif first_line == "chinese":
                return "所有的标识符都是无效的。"
            elif first_line == "korean":
                return "모든 ID가 유효하지 않습니다."
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
                return "Invalid IDs (not valid integers):\n"
            elif first_line == "deutsch":
                return "Ungültige IDs (keine gültigen Ganzzahlen):\n"
            elif first_line == "farsi":
                return "(شناسه‌های نامعتبر(عدد صحیح معتبر نیستند:\n"
            elif first_line == "russian":
                return "Недопустимые идентификаторы (не являются допустимыми целыми числами):\n"
            elif first_line == "spanish":
                return "IDs inválidos (no son enteros válidos):\n"
            elif first_line == "chinese":
                return "无效的标识符（不是有效的整数）：\n"
            elif first_line == "korean":
                return "잘못된 ID (유효한 정수가 아님):\n"
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
                return  "Invalid IDs (not found in the document):\n"
            elif first_line == "deutsch":
                return "Ungültige IDs (nicht im Dokument gefunden):\n"
            elif first_line == "farsi":
                return "(شناسه‌های نامعتبر (در سند یافت نشدند:\n"
            elif first_line == "russian":
                return "Недопустимые идентификаторы (не найдены в документе):\n"
            elif first_line == "spanish":
                return "IDs inválidos (no encontrados en el documento):\n"
            elif first_line == "chinese":
                return "无效的标识符（在文档中未找到）：\n"
            elif first_line == "korean":
                return "잘못된 ID (문서에서 찾을 수 없음):\n"
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
                return  "All IDs are valid."
            elif first_line == "deutsch":
                return "Alle IDs sind gültig."
            elif first_line == "farsi":
                return "تمامی شناسه‌ها معتبر هستند"
            elif first_line == "russian":
                return "Все идентификаторы допустимы."
            elif first_line == "spanish":
                return "Todos los IDs son válidos."
            elif first_line == "chinese":
                return "所有的标识符都是有效的。"
            elif first_line == "korean":
                return "모든 ID가 유효합니다."
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
                return  "deleted"
            elif first_line == "deutsch":
                return "gelöscht"
            elif first_line == "farsi":
                return "حذف شد"
            elif first_line == "russian":
                return "удалено"
            elif first_line == "spanish":
                return "eliminado"
            elif first_line == "chinese":
                return "已删除"
            elif first_line == "korean":
                return "삭제됨"
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
                return  "List of deleted elements"
            elif first_line == "deutsch":
                return "Liste der gelöschten Elemente"
            elif first_line == "farsi":
                return "لیست المان های حذف شده"
            elif first_line == "russian":
                return "Список удаленных элементов"
            elif first_line == "spanish":
                return "Lista de elementos eliminados"
            elif first_line == "chinese":
                return "已删除元素列表"
            elif first_line == "korean":
                return "삭제된 요소 목록"
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
                return "元素标识符"
            elif first_line == "korean":
                return "요소 ID"
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
                return  "Status"
            elif first_line == "deutsch":
                return "Status"
            elif first_line == "farsi":
                return "وضعیت"
            elif first_line == "russian":
                return "Статус"
            elif first_line == "spanish":
                return "Estado"
            elif first_line == "chinese":
                return "状态"
            elif first_line == "korean":
                return "상태"
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
                return  "Information"
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

def str_14(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Delete was successful" 
            elif first_line == "deutsch":
                return "Löschen war erfolgreich"
            elif first_line == "farsi":
                return "حذف با موفقیت انجام شد"
            elif first_line == "russian":
                return "Удаление прошло успешно"
            elif first_line == "spanish":
                return "La eliminación se realizó correctamente"
            elif first_line == "chinese":
                return "删除成功"
            elif first_line == "korean":
                return "삭제가 성공적으로 이루어졌습니다"
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
                return "No element found"
            elif first_line == "deutsch":
                return "Kein Element gefunden"
            elif first_line == "farsi":
                return "هیچ المانی پیدا نشد"
            elif first_line == "russian":
                return "Элементы не найдены"
            elif first_line == "spanish":
                return "No se encontró ningún elemento"
            elif first_line == "chinese":
                return "未找到任何元素"
            elif first_line == "korean":
                return "요소를 찾을 수 없음"
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
                return   "Total"
            elif first_line == "deutsch":
                return "Gesamt"
            elif first_line == "farsi":
                return "کل"
            elif first_line == "russian":
                return "Всего"
            elif first_line == "spanish":
                return "Total"
            elif first_line == "chinese":
                return "总计"
            elif first_line == "korean":
                return "합계"
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
                return  "Information"
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
    
def str_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Due to dependency of some elements could not delete elements."
            elif first_line == "deutsch":
                return "Aufgrund von Abhängigkeiten einiger Elemente konnten die Elemente nicht gelöscht werden."
            elif first_line == "farsi":
                return "به دلیل وابستگی برخی از المان ها، امکان حذف المان ها وجود ندارد"
            elif first_line == "russian":
                return "Из-за зависимости некоторых элементов невозможно удалить элементы."
            elif first_line == "spanish":
                return "Debido a la dependencia de algunos elementos, no se pudieron eliminar los elementos."
            elif first_line == "chinese":
                return "由于某些元素的依赖关系，无法删除元素。"
            elif first_line == "korean":
                return "일부 요소의 종속성으로 인해 요소를 삭제할 수 없습니다."
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
                return "Make sure no element selected"
            elif first_line == "deutsch":
                return "Stellen Sie sicher, dass kein Element ausgewählt ist"
            elif first_line == "farsi":
                return "مطمئن شوید هیچ المانی انتخاب نشده است"
            elif first_line == "russian":
                return "Убедитесь, что ни один элемент не выбран"
            elif first_line == "spanish":
                return "Asegúrese de que no se ha seleccionado ningún elemento"
            elif first_line == "chinese":
                return "确保没有选择任何元素"
            elif first_line == "korean":
                return "어떤 요소도 선택되지 않도록 하세요"
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
    
def str_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Status"
            elif first_line == "deutsch":
                return "Status"
            elif first_line == "farsi":
                return "وضعیت"
            elif first_line == "russian":
                return "Статус"
            elif first_line == "spanish":
                return "Estado"
            elif first_line == "chinese":
                return "状态"
            elif first_line == "korean":
                return "상태"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)

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