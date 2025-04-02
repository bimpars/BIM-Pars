# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_id_generator.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "ID Generator"
            elif first_line == "deutsch":
                return "ID-Generator"
            elif first_line == "farsi":
                return "تولیدکننده شناسه"
            elif first_line == "russian":
                return "Генератор идентификаторов"
            elif first_line == "spanish":
                return "Generador de ID"
            elif first_line == "chinese":
                return "ID生成器"
            elif first_line == "korean":
                return "ID 생성기"
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
                return "Option1: Count elements from '0' or '1' to 'n' :   'ID=...n'"
            elif first_line == "deutsch":
                return "Option 1: Elemente von '0' oder '1' bis 'n' zählen: 'ID=...n'"
            elif first_line == "farsi":
                return "'ID=...n': را محاسبه می کند'n'گزینه 1: تعداد المان ها از '0' یا '1' تا"
            elif first_line == "russian":
                return "Вариант 1: Подсчитать элементы от '0' или '1' до 'n': 'ID=...n'"
            elif first_line == "spanish":
                return "Opción 1: Contar elementos desde '0' o '1' hasta 'n': 'ID=...n'"
            elif first_line == "chinese":
                return "옵션1: '0' 또는 '1'에서 'n'까지 요소 수 세기: 'ID=...n'"
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
                return "Option 2: Get element Id as reference and add the Count before element Id:   'ID=(...n)ElementId'"
            elif first_line == "deutsch":
                return "Option 2: Element-ID als Referenz erhalten und die Anzahl vor der Element-ID hinzufügen: 'ID=(...n)ElementId'"
            elif first_line == "farsi":
                return "'ID=(...n)ElementId': گزینه 2: دریافت شناسه المان به عنوان مرجع و افزودن تعداد قبل از شناسه المان"
            elif first_line == "russian":
                return "Вариант 2: Получить идентификатор элемента в качестве ссылки и добавить количество перед идентификатором элемента: 'ID=(...n)ElementId'"
            elif first_line == "spanish":
                return "Opción 2: Obtener el ID del elemento como referencia y agregar el conteo antes del ID del elemento: 'ID=(...n)ElementId'"
            elif first_line == "chinese":
                return "选项2：通过引用获取元素ID，并在元素ID之前添加计数：'ID=(...n)ElementId'"
            elif first_line == "korean":
                return "옵션2: 요소 ID를 참조로 받아 요소 ID 앞에 개수를 추가합니다: 'ID=(...n)ElementId'"
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
                return "Option 3: Get element Id as reference and add the Count after element Id: 'ID=ElementId(...n)'"
            elif first_line == "deutsch":
                return "Option 3: Element-ID als Referenz erhalten und die Anzahl nach der Element-ID hinzufügen: 'ID=ElementId(...n)'"
            elif first_line == "farsi":
                return "'ID=ElementId(...n)': گزینه 3: دریافت شناسه المان به عنوان مرجع و افزودن تعداد پس از شناسه المان"
            elif first_line == "russian":
                return "Вариант 3: Получить идентификатор элемента в качестве ссылки и добавить количество после идентификатора элемента: 'ID=ElementId(...n)'"
            elif first_line == "spanish":
                return "Opción 3: Obtener el ID del elemento como referencia y agregar el conteo después del ID del elemento: 'ID=ElementId(...n)'"
            elif first_line == "chinese":
                return "选项3：通过引用获取元素ID，并在元素ID之后添加计数：'ID=ElementId(...n)'"
            elif first_line == "korean":
                return "옵션3: 요소 ID를 참조로 받아 요소 ID 뒤에 개수를 추가합니다: 'ID=ElementId(...n)'"
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
                return  "Option 4: Math operation on element Id: 'ID=ElementId(+ - * /)n'"
            elif first_line == "deutsch":
                return "Option 4: Mathematische Operation auf Element-ID: 'ID=ElementId(+ - * /)n'"
            elif first_line == "farsi":
                return "'ID=ElementId(+ - * /)n' : گزینه 4: عملیات ریاضی روی شناسه المان"
            elif first_line == "russian":
                return "Вариант 4: Математическая операция над идентификатором элемента: 'ID=ElementId(+ - * /)n'"
            elif first_line == "spanish":
                return "Opción 4: Operación matemática en el ID del elemento: 'ID=ElementId(+ - * /)n'"
            elif first_line == "chinese":
                return "选项4：对元素ID进行数学运算：'ID=ElementId(+ - * /)n'"
            elif first_line == "korean":
                return "옵션4: 요소 ID에 대한 수학 연산: 'ID=ElementId(+ - * /)n'"
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
                return "Option 5: Random integer with specified number of digits: 'ID=Random integer'"
            elif first_line == "deutsch":
                return "Option 5: Zufallszahl mit angegebener Anzahl von Ziffern: 'ID=Zufallszahl'"
            elif first_line == "farsi":
                return "ID=(Random integer) :گزینه 5: عدد صحیح تصادفی با تعداد مشخصی از رقم‌"
            elif first_line == "russian":
                return "Вариант 5: Случайное целое число с указанным количеством цифр: 'ID=Случайное целое число'"
            elif first_line == "spanish":
                return "Opción 5: Entero aleatorio con número de dígitos especificado: 'ID=Entero aleatorio'"
            elif first_line == "chinese":
                return "选项5：生成指定位数的随机整数：'ID=随机整数'"
            elif first_line == "korean":
                return "옵션5: 지정된 자릿수의 무작위 정수: 'ID=무작위 정수'"
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
                return  "Option 6: Random string with specified number of letters: 'ID=Random string'"
            elif first_line == "deutsch":
                return "Option 6: Zufälliger String mit angegebener Anzahl von Buchstaben: 'ID=Zufälliger String'"
            elif first_line == "farsi":
                return "ID=(Random string) :گزینه 6: رشته تصادفی با تعداد مشخصی از حروف"
            elif first_line == "russian":
                return "Вариант 6: Случайная строка с указанным количеством букв: 'ID=Случайная строка'"
            elif first_line == "spanish":
                return "Opción 6: Cadena aleatoria con número de letras especificado: 'ID=Cadena aleatoria'"
            elif first_line == "chinese":
                return "选项6：生成指定数量字母的随机字符串：'ID=随机字符串'"
            elif first_line == "korean":
                return "옵션6: 지정된 문자 수의 무작위 문자열: 'ID=무작위 문자열'"
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
                return  "Option 7: ElementId before a random integer with specified number of digits: 'ID=ElementId(Random integer)'"
            elif first_line == "deutsch":
                return "Option 7: Element-ID vor einer zufälligen Ganzzahl mit angegebener Anzahl von Ziffern: 'ID=ElementId(Zufallszahl)'"
            elif first_line == "farsi":
                return "'ID=ElementId(Random integer)' :گزینه 7: شناسه المان قبل از یک عدد صحیح تصادفی با تعداد مشخصی از رقم‌"
            elif first_line == "russian":
                return "Вариант 7: Идентификатор элемента перед случайным целым числом с указанным количеством цифр: 'ID=Идентификатор элемента(Случайное целое число)'"
            elif first_line == "spanish":
                return "Opción 7: ID del elemento antes de un número entero aleatorio con número de dígitos especificado: 'ID=ID del elemento(Entero aleatorio)'"
            elif first_line == "chinese":
                return "选项7：元素ID位于指定位数的随机整数之前：'ID=元素ID(随机整数)'"
            elif first_line == "korean":
                return "옵션7: 지정된 자릿수의 무작위 정수 앞에 요소 ID: 'ID=요소 ID(무작위 정수)'"
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
                return "Option 8: ElementId after a random integer with specified number of digits: 'ID=(Random integer)ElementId'"
            elif first_line == "deutsch":
                return "Option 8: Element-ID nach einer zufälligen Ganzzahl mit angegebener Anzahl von Ziffern: 'ID=(Zufallszahl)ElementId'"
            elif first_line == "farsi":
                return "'ID=(Random integer)ElementId' : گزینه 8: شناسه المان پس از یک عدد صحیح تصادفی با تعداد مشخصی از رقم‌"
            elif first_line == "russian":
                return "Вариант 8: Идентификатор элемента после случайного целого числа с указанным количеством цифр: 'ID=(Случайное целое число)Идентификатор элемента'"
            elif first_line == "spanish":
                return "Opción 8: ID del elemento después de un número entero aleatorio con número de dígitos especificado: 'ID=(Entero aleatorio)ID del elemento'"
            elif first_line == "chinese":
                return "选项8：指定位数的随机整数之后的元素ID：'ID=(随机整数)元素ID'"
            elif first_line == "korean":
                return "옵션8: 지정된 자릿수의 무작위 정수 뒤에 요소 ID: 'ID=(무작위 정수)요소 ID'"
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
                return "Option 9: ElementId before a random string with specified number of characters: 'ID=ElementId(Random string)'"
            elif first_line == "deutsch":
                return "Option 9: Element-ID vor einem zufälligen String mit angegebener Anzahl von Zeichen: 'ID=ElementId(Zufälliger String)'"
            elif first_line == "farsi":
                return "'ID=ElementId(Random string)' :گزینه 9: شناسه المان قبل از یک رشته تصادفی با تعداد مشخصی از کاراکتر"
            elif first_line == "russian":
                return "Вариант 9: Идентификатор элемента перед случайной строкой с указанным количеством символов: 'ID=Идентификатор элемента(Случайная строка)'"
            elif first_line == "spanish":
                return "Opción 9: ID del elemento antes de una cadena aleatoria con número de caracteres especificado: 'ID=ID del elemento(Cadena aleatoria)'"
            elif first_line == "chinese":
                return "选项9：元素ID位于指定数量字符的随机字符串之前：'ID=元素ID(随机字符串)'"
            elif first_line == "korean":
                return "옵션9: 지정된 문자 수의 무작위 문자열 앞에 요소 ID: 'ID=요소 ID(무작위 문자열)'"
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
                return "Option 10: ElementId after a random string with specified number of characters: 'ID=(Random string)ElementId'"
            elif first_line == "deutsch":
                return "Option 10: Element-ID nach einem zufälligen String mit angegebener Anzahl von Zeichen: 'ID=(Zufälliger String)ElementId'"
            elif first_line == "farsi":
                return "'ID=(Random string)ElementId' :گزینه 10: شناسه المان پس از یک رشته تصادفی با تعداد مشخصی از کاراکتر"
            elif first_line == "russian":
                return "Вариант 10: Идентификатор элемента после случайной строки с указанным количеством символов: 'ID=(Случайная строка)Идентификатор элемента'"
            elif first_line == "spanish":
                return "Opción 10: ID del elemento después de una cadena aleatoria con número de caracteres especificado: 'ID=(Cadena aleatoria)ID del elemento'"
            elif first_line == "chinese":
                return "选项10：指定数量字符的随机字符串之后的元素ID：'ID=(随机字符串)元素ID'"
            elif first_line == "korean":
                return "옵션10: 지정된 문자 수의 무작위 문자열 뒤에 요소 ID: 'ID=(무작위 문자열)요소 ID'"
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
                return "No element selected."
            elif first_line == "deutsch":
                return "Kein Element ausgewählt."
            elif first_line == "farsi":
                return "هیچ المانی انتخاب نشده است"
            elif first_line == "russian":
                return "Ни один элемент не выбран."
            elif first_line == "spanish":
                return "Ningún elemento seleccionado."
            elif first_line == "chinese":
                return "未选择任何元素。"
            elif first_line == "korean":
                return "선택된 요소가 없습니다."
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
                return "Information"
            elif first_line == "deutsch":
                return "Information"
            elif first_line == "farsi":
                return "اطلاعات"
            elif first_line == "russian":
                return "Информация"
            elif first_line == "spanish":
                return "Información"
            elif first_line == "chinese":
                return  "信息"
            elif first_line == "korean":
                return "정보"
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
                return "Start from:"
            elif first_line == "deutsch":
                return "Beginnen von:"
            elif first_line == "farsi":
                return "شروع از:"
            elif first_line == "russian":
                return "Начать с:"
            elif first_line == "spanish":
                return "Empezar desde:"
            elif first_line == "chinese":
                return  "从...开始:"
            elif first_line == "korean":
                return "다음부터 시작:"
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
                return "Parameter Name:"
            elif first_line == "deutsch":
                return "Parametername:"
            elif first_line == "farsi":
                return "نام پارامتر:"
            elif first_line == "russian":
                return "Имя параметра:"
            elif first_line == "spanish":
                return "Nombre de parámetro:"
            elif first_line == "chinese":
                return  "参数名称："
            elif first_line == "korean":
                return "매개변수 이름:"
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
                return "Parameter"
            elif first_line == "deutsch":
                return "Parameter"
            elif first_line == "farsi":
                return "پارامتر"
            elif first_line == "russian":
                return "Параметр"
            elif first_line == "spanish":
                return "Parámetro"
            elif first_line == "chinese":
                return  "参数"
            elif first_line == "korean":
                return "매개변수"
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
                return "No parameter inserted"
            elif first_line == "deutsch":
                return "Kein Parameter eingefügt"
            elif first_line == "farsi":
                return "هیچ پارامتری وارد نشده است"
            elif first_line == "russian":
                return "Параметр не вставлен"
            elif first_line == "spanish":
                return "No se ha insertado ningún parámetro"
            elif first_line == "chinese":
                return "未插入任何参数"
            elif first_line == "korean":
                return "매개변수가 삽입되지 않음"
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
                return "Parameter is not text."
            elif first_line == "deutsch":
                return "Der Parameter ist kein Text."
            elif first_line == "farsi":
                return "پارامتر متن نیست"
            elif first_line == "russian":
                return "Параметр не является текстом."
            elif first_line == "spanish":
                return "El parámetro no es un texto."
            elif first_line == "chinese":
                return "参数不是文本。"
            elif first_line == "korean":
                return "매개변수가 텍스트가 아닙니다."
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
                return "status"
            elif first_line == "deutsch":
                return "Status"
            elif first_line == "farsi":
                return "وضعیت"
            elif first_line == "russian":
                return "статус"
            elif first_line == "spanish":
                return "estado"
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
    
def str_20(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Operation was successful."
            elif first_line == "deutsch":
                return "Der Vorgang war erfolgreich."
            elif first_line == "farsi":
                return "عملیات با موفقیت انجام شد"
            elif first_line == "russian":
                return "Операция прошла успешно."
            elif first_line == "spanish":
                return "La operación fue exitosa."
            elif first_line == "chinese":
                return "操作成功。"
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
                return "At least one element does not have the parameter. Transaction aborted."
            elif first_line == "deutsch":
                return "Mindestens ein Element hat den Parameter nicht. Transaktion abgebrochen."
            elif first_line == "farsi":
                return "حداقل یک المان فاقد پارامتر است. تراکنش لغو شد"
            elif first_line == "russian":
                return "По крайней мере один элемент не имеет параметра. Транзакция отменена."
            elif first_line == "spanish":
                return "Al menos un elemento no tiene el parámetro. Transacción abortada."
            elif first_line == "chinese":
                return "至少有一个元素没有参数。交易已中止。"
            elif first_line == "korean":
                return "최소 하나의 요소에 매개변수가 없습니다. 트랜잭션이 중단되었습니다."
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
                return "Invalid range selected."
            elif first_line == "deutsch":
                return "Ungültiger Bereich ausgewählt."
            elif first_line == "farsi":
                return "محدوده انتخاب شده نامعتبر است"
            elif first_line == "russian":
                return "Выбран недействительный диапазон."
            elif first_line == "spanish":
                return "Rango seleccionado no válido."
            elif first_line == "chinese":
                return "选择的范围无效。"
            elif first_line == "korean":
                return "잘못된 범위가 선택되었습니다."
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
                return "No range selected."
            elif first_line == "deutsch":
                return "Kein Bereich ausgewählt."
            elif first_line == "farsi":
                return "هیچ محدوده ای انتخاب نشده است"
            elif first_line == "russian":
                return "Диапазон не выбран."
            elif first_line == "spanish":
                return "No se ha seleccionado ningún rango."
            elif first_line == "chinese":
                return "未选择任何范围。"
            elif first_line == "korean":
                return "범위가 선택되지 않았습니다."
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
                return "Separator:"
            elif first_line == "deutsch":
                return "Trennzeichen:"
            elif first_line == "farsi":
                return "جداکننده:"
            elif first_line == "russian":
                return "Разделитель:"
            elif first_line == "spanish":
                return "Separador:"
            elif first_line == "chinese":
                return "分隔符:"
            elif first_line == "korean":
                return "구분자:"
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
                return "Yes"
            elif first_line == "deutsch":
                return "Ja"
            elif first_line == "farsi":
                return "بله"
            elif first_line == "russian":
                return "Да"
            elif first_line == "spanish":
                return "Sí"
            elif first_line == "chinese":
                return "是"
            elif first_line == "korean":
                return "네"
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
                return "No"
            elif first_line == "deutsch":
                return "Nein"
            elif first_line == "farsi":
                return "خیر"
            elif first_line == "russian":
                return "Нет"
            elif first_line == "spanish":
                return "No"
            elif first_line == "chinese":
                return "否"
            elif first_line == "korean":
                return "아니요"
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
                return "Number of characters :"
            elif first_line == "deutsch":
                return "Zeichenanzahl :"
            elif first_line == "farsi":
                return "تعداد کاراکتر ها :"
            elif first_line == "russian":
                return "Количество символов :"
            elif first_line == "spanish":
                return "Número de caracteres :"
            elif first_line == "chinese":
                return "字符数 :"
            elif first_line == "korean":
                return "문자 수 :"
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
                return "Separator"
            elif first_line == "deutsch":
                return "Trennzeichen"
            elif first_line == "farsi":
                return "جداکننده"
            elif first_line == "russian":
                return "Разделитель"
            elif first_line == "spanish":
                return "Separador"
            elif first_line == "chinese":
                return "分隔符"
            elif first_line == "korean":
                return "구분자"
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
                return "Element Id and a random string"
            elif first_line == "deutsch":
                return "Element-ID und eine zufällige Zeichenkette"
            elif first_line == "farsi":
                return "شناسه المان و یک رشته تصادفی"
            elif first_line == "russian":
                return "Идентификатор элемента и случайная строка"
            elif first_line == "spanish":
                return "ID de elemento y una cadena aleatoria"
            elif first_line == "chinese":
                return "元素 ID 和随机字符串"
            elif first_line == "korean":
                return "요소 ID와 임의 문자열"
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
                return "No parameter name entered."
            elif first_line == "deutsch":
                return "Kein Parametername eingegeben."
            elif first_line == "farsi":
                return "هیچ نام پارامتری وارد نشده است"
            elif first_line == "russian":
                return "Имя параметра не введено."
            elif first_line == "spanish":
                return "No se ha introducido ningún nombre de parámetro."
            elif first_line == "chinese":
                return "未输入参数名称。"
            elif first_line == "korean":
                return "매개변수 이름이 입력되지 않았습니다."
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
                return "No separator entered."
            elif first_line == "deutsch":
                return "Kein Trennzeichen eingegeben."
            elif first_line == "farsi":
                return "هیچ جداکننده ای وارد نشده است"
            elif first_line == "russian":
                return "Разделитель не введен."
            elif first_line == "spanish":
                return "No se ha introducido ningún separador."
            elif first_line == "chinese":
                return  "未输入分隔符。"
            elif first_line == "korean":
                return "구분자가 입력되지 않았습니다."
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
                return "Math operations:"
            elif first_line == "deutsch":
                return "Mathematische Operationen:"
            elif first_line == "farsi":
                return "عملیات ریاضی:"
            elif first_line == "russian":
                return "Математические операции:"
            elif first_line == "spanish":
                return "Operaciones matemáticas:"
            elif first_line == "chinese":
                return "数学运算:"
            elif first_line == "korean":
                return "수학 연산:"
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
                return "Math operation on element ID"
            elif first_line == "deutsch":
                return "Mathematische Operation auf Element-ID"
            elif first_line == "farsi":
                return "عملیات ریاضی بر روی شناسه المان"
            elif first_line == "russian":
                return "Математическая операция над идентификатором элемента"
            elif first_line == "spanish":
                return "Operación matemática sobre el ID de elemento"
            elif first_line == "chinese":
                return "在元素 ID 上执行数学运算"
            elif first_line == "korean":
                return "요소 ID에 대한 수학 연산"
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
                return "Note: You can do multiple operations at the same time by separating each operation with commas (e.g., +8,*7,*3,^2)"
            elif first_line == "deutsch":
                return "Hinweis: Sie können mehrere Operationen gleichzeitig durchführen, indem Sie die einzelnen Operationen mit Kommas trennen (z.B. +8,*7,*3,^2)"
            elif first_line == "farsi":
                return "توجه: می توانید چندین عملیات را بوسیله ی جدا کردن هر عملیات با کاماهمزمان انجام دهید (مثال: +8،*7،*3،^2)"
            elif first_line == "russian":
                return "Примечание: Вы можете выполнять несколько операций одновременно, разделяя каждую операцию запятыми (например, +8,*7,*3,^2)"
            elif first_line == "spanish":
                return "Nota: Puede realizar múltiples operaciones al mismo tiempo separando cada operación con comas (por ejemplo, +8,*7,*3,^2)"
            elif first_line == "chinese":
                return "注意:您可以通过用逗号分隔每个操作来同时执行多个操作(例如,+8,*7,*3,^2)"
            elif first_line == "korean":
                return "참고: 각 연산을 쉼표로 구분하여 여러 연산을 동시에 수행할 수 있습니다(예: +8,*7,*3,^2)"
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
                return "Operation canceled"
            elif first_line == "deutsch":
                return "Operation abgebrochen"
            elif first_line == "farsi":
                return "عملیات لغو شد"
            elif first_line == "russian":
                return "Операция отменена"
            elif first_line == "spanish":
                return "Operación cancelada"
            elif first_line == "chinese":
                return "操作已取消"
            elif first_line == "korean":
                return "작업이 취소되었습니다"
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
                return "Error performing math operations on element ID."
            elif first_line == "deutsch":
                return "Fehler beim Ausführen mathematischer Operationen auf Element-ID."
            elif first_line == "farsi":
                return "خطا در انجام عملیات ریاضی بر روی شناسه المان"
            elif first_line == "russian":
                return "Ошибка при выполнении математических операций над идентификатором элемента."
            elif first_line == "spanish":
                return "Error al realizar operaciones matemáticas sobre el ID de elemento."
            elif first_line == "chinese":
                return "在元素 ID 上执行数学运算时出错。"
            elif first_line == "korean":
                return "요소 ID에 대한 수학 연산 수행 중 오류가 발생했습니다."
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
                return "Number of digits:"
            elif first_line == "deutsch":
                return "Anzahl der Ziffern:"
            elif first_line == "farsi":
                return "تعداد ارقام:"
            elif first_line == "russian":
                return "Число цифр:"
            elif first_line == "spanish":
                return "Número de dígitos:"
            elif first_line == "chinese":
                return "数字位数:"
            elif first_line == "korean":
                return "자릿수:"
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
                return "random integer"
            elif first_line == "deutsch":
                return "zufällige ganze Zahl"
            elif first_line == "farsi":
                return "عدد صحیح تصادفی"
            elif first_line == "russian":
                return "случайное целое число"
            elif first_line == "spanish":
                return "entero aleatorio"
            elif first_line == "chinese":
                return "随机整数"
            elif first_line == "korean":
                return "랜덤 정수"
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
                return "Number of characters:"
            elif first_line == "deutsch":
                return "Anzahl der Zeichen:"
            elif first_line == "farsi":
                return "تعدادکاراکترها :"
            elif first_line == "russian":
                return "Количество символов:"
            elif first_line == "spanish":
                return "Número de caracteres:"
            elif first_line == "chinese":
                return "字符数:"
            elif first_line == "korean":
                return "문자 수:"
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
                return "random string"
            elif first_line == "deutsch":
                return "zufälliger Zeichenfolge"
            elif first_line == "farsi":
                return "رشته تصادفی"
            elif first_line == "russian":
                return "случайная строка"
            elif first_line == "spanish":
                return "cadena aleatoria"
            elif first_line == "chinese":
                return "随机字符串"
            elif first_line == "korean":
                return "랜덤 문자열"
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
                return "Element ID and a random integer"
            elif first_line == "deutsch":
                return "Element-ID und eine zufällige ganze Zahl"
            elif first_line == "farsi":
                return "شناسه المان و یک عدد صحیح تصادفی"
            elif first_line == "russian":
                return "Идентификатор элемента и случайное целое число"
            elif first_line == "spanish":
                return "ID de elemento y un entero aleatorio"
            elif first_line == "chinese":
                return "元素 ID 和随机整数"
            elif first_line == "korean":
                return "요소 ID와 랜덤 정수"
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
                return "No character as separator entered."
            elif first_line == "deutsch":
                return "Es wurde kein Zeichen als Trennzeichen eingegeben."
            elif first_line == "farsi":
                return "هیچ کاراکتری به عنوان جداکننده وارد نشده است"
            elif first_line == "russian":
                return "Не введен символ в качестве разделителя."
            elif first_line == "spanish":
                return "No se ha ingresado ningún carácter como separador."
            elif first_line == "chinese":
                return "未输入分隔符字符。"
            elif first_line == "korean":
                return "구분자로 사용할 문자를 입력하지 않았습니다."
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
                return "Generated IDs Report"
            elif first_line == "deutsch":
                return "Bericht zu generierten IDs"
            elif first_line == "farsi":
                return "گزارش شناسه‌های تولید شده"
            elif first_line == "russian":
                return "Отчет о созданных идентификаторах"
            elif first_line == "spanish":
                return "Informe de IDs generados"
            elif first_line == "chinese":
                return "生成的 ID 报告"
            elif first_line == "korean":
                return "생성된 ID 보고서"
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
    
def str_45(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Previous value of parameter"
            elif first_line == "deutsch":
                return "Vorheriger Wert des Parameters"
            elif first_line == "farsi":
                return "مقدار قبلی پارامتر"
            elif first_line == "russian":
                return "Предыдущее значение параметра"
            elif first_line == "spanish":
                return "Valor previo del parámetro"
            elif first_line == "chinese":
                return "参数的先前值"
            elif first_line == "korean":
                return "매개변수의 이전 값"
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
                return "Generated unique ID"
            elif first_line == "deutsch":
                return "Generierte eindeutige ID"
            elif first_line == "farsi":
                return "شناسه منحصر به فرد تولید شده"
            elif first_line == "russian":
                return "Сгенерированный уникальный идентификатор"
            elif first_line == "spanish":
                return "ID único generado"
            elif first_line == "chinese":
                return "生成的唯一 ID"
            elif first_line == "korean":
                return "생성된 고유 ID"
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
                return "Method : "
            elif first_line == "deutsch":
                return "Methode: "
            elif first_line == "farsi":
                return "روش: "
            elif first_line == "russian":
                return "Метод: "
            elif first_line == "spanish":
                return "Método: "
            elif first_line == "chinese":
                return "方法: "
            elif first_line == "korean":
                return "메소드: "
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
                return "Count started from: "
            elif first_line == "deutsch":
                return "Zählung begann von: "
            elif first_line == "farsi":
                return "شروع شمارش از : "
            elif first_line == "russian":
                return "Подсчет начался с: "
            elif first_line == "spanish":
                return "El conteo comenzó desde: "
            elif first_line == "chinese":
                return "计数从以下开始: "
            elif first_line == "korean":
                return "계수 시작: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_49(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unique ID generated by counting elements."
            elif first_line == "deutsch":
                return "Eindeutige ID, die durch Zählen der Elemente generiert wurde."
            elif first_line == "farsi":
                return "شناسه منحصر به فرد با شمارش المان ها ایجاد شده است"
            elif first_line == "russian":
                return "Уникальный идентификатор, сгенерированный путем подсчета элементов."
            elif first_line == "spanish":
                return "ID único generado contando los elementos."
            elif first_line == "chinese":
                return "通过计算元素生成的唯一 ID。"
            elif first_line == "korean":
                return "요소 계수로 생성된 고유 ID."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_50(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter name: "
            elif first_line == "deutsch":
                return "Parametername: "
            elif first_line == "farsi":
                return "نام پارامتر: "
            elif first_line == "russian":
                return "Имя параметра: "
            elif first_line == "spanish":
                return "Nombre del parámetro: "
            elif first_line == "chinese":
                return "参数名称: "
            elif first_line == "korean":
                return "매개변수 이름: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_51(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Separation of actual element ID and count: "
            elif first_line == "deutsch":
                return "Trennung von tatsächlicher Element-ID und Zählung: "
            elif first_line == "farsi":
                return "جداکننده ی شناسه واقعی المان وعدد شمارش: "
            elif first_line == "russian":
                return "Разделение фактического идентификатора элемента и счетчика: "
            elif first_line == "spanish":
                return "Separación del ID de elemento real y el recuento: "
            elif first_line == "chinese":
                return "实际元素 ID 和计数的分隔符: "
            elif first_line == "korean":
                return "실제 요소 ID와 계수의 구분: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_52(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No separation used"
            elif first_line == "deutsch":
                return "Keine Trennung verwendet"
            elif first_line == "farsi":
                return "هیچ جداکننده ای استفاده نشده است"
            elif first_line == "russian":
                return "Разделение не используется"
            elif first_line == "spanish":
                return "No se usa separación"
            elif first_line == "chinese":
                return "未使用分隔符。"
            elif first_line == "korean":
                return "구분자가 사용되지 않습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_53(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unique ID generated by counting elements and adding the number before actual element ID."
            elif first_line == "deutsch":
                return "Eindeutige ID, die durch Zählen der Elemente und Hinzufügen der Nummer vor der tatsächlichen Element-ID generiert wurde."
            elif first_line == "farsi":
                return "شناسه منحصر به فردبا شمارش المان ها و افزودن اعدادشمارش قبل از شناسه واقعی المان ایجادشده است"
            elif first_line == "russian":
                return "Уникальный идентификатор, сгенерированный путем подсчета элементов и добавления номера перед фактическим идентификатором элемента."
            elif first_line == "spanish":
                return "ID único generado contando los elementos y agregando el número antes del ID de elemento real."
            elif first_line == "chinese":
                return "通过计算元素并在实际元素 ID 之前添加数字来生成唯一 ID。"
            elif first_line == "korean":
                return "요소를 계수하고 실제 요소 ID 앞에 숫자를 추가하여 생성된 고유 ID."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"   
    
def str_54(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unique ID generated by counting elements and adding the number after actual element ID."
            elif first_line == "deutsch":
                return "Eindeutige ID, die durch Zählen der Elemente und Hinzufügen der Nummer nach der tatsächlichen Element-ID erzeugt wird."
            elif first_line == "farsi":
                return "شناسه منحصر به فردبا شمارش المان ها و افزودن اعدادشمارش بعداز شناسه واقعی المان ایجادشده است"
            elif first_line == "russian":
                return "Уникальный идентификатор, созданный путем подсчета элементов и добавления числа после фактического идентификатора элемента."
            elif first_line == "spanish":
                return "ID único generado contando los elementos y agregando el número después del ID de elemento real."
            elif first_line == "chinese":
                return "通过计数元素并在实际元素 ID 后添加数字来生成唯一 ID。"
            elif first_line == "korean":
                return "실제 요소 ID 뒤에 번호를 추가하여 요소를 계산하여 생성된 고유 ID."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"   
    
def str_55(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unique ID generated by performing math operation on actual element ID."
            elif first_line == "deutsch":
                return "Eindeutige ID, die durch Ausführen einer mathematischen Operation auf der tatsächlichen Element-ID erzeugt wird."
            elif first_line == "farsi":
                return "شناسه منحصر به فرد  با انجام عملیات ریاضی بر روی عدد شناسه واقعی المان ایجاد شده است."
            elif first_line == "russian":
                return "Уникальный идентификатор, сгенерированный путем выполнения математической операции над фактическим идентификатором элемента."
            elif first_line == "spanish":
                return "ID único generado realizando una operación matemática en el ID de elemento real."
            elif first_line == "chinese":
                return "通过对实际元素 ID 执行数学运算来生成唯一 ID。"
            elif first_line == "korean":
                return "실제 요소 ID에 대한 수학 연산을 수행하여 생성된 고유 ID."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"   
    
def str_56(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Performed Math operation: "
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
    
def str_57(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unique ID generated by generating random integer with specific number of digits."
            elif first_line == "deutsch":
                return "Eindeutige ID, die durch Generieren einer Zufallszahl mit einer bestimmten Anzahl von Ziffern erzeugt wird."
            elif first_line == "farsi":
                return "شناسه منحصر به فرد با ایجاد عدد صحیح تصادفی با تعداد مشخصی از ارقام تولید شده است"
            elif first_line == "russian":
                return "Уникальный идентификатор, сгенерированный путем создания случайного целого числа с определенным количеством цифр."
            elif first_line == "spanish":
                return "ID único generado mediante la generación de un entero aleatorio con un número específico de dígitos."
            elif first_line == "chinese":
                return "通过生成具有特定位数的随机整数来生成唯一 ID。"
            elif first_line == "korean":
                return "특정 자릿수의 랜덤 정수를 생성하여 고유 ID를 생성합니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_58(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Number of digits: "
            elif first_line == "deutsch":
                return "Anzahl der Ziffern: "
            elif first_line == "farsi":
                return "تعداد ارقام: "
            elif first_line == "russian":
                return "Количество цифр: "
            elif first_line == "spanish":
                return "Número de dígitos: "
            elif first_line == "chinese":
                return "数字位数: "
            elif first_line == "korean":
                return "자릿수: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_59(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unique ID generated by generating random string with specific number of characters."
            elif first_line == "deutsch":
                return "Eindeutige ID, die durch Generieren einer zufälligen Zeichenfolge mit einer bestimmten Anzahl von Zeichen erzeugt wird."
            elif first_line == "farsi":
                return "شناسه منحصر به فرد با ایجاد رشته تصادفی با تعداد مشخصی از کاراکتر تولید شده است"
            elif first_line == "russian":
                return "Уникальный идентификатор, сгенерированный путем создания случайной строки с определенным количеством символов."
            elif first_line == "spanish":
                return "ID único generado mediante la generación de una cadena aleatoria con un número específico de caracteres."
            elif first_line == "chinese":
                return "通过生成具有特定字符数的随机字符串来生成唯一 ID。"
            elif first_line == "korean":
                return "특정 문자 수의 랜덤 문자열을 생성하여 고유 ID를 생성합니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_60(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Number of characters: "
            elif first_line == "deutsch":
                return "Anzahl der Zeichen: "
            elif first_line == "farsi":
                return "تعداد کاراکترها: "
            elif first_line == "russian":
                return "Количество символов: "
            elif first_line == "spanish":
                return "Número de caracteres: "
            elif first_line == "chinese":
                return "字符数: "
            elif first_line == "korean":
                return "문자 수: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_61(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unique ID generated by generating random integer and adding the integer after actual element ID."
            elif first_line == "deutsch":
                return "Eindeutige ID, die durch Generieren einer Zufallszahl und Hinzufügen der Zahl nach der tatsächlichen Element-ID erzeugt wird."
            elif first_line == "farsi":
                return "شناسه منحصر به فرد با ایجاد عدد صحیح تصادفی و اضافه کردن عدد پس از شناسه واقعی المان تولید شده است"
            elif first_line == "russian":
                return "Уникальный идентификатор, сгенерированный путем создания случайного целого числа и добавления этого числа после фактического идентификатора элемента."
            elif first_line == "spanish":
                return "ID único generado mediante la generación de un entero aleatorio y la adición del entero después del ID de elemento real."
            elif first_line == "chinese":
                return "通过生成随机整数并将该整数添加到实际元素 ID 之后来生成唯一 ID。"
            elif first_line == "korean":
                return "랜덤 정수를 생성하고 실제 요소 ID 뒤에 정수를 추가하여 고유 ID를 생성합니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_62(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Number of digits for random integer: "
            elif first_line == "deutsch":
                return "Anzahl der Ziffern für die Zufallszahl: "
            elif first_line == "farsi":
                return "تعداد ارقام برای عدد صحیح تصادفی: "
            elif first_line == "russian":
                return "Количество цифр для случайного целого числа: "
            elif first_line == "spanish":
                return "Número de dígitos para el entero aleatorio: "
            elif first_line == "chinese":
                return "随机整数的位数: "
            elif first_line == "korean":
                return "랜덤 정수의 자릿수: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_63(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Separation between actual element ID and random integer: "
            elif first_line == "deutsch":
                return "Trennung zwischen tatsächlicher Element-ID und Zufallszahl: "
            elif first_line == "farsi":
                return "جداکننده بین شناسه واقعی المان و عدد صحیح تصادفی: "
            elif first_line == "russian":
                return "Разделение между фактическим идентификатором элемента и случайным целым числом: "
            elif first_line == "spanish":
                return "Separación entre el ID de elemento real y el entero aleatorio: "
            elif first_line == "chinese":
                return "实际元素 ID 和随机整数之间的分隔符: "
            elif first_line == "korean":
                return "실제 요소 ID와 랜덤 정수 사이의 구분: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_64(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unique ID generated by generating random integer and adding the integer before actual element ID."
            elif first_line == "deutsch":
                return "Eindeutige ID, die durch Generieren einer Zufallszahl und Hinzufügen der Zahl vor der tatsächlichen Element-ID erzeugt wird."
            elif first_line == "farsi":
                return "شناسه منحصر به فرد با ایجاد عدد صحیح تصادفی و اضافه کردن عدد قبل از شناسه واقعی المان تولید شده است"
            elif first_line == "russian":
                return "Уникальный идентификатор, сгенерированный путем создания случайного целого числа и добавления этого числа перед фактическим идентификатором элемента."
            elif first_line == "spanish":
                return "ID único generado mediante la generación de un entero aleatorio y la adición del entero antes del ID de elemento real."
            elif first_line == "chinese":
                return "通过生成随机整数并将该整数添加到实际元素 ID 之前来生成唯一 ID。"
            elif first_line == "korean":
                return "랜덤 정수를 생성하고 실제 요소 ID 앞에 정수를 추가하여 고유 ID를 생성합니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_65(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unique ID generated by generating random string and adding the string after actual element ID."
            elif first_line == "deutsch":
                return "Eindeutige ID, die durch Generieren einer zufälligen Zeichenfolge und Hinzufügen der Zeichenfolge nach der tatsächlichen Element-ID erzeugt wird."
            elif first_line == "farsi":
                return "شناسه منحصر به فردبا تولید رشته تصادفی و اضافه کردن رشته پس از شناسه واقعی المان ایجاد شده است"
            elif first_line == "russian":
                return "Уникальный идентификатор, сгенерированный путем создания случайной строки и добавления этой строки после фактического идентификатора элемента."
            elif first_line == "spanish":
                return "ID único generado mediante la generación de una cadena aleatoria y la adición de la cadena después del ID de elemento real."
            elif first_line == "chinese":
                return "通过生成随机字符串并将该字符串添加到实际元素 ID 之后来生成唯一 ID。"
            elif first_line == "korean":
                return "랜덤 문자열을 생성하고 실제 요소 ID 뒤에 문자열을 추가하여 고유 ID를 생성합니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_66(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Number of characters for random string: "
            elif first_line == "deutsch":
                return "Anzahl der Zeichen für die Zufallszeichenfolge: "
            elif first_line == "farsi":
                return "تعداد کاراکترها برای رشته تصادفی: "
            elif first_line == "russian":
                return "Количество символов для случайной строки: "
            elif first_line == "spanish":
                return "Número de caracteres para la cadena aleatoria: "
            elif first_line == "chinese":
                return "随机字符串的字符数: "
            elif first_line == "korean":
                return "랜덤 문자열의 문자 수: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_67(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Separation between actual element ID and random string: "
            elif first_line == "deutsch":
                return "Trennung zwischen tatsächlicher Element-ID und Zufallszeichenfolge: "
            elif first_line == "farsi":
                return "جداکننده ی بین شناسه واقعی المان و رشته تصادفی: "
            elif first_line == "russian":
                return "Разделение между фактическим идентификатором элемента и случайной строкой: "
            elif first_line == "spanish":
                return "Separación entre el ID de elemento real y la cadena aleatoria: "
            elif first_line == "chinese":
                return "实际元素 ID 和随机字符串之间的分隔符: "
            elif first_line == "korean":
                return "실제 요소 ID와 랜덤 문자열 사이의 구분: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_68(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unique ID generated by generating random string and adding the string before actual element ID."
            elif first_line == "deutsch":
                return "Eindeutige ID, die durch Generieren einer zufälligen Zeichenfolge und Hinzufügen der Zeichenfolge vor der tatsächlichen Element-ID erzeugt wird."
            elif first_line == "farsi":
                return "شناسه منحصر به فردبا تولید رشته تصادفی و اضافه کردن رشته قبل از شناسه واقعی المان ایجاد شده است"
            elif first_line == "russian":
                return "Уникальный идентификатор, сгенерированный путем создания случайной строки и добавления этой строки перед фактическим идентификатором элемента."
            elif first_line == "spanish":
                return "ID único generado mediante la generación de una cadena aleatoria y la adición de la cadena antes del ID de elemento real."
            elif first_line == "chinese":
                return "通过生成随机字符串并将该字符串添加到实际元素 ID 之前来生成唯一 ID。"
            elif first_line == "korean":
                return "랜덤 문자열을 생성하고 실제 요소 ID 앞에 문자열을 추가하여 고유 ID를 생성합니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"  
    
def str_69(file_path):
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
    
def str_70(file_path):
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
    
def str_71(file_path):
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
    
def str_72(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Category"
            elif first_line == "deutsch":
                return "Kategorie"
            elif first_line == "farsi":
                return "دسته‌بندی"
            elif first_line == "russian":
                return "Категория"
            elif first_line == "spanish":
                return "Categoría"
            elif first_line == "chinese":
                return "类别"
            elif first_line == "korean":
                return "카테고리"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_73(file_path):
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
    
def str_74(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Storage Type"
            elif first_line == "deutsch":
                return "Speichertyp"
            elif first_line == "farsi":
                return "نوع ذخیره‌سازی"
            elif first_line == "russian":
                return "Тип хранения"
            elif first_line == "spanish":
                return "Tipo de almacenamiento"
            elif first_line == "chinese":
                return "存储类型"
            elif first_line == "korean":
                return "저장 유형"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_75(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Generate Method"
            elif first_line == "deutsch":
                return "Generierungsmethode"
            elif first_line == "farsi":
                return "روش تولید"
            elif first_line == "russian":
                return "Метод генерации"
            elif first_line == "spanish":
                return "Método de generación"
            elif first_line == "chinese":
                return "生成方法"
            elif first_line == "korean":
                return "생성 방법"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_76(file_path):
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
                return "先前的值"
            elif first_line == "korean":
                return "이전 값"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_77(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "New Value"
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
                return "새로운 값"
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
    