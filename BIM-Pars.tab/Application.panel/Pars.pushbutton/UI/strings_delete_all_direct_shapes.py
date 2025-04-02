# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_delete_all_direct_shapes.py

def str_1(file_path):
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
    
def str_2(file_path):
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
                return "元素标识符"
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
    
def str_5(file_path):
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
    
def str_6(file_path):
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
    
def str_7(file_path):
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
    
def str_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Total"
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
    
def str_9(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return   "Delete"
            elif first_line == "deutsch":
                return "Löschen"
            elif first_line == "farsi":
                return "حذف"
            elif first_line == "russian":
                return "Удалить"
            elif first_line == "spanish":
                return "Eliminar"
            elif first_line == "chinese":
                return "删除"
            elif first_line == "korean":
                return "삭제"
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
                return   "Number of elements"
            elif first_line == "deutsch":
                return "Anzahl der Elemente"
            elif first_line == "farsi":
                return "تعداد المان ها"
            elif first_line == "russian":
                return "Количество элементов"
            elif first_line == "spanish":
                return "Número de elementos"
            elif first_line == "chinese":
                return "元素数量"
            elif first_line == "korean":
                return "요소의 수"
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
                return "Are you sure you wanna delete these elements?"
            elif first_line == "deutsch":
                return "Bist du sicher, dass du diese Elemente löschen möchtest?"
            elif first_line == "farsi":
                return "آیا مطمئن هستید که میخواهید این المان ها را حذف کنید؟"
            elif first_line == "russian":
                return "Вы уверены, что хотите удалить эти элементы?"
            elif first_line == "spanish":
                return "¿Estás seguro de que quieres eliminar estos elementos?"
            elif first_line == "chinese":
                return "您确定要删除这些元素吗？"
            elif first_line == "korean":
                return "이 요소들을 삭제하시겠습니까?"
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
    
def str_13(file_path):
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

def str_14(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete all DirectShape elements"
            elif first_line == "deutsch":
                return "Alle DirectShape-Elemente löschen"
            elif first_line == "farsi":
                return "DirectShape حذف همه المان های "
            elif first_line == "russian":
                return "Удалить все элементы DirectShape"
            elif first_line == "spanish":
                return "Eliminar todos los elementos DirectShape"
            elif first_line == "chinese":
                return "删除所有 DirectShape 元素"
            elif first_line == "korean":
                return "모든 DirectShape 요소 삭제"
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
    
def str_16(file_path):
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
    
def str_17(file_path):
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
    
def str_18(file_path):
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
    
def str_19(file_path):
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
    
def str_20(file_path):
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
    
def str_21(file_path):
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