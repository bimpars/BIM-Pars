# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_set_same_value_for_all_selected_elements.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please select at least one element."
            elif first_line == "deutsch":
                return "Bitte wählen Sie mindestens ein Element aus."
            elif first_line == "farsi":
                return "لطفا حداقل یک المان را انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, выберите хотя бы один элемент."
            elif first_line == "spanish":
                return "Por favor, seleccione al menos un elemento."
            elif first_line == "chinese":
                return "请选择至少一个元素。"
            elif first_line == "korean":
                return "적어도 하나의 요소를 선택하세요."
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
                return "매개변수: "
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
                return "Value:"
            elif first_line == "deutsch":
                return "Wert:"
            elif first_line == "farsi":
                return "مقدار:"
            elif first_line == "russian":
                return "Значение:"
            elif first_line == "spanish":
                return "Valor:"
            elif first_line == "chinese":
                return "值："
            elif first_line == "korean":
                return "값: "
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
                return "True"
            elif first_line == "deutsch":
                return "Wahr"
            elif first_line == "farsi":
                return "درست"
            elif first_line == "russian":
                return "Истина"
            elif first_line == "spanish":
                return "Verdadero"
            elif first_line == "chinese":
                return "真"
            elif first_line == "korean":
                return "참"
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
                return "False"
            elif first_line == "deutsch":
                return "Falsch"
            elif first_line == "farsi":
                return "غلط"
            elif first_line == "russian":
                return "Ложь"
            elif first_line == "spanish":
                return "Falso"
            elif first_line == "chinese":
                return "假"
            elif first_line == "korean":
                return "거짓"
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
                return "Check parameter:"
            elif first_line == "deutsch":
                return "Parameter überprüfen:"
            elif first_line == "farsi":
                return "بررسی پارامتر:"
            elif first_line == "russian":
                return "Проверка параметра:"
            elif first_line == "spanish":
                return "Verificar parámetro:"
            elif first_line == "chinese":
                return "检查参数："
            elif first_line == "korean":
                return "매개변수 확인:"
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
                return "Note that you have to insert the value based on the correct type of the parameter."
            elif first_line == "deutsch":
                return "Beachten Sie, dass Sie den Wert entsprechend dem richtigen Typ des Parameters einfügen müssen."
            elif first_line == "farsi":
                return "لطفا توجه داشته باشید که باید مقدار را بر اساس نوع صحیح پارامتر وارد کنید"
            elif first_line == "russian":
                return "Обратите внимание, что необходимо вводить значение на основе правильного типа параметра."
            elif first_line == "spanish":
                return "Ten en cuenta que debes insertar el valor basado en el tipo correcto del parámetro."
            elif first_line == "chinese":
                return "请注意，您必须根据参数的正确类型插入值。"
            elif first_line == "korean":
                return "매개변수의 올바른 유형에 따라 값을 삽입해야 함을 주의하십시오."
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
                return "The parameter '{0}' does not exist for elements with the following names:\n\n{1}\n\n\n\n{2}"
            elif first_line == "deutsch":
                return "Der Parameter '{0}' existiert nicht für Elemente mit den folgenden Namen:\n\n{1}\n\n\n\n{2}"
            elif first_line == "farsi":
                return "پارامتر '{0}' برای المان های با نام های زیر وجود ندارد:\n\n{1}\n\n\n\n{2}"
            elif first_line == "russian":
                return "Параметр '{0}' не существует для элементов с указанными именами:\n\n{1}\n\n\n\n{2}"
            elif first_line == "spanish":
                return "El parámetro '{0}' no existe para los elementos con los siguientes nombres:\n\n{1}\n\n\n\n{2}"
            elif first_line == "chinese":
                return "元素名称为以下的元素中，参数'{0}'不存在：\n\n{1}\n\n\n\n{2}"
            elif first_line == "korean":
                return "다음 이름을 가진 요소에 대해 '{0}' 매개변수가 존재하지 않습니다:\n\n{1}\n\n\n\n{2}"
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
                return "If you continue, the value will be set for the rest of the elements."
            elif first_line == "deutsch":
                return "Wenn Sie fortfahren, wird der Wert für die restlichen Elemente gesetzt."
            elif first_line == "farsi":
                return "در صورت ادامه، مقدار برای بقیه المان ها تنظیم خواهد شد"
            elif first_line == "russian":
                return "Если вы продолжите, значение будет установлено для остальных элементов."
            elif first_line == "spanish":
                return "Si continúas, se establecerá el valor para el resto de los elementos."
            elif first_line == "chinese":
                return "如果您继续，该值将被设置为其余的元素。"
            elif first_line == "korean":
                return "계속하면 나머지 요소에 대해 값이 설정됩니다."
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
                return "Please enter a value of type: '{0}'"
            elif first_line == "deutsch":
                return "Bitte geben Sie einen Wert vom Typ '{0}' ein"
            elif first_line == "farsi":
                return "لطفاً یک مقدار از نوع '{0}' وارد کنید"
            elif first_line == "russian":
                return "Пожалуйста, введите значение типа: '{0}'"
            elif first_line == "spanish":
                return "Por favor, ingrese un valor del tipo: '{0}'"
            elif first_line == "chinese":
                return "请输入类型为'{0}'的值"
            elif first_line == "korean":
                return "'{0}' 유형의 값을 입력하세요."
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
                return "Invalid Value"
            elif first_line == "deutsch":
                return "Ungültiger Wert"
            elif first_line == "farsi":
                return "مقدار نامعتبر"
            elif first_line == "russian":
                return "Недопустимое значение"
            elif first_line == "spanish":
                return "Valor inválido"
            elif first_line == "chinese":
                return "无效值"
            elif first_line == "korean":
                return "유효하지 않은 값"
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
                return "Same value for all selected elements"
            elif first_line == "deutsch":
                return "Derselbe Wert für alle ausgewählten Elemente"
            elif first_line == "farsi":
                return "مقدار یکسان برای همه المان های انتخاب شده"
            elif first_line == "russian":
                return "Одинаковое значение для всех выбранных элементов"
            elif first_line == "spanish":
                return "Mismo valor para todos los elementos seleccionados"
            elif first_line == "chinese":
                return "所有选定元素的相同值"
            elif first_line == "korean":
                return "선택된 모든 요소에 동일한 값"
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
                return "Target parameter: "
            elif first_line == "deutsch":
                return "Zielparameter: "
            elif first_line == "farsi":
                return "پارامتر هدف: "
            elif first_line == "russian":
                return "Целевой параметр: "
            elif first_line == "spanish":
                return "Parámetro objetivo: "
            elif first_line == "chinese":
                return "目标参数: "
            elif first_line == "korean":
                return "대상 매개변수: "
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
                return "Parameter type: "
            elif first_line == "deutsch":
                return "Parametertyp: "
            elif first_line == "farsi":
                return "نوع پارامتر: "
            elif first_line == "russian":
                return "Тип параметра: "
            elif first_line == "spanish":
                return "Tipo de parámetro: "
            elif first_line == "chinese":
                return "参数类型: "
            elif first_line == "korean":
                return "매개변수 유형: "
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
                return "Text"
            elif first_line == "deutsch":
                return "Text"
            elif first_line == "farsi":
                return "متن"
            elif first_line == "russian":
                return "Текст"
            elif first_line == "spanish":
                return "Texto"
            elif first_line == "chinese":
                return "文本"
            elif first_line == "korean":
                return "텍스트"
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
                return "Boolean"
            elif first_line == "deutsch":
                return "Boolesch"
            elif first_line == "farsi":
                return "بولین"
            elif first_line == "russian":
                return "Булев"
            elif first_line == "spanish":
                return "Booleano"
            elif first_line == "chinese":
                return "布尔型"
            elif first_line == "korean":
                return "부울"
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
    
def str_22(file_path):
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
    
def str_23(file_path):
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
    
def str_24(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter Type"
            elif first_line == "deutsch":
                return "Parametertyp"
            elif first_line == "farsi":
                return "نوع پارامتر"
            elif first_line == "russian":
                return "Тип параметра"
            elif first_line == "spanish":
                return "Tipo de parámetro"
            elif first_line == "chinese":
                return "参数类型"
            elif first_line == "korean":
                return "매개변수 유형"
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
    