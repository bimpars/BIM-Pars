# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_pair_compare_check.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "### Instance Properties"
            elif first_line == "deutsch":
                return "### Instanzeigenschaften"
            elif first_line == "farsi":
                return "### خصوصیات نمونه"
            elif first_line == "russian":
                return "### Свойства экземпляра"
            elif first_line == "spanish":
                return "### Propiedades de la instancia"
            elif first_line == "chinese":
                return "### 实例属性"
            elif first_line == "korean":
                return "### 인스턴스 속성"
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
                return "Passed"
            elif first_line == "deutsch":
                return "Bestanden"
            elif first_line == "farsi":
                return "قبول"
            elif first_line == "russian":
                return "Пройдено"
            elif first_line == "spanish":
                return "Aprobado"
            elif first_line == "chinese":
                return "通过"
            elif first_line == "korean":
                return "통과"
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
                return  "Failed"
            elif first_line == "deutsch":
                return "Fehlgeschlagen"
            elif first_line == "farsi":
                return "ناموفق"
            elif first_line == "russian":
                return "Неудача"
            elif first_line == "spanish":
                return "Fallido"
            elif first_line == "chinese":
                return "失败"
            elif first_line == "korean":
                return "실패"
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
                return "Parameter Name"
            elif first_line == "deutsch":
                return "Parametername"
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
    
def str_5(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "{} Value"
            elif first_line == "deutsch":
                return "{} Wert"
            elif first_line == "farsi":
                return "مقدار {}"
            elif first_line == "russian":
                return "Значение {}"
            elif first_line == "spanish":
                return "Valor {}"
            elif first_line == "chinese":
                return "{} 值"
            elif first_line == "korean":
                return "{} 값"
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
        return "An error occurred: {e}"
    
def str_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Instance Properties Comparison"
            elif first_line == "deutsch":
                return "Vergleich der Instanzeigenschaften"
            elif first_line == "farsi":
                return "مقایسه خصوصیات نمونه"
            elif first_line == "russian":
                return "Сравнение свойств экземпляра"
            elif first_line == "spanish":
                return "Comparación de propiedades de instancia"
            elif first_line == "chinese":
                return "实例属性比较"
            elif first_line == "korean":
                return "인스턴스 속성 비교"
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
                return "Unique Instance Properties"
            elif first_line == "deutsch":
                return "Eindeutige Instanzeigenschaften"
            elif first_line == "farsi":
                return "خصوصیات منحصر به فرد نمونه"
            elif first_line == "russian":
                return "Уникальные свойства экземпляра"
            elif first_line == "spanish":
                return "Propiedades únicas de la instancia"
            elif first_line == "chinese":
                return "唯一实例属性"
            elif first_line == "korean":
                return "고유 인스턴스 속성"
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
                return "### Type Properties"
            elif first_line == "deutsch":
                return "### Typ-Eigenschaften"
            elif first_line == "farsi":
                return "### خصوصیات نوع"
            elif first_line == "russian":
                return "### Свойства типа"
            elif first_line == "spanish":
                return "### Propiedades de tipo"
            elif first_line == "chinese":
                return "### 类型属性"
            elif first_line == "korean":
                return "### 타입 속성"
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
                return "Type Parameter Name"
            elif first_line == "deutsch":
                return "Typ-Parametername"
            elif first_line == "farsi":
                return "نام پارامتر نوع"
            elif first_line == "russian":
                return "Имя параметра типа"
            elif first_line == "spanish":
                return "Nombre del parámetro de tipo"
            elif first_line == "chinese":
                return "类型参数名称"
            elif first_line == "korean":
                return "타입 매개변수 이름"
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
                return "Type Properties Comparison"
            elif first_line == "deutsch":
                return "Vergleich der Typ-Eigenschaften"
            elif first_line == "farsi":
                return "مقایسه خصوصیات نوع"
            elif first_line == "russian":
                return "Сравнение свойств типа"
            elif first_line == "spanish":
                return "Comparación de propiedades de tipo"
            elif first_line == "chinese":
                return "类型属性比较"
            elif first_line == "korean":
                return "타입 속성 비교"
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
                return  "Unique Type Properties"
            elif first_line == "deutsch":
                return "Eindeutige Typ-Eigenschaften"
            elif first_line == "farsi":
                return "خصوصیات منحصر به فرد نوع"
            elif first_line == "russian":
                return "Уникальные свойства типа"
            elif first_line == "spanish":
                return "Propiedades únicas de tipo"
            elif first_line == "chinese":
                return "唯一类型属性"
            elif first_line == "korean":
                return "고유 타입 속성"
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
                return  "Comparison Mode"
            elif first_line == "deutsch":
                return "Vergleichsmodus"
            elif first_line == "farsi":
                return "حالت مقایسه"
            elif first_line == "russian":
                return "Режим сравнения"
            elif first_line == "spanish":
                return "Modo de comparación"
            elif first_line == "chinese":
                return "比较模式"
            elif first_line == "korean":
                return "비교 모드"
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
                return  "View" 
            elif first_line == "deutsch":
                return "Ansicht"
            elif first_line == "farsi":
                return "نما"
            elif first_line == "russian":
                return "Вид"
            elif first_line == "spanish":
                return "Vista"
            elif first_line == "chinese":
                return "视图"
            elif first_line == "korean":
                return "보기"
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
                return  "Element"
            elif first_line == "deutsch":
                return "Element"
            elif first_line == "farsi":
                return "المان"
            elif first_line == "russian":
                return "Элемент"
            elif first_line == "spanish":
                return "Elemento"
            elif first_line == "chinese":
                return "元素"
            elif first_line == "korean":
                return "요소"
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
                return  "Select Source View"
            elif first_line == "deutsch":
                return "Quellansicht auswählen"
            elif first_line == "farsi":
                return "انتخاب نمایشگر منبع"
            elif first_line == "russian":
                return "Выберите исходное представление"
            elif first_line == "spanish":
                return "Seleccionar vista de origen"
            elif first_line == "chinese":
                return "选择源视图"
            elif first_line == "korean":
                return "원본 보기 선택"
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
                return  "Select Target View"
            elif first_line == "deutsch":
                return "Zielansicht auswählen"
            elif first_line == "farsi":
                return "انتخاب نمایشگر مقصد"
            elif first_line == "russian":
                return "Выберите целевое представление"
            elif first_line == "spanish":
                return "Seleccionar vista de destino"
            elif first_line == "chinese":
                return "选择目标视图"
            elif first_line == "korean":
                return "대상 보기 선택"
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
                return  "Pick source object"
            elif first_line == "deutsch":
                return "Quellobjekt auswählen"
            elif first_line == "farsi":
                return "انتخاب شیء منبع"
            elif first_line == "russian":
                return "Выберите исходный объект"
            elif first_line == "spanish":
                return "Seleccionar objeto de origen"
            elif first_line == "chinese":
                return "选择源对象"
            elif first_line == "korean":
                return "소스 개체 선택"
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
                return  "Pick target element"
            elif first_line == "deutsch":
                return "Zielelement auswählen"
            elif first_line == "farsi":
                return "انتخاب المان مقصد"
            elif first_line == "russian":
                return "Выберите целевой элемент"
            elif first_line == "spanish":
                return "Seleccionar elemento de destino"
            elif first_line == "chinese":
                return "选择目标元素"
            elif first_line == "korean":
                return "대상 요소 선택"
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
                return  "Pair comparer"
            elif first_line == "deutsch":
                return "Paar-Vergleicher"
            elif first_line == "farsi":
                return "جفت مقایسه کننده"
            elif first_line == "russian":
                return "Сравниватель пар"
            elif first_line == "spanish":
                return "Comparador de pares"
            elif first_line == "chinese":
                return "对比器"
            elif first_line == "korean":
                return "쌍 비교기"
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
                return "Comparison"
            elif first_line == "deutsch":
                return "Vergleich"
            elif first_line == "farsi":
                return "مقایسه"
            elif first_line == "russian":
                return "Сравнение"
            elif first_line == "spanish":
                return "Comparación"
            elif first_line == "chinese":
                return "比较"
            elif first_line == "korean":
                return "비교"
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