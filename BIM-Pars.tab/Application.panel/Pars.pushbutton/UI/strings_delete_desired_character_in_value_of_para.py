# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_delete_desired_character_in_value_of_para.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No elements selected. Please select at least one element."
            elif first_line == "deutsch":
                return "Keine Elemente ausgewählt. Bitte wählen Sie mindestens ein Element aus."
            elif first_line == "farsi":
                return "هیچ المانی انتخاب نشده است. لطفاً حداقل یک المان انتخاب کنید"
            elif first_line == "russian":
                return "Не выбрано ни одного элемента. Пожалуйста, выберите хотя бы один элемент."
            elif first_line == "spanish":
                return "No se han seleccionado elementos. Por favor, seleccione al menos un elemento."
            elif first_line == "chinese":
                return "没有选择任何元素。请至少选择一个元素。"
            elif first_line == "korean":
                return "선택된 요소가 없습니다. 최소한 하나의 요소를 선택해주세요."
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
                return "Parameter:"
            elif first_line == "deutsch":
                return "Parameter:"
            elif first_line == "farsi":
                return "پارامتر:"
            elif first_line == "russian":
                return "Параметр:"
            elif first_line == "spanish":
                return "Parámetro:"
            elif first_line == "chinese":
                return "参数："
            elif first_line == "korean":
                return "매개변수:"
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
                return "Character:"
            elif first_line == "deutsch":
                return "Zeichen:"
            elif first_line == "farsi":
                return "کاراکتر:"
            elif first_line == "russian":
                return "Символ:"
            elif first_line == "spanish":
                return "Carácter:"
            elif first_line == "chinese":
                return "字符："
            elif first_line == "korean":
                return "문자:"
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
                return "Parameter Value Changes"
            elif first_line == "deutsch":
                return "Änderungen des Parameterwerts"
            elif first_line == "farsi":
                return "تغییرات مقدار پارامتر"
            elif first_line == "russian":
                return "Изменения значения параметра"
            elif first_line == "spanish":
                return "Cambios en el valor del parámetro"
            elif first_line == "chinese":
                return "参数值变更"
            elif first_line == "korean":
                return "매개변수 값 변경"
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
                return "Element ID"
            elif first_line == "deutsch":
                return "Element-ID"
            elif first_line == "farsi":
                return "شناسه المان"
            elif first_line == "russian":
                return "Идентификатор элемента"
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
        return "An error occurred: {e}"
    
def str_6(file_path):
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
                return "上一个值"
            elif first_line == "korean":
                return "이전 값"
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
                return "Current Value"
            elif first_line == "deutsch":
                return "Aktueller Wert"
            elif first_line == "farsi":
                return "مقدار فعلی"
            elif first_line == "russian":
                return "Текущее значение"
            elif first_line == "spanish":
                return "Valor actual"
            elif first_line == "chinese":
                return "当前值"
            elif first_line == "korean":
                return "현재 값"
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
                return "Note that this tool is only for parameters of type 'Text'. You can remove any character inside value of text parameters."
            elif first_line == "deutsch":
                return "Beachten Sie, dass dieses Tool nur für Parameter vom Typ 'Text' geeignet ist. Sie können beliebige Zeichen im Wert von Textparametern entfernen."
            elif first_line == "farsi":
                return "توجه کنید که این ابزار فقط برای پارامترهای نوع 'متن' می‌باشد. شما میتوانید هر کاراکتری را درون مقدار پارامترهای متنی حذف کنید"
            elif first_line == "russian":
                return "Обратите внимание, что этот инструмент предназначен только для параметров типа 'Текст'. Вы можете удалить любой символ внутри значений текстовых параметров."
            elif first_line == "spanish":
                return "Tenga en cuenta que esta herramienta solo es para parámetros de tipo 'Texto'. Puede eliminar cualquier carácter dentro del valor de los parámetros de texto."
            elif first_line == "chinese":
                return "请注意，此工具仅适用于“文本”类型的参数。您可以删除文本参数值中的任何字符。"
            elif first_line == "korean":
                return "이 도구는 '텍스트' 유형의 매개변수에만 적용됨을 유의하세요. 텍스트 매개변수 값 내에서 어떤 문자든 제거할 수 있습니다."
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
    
def str_10(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "The parameter '{0}' does not exist or is not of type 'Text' for the following elements:\n{1}"
            elif first_line == "deutsch":
                return "Der Parameter '{0}' existiert nicht oder ist nicht vom Typ 'Text' für die folgenden Elemente:\n{1}"
            elif first_line == "farsi":
                return "پارامتر \n'{0}'\nوجود ندارد یا نوع 'متن' نیست برای المان های زیر\n{1}"
            elif first_line == "russian":
                return "Параметр '{0}' не существует или не является типом 'Текст' для следующих элементов:\n{1}"
            elif first_line == "spanish":
                return "El parámetro '{0}' no existe o no es de tipo 'Texto' para los siguientes elementos:\n{1}"
            elif first_line == "chinese":
                return "参数 '{0}' 不存在或不是以下元素的 '文本' 类型：\n{1}"
            elif first_line == "korean":
                return "다음 요소에 대해 '{0}' 매개변수가 존재하지 않거나 '텍스트' 유형이 아닙니다:\n{1}"
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
                return "Operation was successful."
            elif first_line == "deutsch":
                return "Die Operation war erfolgreich."
            elif first_line == "farsi":
                return "عملیات با موفقیت انجام شد"
            elif first_line == "russian":
                return "Операция выполнена успешно."
            elif first_line == "spanish":
                return "La operación se realizó con éxito."
            elif first_line == "chinese":
                return "操作成功完成。"
            elif first_line == "korean":
                return "작업이 성공적으로 완료되었습니다."
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
                return "Operation failed. {}"
            elif first_line == "deutsch":
                return "Die Operation ist fehlgeschlagen. {}"
            elif first_line == "farsi":
                return "عملیات ناموفق بود. {}"
            elif first_line == "russian":
                return "Операция не удалась. {}"
            elif first_line == "spanish":
                return "La operación ha fallado. {}"
            elif first_line == "chinese":
                return "操作失败。{}"
            elif first_line == "korean":
                return "작업 실패. {}"
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
                return "Delete of character from parameter value"
            elif first_line == "deutsch":
                return "Löschen von Zeichen aus Parameterwert"
            elif first_line == "farsi":
                return "حذف کاراکتر از مقدار پارامتر"
            elif first_line == "russian":
                return "Удаление символа из значения параметра"
            elif first_line == "spanish":
                return "Eliminar carácter del valor del parámetro"
            elif first_line == "chinese":
                return "从参数值中删除字符"
            elif first_line == "korean":
                return "매개변수 값에서 문자 삭제"
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
                return "Parameter name : "
            elif first_line == "deutsch":
                return "Parametername : "
            elif first_line == "farsi":
                return "نام پارامتر : "
            elif first_line == "russian":
                return "Имя параметра : "
            elif first_line == "spanish":
                return "Nombre del parámetro : "
            elif first_line == "chinese":
                return "参数名称 : "
            elif first_line == "korean":
                return "매개변수 이름 : "
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
                return "Erased characters : "
            elif first_line == "deutsch":
                return "Gelöschte Zeichen : "
            elif first_line == "farsi":
                return "کارکتر های پاک شده : "
            elif first_line == "russian":
                return "Стёртые символы : "
            elif first_line == "spanish":
                return "Caracteres borrados : "
            elif first_line == "chinese":
                return "已擦除字符 : "
            elif first_line == "korean":
                return "삭제된 문자 : "
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
    
def str_17(file_path):
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
    
def str_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Target Parameter"
            elif first_line == "deutsch":
                return "Zielparameter"
            elif first_line == "farsi":
                return "پارامتر هدف"
            elif first_line == "russian":
                return "Целевой параметр"
            elif first_line == "spanish":
                return "Parámetro objetivo"
            elif first_line == "chinese":
                return "目标参数"
            elif first_line == "korean":
                return "대상 매개변수"
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
                return "Erased Character"
            elif first_line == "deutsch":
                return "Gelöschtes Zeichen"
            elif first_line == "farsi":
                return "کارکتر حذف شده"
            elif first_line == "russian":
                return "Стертый символ"
            elif first_line == "spanish":
                return "Carácter borrado"
            elif first_line == "chinese":
                return "已删除字符"
            elif first_line == "korean":
                return "지워진 문자"
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
                return "The trash character '{}' is not found in the parameter value for element '{}'."
            elif first_line == "deutsch":
                return "Das gelöschte Zeichen '{}' wurde im Parameterwert für das Element '{}' nicht gefunden."
            elif first_line == "farsi":
                return "کاراکتر حذف شده \n'{}'\n در مقدار پارامتر المان \n'{}'\n .پیدا نشد"
            elif first_line == "russian":
                return "Стертый символ '{}' не найден в значении параметра элемента '{}'."
            elif first_line == "spanish":
                return "El carácter borrado '{}' no se encuentra en el valor del parámetro del elemento '{}'."
            elif first_line == "chinese":
                return "在元素'{}'的参数值中找不到废弃字符'{}'。"
            elif first_line == "korean":
                return "요소 '{}'의 매개변수 값에서 삭제된 문자 '{}'를 찾을 수 없습니다."
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