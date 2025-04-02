# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_parameter_value_editor.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Option 1: Replace Letters except ',' for 'Text' parameters"
            elif first_line == "deutsch":
                return "Option 1: Ersetze Buchstaben außer ',' für 'Text'-Parameter"
            elif first_line == "farsi":
                return "گزینه ۱: جایگزینی حروف به جز ',' برای پارامترهای 'متن'"
            elif first_line == "russian":
                return "Вариант 1: Заменить буквы, кроме ',', для параметров 'Текст'"
            elif first_line == "spanish":
                return "Opción 1: Reemplazar letras excepto ',' para los parámetros 'Texto'"
            elif first_line == "chinese":
                return "选项1：替换除了','之外的字母作为'Text'参数"
            elif first_line == "korean":
                return "옵션1: 'Text' 매개변수의 ',' 이외의 문자를 대체합니다."
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
                return "Option 2: Add Prefix to 'Text' parameters"
            elif first_line == "deutsch":
                return "Option 2: Präfix zu 'Text'-Parametern hinzufügen"
            elif first_line == "farsi":
                return "گزینه ۲: افزودن پیشوند به پارامترهای 'متن'"
            elif first_line == "russian":
                return "Вариант 2: Добавить префикс к параметрам 'Текст'"
            elif first_line == "spanish":
                return "Opción 2: Agregar prefijo a los parámetros 'Texto'"
            elif first_line == "chinese":
                return "选项2：为'Text'参数添加前缀"
            elif first_line == "korean":
                return "옵션2: 'Text' 매개변수에 접두사 추가"
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
                return  "Option 3: Add Suffix to 'Text' parameters"
            elif first_line == "deutsch":
                return "Option 3: Suffix zu 'Text'-Parametern hinzufügen"
            elif first_line == "farsi":
                return "گزینه ۳: افزودن پسوند به پارامترهای 'متن'"
            elif first_line == "russian":
                return "Вариант 3: Добавить суффикс к параметрам 'Текст'"
            elif first_line == "spanish":
                return "Opción 3: Agregar sufijo a los parámetros 'Texto'"
            elif first_line == "chinese":
                return "选项3：为'Text'参数添加后缀"
            elif first_line == "korean":
                return "옵션3: 'Text' 매개변수에 접미사 추가"
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
                return "Option 4: Perform Math operations on 'Numeric' parameters"
            elif first_line == "deutsch":
                return "Option 4: Mathematische Operationen auf 'Numerische' Parameter durchführen"
            elif first_line == "farsi":
                return "گزینه ۴: انجام عملیات ریاضی بر روی پارامترهای 'عددی'"
            elif first_line == "russian":
                return "Вариант 4: Выполнить математические операции над параметрами 'Числовые'"
            elif first_line == "spanish":
                return "Opción 4: Realizar operaciones matemáticas en los parámetros 'Numéricos'"
            elif first_line == "chinese":
                return "选项4：对'数值'参数执行数学运算"
            elif first_line == "korean":
                return "옵션4: '숫자' 매개변수에서 수학 연산 수행"
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
                return  "You can replace each letter of parameter value with a new inserted letter for all the selected elements."
            elif first_line == "deutsch":
                return "Sie können jeden Buchstaben des Parameterwerts durch einen neu eingefügten Buchstaben für alle ausgewählten Elemente ersetzen."
            elif first_line == "farsi":
                return "شما می‌توانید هر حرف از مقدار پارامتر را با یک حرف جدیدی که وارد شده است برای تمام المان های انتخاب شده جایگزین کنید"
            elif first_line == "russian":
                return "Вы можете заменить каждую букву значения параметра на новую вставленную букву для всех выбранных элементов."
            elif first_line == "spanish":
                return "Puedes reemplazar cada letra del valor del parámetro con una nueva letra insertada para todos los elementos seleccionados."
            elif first_line == "chinese":
                return "您可以将参数值的每个字母替换为新插入的字母，适用于所有选定的元素。"
            elif first_line == "korean":
                return "선택한 모든 요소에 대해 매개변수 값의 각 문자를 새로 삽입된 문자로 대체할 수 있습니다."
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
                return "You can add a prefix to the parameter value for all the selected elements."
            elif first_line == "deutsch":
                return "Sie können allen ausgewählten Elementen einen Präfix zum Parameterwert hinzufügen."
            elif first_line == "farsi":
                return "شما می‌توانید به تمام المان های انتخاب شده یک پیشوند به مقدار پارامتر اضافه کنید"
            elif first_line == "russian":
                return "Вы можете добавить префикс к значению параметра для всех выбранных элементов."
            elif first_line == "spanish":
                return "Puedes agregar un prefijo al valor del parámetro para todos los elementos seleccionados."
            elif first_line == "chinese":
                return "您可以为所有选定的元素的参数值添加前缀。"
            elif first_line == "korean":
                return "선택한 모든 요소에 대해 매개변수 값에 접두사를 추가할 수 있습니다."
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
                return  "You can add a suffix to the parameter value for all the selected elements."
            elif first_line == "deutsch":
                return "Sie können allen ausgewählten Elementen einen Suffix zum Parameterwert hinzufügen."
            elif first_line == "farsi":
                return "شما می‌توانید به تمام المان های انتخاب شده یک پسوند به مقدار پارامتر اضافه کنید"
            elif first_line == "russian":
                return "Вы можете добавить суффикс к значению параметра для всех выбранных элементов."
            elif first_line == "spanish":
                return "Puedes agregar un sufijo al valor del parámetro para todos los elementos seleccionados."
            elif first_line == "chinese":
                return "您可以为所有选定的元素的参数值添加后缀。"
            elif first_line == "korean":
                return "선택한 모든 요소에 대해 매개변수 값에 접미사를 추가할 수 있습니다."
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
                return   "You can perform mathematical operations on a Numeric type parameter for all the selected elements."
            elif first_line == "deutsch":
                return "Sie können mathematische Operationen auf einen parameter vom Typ Numeric für alle ausgewählten Elemente durchführen."
            elif first_line == "farsi":
                return "شما می‌توانید عملیات ریاضی را برروی یک پارامتر از نوع عددی برای تمام المان های انتخاب شده انجام دهید"
            elif first_line == "russian":
                return "Вы можете выполнять математические операции с параметром типа Numeric для всех выбранных элементов."
            elif first_line == "spanish":
                return "Puedes realizar operaciones matemáticas en un parámetro de tipo Numérico para todos los elementos seleccionados."
            elif first_line == "chinese":
                return "您可以对所选元素的 Numeric 类型参数执行数学运算。"
            elif first_line == "korean":
                return "선택한 모든 요소에 대해 Numeric 유형의 매개변수에 수학 연산을 수행할 수 있습니다."
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
                return "Note that each of the tools is designed for a specific type of parameter and can be used only for the correct parameter type."
            elif first_line == "deutsch":
                return "Beachten Sie, dass jedes der Werkzeuge für einen bestimmten Parametertyp entwickelt wurde und nur für den richtigen Parametertyp verwendet werden kann."
            elif first_line == "farsi":
                return "توجه داشته باشید که هر یک از ابزارها برای یک نوع خاص از پارامتر طراحی شده‌اند و فقط برای نوع پارامتر صحیح قابل استفاده هستند"
            elif first_line == "russian":
                return "Обратите внимание, что каждый из инструментов разработан для определенного типа параметра и может использоваться только для правильного типа параметра."
            elif first_line == "spanish":
                return "Ten en cuenta que cada una de las herramientas está diseñada para un tipo específico de parámetro y solo se puede utilizar para el tipo de parámetro correcto."
            elif first_line == "chinese":
                return "请注意，每个工具都设计用于特定类型的参数，并且只能用于正确的参数类型。"
            elif first_line == "korean":
                return "각 도구는 특정 유형의 매개변수에 대해 설계된 것이며 올바른 매개변수 유형에만 사용할 수 있음을 유의하세요."
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
    
def str_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Replace:" 
            elif first_line == "deutsch":
                return "Ersetzen:"
            elif first_line == "farsi":
                return "جایگزین:"
            elif first_line == "russian":
                return "Заменить:"
            elif first_line == "spanish":
                return "Reemplazar:"
            elif first_line == "chinese":
                return "替换："
            elif first_line == "korean":
                return "대체:"
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
                return "Type of parameter: " 
            elif first_line == "deutsch":
                return "Typ des Parameters: "
            elif first_line == "farsi":
                return "نوع پارامتر: "
            elif first_line == "russian":
                return "Тип параметра: "
            elif first_line == "spanish":
                return "Tipo de parámetro: "
            elif first_line == "chinese":
                return "参数类型："
            elif first_line == "korean":
                return "매개변수 유형: "
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
                return "Note: \n\nThis tool is only for text type parameters.\n\nTo replace 'A' with 'B' use the following format:\n\nA|B\n\n"
            elif first_line == "deutsch":
                return "Hinweis: \n\nDieses Tool ist nur für Text-Parameter geeignet.\n\nUm 'A' durch 'B' zu ersetzen, verwenden Sie das folgende Format:\n\nA|B\n\n"
            elif first_line == "farsi":
                return "توجه: \n\nاین ابزار فقط برای پارامترهای نوع متن مناسب است\n\nبرای جایگزینی 'A' با 'B' از قالب زیر استفاده کنید\n\nA|B"
            elif first_line == "russian":
                return "Примечание: \n\nЭтот инструмент предназначен только для параметров типа текст.\n\nДля замены 'A' на 'B' используйте следующий формат:\n\nA|B\n\n"
            elif first_line == "spanish":
                return "Nota: \n\nEsta herramienta es solo para parámetros de tipo texto.\n\nPara reemplazar 'A' con 'B', utiliza el siguiente formato:\n\nA|B\n\n"
            elif first_line == "chinese":
                return "注意：\n\n此工具仅适用于文本类型参数。\n\n要将 'A' 替换为 'B'，请使用以下格式：\n\nA|B\n\n"
            elif first_line == "korean":
                return "참고: \n\n이 도구는 텍스트 유형의 매개변수에만 적용됩니다.\n\n'A'를 'B'로 대체하려면 다음 형식을 사용하세요:\n\nA|B\n\n"
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
                return "replace"
            elif first_line == "deutsch":
                return "ersetzen"
            elif first_line == "farsi":
                return "جایگزین کردن"
            elif first_line == "russian":
                return "заменить"
            elif first_line == "spanish":
                return "reemplazar"
            elif first_line == "chinese":
                return "替换"
            elif first_line == "korean":
                return "바꾸기"
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
                return "This tool only works for parameters with a text type."
            elif first_line == "deutsch":
                return "Dieses Tool funktioniert nur für Parameter vom Typ Text."
            elif first_line == "farsi":
                return "این ابزار فقط برای پارامترهایی با نوع متن کار می‌کند"
            elif first_line == "russian":
                return "Этот инструмент работает только с параметрами типа текст."
            elif first_line == "spanish":
                return "Esta herramienta solo funciona para parámetros con tipo de texto."
            elif first_line == "chinese":
                return "此工具仅适用于文本类型的参数。"
            elif first_line == "korean":
                return "이 도구는 텍스트 유형의 매개변수에만 작동합니다."
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
    
def str_17(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "This tool cannot handle commas in the input. Please remove them. For replacing commas please use Parameter value editor for special characters."
            elif first_line == "deutsch":
                return "Dieses Tool kann keine Kommas im Eingabefeld verarbeiten. Bitte entfernen Sie sie. Um Kommas zu ersetzen, verwenden Sie den Parameter-Wert-Editor für Sonderzeichen."
            elif first_line == "farsi":
                return "این ابزار قادر به مدیریت کاما در ورودی نیست. لطفاً آنها را حذف کنید. برای جایگزینی کاما ازابزار ویرایشگر مقدار پارامتر برای کاراکترهای خاص استفاده کنید"
            elif first_line == "russian":
                return "Этот инструмент не может обрабатывать запятые во входных данных. Пожалуйста, удалите их. Для замены запятых используйте редактор значения параметра для специальных символов."
            elif first_line == "spanish":
                return "Esta herramienta no puede manejar comas en la entrada. Por favor, elimínelas. Para reemplazar comas utilice el editor de valor de parámetro para caracteres especiales."
            elif first_line == "chinese":
                return "此工具无法处理输入中的逗号。请删除它们。要替换逗号请使用参数值编辑器处理特殊字符。"
            elif first_line == "korean":
                return "이 도구는 입력의 쉼표를 처리할 수 없습니다. 제거해 주세요. 쉼표를 대체하려면 매개변수 값 편집기를 사용하십시오."
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
                return "No elements selected. Please select at least one element."
            elif first_line == "deutsch":
                return "Keine Elemente ausgewählt. Bitte wählen Sie mindestens ein Element aus."
            elif first_line == "farsi":
                return "هیچ المانی انتخاب نشده است. لطفاً حداقل یک المان را انتخاب کنید"
            elif first_line == "russian":
                return "Не выбрано ни одного элемента. Пожалуйста, выберите хотя бы один элемент."
            elif first_line == "spanish":
                return "No se han seleccionado elementos. Por favor, seleccione al menos un elemento."
            elif first_line == "chinese":
                return "未选择任何元素。请至少选择一个元素。"
            elif first_line == "korean":
                return "선택된 요소가 없습니다. 최소한 하나의 요소를 선택해주세요."
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
    
def str_20(file_path):
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
    
def str_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Failed to set parameter value. {}"
            elif first_line == "deutsch":
                return "Fehler beim Festlegen des Parameterwerts. {}"
            elif first_line == "farsi":
                return "تنظیم مقدار پارامتر با شکست مواجه شد {}"
            elif first_line == "russian":
                return "Не удалось установить значение параметра. {}"
            elif first_line == "spanish":
                return "No se pudo establecer el valor del parámetro. {}"
            elif first_line == "chinese":
                return "无法设置参数值。{}"
            elif first_line == "korean":
                return "매개변수 값을 설정하는 데 실패했습니다. {}"
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
                return "Prefix:"
            elif first_line == "deutsch":
                return "Präfix:"
            elif first_line == "farsi":
                return "پیشوند:"
            elif first_line == "russian":
                return "Префикс:"
            elif first_line == "spanish":
                return "Prefijo:"
            elif first_line == "chinese":
                return "前缀："
            elif first_line == "korean":
                return "접두사:"
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
                return "Note: \n\nThis tool is only for text type parameters.\n\nAny number or string you insert as prefix will be set for all the values even if the values are different for each element in selection."
            elif first_line == "deutsch":
                return "Hinweis: \n\nDieses Tool gilt nur für Parameter vom Typ Text.\n\nJede Zahl oder Zeichenkette, die Sie als Präfix einfügen, wird für alle Werte festgelegt, auch wenn die Werte für jedes Element in der Auswahl unterschiedlich sind."
            elif first_line == "farsi":
                return "توجه: \n\nاین ابزار تنها برای پارامترهای نوع متن استفاده می‌شود\n\nهر عدد یا رشته‌ای که به عنوان پیشوند وارد می‌کنید، برای همه مقادیر تنظیم خواهد شد، حتی اگر مقادیر برای هر المان در انتخاب متفاوت باشند"
            elif first_line == "russian":
                return "Примечание: \n\nЭтот инструмент предназначен только для параметров типа текст.\n\nЛюбое число или строка, которые вы вводите в качестве префикса, будут установлены для всех значений, даже если значения отличаются для каждого элемента в выборке."
            elif first_line == "spanish":
                return "Nota: \n\nEsta herramienta es solo para parámetros de tipo texto.\n\nCualquier número o cadena que insertes como prefijo se establecerá para todos los valores, incluso si los valores son diferentes para cada elemento en la selección."
            elif first_line == "chinese":
                return "注意：\n\n此工具仅适用于文本类型的参数。\n\n无论你插入的数字或字符串作为前缀，都将应用于所有值，即使每个元素的值在选择中是不同的。"
            elif first_line == "korean":
                return "참고: \n\n이 도구는 텍스트 유형의 매개변수에만 사용됩니다.\n\n접두사로 입력하는 숫자나 문자열은 선택한 요소들 각각의 값이 다르더라도 모든 값에 설정됩니다."
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
                return "prefix"
            elif first_line == "deutsch":
                return "Präfix"
            elif first_line == "farsi":
                return "پیشوند"
            elif first_line == "russian":
                return "префикс"
            elif first_line == "spanish":
                return "prefijo"
            elif first_line == "chinese":
                return "前缀"
            elif first_line == "korean":
                return "접두사"
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
                return "Suffix:"
            elif first_line == "deutsch":
                return "Suffix:"
            elif first_line == "farsi":
                return "پسوند:"
            elif first_line == "russian":
                return "Суффикс:"
            elif first_line == "spanish":
                return "Sufijo:"
            elif first_line == "chinese":
                return "后缀："
            elif first_line == "korean":
                return "접미사:"
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
                return  "Note: \n\nThis tool is only for text type parameters.\n\nAny number or string you insert as suffix will be set for all the values even if the values are different for each element in selection."
            elif first_line == "deutsch":
                return "Hinweis: \n\nDieses Tool gilt nur für Parameter vom Typ Text.\n\nJede Zahl oder Zeichenkette, die Sie als Suffix einfügen, wird für alle Werte festgelegt, auch wenn die Werte für jedes Element in der Auswahl unterschiedlich sind."
            elif first_line == "farsi":
                return "توجه: \n\nاین ابزار تنها برای پارامترهای نوع متن استفاده می‌شود\n\nهر عدد یا رشته‌ای که به عنوان پسوند وارد می‌کنید، برای همه مقادیر تنظیم خواهد شد، حتی اگر مقادیر برای هر المان در انتخاب متفاوت باشند"
            elif first_line == "russian":
                return "Примечание: \n\nЭтот инструмент предназначен только для параметров типа текст.\n\nЛюбое число или строка, которые вы вводите в качестве суффикса, будут установлены для всех значений, даже если значения отличаются для каждого элемента в выборке."
            elif first_line == "spanish":
                return "Nota: \n\nEsta herramienta es solo para parámetros de tipo texto.\n\nCualquier número o cadena que insertes como sufijo se establecerá para todos los valores, incluso si los valores son diferentes para cada elemento en la selección."
            elif first_line == "chinese":
                return "注意：\n\n此工具仅适用于文本类型的参数。\n\n无论你插入的数字或字符串作为后缀，都将应用于所有值，即使每个元素的值在选择中是不同的。"
            elif first_line == "korean":
                return "참고: \n\n이 도구는 텍스트 유형의 매개변수에만 사용됩니다.\n\n접미사로 입력하는 숫자나 문자열은 선택한 요소들 각각의 값이 다르더라도 모든 값에 설정됩니다."
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
                return "Suffix"
            elif first_line == "deutsch":
                return "Suffix"
            elif first_line == "farsi":
                return "پسوند"
            elif first_line == "russian":
                return "суффикс"
            elif first_line == "spanish":
                return "Sufijo"
            elif first_line == "chinese":
                return "后缀"
            elif first_line == "korean":
                return "접미사"
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
                return "Mathematical Operation:"
            elif first_line == "deutsch":
                return "Mathematische Operation:"
            elif first_line == "farsi":
                return "عملیات ریاضی:"
            elif first_line == "russian":
                return "Математическая операция:"
            elif first_line == "spanish":
                return "Operación Matemática:"
            elif first_line == "chinese":
                return "数学运算："
            elif first_line == "korean":
                return "수학 연산:"
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
                return "Note: \n\nThis tool is only for numeric type parameters.\n\nFormat: operation + value (e.g., +10)"
            elif first_line == "deutsch":
                return "Hinweis: \n\nDieses Tool gilt nur für numerische Parameter.\n\nFormat: Operation + Wert (z. B. +10)"
            elif first_line == "farsi":
                return "توجه: \n\nاین ابزار تنها برای پارامترهای عددی استفاده می‌شود\n\nفرمت: عملیات ریاضی + مقدار (e.g., +10)"
            elif first_line == "russian":
                return "Примечание: \n\nЭтот инструмент предназначен только для числовых параметров.\n\nФормат: операция + значение (например, +10)"
            elif first_line == "spanish":
                return "Nota: \n\nEsta herramienta es solo para parámetros numéricos.\n\nFormato: operación + valor (por ejemplo, +10)"
            elif first_line == "chinese":
                return "注意：\n\n此工具仅适用于数值类型的参数。\n\n格式：操作 + 值（例如，+10)"
            elif first_line == "korean":
                return "참고: \n\n이 도구는 숫자 유형의 매개변수에만 사용됩니다.\n\n형식: 연산 + 값 (예: +10)"
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
                return "Math operation"
            elif first_line == "deutsch":
                return "Mathematische Operation"
            elif first_line == "farsi":
                return "عملیات ریاضی"
            elif first_line == "russian":
                return "Математическая операция"
            elif first_line == "spanish":
                return "Operación matemática"
            elif first_line == "chinese":
                return "数学运算"
            elif first_line == "korean":
                return "수학 연산"
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
                return "Invalid Math operation: {0}"
            elif first_line == "deutsch":
                return "Ungültige mathematische Operation: {0}"
            elif first_line == "farsi":
                return "عملیات ریاضی نامعتبر: {0}"
            elif first_line == "russian":
                return "Недопустимая математическая операция: {0}"
            elif first_line == "spanish":
                return "Operación matemática no válida: {0}"
            elif first_line == "chinese":
                return "无效的数学运算：{0}"
            elif first_line == "korean":
                return "잘못된 수학 연산: {0}"
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
                return "Parameter value editor"
            elif first_line == "deutsch":
                return "Parameter-Wert-Editor"
            elif first_line == "farsi":
                return "ویرایشگر مقدار پارامتر"
            elif first_line == "russian":
                return "Редактор значения параметра"
            elif first_line == "spanish":
                return "Editor de valor de parámetro"
            elif first_line == "chinese":
                return "参数值编辑器"
            elif first_line == "korean":
                return "매개변수 값 편집기"
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
                return "Replaced character report"
            elif first_line == "deutsch":
                return "Bericht zu ersetzten Zeichen"
            elif first_line == "farsi":
                return "گزارش کاراکتر جایگزین شده"
            elif first_line == "russian":
                return "Отчет о замененных символах"
            elif first_line == "spanish":
                return "Informe de caracteres reemplazados"
            elif first_line == "chinese":
                return "替换字符报告"
            elif first_line == "korean":
                return "대체된 문자 보고서"
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
    
def str_35(file_path):
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
    
def str_36(file_path):
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
    
def str_37(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Added prefix report"
            elif first_line == "deutsch":
                return "Bericht zu hinzugefügten Präfixen"
            elif first_line == "farsi":
                return "گزارش پیشوند اضافه شده"
            elif first_line == "russian":
                return "Отчет о добавленных префиксах"
            elif first_line == "spanish":
                return "Informe de prefijos agregados"
            elif first_line == "chinese":
                return "添加前缀报告"
            elif first_line == "korean":
                return "추가된 접두사 보고서"
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
                return "Added suffix report"
            elif first_line == "deutsch":
                return "Bericht zu hinzugefügten Suffixen"
            elif first_line == "farsi":
                return "گزارش پسوند اضافه شده"
            elif first_line == "russian":
                return "Отчет о добавленных суффиксах"
            elif first_line == "spanish":
                return "Informe de sufijos agregados"
            elif first_line == "chinese":
                return "添加后缀报告"
            elif first_line == "korean":
                return "추가된 접미사 보고서"
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
                return "Performed math operation report"
            elif first_line == "deutsch":
                return "Bericht zu durchgeführten mathematischen Operationen"
            elif first_line == "farsi":
                return "گزارش عملیات ریاضی انجام شده"
            elif first_line == "russian":
                return "Отчет о выполненных математических операциях"
            elif first_line == "spanish":
                return "Informe de operación matemática realizada"
            elif first_line == "chinese":
                return "执行的数学运算报告"
            elif first_line == "korean":
                return "수행된 수학 연산 보고서"
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
                return "Performed math operation: "
            elif first_line == "deutsch":
                return "Durchgeführte mathematische Operation: "
            elif first_line == "farsi":
                return "عملیات ریاضی انجام شده: "
            elif first_line == "russian":
                return "Выполненная математическая операция: "
            elif first_line == "spanish":
                return "Operación matemática realizada: "
            elif first_line == "chinese":
                return "执行的数学运算: "
            elif first_line == "korean":
                return "수행된 수학 연산: "
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

def str_42(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Replacement : "
            elif first_line == "deutsch":
                return "Ersatz : "
            elif first_line == "farsi":
                return "جایگزین : "
            elif first_line == "russian":
                return "Замена : "
            elif first_line == "spanish":
                return "Reemplazo : "
            elif first_line == "chinese":
                return "替换 : "
            elif first_line == "korean":
                return "대체 : "
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
                return "Prefix : "
            elif first_line == "deutsch":
                return "Präfix : "
            elif first_line == "farsi":
                return "پیشوند : "
            elif first_line == "russian":
                return "Префикс : "
            elif first_line == "spanish":
                return "Prefijo : "
            elif first_line == "chinese":
                return "前缀 : "
            elif first_line == "korean":
                return "접두사 : "
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
                return "Suffix : "
            elif first_line == "deutsch":
                return "Suffix : "
            elif first_line == "farsi":
                return "پسوند : "
            elif first_line == "russian":
                return "Суффикс : "
            elif first_line == "spanish":
                return "Sufijo : "
            elif first_line == "chinese":
                return "后缀 : "
            elif first_line == "korean":
                return "접미사 : "
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
    
def str_46(file_path):
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
    
def str_47(file_path):
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
    
def str_48(file_path):
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
    