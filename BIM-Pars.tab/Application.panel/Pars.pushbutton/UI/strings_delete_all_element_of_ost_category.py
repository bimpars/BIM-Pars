# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_delete_all_element_of_category.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select Categories"
            elif first_line == "deutsch":
                return "Kategorien auswählen"
            elif first_line == "farsi":
                return "انتخاب دسته‌بندی‌ها"
            elif first_line == "russian":
                return "Выберите категории"
            elif first_line == "spanish":
                return "Seleccionar categorías"
            elif first_line == "chinese":
                return "选择分类"
            elif first_line == "korean":
                return "카테고리 선택"
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
                return "Select"
            elif first_line == "deutsch":
                return "Auswählen"
            elif first_line == "farsi":
                return "انتخاب "
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
    
def str_3(file_path):
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
    
def str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Category Name: " 
            elif first_line == "deutsch":
                return "Kategoriename: "
            elif first_line == "farsi":
                return "نام دسته‌بندی: "
            elif first_line == "russian":
                return "Название категории: "
            elif first_line == "spanish":
                return "Nombre de la categoría: "
            elif first_line == "chinese":
                return "类别名称："
            elif first_line == "korean":
                return "카테고리 이름: "
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

def str_6(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete all elements of category"
            elif first_line == "deutsch":
                return "Alle Elemente der Kategorie löschen"
            elif first_line == "farsi":
                return "حذف همه المان های دسته بندی"
            elif first_line == "russian":
                return "Удалить все элементы категории"
            elif first_line == "spanish":
                return "Eliminar todos los elementos de la categoría"
            elif first_line == "chinese":
                return "删除该类别的所有元素"
            elif first_line == "korean":
                return "범주의 모든 요소 삭제"
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
    
def str_8(file_path):
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
    
def str_9(file_path):
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
    
def str_10(file_path):
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
    
def str_11(file_path):
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
    
def str_12(file_path):
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
    
def str_13(file_path):
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
    
def str_14(file_path):
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
