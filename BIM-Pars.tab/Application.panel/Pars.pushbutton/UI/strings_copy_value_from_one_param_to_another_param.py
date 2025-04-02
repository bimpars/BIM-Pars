# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_copy_value_from_one_param_to_another_param.py

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
                return "Copy parameter value from: "
            elif first_line == "deutsch":
                return "Parameterwert kopieren von: "
            elif first_line == "farsi":
                return "مقدار پارامتر را از اینجا کپی کن:"
            elif first_line == "russian":
                return "Скопировать значение параметра из: "
            elif first_line == "spanish":
                return "Copiar valor del parámetro de: "
            elif first_line == "chinese":
                return "从以下位置复制参数值: "
            elif first_line == "korean":
                return "다음에서 매개변수 값 복사: "
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
                return "Paste parameter value to:"
            elif first_line == "deutsch":
                return "Füge den Parameterwert ein in:"
            elif first_line == "farsi":
                return "مقدار پارامتر را در اینجاقرار  بده:"
            elif first_line == "russian":
                return "Вставьте значение параметра в:"
            elif first_line == "spanish":
                return "Pegar el valor del parámetro en:"
            elif first_line == "chinese":
                return "将参数值粘贴到以下位置："
            elif first_line == "korean":
                return "매개변수 값을 다음 위치에 붙여넣으세요:"
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
                return "Type Boolean:\n\nThis tool identifys 'Bool' parameters as integer, therefore you can copy them to both string and numeric type parameters based on the bellow coditions.\n\n'Value=1' >> 'checked'\n'Value=0' >> 'unchecked'\n'value= any other number' >> 'Gray'\n\nA Gray bool parameter is actualy '0' and can be copied only to numeric type parameters.\n\n\nType String:\n\nAny parameter can be copied in string type parameters except gray boolean.\n\n\nType Numeric:\n\nAny number from the string type and numeric type can be copied in them except when the value is a string. Gry boolean makes them  '0'."
            elif first_line == "deutsch":
                return "Boolescher Typ:\n\nDieses Tool identifiziert 'Bool'-Parameter als Ganzzahlen. Daher können Sie sie basierend auf den unten stehenden Bedingungen sowohl in String- als auch in numerische Parameter kopieren.\n\n'Value=1' >> 'ausgewählt'\n'Value=0' >> 'nicht ausgewählt'\n'Value=andere Zahl' >> 'Grau'\n\nEin grauer Boolescher Parameter ist tatsächlich '0' und kann nur in numerische Parameter kopiert werden.\n\n\nString-Typ:\n\nJeder Parameter kann in String-Parameter kopiert werden, außer dem grauen Booleschen Wert.\n\n\nNumerischer Typ:\n\nJede Zahl aus dem String-Typ und numerischen Typ kann in sie kopiert werden, außer wenn der Wert ein String ist. Ein grauer Boolescher Wert setzt sie auf '0'."
            elif first_line == "farsi":
                return "نوع بولین:\n\nاین ابزار پارامترهای نوع بولین را به عنوان اعداد صحیح شناسایی می‌کند، بنابراین می‌توانید آن‌ها را بر اساس شرایط زیر به هر دو پارامتر نوع رشته و عددی کپی کنید\n\n'Value=1' >> 'انتخاب شده'\n'Value=0' >> ' انتخاب نشده'\n'value= هر عدد دیگری' >> 'خاکستری'\n\nیک پارامتر بولین خاکستری در واقع برابر '0' است و فقط می‌توان آن را به پارامترهای عددی کپی کرد.\n\n\nنوع رشته:\n\nهر پارامتری به جز بولین خاکستری می‌تواند در پارامترهای نوع رشته کپی شود.\n\n\nنوع عددی:\n\nهر عدد از نوع رشته و نوع عددی می‌تواند در آن‌ها کپی شود، به استثنای زمانی که مقدار یک رشته بولین خاکستری  است.بولین خاکستری آن‌ها را برابر '0' قرار می‌دهد"
            elif first_line == "russian":
                return "Тип Булево:\n\nЭтот инструмент идентифицирует параметры 'Bool' как целые числа, поэтому вы можете копировать их как в строковые, так и в числовые параметры в соответствии с нижеприведенными условиями.\n\n'Value=1' >> 'выбрано'\n'Value=0' >> 'не выбрано'\n'Value=любое другое число' >> 'Серый'\n\nСерый булев параметр на самом деле равен '0' и может быть скопирован только в числовые параметры.\n\n\nТип Строка:\n\nЛюбой параметр может быть скопирован в параметры типа строка, за исключением серого булева.\n\n\nТип Числовой:\n\nЛюбое число из типа строка и числовой тип может быть скопировано в них, за исключением случаев, когда значение является строкой. Серый булев делает их '0'."
            elif first_line == "spanish":
                return "Tipo Booleano:\n\nEsta herramienta identifica los parámetros 'Bool' como enteros, por lo tanto, puedes copiarlos tanto en parámetros de tipo cadena como en parámetros de tipo numérico según las siguientes condiciones.\n\n'Value=1' >> 'seleccionado'\n'Value=0' >> 'no seleccionado'\n'value= cualquier otro número' >> 'Gris'\n\nUn parámetro booleano Gris es en realidad un '0' y solo se puede copiar en parámetros de tipo numérico.\n\nTipo Cadena:\n\nCualquier parámetro se puede copiar en parámetros de tipo cadena, excepto los booleanos Gris.\n\nTipo Numérico:\n\nCualquier número, ya sea del tipo cadena o del tipo numérico, se puede copiar en ellos, excepto cuando el valor es una cadena. Los booleanos Gris los convierten en '0'."
            elif first_line == "chinese":
                return "布尔类型：\n\n该工具将'Bool'参数识别为整数，因此您可以根据以下条件将它们复制到字符串和数值类型参数中。\n\n'Value=1' >> '选中'\n'Value=0' >> '未选中'\n'value=其他任意数字' >> '灰色'\n\n灰色布尔参数实际上是'0'，只能复制到数值类型参数中。\n\n字符串类型：\n\n除了灰色布尔值以外，任何参数都可以复制到字符串类型参数中。\n\n数值类型：\n\n字符串类型和数值类型中的任何数字都可以复制到它们中，除非该值为字符串。灰色布尔值将它们设为'0'。"
            elif first_line == "korean":
                return "부울 타입:\n\n이 도구는 'Bool' 매개변수를 정수로 인식하므로 아래 조건에 따라 문자열 및 숫자 형식 매개변수로 복사할 수 있습니다.\n\n'Value=1' >> '선택됨'\n'Value=0' >> '선택되지 않음'\n'value=기타 다른 숫자' >> '회색'\n\n회색 부울 매개변수는 실제로 '0'이며 숫자 형식 매개변수로만 복사할 수 있습니다.\n\n문자열 타입:\n\n회색 부울을 제외한 모든 매개변수는 문자열 타입 매개변수로 복사할 수 있습니다.\n\n숫자 타입:\n\n문자열 형식과 숫자 형식에서 숫자는 문자열이 아닐 때 복사할 수 있습니다. 회색 부울은 '0'으로 설정합니다."
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
                return 'Operation canceled.'
            elif first_line == "deutsch":
                return "Vorgang abgebrochen."
            elif first_line == "farsi":
                return  "عملیات لغو شد"
            elif first_line == "russian":
                return  "Операция отменена."
            elif first_line == "spanish":
                return  "Operación cancelada."
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
    
def str_6(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "The second parameter '{0}' does not exist for the following elements:\n{1}"
            elif first_line == "deutsch":
                return "Der zweite Parameter '{0}' existiert nicht für die folgenden Elemente:\n{1}"
            elif first_line == "farsi":
                return "پارامتر دوم '{0}' برای المان های زیر وجود ندارد:\n{1}"
            elif first_line == "russian":
                return "Второй параметр '{0}' не существует для следующих элементов:\n{1}"
            elif first_line == "spanish":
                return "El segundo parámetro '{0}' no existe para los siguientes elementos:\n{1}"
            elif first_line == "chinese":
                return "以下元素中不存在第二个参数 '{0}':\n{1}"
            elif first_line == "korean":
                return "다음 요소에 대한 두 번째 매개변수 '{0}'가 존재하지 않습니다:\n{1}"
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
                return "The first parameter '{0}' does not exist for the following elements:\n{1}"
            elif first_line == "deutsch":
                return "Der erste Parameter '{0}' existiert nicht für die folgenden Elemente:\n{1}"
            elif first_line == "farsi":
                return "پارامتر اول '{0}' برای المان های زیر وجود ندارد:\n{1}"
            elif first_line == "russian":
                return "Первый параметр '{0}' не существует для следующих элементов:\n{1}"
            elif first_line == "spanish":
                return "El primer parámetro '{0}' no existe para los siguientes elementos:\n{1}"
            elif first_line == "chinese":
                return "以下元素中不存在第一个参数 '{0}':\n{1}"
            elif first_line == "korean":
                return "다음 요소에 대한 첫 번째 매개변수 '{0}'가 존재하지 않습니다:\n{1}"
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
                return "Parameter Types"
            elif first_line == "deutsch":
                return "Parameter-Typen"
            elif first_line == "farsi":
                return "نوع پارامتر"
            elif first_line == "russian":
                return "Типы параметров"
            elif first_line == "spanish":
                return "Tipos de parámetros"
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
    
def str_9(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "The parameter type of the first parameter is: {0}\n\nThe parameter type of the second parameter is: {1}"
            elif first_line == "deutsch":
                return "Der Parameter-Typ des ersten Parameters lautet: {0}\n\nDer Parameter-Typ des zweiten Parameters lautet: {1}"
            elif first_line == "farsi":
                return "نوع پارامتر اول: {0}\n\nنوع پارامتر دوم: {1}"
            elif first_line == "russian":
                return "Тип параметра первого параметра: {0}\n\nТип параметра второго параметра: {1}"
            elif first_line == "spanish":
                return "El tipo de parámetro del primer parámetro es: {0}\n\nEl tipo de parámetro del segundo parámetro es: {1}"
            elif first_line == "chinese":
                return "第一个参数的参数类型为：{0}\n\n第二个参数的参数类型为：{1}"
            elif first_line == "korean":
                return "첫 번째 매개변수의 매개변수 유형: {0}\n\n두 번째 매개변수의 매개변수 유형: {1}"
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
                return "Copy from one parameter to another parameter"
            elif first_line == "deutsch":
                return "Von einem Parameter in einen anderen Parameter kopieren"
            elif first_line == "farsi":
                return "کپی از یک پارامتر به پارامتر دیگر"
            elif first_line == "russian":
                return "Скопировать из одного параметра в другой параметр"
            elif first_line == "spanish":
                return "Copiar de un parámetro a otro parámetro"
            elif first_line == "chinese":
                return "从一个参数复制到另一个参数"
            elif first_line == "korean":
                return "한 매개변수에서 다른 매개변수로 복사"
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
                return "Copied values report"
            elif first_line == "deutsch":
                return "Bericht zu kopierten Werten"
            elif first_line == "farsi":
                return "گزارش مقادیر کپی شده"
            elif first_line == "russian":
                return "Отчет о скопированных значениях"
            elif first_line == "spanish":
                return "Informe de valores copiados"
            elif first_line == "chinese":
                return "已复制的值报告"
            elif first_line == "korean":
                return "복사된 값 보고서"
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
        return "An error occurred: {e}"
    
def str_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Copied from  : "
            elif first_line == "deutsch":
                return "Kopiert von  : "
            elif first_line == "farsi":
                return " کپی شده از  : "
            elif first_line == "russian":
                return "Скопировано из  : "
            elif first_line == "spanish":
                return "Copiado de  : "
            elif first_line == "chinese":
                return "复制自  : "
            elif first_line == "korean":
                return "복사된 위치  : "
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
                return "Set for  : "
            elif first_line == "deutsch":
                return "Eingestellt für  : "
            elif first_line == "farsi":
                return " تنظیم شده برای : "
            elif first_line == "russian":
                return "Установлено для  : "
            elif first_line == "spanish":
                return "Configurado para  : "
            elif first_line == "chinese":
                return "设置为  : "
            elif first_line == "korean":
                return "설정된 대상  : "
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
                return "Source parameter type: "
            elif first_line == "deutsch":
                return "Quellparametertyp: "
            elif first_line == "farsi":
                return "نوع پارامتر منبع: "
            elif first_line == "russian":
                return "Тип исходного параметра: "
            elif first_line == "spanish":
                return "Tipo de parámetro de origen: "
            elif first_line == "chinese":
                return "源参数类型: "
            elif first_line == "korean":
                return "소스 매개변수 유형: "
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
                return "Target parameter type: "
            elif first_line == "deutsch":
                return "Zielparametertyp: "
            elif first_line == "farsi":
                return "نوع پارامتر هدف: "
            elif first_line == "russian":
                return "Тип целевого параметра: "
            elif first_line == "spanish":
                return "Tipo de parámetro de destino: "
            elif first_line == "chinese":
                return "目标参数类型: "
            elif first_line == "korean":
                return "대상 매개변수 유형: "
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
                return "Source parameter name : "
            elif first_line == "deutsch":
                return "Name des Quellparameters : "
            elif first_line == "farsi":
                return "نام پارامتر منبع : "
            elif first_line == "russian":
                return "Имя исходного параметра : "
            elif first_line == "spanish":
                return "Nombre del parámetro de origen : "
            elif first_line == "chinese":
                return "源参数名称 : "
            elif first_line == "korean":
                return "소스 매개변수 이름 : "
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
                return "Target parameter name : "
            elif first_line == "deutsch":
                return "Name des Zielparameters : "
            elif first_line == "farsi":
                return "نام پارامتر هدف : "
            elif first_line == "russian":
                return "Имя целевого параметра : "
            elif first_line == "spanish":
                return "Nombre del parámetro de destino : "
            elif first_line == "chinese":
                return "目标参数名称 : "
            elif first_line == "korean":
                return "대상 매개변수 이름 : "
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
    
def str_20(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Source Parameter"
            elif first_line == "deutsch":
                return "Quellparameter"
            elif first_line == "farsi":
                return "پارامتر منبع"
            elif first_line == "russian":
                return "Исходный параметр"
            elif first_line == "spanish":
                return "Parámetro de origen"
            elif first_line == "chinese":
                return "源参数"
            elif first_line == "korean":
                return "출처 매개변수"
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
                return "Source Type"
            elif first_line == "deutsch":
                return "Quelltyp"
            elif first_line == "farsi":
                return "نوع منبع"
            elif first_line == "russian":
                return "Тип источника"
            elif first_line == "spanish":
                return "Tipo de fuente"
            elif first_line == "chinese":
                return "源类型"
            elif first_line == "korean":
                return "출처 유형"
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
                return "Source Value"
            elif first_line == "deutsch":
                return "Quellwert"
            elif first_line == "farsi":
                return "مقدار منبع"
            elif first_line == "russian":
                return "Исходное значение"
            elif first_line == "spanish":
                return "Valor de origen"
            elif first_line == "chinese":
                return "源值"
            elif first_line == "korean":
                return "출처 값"
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
                return "Target Type"
            elif first_line == "deutsch":
                return "Zieltyp"
            elif first_line == "farsi":
                return "نوع هدف"
            elif first_line == "russian":
                return "Целевой тип"
            elif first_line == "spanish":
                return "Tipo de objetivo"
            elif first_line == "chinese":
                return "目标类型"
            elif first_line == "korean":
                return "대상 유형"
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
                return "Previous Value of Target"
            elif first_line == "deutsch":
                return "Vorheriger Wert des Ziels"
            elif first_line == "farsi":
                return "مقدار قبلی هدف"
            elif first_line == "russian":
                return "Предыдущее значение цели"
            elif first_line == "spanish":
                return "Valor anterior del objetivo"
            elif first_line == "chinese":
                return "目标的先前值"
            elif first_line == "korean":
                return "목표의 이전 값"
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
                return "New Value of Target"
            elif first_line == "deutsch":
                return "Neuer Wert des Ziels"
            elif first_line == "farsi":
                return "مقدار جدید هدف"
            elif first_line == "russian":
                return "Новое значение цели"
            elif first_line == "spanish":
                return "Nuevo valor del objetivo"
            elif first_line == "chinese":
                return "目标的新值"
            elif first_line == "korean":
                return "목표의 새로운 값"
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
    
    