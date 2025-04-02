# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_parameter_value_editor_for_special_character.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No elements selected. Please select at least one element."
            elif first_line == "deutsch":
                return "Keine Elemente ausgewählt. Bitte wählen Sie mindestens ein Element aus."
            elif first_line == "farsi":
                return "هیچ المانی انتخاب نشده است. لطفا حداقل یک المان را انتخاب کنید"
            elif first_line == "russian":
                return "Не выбрано ни одного элемента. Пожалуйста, выберите хотя бы один элемент."
            elif first_line == "spanish":
                return "No se han seleccionado elementos. Por favor, seleccione al menos un elemento."
            elif first_line == "chinese":
                return "未选择任何元素。请至少选择一个元素。"
            elif first_line == "korean":
                return "요소를 선택하지 않았습니다. 적어도 하나의 요소를 선택해주세요."
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
                return "Option 1: Comma"
            elif first_line == "deutsch":
                return "Option 1: Komma"
            elif first_line == "farsi":
                return "گزینه 1: ویرگول"
            elif first_line == "russian":
                return "Вариант 1: Запятая"
            elif first_line == "spanish":
                return "Opción 1: Coma"
            elif first_line == "chinese":
                return "选项1：逗号"
            elif first_line == "korean":
                return "옵션 1: 쉼표"
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
                return  "Replace ',' with desired character"
            elif first_line == "deutsch":
                return "Ersetze ',' durch gewünschtes Zeichen"
            elif first_line == "farsi":
                return "جایگزینی ',' با کاراکتر مورد نظر"
            elif first_line == "russian":
                return "Замените ',' на желаемый символ"
            elif first_line == "spanish":
                return "Reemplazar ',' por el carácter deseado"
            elif first_line == "chinese":
                return "用所需字符替换','"
            elif first_line == "korean":
                return "','를 원하는 문자로 바꾸기"
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
                return "Option 2: Umlaut characters"
            elif first_line == "deutsch":
                return "Option 2: Umlaut-Zeichen"
            elif first_line == "farsi":
                return "گزینه 2: حروف اوملاوت"
            elif first_line == "russian":
                return "Вариант 2: Буквы с умляутом"
            elif first_line == "spanish":
                return "Opción 2: Caracteres diacríticos (Umlaut)"
            elif first_line == "chinese":
                return "选项 2：变音符号字符"
            elif first_line == "korean":
                return "옵션 2: 움라우트 문자"
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
                return  "Replaces 'Ä' with 'Ae', 'ä' with 'ae', 'Ü' with 'Ue', 'ü' with 'ue', 'Ö' with 'Oe', 'ö' with 'oe' and 'ß' with 'ss'"
            elif first_line == "deutsch":
                return "Ersetzt 'Ä' durch 'Ae', 'ä' durch 'ae', 'Ü' durch 'Ue', 'ü' durch 'ue', 'Ö' durch 'Oe', 'ö' durch 'oe' und 'ß' durch 'ss'"
            elif first_line == "farsi":
                return "'Ae' با 'Ä'، 'ae' با 'ä'، 'Ue' با 'Ü'، 'ue' با 'ü'، 'Oe' با 'Ö'، 'oe' با 'ö' و 'ss' با 'ß'"
            elif first_line == "russian":
                return "Заменяет 'Ä' на 'Ae', 'ä' на 'ae', 'Ü' на 'Ue', 'ü' на 'ue', 'Ö' на 'Oe', 'ö' на 'oe' и 'ß' на 'ss'"
            elif first_line == "spanish":
                return "Reemplaza 'Ä' por 'Ae', 'ä' por 'ae', 'Ü' por 'Ue', 'ü' por 'ue', 'Ö' por 'Oe', 'ö' por 'oe' y 'ß' por 'ss'"
            elif first_line == "chinese":
                return "将 'Ä' 替换为 'Ae'，'ä' 替换为 'ae'，'Ü' 替换为 'Ue'，'ü' 替换为 'ue'，'Ö' 替换为 'Oe'，'ö' 替换为 'oe'，'ß' 替换为 'ss'"
            elif first_line == "korean":
                return "'Ä'를 'Ae'로, 'ä'를 'ae'로, 'Ü'를 'Ue'로, 'ü'를 'ue'로, 'Ö'를 'Oe'로, 'ö'를 'oe'로, 'ß'를 'ss'로 바꿉니다."
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
    
def str_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Replace comma with:"
            elif first_line == "deutsch":
                return "Ersetze Komma durch:"
            elif first_line == "farsi":
                return "جایگزینی ویرگول با:"
            elif first_line == "russian":
                return "Заменить запятую на:"
            elif first_line == "spanish":
                return "Reemplazar coma por:"
            elif first_line == "chinese":
                return "用以下字符替换逗号："
            elif first_line == "korean":
                return "쉼표를 다음 문자로 바꾸기:"
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
                return   "Comma"
            elif first_line == "deutsch":
                return "Komma"
            elif first_line == "farsi":
                return "ویرگول"
            elif first_line == "russian":
                return "Запятая"
            elif first_line == "spanish":
                return "Coma"
            elif first_line == "chinese":
                return "逗号"
            elif first_line == "korean":
                return "쉼표"
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
                return "The parameter '{0}' does not exist or is not of type 'Text' for the following elements:\n{1}"
            elif first_line == "deutsch":
                return "Der Parameter '{0}' existiert nicht oder ist nicht vom Typ 'Text' für die folgenden Elemente:\n{1}"
            elif first_line == "farsi":
                return "پارامتر '{0}' وجود ندارد یا از نوع 'متن' نیست برای المان های زیر:\n{1}"
            elif first_line == "russian":
                return "Параметр '{0}' не существует или не является типом 'Текст' для следующих элементов:\n{1}"
            elif first_line == "spanish":
                return "El parámetro '{0}' no existe o no es del tipo 'Texto' para los siguientes elementos:\n{1}"
            elif first_line == "chinese":
                return "参数 '{0}' 不存在或不是以下元素的 '文本' 类型：\n{1}"
            elif first_line == "korean":
                return "다음 요소에 대해 매개변수 '{0}'가 존재하지 않거나 '텍스트' 유형이 아닙니다:\n{1}"
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
                return "result"
            elif first_line == "deutsch":
                return "Ergebnis"
            elif first_line == "farsi":
                return "نتیجه"
            elif first_line == "russian":
                return "результат"
            elif first_line == "spanish":
                return "resultado"
            elif first_line == "chinese":
                return "结果"
            elif first_line == "korean":
                return "결과"
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
                return "La operación fue exitosa."
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
                return "Failed to set parameter value. {}"
            elif first_line == "deutsch":
                return "Fehler beim Setzen des Parameterwerts. {}"
            elif first_line == "farsi":
                return "تنظیم مقدار پارامتر با خطا مواجه شد. {}"
            elif first_line == "russian":
                return "Не удалось установить значение параметра. {}"
            elif first_line == "spanish":
                return "No se pudo establecer el valor del parámetro. {}"
            elif first_line == "chinese":
                return "无法设置参数值。{}"
            elif first_line == "korean":
                return "매개변수 값을 설정하지 못했습니다. {}"
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
                return "Replace Umlaut characters"
            elif first_line == "deutsch":
                return "Umlaut-Zeichen ersetzen"
            elif first_line == "farsi":
                return "جایگزینی حروف اوملاوت"
            elif first_line == "russian":
                return "Заменить символы с умляутом"
            elif first_line == "spanish":
                return "Reemplazar caracteres diacríticos (Umlaut)"
            elif first_line == "chinese":
                return "替换变音符号字符"
            elif first_line == "korean":
                return "움라우트 문자 대체"
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
                return "Parameter value editor for special characters"
            elif first_line == "deutsch":
                return "Parameter-Wert-Editor für Sonderzeichen"
            elif first_line == "farsi":
                return "ویرایشگر مقدار پارامتر برای کاراکترهای خاص"
            elif first_line == "russian":
                return "Редактор значения параметра для специальных символов"
            elif first_line == "spanish":
                return "Editor de valor de parámetro para caracteres especiales"
            elif first_line == "chinese":
                return "特殊字符的参数值编辑器"
            elif first_line == "korean":
                return "특수 문자의 매개변수 값 편집기"
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
                return "Replaced commas report"
            elif first_line == "deutsch":
                return "Bericht zu ersetzten Kommas"
            elif first_line == "farsi":
                return "گزارش جایگزینی کاما ها"
            elif first_line == "russian":
                return "Отчет о замененных запятых"
            elif first_line == "spanish":
                return "Informe de comas reemplazados"
            elif first_line == "chinese":
                return "替换逗号报告"
            elif first_line == "korean":
                return "대체된 쉼표 보고서"
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
    
def str_17(file_path):
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
    
def str_18(file_path):
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
    
def str_19(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Replaced Umlauts report"
            elif first_line == "deutsch":
                return "Bericht zu ersetzten Umlauten"
            elif first_line == "farsi":
                return "گزارش جایگزینی اوملات ها"
            elif first_line == "russian":
                return "Отчет о замененных умляутах"
            elif first_line == "spanish":
                return "Informe de diéresis reemplazados"
            elif first_line == "chinese":
                return "替换分音符报告"
            elif first_line == "korean":
                return "대체된 움라우트 보고서"
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
    
def str_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Comma replaced with : "
            elif first_line == "deutsch":
                return "Komma ersetzt durch : "
            elif first_line == "farsi":
                return "کاما جایگزین شده با : "
            elif first_line == "russian":
                return "Запятая заменена на : "
            elif first_line == "spanish":
                return "Coma reemplazada con : "
            elif first_line == "chinese":
                return "逗号替换为 : "
            elif first_line == "korean":
                return "쉼표가 다음으로 대체됨 : "
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
                return "All the umlauts in value replaced with standard form."
            elif first_line == "deutsch":
                return "Alle Umlaute im Wert durch Standardform ersetzt."
            elif first_line == "farsi":
                return "همه اوملات ها در مقدار با شکل استاندارد جایگزین شده است"
            elif first_line == "russian":
                return "Все умляуты в значении заменены стандартной формой."
            elif first_line == "spanish":
                return "Todos los diéresis en el valor reemplazados con la forma estándar."
            elif first_line == "chinese":
                return "值中所有的分音符都已替换为标准形式。"
            elif first_line == "korean":
                return "값 내의 모든 분음 부호가 표준 형식으로 대체되었습니다."
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
    
def str_24(file_path):
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
    
def str_25(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter Name"
            elif first_line == "deutsch":
                return "Parameternamen"
            elif first_line == "farsi":
                return "نام پارامتر"
            elif first_line == "russian":
                return "Имя параметра"
            elif first_line == "spanish":
                return "Nombre del parámetro"
            elif first_line == "chinese":
                return "参数名称"
            elif first_line == "korean":
                return "매개변수 이름"
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
    


