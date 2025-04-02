# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings4_type_filter.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Levels"
            elif first_line == "deutsch":
                return "Ebenen"
            elif first_line == "farsi":
                return "سطوح"
            elif first_line == "russian":
                return "Уровни"
            elif first_line == "spanish":
                return"Niveles"
            elif first_line == "chinese":
                return "层级"
            elif first_line == "korean":
                return "레벨"
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
                return  "Select Level"
            elif first_line == "deutsch":
                return "Ebene auswählen"
            elif first_line == "farsi":
                return "سطح را انتخاب کنید"
            elif first_line == "russian":
                return "Выберите уровень"
            elif first_line == "spanish":
                return "Seleccionar nivel"
            elif first_line == "chinese":
                return "选择层级"
            elif first_line == "korean":
                return "레벨 선택"
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
                return  "Views"
            elif first_line == "deutsch":
                return "Ansichten"
            elif first_line == "farsi":
                return "نماها"
            elif first_line == "russian":
                return "Просмотры"
            elif first_line == "spanish":
                return "Vistas"
            elif first_line == "chinese":
                return "视图"
            elif first_line == "korean":
                return "조회수"
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
                return  "Select View"
            elif first_line == "deutsch":
                return "Auswahl anzeigen"
            elif first_line == "farsi":
                return "انتخاب نما"
            elif first_line == "russian":
                return "Выберите вид"
            elif first_line == "spanish":
                return "Seleccionar vista"
            elif first_line == "chinese":
                return "选择视图"
            elif first_line == "korean":
                return "보기 선택"
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
                return "Select Category"
            elif first_line == "deutsch":
                return "Kategorie auswählen"
            elif first_line == "farsi":
                return "دسته بندی را انتخاب کنید"
            elif first_line == "russian":
                return "Выберите категорию"
            elif first_line == "spanish":
                return "Seleccionar categoría"
            elif first_line == "chinese":
                return "选择类别"
            elif first_line == "korean":
                return "카테고리 선택"
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
                return "Category" 
            elif first_line == "deutsch":
                return "Kategorie"
            elif first_line == "farsi":
                return "دسته بندی"
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
    
def str_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Select Family"
            elif first_line == "deutsch":
                return "Familie auswählen"
            elif first_line == "farsi":
                return "انتخاب خانواده"
            elif first_line == "russian":
                return "Выберите семейство"
            elif first_line == "spanish":
                return "Seleccionar familia"
            elif first_line == "chinese":
                return "选择家族"
            elif first_line == "korean":
                return "가족 선택"
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
                return "Family"
            elif first_line == "deutsch":
                return "Familie"
            elif first_line == "farsi":
                return "خانواده"
            elif first_line == "russian":
                return "Семья"
            elif first_line == "spanish":
                return "Familia"
            elif first_line == "chinese":
                return "家族"
            elif first_line == "korean":
                return "가족"
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
                return  "Select Type"
            elif first_line == "deutsch":
                return "Typ auswählen"
            elif first_line == "farsi":
                return "انتخاب نوع"
            elif first_line == "russian":
                return "Выберите тип"
            elif first_line == "spanish":
                return "Seleccionar tipo"
            elif first_line == "chinese":
                return "选择类型"
            elif first_line == "korean":
                return "유형 선택"
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
                return  "Type"
            elif first_line == "deutsch":
                return "Typ"
            elif first_line == "farsi":
                return "نوع"
            elif first_line == "russian":
                return "Тип"
            elif first_line == "spanish":
                return "Tipo"
            elif first_line == "chinese":
                return "类型"
            elif first_line == "korean":
                return "유형"
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
                return  "No level available for the selected view."
            elif first_line == "deutsch":
                return "Keine Ebene für die ausgewählte Ansicht verfügbar."
            elif first_line == "farsi":
                return "برای نمای انتخاب شده هیچ سطحی در دسترس نیست"
            elif first_line == "russian":
                return "Для выбранного вида нет доступных уровней."
            elif first_line == "spanish":
                return "No hay niveles disponibles para la vista seleccionada."
            elif first_line == "chinese":
                return "所选视图中没有可用的层级。"
            elif first_line == "korean":
                return "선택한 보기에는 사용 가능한 레벨이 없습니다."
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
                return  "Operation canceled."
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
    
def str_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "No categories with elements in the selected levels."
            elif first_line == "deutsch":
                return "Keine Kategorien mit Elementen in den ausgewählten Ebenen."
            elif first_line == "farsi":
                return "دسته‌بندی‌ ای همراه با المان در سطوح انتخاب شده وجود ندارد"
            elif first_line == "russian":
                return "Нет категорий с элементами на выбранных уровнях."
            elif first_line == "spanish":
                return "No hay categorías con elementos en los niveles seleccionados."
            elif first_line == "chinese":
                return "在所选层级中没有包含元素的类别。"
            elif first_line == "korean":
                return "선택한 레벨에 요소가 있는 카테고리가 없습니다."
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
                return  "No families with elements in the selected levels and category."
            elif first_line == "deutsch":
                return "Keine Familien mit Elementen in den ausgewählten Ebenen und Kategorie."
            elif first_line == "farsi":
                return "خانواده‌ای همراه با المان در سطوح و دسته‌بندی انتخاب شده وجود ندارد"
            elif first_line == "russian":
                return "Нет семейств с элементами на выбранных уровнях и категории."
            elif first_line == "spanish":
                return "No hay familias con elementos en los niveles y categoría seleccionados."
            elif first_line == "chinese":
                return "在所选层级和类别中没有包含元素的家族。"
            elif first_line == "korean":
                return "선택한 레벨과 카테고리에 요소가 있는 가족이 없습니다."
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
                return  "No types with elements in the selected levels, category, and family."
            elif first_line == "deutsch":
                return "Keine Typen mit Elementen in den ausgewählten Ebenen, Kategorie und Familie."
            elif first_line == "farsi":
                return "هیچ نوعی همراه با المان در سطوح، دسته‌بندی و خانواده انتخاب شده وجود ندارد"
            elif first_line == "russian":
                return "Нет типов с элементами на выбранных уровнях, категории и семействе."
            elif first_line == "spanish":
                return "No hay tipos con elementos en los niveles, categoría y familia seleccionados."
            elif first_line == "chinese":
                return "在所选层级、类别和家族中没有包含元素的类型。"
            elif first_line == "korean":
                return "선택한 레벨, 카테고리 및 가족에 요소가 있는 유형이 없습니다."
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
                return  "Selected Levels: "
            elif first_line == "deutsch":
                return "Ausgewählte Ebenen: "
            elif first_line == "farsi":
                return "سطوح انتخاب شده: "
            elif first_line == "russian":
                return "Выбранные уровни: "
            elif first_line == "spanish":
                return "Niveles seleccionados: "
            elif first_line == "chinese":
                return "已选择的层级："
            elif first_line == "korean":
                return "선택한 레벨: "
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
                return  "- Element ID: {} | Element Name: {} | Family Name: {} | Type Name: {}"
            elif first_line == "deutsch":
                return "- Element-ID: {} | Elementname: {} | Familienname: {} | Typname: {}"
            elif first_line == "farsi":
                return "- {}شناسه المان    | {}نام المان   | {}نام خانواده  |{} نام نوع  "
            elif first_line == "russian":
                return "- Идентификатор элемента: {} | Имя элемента: {} | Имя семейства: {} | Имя типа: {}"
            elif first_line == "spanish":
                return "- ID del elemento: {} | Nombre del elemento: {} | Nombre de la familia: {} | Nombre del tipo: {}"
            elif first_line == "chinese":
                return "- 元素ID：{} | 元素名称：{} | 家族名称：{} | 类型名称：{}"
            elif first_line == "korean":
                return "- 요소 ID: {} | 요소 이름: {} | 가족 이름: {} | 유형 이름: {}"
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
                return  "No type selected."
            elif first_line == "deutsch":
                return "Kein Typ ausgewählt."
            elif first_line == "farsi":
                return "نوعی انتخاب نشده است"
            elif first_line == "russian":
                return "Тип не выбран."
            elif first_line == "spanish":
                return "No se ha seleccionado ningún tipo."
            elif first_line == "chinese":
                return "未选择类型。"
            elif first_line == "korean":
                return "선택된 유형이 없습니다."
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
                return  "No family selected."
            elif first_line == "deutsch":
                return "Keine Familie ausgewählt."
            elif first_line == "farsi":
                return "خانواده‌ای انتخاب نشده است"
            elif first_line == "russian":
                return "Семейство не выбрано."
            elif first_line == "spanish":
                return "No se ha seleccionado ninguna familia."
            elif first_line == "chinese":
                return "未选择家族。"
            elif first_line == "korean":
                return "선택된 가족이 없습니다."
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
                return  "No category selected."
            elif first_line == "deutsch":
                return "Keine Kategorie ausgewählt."
            elif first_line == "farsi":
                return "هیچ دسته‌بندی انتخاب نشده است"
            elif first_line == "russian":
                return "Категория не выбрана."
            elif first_line == "spanish":
                return "No se ha seleccionado ninguna categoría."
            elif first_line == "chinese":
                return "未选择类别。"
            elif first_line == "korean":
                return "선택된 카테고리가 없습니다."
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
                return  "No levels selected."
            elif first_line == "deutsch":
                return "Es wurden keine Ebenen ausgewählt."
            elif first_line == "farsi":
                return "هیچ سطحی انتخاب نشده است"
            elif first_line == "russian":
                return "Уровни не выбраны."
            elif first_line == "spanish":
                return "No se han seleccionado niveles."
            elif first_line == "chinese":
                return "未选择层级。"
            elif first_line == "korean":
                return "선택된 레벨이 없습니다."
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
                return  "Filtering based on level does not include any type of object or element without having the 'Level' parameter."
            elif first_line == "deutsch":
                return "Die Filterung basierend auf der Ebene schließt keine Art von Objekt oder Element ein, das keinen 'Level'-Parameter hat."
            elif first_line == "farsi":
                return "فیلترینگ بر اساس سطح هیچ المانی را بدون داشتن پارامتر 'سطح' شامل نمی‌شود"
            elif first_line == "russian":
                return "Фильтрация на основе уровня не включает ни одного типа объекта или элемента, не имеющего параметра 'Уровень'."
            elif first_line == "spanish":
                return "La filtración basada en el nivel no incluye ningún tipo de objeto o elemento sin tener el parámetro 'Nivel'."
            elif first_line == "chinese":
                return "基于层级的过滤不包括任何没有'层级'参数的对象或元素。"
            elif first_line == "korean":
                return "'레벨' 매개변수가 없는 경우, 레벨을 기반으로 한 필터링은 어떤 종류의 객체나 요소도 포함하지 않습니다."
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
                return  "No views selected."
            elif first_line == "deutsch":
                return "Es wurden keine Ansichten ausgewählt."
            elif first_line == "farsi":
                return "هیچ نمایی انتخاب نشده است"
            elif first_line == "russian":
                return "Не выбраны виды."
            elif first_line == "spanish":
                return "No se han seleccionado vistas."
            elif first_line == "chinese":
                return "未选择视图。"
            elif first_line == "korean":
                return "선택된 뷰가 없습니다."
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
                return "Select By Type"
            elif first_line == "deutsch":
                return "Auswählen nach Typ"
            elif first_line == "farsi":
                return "انتخاب بر اساس نوع"
            elif first_line == "russian":
                return "Выбрать по типу"
            elif first_line == "spanish":
                return "Seleccionar Por Tipo"
            elif first_line == "chinese":
                return "按类型选择"
            elif first_line == "korean":
                return "유형별 선택"
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