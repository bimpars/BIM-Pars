# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_delete_elements_by_type_filter.py
    
def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "View"
            elif first_line == "deutsch":
                return "Ansicht"
            elif first_line == "farsi":
                return "نما"
            elif first_line == "russian":
                return "Вид"
            elif first_line == "spanish":
                return "Vista"
            elif first_line == "chinese":
                return "视图"
            elif first_line == "korean":
                return "보기"
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
                return  "Current view"
            elif first_line == "deutsch":
                return "Aktuelle Ansicht"
            elif first_line == "farsi":
                return "نمای فعلی"
            elif first_line == "russian":
                return "Текущий вид"
            elif first_line == "spanish":
                return "Vista actual"
            elif first_line == "chinese":
                return "当前视图"
            elif first_line == "korean":
                return "현재 보기"
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
                return  "Multiple views"
            elif first_line == "deutsch":
                return "Mehrere Ansichten"
            elif first_line == "farsi":
                return "چندین نما"
            elif first_line == "russian":
                return "Несколько видов"
            elif first_line == "spanish":
                return "Vistas múltiples"
            elif first_line == "chinese":
                return "多个视图"
            elif first_line == "korean":
                return "다중 보기"
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
                return  "Level"
            elif first_line == "deutsch":
                return "Ebene"
            elif first_line == "farsi":
                return "سطح"
            elif first_line == "russian":
                return "Уровень"
            elif first_line == "spanish":
                return "Nivel"
            elif first_line == "chinese":
                return "层级"
            elif first_line == "korean":
                return "수준"
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
                return "Include levels"
            elif first_line == "deutsch":
                return "Ebenen einbeziehen"
            elif first_line == "farsi":
                return "شامل کردن سطوح"
            elif first_line == "russian":
                return "Включить уровни"
            elif first_line == "spanish":
                return "Incluir niveles"
            elif first_line == "chinese":
                return "包括层级"
            elif first_line == "korean":
                return "레벨 포함"
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
                return "Ignore levels"
            elif first_line == "deutsch":
                return "Ebenen ignorieren"
            elif first_line == "farsi":
                return "سطوح را نادیده بگیرد"
            elif first_line == "russian":
                return "Игнорировать уровни"
            elif first_line == "spanish":
                return "Ignorar niveles"
            elif first_line == "chinese":
                return "忽略层级"
            elif first_line == "korean":
                return "레벨 무시"
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
                return "Delete by type filter"
            elif first_line == "deutsch":
                return "Löschen nach Typfilter"
            elif first_line == "farsi":
                return "حذف بر اساس فیلتر نوع"
            elif first_line == "russian":
                return "Удалить по фильтру типа"
            elif first_line == "spanish":
                return "Eliminar por filtro de tipo"
            elif first_line == "chinese":
                return "按类型过滤器删除"
            elif first_line == "korean":
                return "유형 필터로 삭제"
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
    
def str_9(file_path):
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
    
def str_10(file_path):
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
    
def str_11(file_path):
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
    
def str_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Deletion Failed - Element Still Exists"
            elif first_line == "deutsch":
                return "Löschung fehlgeschlagen - Element existiert weiterhin"
            elif first_line == "farsi":
                return "حذف ناموفق - المان هنوز وجود دارد"
            elif first_line == "russian":
                return "Удаление не удалось - элемент все еще существует"
            elif first_line == "spanish":
                return "Eliminación fallida - El elemento sigue existiendo"
            elif first_line == "chinese":
                return "删除失败 - 元素仍然存在"
            elif first_line == "korean":
                return "삭제 실패 - 요소가 여전히 존재합니다."
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
                return "Deleted"
            elif first_line == "deutsch":
                return "Gelöscht"
            elif first_line == "farsi":
                return "حذف شده"
            elif first_line == "russian":
                return "Удалено"
            elif first_line == "spanish":
                return "Eliminado"
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
    
def str_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No elements were processed for verification."
            elif first_line == "deutsch":
                return "Es wurden keine Elemente zur Überprüfung verarbeitet."
            elif first_line == "farsi":
                return ".هیچ المانی برای تأیید پردازش نشد"
            elif first_line == "russian":
                return "Не было обработано ни одного элемента для проверки."
            elif first_line == "spanish":
                return "No se procesaron elementos para la verificación."
            elif first_line == "chinese":
                return "没有元素被处理以进行验证。"
            elif first_line == "korean":
                return "검증을 위해 처리된 요소가 없습니다."
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
                return "Verification Result"
            elif first_line == "deutsch":
                return "Überprüfungsergebnis"
            elif first_line == "farsi":
                return "نتیجه تأیید"
            elif first_line == "russian":
                return "Результат проверки"
            elif first_line == "spanish":
                return "Resultado de la verificación"
            elif first_line == "chinese":
                return "验证结果"
            elif first_line == "korean":
                return "검증 결과"
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