# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_list_maker_of_values_from_excel.py

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
                return "Select an item"
            elif first_line == "deutsch":
                return "Wähle einen Eintrag aus"
            elif first_line == "farsi":
                return "یک مورد را انتخاب کنید"
            elif first_line == "russian":
                return "Выберите элемент"
            elif first_line == "spanish":
                return "Seleccionar un elemento"
            elif first_line == "chinese":
                return "选择一个项目"
            elif first_line == "korean":
                return "항목 선택"
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
    
def str_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "The parameter '{0}' does not exist for the following elements:\n{1}"
            elif first_line == "deutsch":
                return "Der Parameter '{0}' existiert nicht für die folgenden Elemente:\n{1}"
            elif first_line == "farsi":
                return "پارامتر '{0}' برای عناصر زیر وجود ندارد:\n{1}"
            elif first_line == "russian":
                return "Параметр '{0}' не существует для следующих элементов:\n{1}"
            elif first_line == "spanish":
                return "El parámetro '{0}' no existe para los siguientes elementos:\n{1}"
            elif first_line == "chinese":
                return "以下元素不存在参数 '{0}':\n{1}"
            elif first_line == "korean":
                return "다음 요소에 '{0}' 매개변수가 존재하지 않습니다:\n{1}"
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
                return "Transaction"
            elif first_line == "deutsch":
                return "Transaktion"
            elif first_line == "farsi":
                return "تراکنش"
            elif first_line == "russian":
                return "Транзакция"
            elif first_line == "spanish":
                return "Transacción"
            elif first_line == "chinese":
                return "交易"
            elif first_line == "korean":
                return "거래"
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
                return "Make sure that the selected value is of type '{0}':"
            elif first_line == "deutsch":
                return "Stellen Sie sicher, dass der ausgewählte Wert vom Typ '{0}' ist:"
            elif first_line == "farsi":
                return "مطمئن شوید که مقدار انتخاب شده از نوع '{0}' است:"
            elif first_line == "russian":
                return "Убедитесь, что выбранное значение имеет тип '{0}':"
            elif first_line == "spanish":
                return "Asegúrese de que el valor seleccionado es de tipo '{0}':"
            elif first_line == "chinese":
                return "请确保所选值的类型为 '{0}':"
            elif first_line == "korean":
                return "선택한 값의 유형이 '{0}'인지 확인하세요:"
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
                return "Continue"
            elif first_line == "deutsch":
                return "Fortfahren"
            elif first_line == "farsi":
                return "ادامه"
            elif first_line == "russian":
                return "Продолжить"
            elif first_line == "spanish":
                return "Continuar"
            elif first_line == "chinese":
                return "继续"
            elif first_line == "korean":
                return "계속"
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
                return "List maker of values from Excel"
            elif first_line == "deutsch":
                return "Listengenerator für Werte aus Excel"
            elif first_line == "farsi":
                return "لیست ساز مقادیر از اکسل"
            elif first_line == "russian":
                return "Создатель списка значений из Excel"
            elif first_line == "spanish":
                return "Creador de listas de valores desde Excel"
            elif first_line == "chinese":
                return "从 Excel 提取值的列表生成器"
            elif first_line == "korean":
                return "엑셀에서 값 가져와 리스트 만들기"
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
                return "Invalid value for Integer type. Please enter a valid Integer."
            elif first_line == "deutsch":
                return "Ungültiger Wert für den Ganzzahltyp. Bitte geben Sie eine gültige Ganzzahl ein."
            elif first_line == "farsi":
                return "مقدار نامعتبر برای نوع عدد صحیح. لطفاً یک عدد صحیح معتبر وارد کنید"
            elif first_line == "russian":
                return "Недопустимое значение для типа Integer. Пожалуйста, введите действительное целое число."
            elif first_line == "spanish":
                return "Valor no válido para el tipo Entero. Por favor, ingrese un Entero válido."
            elif first_line == "chinese":
                return "整数类型无效。请输入有效的整数。"
            elif first_line == "korean":
                return "정수 형식의 값이 잘못되었습니다. 유효한 정수를 입력하세요."
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
                return "Invalid value for Number type. Please enter a valid Number."
            elif first_line == "deutsch":
                return "Ungültiger Wert für den Zahlentyp. Bitte geben Sie eine gültige Zahl ein."
            elif first_line == "farsi":
                return "مقدار نامعتبر برای نوع عدد. لطفاً یک عدد معتبر وارد کنید"
            elif first_line == "russian":
                return "Недопустимое значение для типа Number. Пожалуйста, введите действительное число."
            elif first_line == "spanish":
                return "Valor no válido para el tipo Número. Por favor, ingrese un Número válido."
            elif first_line == "chinese":
                return "数字类型无效。请输入有效的数字。"
            elif first_line == "korean":
                return "숫자 형식의 값이 잘못되었습니다. 유효한 숫자를 입력하세요."
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
                return "Parameter is invalid. Storage type is element Id."
            elif first_line == "deutsch":
                return "Der Parameter ist ungültig. Der Speichertyp ist die Element-ID."
            elif first_line == "farsi":
                return "پارامتر نامعتبر است. نوع ذخیره سازی شناسه المان است"
            elif first_line == "russian":
                return "Параметр недействителен. Тип хранилища - идентификатор элемента."
            elif first_line == "spanish":
                return "El parámetro no es válido. El tipo de almacenamiento es el Id de elemento."
            elif first_line == "chinese":
                return "参数无效。存储类型是元素 Id。"
            elif first_line == "korean":
                return "매개변수가 잘못되었습니다. 저장 유형은 요소 ID입니다."
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
                return "Invalid value for Boolean type. Please select a valid Boolean."
            elif first_line == "deutsch":
                return "Ungültiger Wert für den Booleschen Typ. Bitte wählen Sie einen gültigen Booleschen Wert aus."
            elif first_line == "farsi":
                return "مقدار نامعتبر برای پارامترنوع بولین. لطفاً یک مقدار معتبر ازنوع بولینرا انتخاب کنید"
            elif first_line == "russian":
                return "Недопустимое значение для типа Boolean. Выберите допустимое значение Boolean."
            elif first_line == "spanish":
                return "Valor no válido para el tipo Booleano. Seleccione un Booleano válido."
            elif first_line == "chinese":
                return "布尔类型的值无效。请选择一个有效的布尔值。"
            elif first_line == "korean":
                return "부울 유형의 값이 잘못되었습니다. 유효한 부울 값을 선택하세요."
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
                return "Invalid parameter. Storage type is unknown."
            elif first_line == "deutsch":
                return "Ungültiger Parameter. Der Speichertyp ist unbekannt."
            elif first_line == "farsi":
                return "پارامتر نامعتبر است. نوع ذخیره سازی ناشناخته است"
            elif first_line == "russian":
                return "Недействительный параметр. Тип хранилища неизвестен."
            elif first_line == "spanish":
                return "Parámetro no válido. El tipo de almacenamiento es desconocido."
            elif first_line == "chinese":
                return "参数无效。存储类型未知。"
            elif first_line == "korean":
                return "잘못된 매개변수입니다. 저장 유형이 알 수 없습니다."
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
                return 'Error during transaction: {0}'
            elif first_line == "deutsch":
                return 'Fehler während der Transaktion: {0}'
            elif first_line == "farsi":
                return 'خطا در هنگام تراکنش: {0}'
            elif first_line == "russian":
                return 'Ошибка во время транзакции: {0}'
            elif first_line == "spanish":
                return 'Error durante la transacción: {0}'
            elif first_line == "chinese":
                return '交易过程中出错: {0}'
            elif first_line == "korean":
                return '거래 중 오류 발생: {0}'
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
                return "Use 0 and 1 for boolean parameters."
            elif first_line == "deutsch":
                return "Verwenden Sie 0 und 1 für boolesche Parameter."
            elif first_line == "farsi":
                return "از 0 و 1 برای پارامترهای بولین استفاده کنید"
            elif first_line == "russian":
                return "Используйте 0 и 1 для булевых параметров."
            elif first_line == "spanish":
                return "Use 0 y 1 para los parámetros booleanos."
            elif first_line == "chinese":
                return "使用 0 和 1 作为布尔参数。"
            elif first_line == "korean":
                return "부울 매개변수에 0과 1을 사용하세요."
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
                return "Row: "
            elif first_line == "deutsch":
                return "Zeile: "
            elif first_line == "farsi":
                return "ردیف: "
            elif first_line == "russian":
                return "Строка: "
            elif first_line == "spanish":
                return "Fila: "
            elif first_line == "chinese":
                return "行: "
            elif first_line == "korean":
                return "행: "
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
                return "Column: "
            elif first_line == "deutsch":
                return "Spalte: "
            elif first_line == "farsi":
                return "ستون: "
            elif first_line == "russian":
                return "Столбец: "
            elif first_line == "spanish":
                return "Columna: "
            elif first_line == "chinese":
                return "列: "
            elif first_line == "korean":
                return "열: "
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
                return "Invalid row or column"
            elif first_line == "deutsch":
                return "Ungültige Zeile oder Spalte"
            elif first_line == "farsi":
                return "ردیف یا ستون نامعتبر"
            elif first_line == "russian":
                return "Недействительная строка или столбец"
            elif first_line == "spanish":
                return "Fila o columna no válida"
            elif first_line == "chinese":
                return "行或列无效"
            elif first_line == "korean":
                return "잘못된 행 또는 열"
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
                return "Invalid parameter"
            elif first_line == "deutsch":
                return "Ungültiger Parameter"
            elif first_line == "farsi":
                return "پارامتر نامعتبر"
            elif first_line == "russian":
                return "Недействительный параметр"
            elif first_line == "spanish":
                return "Parámetro no válido"
            elif first_line == "chinese":
                return "参数无效"
            elif first_line == "korean":
                return "잘못된 매개변수"
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
    
def str_31(file_path):
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
    
def str_32(file_path):
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
    