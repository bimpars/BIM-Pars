# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_delete_elements_by_ids_from_excel.py
    
def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Row-Column" 
            elif first_line == "deutsch":
                return "Zeile-Spalte"
            elif first_line == "farsi":
                return "ردیف-ستون"
            elif first_line == "russian":
                return "Строка-столбец"
            elif first_line == "spanish":
                return "Fila-Columna"
            elif first_line == "chinese":
                return "行-列"
            elif first_line == "korean":
                return "행-열"
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
                return "Row:"
            elif first_line == "deutsch":
                return "Zeile:"
            elif first_line == "farsi":
                return "ردیف:"
            elif first_line == "russian":
                return "Строка:"
            elif first_line == "spanish":
                return "Fila:"
            elif first_line == "chinese":
                return "行:"
            elif first_line == "korean":
                return "행:"
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
    
def str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Row"
            elif first_line == "deutsch":
                return "Zeile"
            elif first_line == "farsi":
                return "ردیف"
            elif first_line == "russian":
                return "Строка"
            elif first_line == "spanish":
                return "Fila"
            elif first_line == "chinese":
                return "行"
            elif first_line == "korean":
                return "행"
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
                return "Column"
            elif first_line == "deutsch":
                return "Spalte"
            elif first_line == "farsi":
                return "ستون"
            elif first_line == "russian":
                return "Столбец"
            elif first_line == "spanish":
                return "Columna"
            elif first_line == "chinese":
                return "列"
            elif first_line == "korean":
                return "열"
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
                return "Row {}, Column {}"
            elif first_line == "deutsch":
                return "Zeile {}, Spalte {}"
            elif first_line == "farsi":
                return "ردیف {}، ستون {}"
            elif first_line == "russian":
                return "Строка {}, Столбец {}"
            elif first_line == "spanish":
                return "Fila {}, Columna {}"
            elif first_line == "chinese":
                return "第{}行，第{}列"
            elif first_line == "korean":
                return "{}행, {}열"
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
                return "شناسه‌های نامعتبر (در سند یافت نشدند)\n"
            elif first_line == "russian":
                return "Недопустимые идентификаторы (не найдены в документе):\n"
            elif first_line == "spanish":
                return "IDs inválidos (no encontrados en el documento):\n"
            elif first_line == "chinese":
                return "无效的ID（在文档中未找到）：\n"
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
                return "Все идентификаторы действительны."
            elif first_line == "spanish":
                return "Todos los IDs son válidos."
            elif first_line == "chinese":
                return "所有ID均有效。"
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
                return  "Invalid IDs"
            elif first_line == "deutsch":
                return "Ungültige IDs"
            elif first_line == "farsi":
                return "شناسه‌های نامعتبر"
            elif first_line == "russian":
                return "Недопустимые идентификаторы"
            elif first_line == "spanish":
                return "IDs inválidos"
            elif first_line == "chinese":
                return "无效的ID"
            elif first_line == "korean":
                return "잘못된 ID"
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
                return  "Please enter valid numeric values for row and column numbers."
            elif first_line == "deutsch":
                return "Bitte geben Sie gültige numerische Werte für Zeilen- und Spaltennummern ein."
            elif first_line == "farsi":
                return "لطفاً برای شماره ردیف و ستون مقادیر عددی معتبر وارد کنید"
            elif first_line == "russian":
                return "Пожалуйста, введите действительные числовые значения для номеров строки и столбца."
            elif first_line == "spanish":
                return "Por favor, ingrese valores numéricos válidos para los números de fila y columna."
            elif first_line == "chinese":
                return "请为行号和列号输入有效的数值。"
            elif first_line == "korean":
                return "행 번호와 열 번호에 유효한 숫자 값을 입력해주세요."
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
                return  "Invalid Input"
            elif first_line == "deutsch":
                return "Ungültige Eingabe"
            elif first_line == "farsi":
                return "ورودی نامعتبر"
            elif first_line == "russian":
                return "Неверный ввод"
            elif first_line == "spanish":
                return "Entrada inválida"
            elif first_line == "chinese":
                return "无效输入"
            elif first_line == "korean":
                return "잘못된 입력"
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
                return  "Enter the row number:"
            elif first_line == "deutsch":
                return "Geben Sie die Zeilennummer ein:"
            elif first_line == "farsi":
                return "شماره ردیف را وارد کنید:"
            elif first_line == "russian":
                return "Введите номер строки:"
            elif first_line == "spanish":
                return "Ingrese el número de fila:"
            elif first_line == "chinese":
                return "输入行号："
            elif first_line == "korean":
                return "행 번호를 입력하세요:"
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
                return  "Row Number"
            elif first_line == "deutsch":
                return "Zeilennummer"
            elif first_line == "farsi":
                return "شماره ردیف"
            elif first_line == "russian":
                return "Номер строки"
            elif first_line == "spanish":
                return "Número de fila"
            elif first_line == "chinese":
                return "行号"
            elif first_line == "korean":
                return "행 번호"
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
                return  "Column {}"
            elif first_line == "deutsch":
                return "Spalte {}"
            elif first_line == "farsi":
                return "ستون {}"
            elif first_line == "russian":
                return "Столбец {}"
            elif first_line == "spanish":
                return "Columna {}"
            elif first_line == "chinese":
                return "列 {}"
            elif first_line == "korean":
                return "{}열"
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
                return   "Please enter a positive integer."
            elif first_line == "deutsch":
                return "Bitte geben Sie eine positive ganze Zahl ein."
            elif first_line == "farsi":
                return "لطفاً یک عدد صحیح مثبت وارد کنید"
            elif first_line == "russian":
                return "Пожалуйста, введите положительное целое число."
            elif first_line == "spanish":
                return "Por favor, ingrese un número entero positivo."
            elif first_line == "chinese":
                return "请输入一个正整数。"
            elif first_line == "korean":
                return "양의 정수를 입력하세요."
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
                return  "Please enter an integer."
            elif first_line == "deutsch":
                return "Bitte geben Sie eine ganze Zahl ein."
            elif first_line == "farsi":
                return "لطفاً یک عدد صحیح وارد کنید"
            elif first_line == "russian":
                return "Пожалуйста, введите целое число."
            elif first_line == "spanish":
                return "Por favor, ingrese un número entero."
            elif first_line == "chinese":
                return "请输入一个整数。"
            elif first_line == "korean":
                return "정수를 입력하세요."
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
                return   "Enter the column number:"
            elif first_line == "deutsch":
                return "Geben Sie die Spaltennummer ein:"
            elif first_line == "farsi":
                return "شماره ستون را وارد کنید:"
            elif first_line == "russian":
                return "Введите номер столбца:"
            elif first_line == "spanish":
                return "Ingrese el número de columna:"
            elif first_line == "chinese":
                return "输入列号："
            elif first_line == "korean":
                return "열 번호를 입력하세요:"
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
                return  "Column Number"
            elif first_line == "deutsch":
                return "Spaltennummer"
            elif first_line == "farsi":
                return "شماره ستون"
            elif first_line == "russian":
                return "Номер столбца"
            elif first_line == "spanish":
                return "Número de columna"
            elif first_line == "chinese":
                return "列号"
            elif first_line == "korean":
                return "열 번호"
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
                return  "Row {}"
            elif first_line == "deutsch":
                return "Zeile {}"
            elif first_line == "farsi":
                return "ردیف {}"
            elif first_line == "russian":
                return "Строка {}"
            elif first_line == "spanish":
                return "Fila {}"
            elif first_line == "chinese":
                return "第{}行"
            elif first_line == "korean":
                return "{}행"
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

def str_21(file_path):
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
    
def str_22(file_path):
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
    
def str_23(file_path):
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
    
def str_24(file_path):
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
    
def str_25(file_path):
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
    
def str_26(file_path):
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
    
def str_27(file_path):
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
    
def str_28(file_path):
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

def str_29(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return   "Delete By IDs From Excel"
            elif first_line == "deutsch":
                return "Löschen nach IDs aus Excel"
            elif first_line == "farsi":
                return "حذف بر اساس شناسه‌ها از اکسل"
            elif first_line == "russian":
                return "Удалить по идентификаторам из Excel"
            elif first_line == "spanish":
                return "Eliminar por IDs desde Excel"
            elif first_line == "chinese":
                return "从Excel按标识符删除"
            elif first_line == "korean":
                return "엑셀에서 ID로 삭제"
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
                return "به دلیل وابستگی برخی ازالمان ها، امکان حذف المان ها وجود ندارد"
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
    
def str_30(file_path):
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
    
def str_31(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Due to dependency of some elements could not delete elements."
            elif first_line == "deutsch":
                return "Aufgrund von Abhängigkeiten einiger Elemente konnten die Elemente nicht gelöscht werden."
            elif first_line == "farsi":
                return "به دلیل وابستگی برخی از المان ها، امکان حذف المان ها وجود ندارد."
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
    
def str_32(file_path):
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
    
def str_33(file_path):
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
    
def str_34(file_path):
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
    
def str_35(file_path):
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
    
def str_36(file_path):
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
    
def str_37(file_path):
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
    
def str_38(file_path):
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
    
def str_39(file_path):
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