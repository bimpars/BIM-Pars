# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_bimpars_tools.py

def tool_str_1(file_path):
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
    
def tool_str_2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Creator Finder"
            elif first_line == "deutsch":
                return "Erstellerfinder"
            elif first_line == "farsi":
                return " خالق المان"
            elif first_line == "russian":
                return "Поиск Создателя"
            elif first_line == "spanish":
                return "Buscador de Creadores"
            elif first_line == "chinese":
                return "创建者查找器"
            elif first_line == "korean":
                return "작성자 찾기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Active View"
            elif first_line == "deutsch":
                return "Aktive Ansicht"
            elif first_line == "farsi":
                return "نمای فعال"
            elif first_line == "russian":
                return "Активный вид"
            elif first_line == "spanish":
                return "Vista Activa"
            elif first_line == "chinese":
                return "活动视图"
            elif first_line == "korean":
                return "활성 뷰"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Hierarchy"
            elif first_line == "deutsch":
                return "Hierarchie"
            elif first_line == "farsi":
                return "سلسله مراتب"
            elif first_line == "russian":
                return "Иерархия"
            elif first_line == "spanish":
                return "Jerarquía"
            elif first_line == "chinese":
                return "层次结构"
            elif first_line == "korean":
                return "계층 구조"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_5(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "DUDUL"
            elif first_line == "deutsch":
                return "DUDUL"
            elif first_line == "farsi":
                return "دودول"
            elif first_line == "russian":
                return "DUDUL"
            elif first_line == "spanish":
                return "DUDUL"
            elif first_line == "chinese":
                return "DUDUL"
            elif first_line == "korean":
                return "DUDUL"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_str_6(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Type"
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
    
def tool_str_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select by Search for Value of Instance Parameters"
            elif first_line == "deutsch":
                return "Nach Wert von Instanzparametern suchen und auswählen"
            elif first_line == "farsi":
                return "انتخاب با جستجو برای مقدار پارامترهای نمونه"
            elif first_line == "russian":
                return "Выбор по поиску значения параметров экземпляра"
            elif first_line == "spanish":
                return "Seleccionar por búsqueda del valor de parámetros de instancia"
            elif first_line == "chinese":
                return "按实例参数值搜索选择"
            elif first_line == "korean":
                return "인스턴스 매개변수 값을 검색하여 선택"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select based on Existence of Parameters Values"
            elif first_line == "deutsch":
                return "Auswahl basierend auf Existenz von Parameterwerten"
            elif first_line == "farsi":
                return "انتخاب بر اساس وجود مقادیر پارامترها"
            elif first_line == "russian":
                return "Выбор на основе существования значений параметров"
            elif first_line == "spanish":
                return "Seleccionar basado en la existencia de valores de parámetros"
            elif first_line == "chinese":
                return "基于参数值存在的选择"
            elif first_line == "korean":
                return "매개변수 값 존재 여부에 따른 선택"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_9(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "All Elements in Selected Categories"
            elif first_line == "deutsch":
                return "Alle Elemente in ausgewählten Kategorien"
            elif first_line == "farsi":
                return "تمام المان ها در دسته‌بندی های انتخاب‌ شده"
            elif first_line == "russian":
                return "Все элементы в выбранных категориях"
            elif first_line == "spanish":
                return "Todos los elementos en categorías seleccionadas"
            elif first_line == "chinese":
                return "所选类别中的所有元素"
            elif first_line == "korean":
                return "선택한 카테고리의 모든 요소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_10(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "All Elements in Selected Views"
            elif first_line == "deutsch":
                return "Alle Elemente in ausgewählten Ansichten"
            elif first_line == "farsi":
                return "تمام المان ها در نماهای انتخاب‌ شده"
            elif first_line == "russian":
                return "Все элементы в выбранных видах"
            elif first_line == "spanish":
                return "Todos los elementos en vistas seleccionadas"
            elif first_line == "chinese":
                return "所选视图中的所有元素"
            elif first_line == "korean":
                return "선택한 뷰의 모든 요소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "All Elements on Selected Levels"
            elif first_line == "deutsch":
                return "Alle Elemente auf ausgewählten Ebenen"
            elif first_line == "farsi":
                return "تمام المان ها در سطوح انتخاب‌ شده"
            elif first_line == "russian":
                return "Все элементы на выбранных уровнях"
            elif first_line == "spanish":
                return "Todos los elementos en niveles seleccionados"
            elif first_line == "chinese":
                return "所选楼层上的所有元素"
            elif first_line == "korean":
                return "선택한 레벨의 모든 요소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_12(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Ownership of Elements"
            elif first_line == "deutsch":
                return "Eigentum von Elementen"
            elif first_line == "farsi":
                return "مالکیت المان ها"
            elif first_line == "russian":
                return "Владение элементами"
            elif first_line == "spanish":
                return "Propiedad de elementos"
            elif first_line == "chinese":
                return "元素的所有权"
            elif first_line == "korean":
                return "요소의 소유권"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unbound Rooms"
            elif first_line == "deutsch":
                return "Ungebundene Räume"
            elif first_line == "farsi":
                return "اتاق‌های محدودنشده"
            elif first_line == "russian":
                return "Несвязанные комнаты"
            elif first_line == "spanish":
                return "Habitaciones no vinculadas"
            elif first_line == "chinese":
                return "未绑定的房间"
            elif first_line == "korean":
                return "바인딩되지 않은 방"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_14(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Mirrored Doors"
            elif first_line == "deutsch":
                return "Symmetrische Türen"
            elif first_line == "farsi":
                return " درهای متقارن"
            elif first_line == "russian":
                return "Симметричные двери"
            elif first_line == "spanish":
                return "Puertas simétricas"
            elif first_line == "chinese":
                return "对称门"
            elif first_line == "korean":
                return "대칭적인 문"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "IDs from Excel"
            elif first_line == "deutsch":
                return "IDs aus Excel"
            elif first_line == "farsi":
                return "شناسه‌ها از اکسل"
            elif first_line == "russian":
                return "Идентификаторы из Excel"
            elif first_line == "spanish":
                return "Identificadores de Excel"
            elif first_line == "chinese":
                return "来自Excel的ID"
            elif first_line == "korean":
                return "Excel에서 ID"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_16(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Reduce Selection by ID"
            elif first_line == "deutsch":
                return "Auswahl nach ID reduzieren"
            elif first_line == "farsi":
                return "کاهش انتخاب بر اساس شناسه"
            elif first_line == "russian":
                return "Уменьшить выбор по ID"
            elif first_line == "spanish":
                return "Reducir selección por ID"
            elif first_line == "chinese":
                return "按ID减少选择"
            elif first_line == "korean":
                return "ID로 선택 축소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_str_17(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Reduce Selection by OST Categories"
            elif first_line == "deutsch":
                return "Auswahl nach OST-Kategorien reduzieren"
            elif first_line == "farsi":
                return "OST کاهش انتخاب بر اساس دسته‌بندی‌های "
            elif first_line == "russian":
                return "Уменьшить выбор по категориям OST"
            elif first_line == "spanish":
                return "Reducir selección por categorías OST"
            elif first_line == "chinese":
                return "按OST类别减少选择"
            elif first_line == "korean":
                return "OST 카테고리로 선택 축소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Reduce Selection by Searching Value of Instance Parameters"
            elif first_line == "deutsch":
                return "Auswahl durch Suchen des Werts von Instanzparametern reduzieren"
            elif first_line == "farsi":
                return "کاهش انتخاب با جستجوی مقدار پارامترهای نمونه"
            elif first_line == "russian":
                return "Уменьшить выбор по поиску значения параметров экземпляра"
            elif first_line == "spanish":
                return "Reducir selección buscando el valor de parámetros de instancia"
            elif first_line == "chinese":
                return "通过搜索实例参数值减少选择"
            elif first_line == "korean":
                return "인스턴스 매개변수 값을 검색하여 선택 축소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_19(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Reduce Selection by Existence of Parameters Values"
            elif first_line == "deutsch":
                return "Auswahl durch Existenz von Parameterwerten reduzieren"
            elif first_line == "farsi":
                return "کاهش انتخاب بر اساس وجود مقادیر پارامترها"
            elif first_line == "russian":
                return "Уменьшить выбор по существованию значений параметров"
            elif first_line == "spanish":
                return "Reducir selección por existencia de valores de parámetros"
            elif first_line == "chinese":
                return "根据参数值的存在减少选择"
            elif first_line == "korean":
                return "매개변수 값 존재 여부에 따른 선택 축소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_20(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete Elements by ID"
            elif first_line == "deutsch":
                return "Elemente nach ID löschen"
            elif first_line == "farsi":
                return "حذف المان ها بر اساس شناسه"
            elif first_line == "russian":
                return "Удалить элементы по ID"
            elif first_line == "spanish":
                return "Eliminar elementos por ID"
            elif first_line == "chinese":
                return "按ID删除元素"
            elif first_line == "korean":
                return "ID로 요소 삭제"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete Elements by IDs from Excel"
            elif first_line == "deutsch":
                return "Elemente nach IDs aus Excel löschen"
            elif first_line == "farsi":
                return "حذف المان ها بر اساس شناسه‌ها از اکسل"
            elif first_line == "russian":
                return "Удалить элементы по ID из Excel"
            elif first_line == "spanish":
                return "Eliminar elementos por IDs desde Excel"
            elif first_line == "chinese":
                return "按来自Excel的ID删除元素"
            elif first_line == "korean":
                return "Excel에서 ID로 요소 삭제"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_22(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete Elements by Type Filter"
            elif first_line == "deutsch":
                return "Elemente nach Typfilter löschen"
            elif first_line == "farsi":
                return "حذف المان ها بر اساس فیلتر نوع"
            elif first_line == "russian":
                return "Удалить элементы по фильтру типа"
            elif first_line == "spanish":
                return "Eliminar elementos por filtro de tipo"
            elif first_line == "chinese":
                return "按类型过滤器删除元素"
            elif first_line == "korean":
                return "유형 필터로 요소 삭제"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_23(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete All DirectShape Elements"
            elif first_line == "deutsch":
                return "Alle DirectShape-Elemente löschen"
            elif first_line == "farsi":
                return " DirectShape حذف تمام المان های"
            elif first_line == "russian":
                return "Удалить все элементы DirectShape"
            elif first_line == "spanish":
                return "Eliminar todos los elementos DirectShape"
            elif first_line == "chinese":
                return "删除所有 DirectShape 元素"
            elif first_line == "korean":
                return "모든 DirectShape 요소 삭제"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_str_24(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete All Elements of OST Category"
            elif first_line == "deutsch":
                return "Alle Elemente der OST-Kategorie löschen"
            elif first_line == "farsi":
                return "OST حذف تمام المان های بندی های "
            elif first_line == "russian":
                return "Удалить все элементы категории OST"
            elif first_line == "spanish":
                return "Eliminar todos los elementos de la categoría OST"
            elif first_line == "chinese":
                return "删除OST类别的所有元素"
            elif first_line == "korean":
                return "OST 카테고리의 모든 요소 삭제"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_25(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Search Values of Parameters by Filter"
            elif first_line == "deutsch":
                return "Werte von Parametern nach Filter suchen"
            elif first_line == "farsi":
                return "جستجوی مقادیر پارامترها بر اساس فیلتر"
            elif first_line == "russian":
                return "Поиск значений параметров по фильтру"
            elif first_line == "spanish":
                return "Buscar valores de parámetros por filtro"
            elif first_line == "chinese":
                return "按筛选器搜索参数值"
            elif first_line == "korean":
                return "필터로 매개변수 값 검색"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_str_26(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Search Values of Parameters by Filter for Family Document"
            elif first_line == "deutsch":
                return "Werte von Parametern nach Filter für Familien-Dokument suchen"
            elif first_line == "farsi":
                return "جستجوی مقادیر پارامترها بر اساس فیلتر برای سند خانواده"
            elif first_line == "russian":
                return "Поиск значений параметров по фильтру для семейного документа"
            elif first_line == "spanish":
                return "Buscar valores de parámetros por filtro para documento de familia"
            elif first_line == "chinese":
                return "按筛选器搜索家族文档的参数值"
            elif first_line == "korean":
                return "가족 문서에 대한 필터로 매개변수 값 검색"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_27(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Snipe Parameter Value"
            elif first_line == "deutsch":
                return "Parameterwert anvisieren"
            elif first_line == "farsi":
                return "اسنایپ مقدارپارامتر"
            elif first_line == "russian":
                return "Нацеливание на значение параметра"
            elif first_line == "spanish":
                return "Apuntar al valor del parámetro"
            elif first_line == "chinese":
                return "瞄准参数值"
            elif first_line == "korean":
                return "파라미터 값 조준"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_28(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Snipe Parameter Value for Family Document"
            elif first_line == "deutsch":
                return "Parameterwert für Familien-Dokument anvisieren"
            elif first_line == "farsi":
                return "اسنایپ مقدار پارامتر برای سند خانواده"
            elif first_line == "russian":
                return "Нацеливание на значение параметра для семейного документа"
            elif first_line == "spanish":
                return "Apuntar al valor del parámetro para documento de familia"
            elif first_line == "chinese":
                return "针对家庭文档瞄准参数值"
            elif first_line == "korean":
                return "가족 문서의 파라미터 값 조준"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_29(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Dictionary"
            elif first_line == "deutsch":
                return "Wörterbuch"
            elif first_line == "farsi":
                return "دیکشنری"
            elif first_line == "russian":
                return "Словарь"
            elif first_line == "spanish":
                return "Diccionario"
            elif first_line == "chinese":
                return "字典"
            elif first_line == "korean":
                return "사전"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_30(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Check Existence of Parameters Values"
            elif first_line == "deutsch":
                return "Existenz von Parameterwerten überprüfen"
            elif first_line == "farsi":
                return "بررسی وجود مقادیر پارامترها"
            elif first_line == "russian":
                return "Проверить наличие значений параметров"
            elif first_line == "spanish":
                return "Comprobar existencia de valores de parámetros"
            elif first_line == "chinese":
                return "检查参数值的存在性"
            elif first_line == "korean":
                return "매개변수 값 존재 여부 확인"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_str_31(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Check Parameter Against Category"
            elif first_line == "deutsch":
                return "Parameter mit Kategorie abgleichen"
            elif first_line == "farsi":
                return "بررسی پارامتر با دسته بندی"
            elif first_line == "russian":
                return "Проверить параметр с категорией"
            elif first_line == "spanish":
                return "Comprobar parámetro contra categoría"
            elif first_line == "chinese":
                return "检查参数与类别"
            elif first_line == "korean":
                return "카테고리와 매개변수 확인"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_32(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete Parameter Completely from Model"
            elif first_line == "deutsch":
                return "Parameter vollständig aus dem Modell löschen"
            elif first_line == "farsi":
                return "حذف کامل پارامتر از مدل"
            elif first_line == "russian":
                return "Полностью удалить параметр из модели"
            elif first_line == "spanish":
                return "Eliminar completamente el parámetro del modelo"
            elif first_line == "chinese":
                return "完全从模型中删除参数"
            elif first_line == "korean":
                return "모델에서 파라미터 완전히 삭제"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_33(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Search for Value of Instance Parameters"
            elif first_line == "deutsch":
                return "Nach Wert von Instanzparametern suchen"
            elif first_line == "farsi":
                return "جستجوی مقدار پارامترهای نمونه"
            elif first_line == "russian":
                return "Поиск значения параметров экземпляра"
            elif first_line == "spanish":
                return "Buscar el valor de los parámetros de instancia"
            elif first_line == "chinese":
                return "搜索实例参数的值"
            elif first_line == "korean":
                return "인스턴스 매개변수 값 검색"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_34(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Search for Any Value"
            elif first_line == "deutsch":
                return "Nach beliebigem Wert suchen"
            elif first_line == "farsi":
                return "جستجو برای هر مقدار"
            elif first_line == "russian":
                return "Поиск любого значения"
            elif first_line == "spanish":
                return "Buscar cualquier valor"
            elif first_line == "chinese":
                return "搜索任何值"
            elif first_line == "korean":
                return "모든 값 검색"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_35(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Pair Comparer"
            elif first_line == "deutsch":
                return "Paar-Vergleicher"
            elif first_line == "farsi":
                return "جفت مقایسه کننده"
            elif first_line == "russian":
                return "Сравнение пар"
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

def tool_str_36(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Comparer of Multiple Elements"
            elif first_line == "deutsch":
                return "Vergleicher mehrerer Elemente"
            elif first_line == "farsi":
                return "مقایسه کننده چندین المان"
            elif first_line == "russian":
                return "Сравнение нескольких элементов"
            elif first_line == "spanish":
                return "Comparador de múltiples elementos"
            elif first_line == "chinese":
                return "多元素对比器"
            elif first_line == "korean":
                return "다중 요소 비교기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_37(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Same Value for All Selected Elements"
            elif first_line == "deutsch":
                return "Gleicher Wert für alle ausgewählten Elemente"
            elif first_line == "farsi":
                return "مقدار یکسان برای تمام المان‌های انتخاب شده"
            elif first_line == "russian":
                return "Одинаковое значение для всех выбранных элементов"
            elif first_line == "spanish":
                return "Mismo valor para todos los elementos seleccionados"
            elif first_line == "chinese":
                return "所有选定元素的相同值"
            elif first_line == "korean":
                return "선택된 모든 요소에 대한 동일한 값"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_str_38(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Copy from One Parameter to Another Parameter"
            elif first_line == "deutsch":
                return "Kopieren von einem Parameter zu einem anderen Parameter"
            elif first_line == "farsi":
                return "کپی از یک پارامتر به پارامتر دیگر"
            elif first_line == "russian":
                return "Копировать из одного параметра в другой параметр"
            elif first_line == "spanish":
                return "Copiar de un parámetro a otro parámetro"
            elif first_line == "chinese":
                return "从一个参数复制到另一个参数"
            elif first_line == "korean":
                return "하나의 파라미터에서 다른 파라미터로 복사"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_str_39(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "List Maker of Values from Excel"
            elif first_line == "deutsch":
                return "Listenmacher für Werte aus Excel"
            elif first_line == "farsi":
                return "ابزار فهرست‌سازی مقادیر از اکسل"
            elif first_line == "russian":
                return "Создатель списка значений из Excel"
            elif first_line == "spanish":
                return "Creador de listas de valores desde Excel"
            elif first_line == "chinese":
                return "从Excel列出值的工具"
            elif first_line == "korean":
                return "Excel에서 값의 목록 생성기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_40(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Batch Parameter Set using Dataset"
            elif first_line == "deutsch":
                return "Stapel-Parameter setzen mit Datensatz"
            elif first_line == "farsi":
                return "تنظیم دسته‌ای پارامتر با استفاده از مجموعه داده"
            elif first_line == "russian":
                return "Пакетная настройка параметров с использованием набора данных"
            elif first_line == "spanish":
                return "Conjunto de parámetros por lotes usando conjunto de datos"
            elif first_line == "chinese":
                return "使用数据集批量设置参数"
            elif first_line == "korean":
                return "데이터셋을 사용한 배치 파라미터 설정"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_41(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "ID Generator"
            elif first_line == "deutsch":
                return "ID-Generator"
            elif first_line == "farsi":
                return "تولید کننده شناسه"
            elif first_line == "russian":
                return "Генератор ID"
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
    
def tool_str_42(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter Value Editor"
            elif first_line == "deutsch":
                return "Parameterwert-Editor"
            elif first_line == "farsi":
                return "ویرایشگر مقدار پارامتر"
            elif first_line == "russian":
                return "Редактор значения параметра"
            elif first_line == "spanish":
                return "Editor de valor de parámetro"
            elif first_line == "chinese":
                return "参数值编辑器"
            elif first_line == "korean":
                return "파라미터 값 편집기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_str_43(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter Value Editor for Special Characters"
            elif first_line == "deutsch":
                return "Parameterwert-Editor für Sonderzeichen"
            elif first_line == "farsi":
                return "ویرایشگر مقدار پارامتر برای کاراکترهای خاص"
            elif first_line == "russian":
                return "Редактор значения параметра для специальных символов"
            elif first_line == "spanish":
                return "Editor de valor de parámetro para caracteres especiales"
            elif first_line == "chinese":
                return "特殊字符参数值编辑器"
            elif first_line == "korean":
                return "특수 문자 매개변수 값 편집기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_44(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Value of Parameter for Selected Elements"
            elif first_line == "deutsch":
                return "Wert des Parameters für ausgewählte Elemente"
            elif first_line == "farsi":
                return "مقدار پارامتر برای المان‌های انتخاب شده"
            elif first_line == "russian":
                return "Значение параметра для выбранных элементов"
            elif first_line == "spanish":
                return "Valor del parámetro para los elementos seleccionados"
            elif first_line == "chinese":
                return "所选元素的参数值"
            elif first_line == "korean":
                return "선택된 요소의 파라미터 값"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_str_45(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Desired Character in Value of Parameter for Selected Elements"
            elif first_line == "deutsch":
                return "Gewünschtes Zeichen im Parameterwert für ausgewählte Elemente"
            elif first_line == "farsi":
                return "کاراکتر مورد نظر در مقدار پارامتر برای المان‌های انتخاب شده"
            elif first_line == "russian":
                return "Желаемый символ в значении параметра для выбранных элементов"
            elif first_line == "spanish":
                return "Carácter deseado en el valor del parámetro para los elementos seleccionados"
            elif first_line == "chinese":
                return "所选元素的参数值中的所需字符"
            elif first_line == "korean":
                return "선택된 요소의 파라미터 값에서 원하는 문자"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_46(file_path):
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
                return "信息"
            elif first_line == "korean":
                return "정보"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_47(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Load and Select Elements"
            elif first_line == "deutsch":
                return "Elemente laden und auswählen"
            elif first_line == "farsi":
                return "بارگذاری و انتخاب المان‌ها"
            elif first_line == "russian":
                return "Загрузить и выбрать элементы"
            elif first_line == "spanish":
                return "Cargar y seleccionar elementos"
            elif first_line == "chinese":
                return "加载并选择元素"
            elif first_line == "korean":
                return "요소 로드 및 선택"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_48(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Load and Reduce Selected Elements"
            elif first_line == "deutsch":
                return "Elemente laden und reduzieren"
            elif first_line == "farsi":
                return "بارگذاری و کاهش المان‌های انتخاب شده"
            elif first_line == "russian":
                return "Загрузить и уменьшить выбранные элементы"
            elif first_line == "spanish":
                return "Cargar y reducir los elementos seleccionados"
            elif first_line == "chinese":
                return "加载并减少选定的元素"
            elif first_line == "korean":
                return "선택된 요소 로드 및 축소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_49(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Import Selection from XML"
            elif first_line == "deutsch":
                return "Auswahl aus XML importieren"
            elif first_line == "farsi":
                return "XML وارد کردن انتخاب از "
            elif first_line == "russian":
                return "Импорт выбора из XML"
            elif first_line == "spanish":
                return "Importar selección desde XML"
            elif first_line == "chinese":
                return "从 XML 导入选择"
            elif first_line == "korean":
                return "XML에서 선택 가져오기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_50(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Import HTML"
            elif first_line == "deutsch":
                return "HTML importieren"
            elif first_line == "farsi":
                return "HTML وارد کردن از "
            elif first_line == "russian":
                return "Импорт HTML"
            elif first_line == "spanish":
                return "Importar HTML"
            elif first_line == "chinese":
                return "导入 HTML"
            elif first_line == "korean":
                return "HTML 가져오기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_str_51(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Export Selection to XML"
            elif first_line == "deutsch":
                return "Auswahl in XML exportieren"
            elif first_line == "farsi":
                return "XML اکسپورت کردن انتخاب به "
            elif first_line == "russian":
                return "Экспорт выбора в XML"
            elif first_line == "spanish":
                return "Exportar selección a XML"
            elif first_line == "chinese":
                return "导出选择到 XML"
            elif first_line == "korean":
                return "선택 항목을 XML로 내보내기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_str_52(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Export Selection to CSV"
            elif first_line == "deutsch":
                return "Auswahl in CSV exportieren"
            elif first_line == "farsi":
                return "CSV اکسپورت کردن انتخاب به "
            elif first_line == "russian":
                return "Экспорт выбора в CSV"
            elif first_line == "spanish":
                return "Exportar selección a CSV"
            elif first_line == "chinese":
                return "导出选择到 CSV"
            elif first_line == "korean":
                return "선택 항목을 CSV로 내보내기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"






    
#tools name 
def tool_tip_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Element ID]\nRetrieve the unique identifier for each element in the project."
            elif first_line == "deutsch":
                return "[Element-ID]\nErmitteln Sie die eindeutige Kennung für jedes Element im Projekt."
            elif first_line == "farsi":
                return "[شناسه المان]\nشناسه منحصر به فرد هر المان در پروژه را بازیابی کنید"
            elif first_line == "russian":
                return "[ID элемента]\nПолучите уникальный идентификатор для каждого элемента в проекте."
            elif first_line == "spanish":
                return "[ID del elemento]\nRecupere el identificador único de cada elemento en el proyecto."
            elif first_line == "chinese":
                return "[元素ID]\n检索项目中每个元素的唯一标识符。"
            elif first_line == "korean":
                return "[요소 ID]\n프로젝트에서 각 요소의 고유 식별자를 검색합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Creator Finder]\nRetrieve the creator, owner, and last modified user for each element in the project."
            elif first_line == "deutsch":
                return "[Erstellerfinder]\nErmitteln Sie den Ersteller, Besitzer und den letzten Bearbeiter für jedes Element im Projekt."
            elif first_line == "farsi":
                return "[خالق المان]\nخالق، مالک و آخرین کاربری که المان را تغییر داده است را بازیابی کنید"
            elif first_line == "russian":
                return "[Поиск Создателя]\nПолучите информацию о создателе, владельце и последнем пользователе, изменившем каждый элемент в проекте."
            elif first_line == "spanish":
                return "[Buscador de Creadores]\nRecupere el creador, propietario y el último usuario que modificó cada elemento en el proyecto."
            elif first_line == "chinese":
                return "[创建者查找器]\n检索项目中每个元素的创建者、所有者和最后修改用户。"
            elif first_line == "korean":
                return "[작성자 찾기]\n프로젝트에서 각 요소의 작성자, 소유자 및 마지막 수정 사용자를 검색합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Active View]\nRetrieve and display details of the currently active view in the project."
            elif first_line == "deutsch":
                return "[Aktive Ansicht]\nErmitteln und zeigen Sie Details der aktuell aktiven Ansicht im Projekt an."
            elif first_line == "farsi":
                return "[نمای فعال]\nجزئیات نمای فعال فعلی در پروژه را بازیابی و نمایش دهید"
            elif first_line == "russian":
                return "[Активный вид]\nПолучите и отобразите детали текущего активного вида в проекте."
            elif first_line == "spanish":
                return "[Vista Activa]\nRecupere y muestre detalles de la vista activa actual en el proyecto."
            elif first_line == "chinese":
                return "[活动视图]\n检索并显示项目中当前活动视图的详细信息。"
            elif first_line == "korean":
                return "[활성 뷰]\n프로젝트에서 현재 활성 뷰의 세부 정보를 검색하고 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Hierarchy]\nFilter elements based on various criteria such as view, level, category, family, type, parameter, value, owner, modifier, and creator."
            elif first_line == "deutsch":
                return "[Hierarchie]\nFiltern Sie Elemente basierend auf verschiedenen Kriterien wie Ansicht, Ebene, Kategorie, Familie, Typ, Parameter, Wert, Besitzer, Bearbeiter und Ersteller."
            elif first_line == "farsi":
                return "[سلسله مراتب]\nالمان ها را بر اساس معیارهای مختلف مانند نمای، سطح، دسته‌بندی، خانواده، نوع، پارامتر، مقدار، مالک، ویرایشگر و خالق فیلتر کنید"
            elif first_line == "russian":
                return "[Иерархия]\nФильтруйте элементы на основе различных критериев, таких как вид, уровень, категория, семейство, тип, параметр, значение, владелец, модификатор и создатель."
            elif first_line == "spanish":
                return "[Jerarquía]\nFiltre elementos según varios criterios, como vista, nivel, categoría, familia, tipo, parámetro, valor, propietario, modificador y creador."
            elif first_line == "chinese":
                return "[层次结构]\n根据视图、标高、类别、族、类型、参数、值、所有者、修改者和创建者等多种条件过滤元素。"
            elif first_line == "korean":
                return "[계층 구조]\n뷰, 레벨, 카테고리, 패밀리, 유형, 매개변수, 값, 소유자, 수정자 및 작성자와 같은 다양한 기준에 따라 요소를 필터링합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_5(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[DUDUL]\nFilter elements based on various criteria such as view, level, category, family, type, parameter, value, string in value, number in value, owner, modifier, and creator."
            elif first_line == "deutsch":
                return "[DUDUL]\nFiltern Sie Elemente basierend auf verschiedenen Kriterien wie Ansicht, Ebene, Kategorie, Familie, Typ, Parameter, Wert, Zeichenkette im Wert, Zahl im Wert, Besitzer, Bearbeiter und Ersteller."
            elif first_line == "farsi":
                return "[دودول]\nالمان ها را بر اساس معیارهای مختلف مانند نمای، سطح، دسته‌بندی، خانواده، نوع، پارامتر، مقدار، رشته در مقدار، عدد در مقدار، مالک، ویرایشگر و خالق فیلتر کنید"
            elif first_line == "russian":
                return "[DUDUL]\nФильтруйте элементы на основе различных критериев, таких как вид, уровень, категория, семейство, тип, параметр, значение, строка в значении, число в значении, владелец, модификатор и создатель."
            elif first_line == "spanish":
                return "[DUDUL]\nFiltre elementos según varios criterios, como vista, nivel, categoría, familia, tipo, parámetro, valor, cadena en el valor, número en el valor, propietario, modificador y creador."
            elif first_line == "chinese":
                return "[DUDUL]\n根据视图、标高、类别、族、类型、参数、值、值中的字符串、值中的数字、所有者、修改者和创建者等多种条件过滤元素。"
            elif first_line == "korean":
                return "[DUDUL]\n뷰, 레벨, 카테고리, 패밀리, 유형, 매개변수, 값, 값의 문자열, 값의 숫자, 소유자, 수정자 및 작성자와 같은 다양한 기준에 따라 요소를 필터링합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_tip_6(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Type]\nFilter elements based on their type, allowing for precise selection and organization of elements in the project."
            elif first_line == "deutsch":
                return "[Typ]\nFiltern Sie Elemente basierend auf ihrem Typ, um eine präzise Auswahl und Organisation der Elemente im Projekt zu ermöglichen."
            elif first_line == "farsi":
                return "[نوع]\nالمان ها را بر اساس نوع آنها فیلتر کنید تا امکان انتخاب دقیق و سازمان‌دهی المان‌ها در پروژه فراهم شود"
            elif first_line == "russian":
                return "[Тип]\nФильтруйте элементы по их типу для точного выбора и организации элементов в проекте."
            elif first_line == "spanish":
                return "[Tipo]\nFiltre elementos según su tipo para permitir una selección y organización precisa de los elementos en el proyecto."
            elif first_line == "chinese":
                return "[类型]\n根据元素的类型进行过滤，以便在项目中进行精确的选择和组织。"
            elif first_line == "korean":
                return "[유형]\n요소의 유형에 따라 필터링하여 프로젝트에서 정확한 선택 및 구성을 가능하게 합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Select by Search for Value of Instance Parameters]\nSearch and select elements based on specific instance parameter values, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Nach Wert von Instanzparametern suchen und auswählen]\nSuchen und wählen Sie Elemente basierend auf spezifischen Instanzparameterwerten aus und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[انتخاب با جستجو برای مقدار پارامترهای نمونه]\nبر اساس مقادیر خاص پارامترهای نمونه، المان‌ها را جستجو و انتخاب کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Выбор по поиску значения параметров экземпляра]\nИщите и выбирайте элементы на основе конкретных значений параметров экземпляра и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Seleccionar por búsqueda del valor de parámetros de instancia]\nBusque y seleccione elementos basados en valores específicos de parámetros de instancia y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[按实例参数值搜索选择]\n根据特定的实例参数值搜索并选择元素，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[인스턴스 매개변수 값을 검색하여 선택]\n특정 인스턴스 매개변수 값을 기반으로 요소를 검색 및 선택하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Select based on Existence of Parameter Values]\nFilter and select elements based on the existence of specific parameter values, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Auswahl basierend auf Existenz von Parameterwerten]\nFiltern und wählen Sie Elemente basierend auf der Existenz spezifischer Parameterwerte aus und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[انتخاب بر اساس وجود مقادیر پارامترها]\nبر اساس وجود مقادیر خاص پارامترها، المان‌ها را فیلتر و انتخاب کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Выбор на основе существования значений параметров]\nФильтруйте и выбирайте элементы на основе существования конкретных значений параметров и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Seleccionar basado en la existencia de valores de parámetros]\nFiltre y seleccione elementos basados en la existencia de valores específicos de parámetros y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[基于参数值存在的选择]\n根据特定参数值的存在过滤并选择元素，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[매개변수 값 존재 여부에 따른 선택]\n특정 매개변수 값의 존재 여부에 따라 요소를 필터링 및 선택하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_9(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[All Elements in Selected Categories]\nFilter and select all elements within the specified categories, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Alle Elemente in ausgewählten Kategorien]\nFiltern und wählen Sie alle Elemente in den angegebenen Kategorien aus und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[تمام المان ها در دسته‌بندی های انتخاب‌ شده]\nتمام المان‌ها در دسته‌بندی‌های مشخص‌شده را فیلتر و انتخاب کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Все элементы в выбранных категориях]\nФильтруйте и выбирайте все элементы в указанных категориях и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Todos los elementos en categorías seleccionadas]\nFiltre y seleccione todos los elementos en las categorías especificadas y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[所选类别中的所有元素]\n过滤并选择指定类别中的所有元素，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[선택한 카테고리의 모든 요소]\n지정된 카테고리의 모든 요소를 필터링 및 선택하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_10(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[All Elements in Selected Views]\nFilter and select all elements within the specified views, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Alle Elemente in ausgewählten Ansichten]\nFiltern und wählen Sie alle Elemente in den angegebenen Ansichten aus und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[تمام المان ها در نماهای انتخاب‌ شده]\nتمام المان‌ها در نماهای مشخص‌شده را فیلتر و انتخاب کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Все элементы в выбранных видах]\nФильтруйте и выбирайте все элементы в указанных видах и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Todos los elementos en vistas seleccionadas]\nFiltre y seleccione todos los elementos en las vistas especificadas y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[所选视图中的所有元素]\n过滤并选择指定视图中的所有元素，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[선택한 뷰의 모든 요소]\n지정된 뷰의 모든 요소를 필터링 및 선택하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[All Elements on Selected Levels]\nFilter and select all elements located on the specified levels, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Alle Elemente auf ausgewählten Ebenen]\nFiltern und wählen Sie alle Elemente auf den angegebenen Ebenen aus und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[تمام المان ها در سطوح انتخاب‌ شده]\nتمام المان‌ها در سطوح مشخص‌شده را فیلتر و انتخاب کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Все элементы на выбранных уровнях]\nФильтруйте и выбирайте все элементы на указанных уровнях и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Todos los elementos en niveles seleccionados]\nFiltre y seleccione todos los elementos en los niveles especificados y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[所选楼层上的所有元素]\n过滤并选择指定楼层上的所有元素，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[선택한 레벨의 모든 요소]\n지정된 레벨의 모든 요소를 필터링 및 선택하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_12(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Ownership of Elements]\nFilter and select elements based on their ownership, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Eigentum von Elementen]\nFiltern und wählen Sie Elemente basierend auf ihrem Eigentum aus und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[مالکیت المان ها]\nبر اساس مالکیت المان‌ها، آن‌ها را فیلتر و انتخاب کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Владение элементами]\nФильтруйте и выбирайте элементы на основе их владения и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Propiedad de elementos]\nFiltre y seleccione elementos basados en su propiedad y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[元素的所有权]\n根据元素的所有权进行过滤和选择，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[요소의 소유권]\n요소의 소유권에 따라 필터링 및 선택하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Unbound Rooms]\nFilter and select rooms that are not bound to any elements, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Ungebundene Räume]\nFiltern und wählen Sie Räume aus, die an keine Elemente gebunden sind, und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[اتاق‌های محدودنشده]\nاتاق‌هایی که به هیچ المانی محدود نشده‌اند را فیلتر و انتخاب کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Несвязанные комнаты]\nФильтруйте и выбирайте комнаты, не связанные с какими-либо элементами, и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Habitaciones no vinculadas]\nFiltre y seleccione habitaciones que no estén vinculadas a ningún elemento y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[未绑定的房间]\n过滤并选择未绑定到任何元素的房间，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[바인딩되지 않은 방]\n어떤 요소에도 바인딩되지 않은 방을 필터링 및 선택하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_14(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Mirrored Doors]\nFilter and select doors that are mirrored, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Symmetrische Türen]\nFiltern und wählen Sie Türen aus, die gespiegelt sind, und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[درهای متقارن]\nدرهایی که متقارن هستند را فیلتر و انتخاب کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Симметричные двери]\nФильтруйте и выбирайте двери, которые являются симметричными, и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Puertas simétricas]\nFiltre y seleccione puertas que estén simétricas y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[对称门]\n过滤并选择对称的门，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[대칭적인 문]\n대칭적인 문을 필터링 및 선택하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[IDs from Excel]\nImport element IDs from an Excel file, filter elements based on these IDs, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[IDs aus Excel]\nImportieren Sie Element-IDs aus einer Excel-Datei, filtern Sie Elemente basierend auf diesen IDs und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[شناسه‌ها از اکسل]\nشناسه‌های المان‌ها را از یک فایل اکسل وارد کنید، بر اساس این شناسه‌ها المان‌ها را فیلتر کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Идентификаторы из Excel]\nИмпортируйте идентификаторы элементов из файла Excel, фильтруйте элементы на основе этих идентификаторов и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Identificadores de Excel]\nImporte identificadores de elementos desde un archivo de Excel, filtre elementos basados en estos identificadores y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[来自Excel的ID]\n从Excel文件中导入元素ID，根据这些ID过滤元素，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[Excel에서 ID]\nExcel 파일에서 요소 ID를 가져오고, 이러한 ID를 기반으로 요소를 필터링한 후 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_16(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Reduce Selection by ID]\nReduce the current selection by removing elements with specified IDs, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Auswahl nach ID reduzieren]\nReduzieren Sie die aktuelle Auswahl, indem Sie Elemente mit bestimmten IDs entfernen, und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[کاهش انتخاب بر اساس شناسه]\nانتخاب فعلی را با حذف المان‌های دارای شناسه‌های مشخص کاهش دهید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Уменьшить выбор по ID]\nУменьшите текущий выбор, удалив элементы с указанными идентификаторами, и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Reducir selección por ID]\nReduzca la selección actual eliminando elementos con identificadores específicos y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[按ID减少选择]\n通过移除指定ID的元素来减少当前选择，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[ID로 선택 축소]\n지정된 ID를 가진 요소를 제거하여 현재 선택을 축소하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_tip_17(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Reduce Selection by OST Categories]\nReduce the current selection by removing elements in specified OST categories, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Auswahl nach OST-Kategorien reduzieren]\nReduzieren Sie die aktuelle Auswahl, indem Sie Elemente in bestimmten OST-Kategorien entfernen, und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[کاهش انتخاب بر اساس دسته‌بندی‌های OST]\nانتخاب فعلی را با حذف المان‌های در دسته‌بندی‌های مشخص‌شده OST کاهش دهید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Уменьшить выбор по категориям OST]\nУменьшите текущий выбор, удалив элементы в указанных категориях OST, и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Reducir selección por categorías OST]\nReduzca la selección actual eliminando elementos en categorías OST específicas y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[按OST类别减少选择]\n通过移除指定OST类别中的元素来减少当前选择，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[OST 카테고리로 선택 축소]\n지정된 OST 카테고리의 요소를 제거하여 현재 선택을 축소하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Reduce Selection by Searching Value of Instance Parameters]\nReduce the current selection by removing elements with specified instance parameter values, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Auswahl durch Suchen des Werts von Instanzparametern reduzieren]\nReduzieren Sie die aktuelle Auswahl, indem Sie Elemente mit bestimmten Instanzparameterwerten entfernen, und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[کاهش انتخاب با جستجوی مقدار پارامترهای نمونه]\nانتخاب فعلی را با حذف المان‌های دارای مقادیر مشخص پارامترهای نمونه کاهش دهید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Уменьшить выбор по поиску значения параметров экземпляра]\nУменьшите текущий выбор, удалив элементы с указанными значениями параметров экземпляра, и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Reducir selección buscando el valor de parámetros de instancia]\nReduzca la selección actual eliminando elementos con valores específicos de parámetros de instancia y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[通过搜索实例参数值减少选择]\n通过移除具有指定实例参数值的元素来减少当前选择，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[인스턴스 매개변수 값을 검색하여 선택 축소]\n지정된 인스턴스 매개변수 값을 가진 요소를 제거하여 현재 선택을 축소하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_19(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Reduce Selection by Existence of Parameter Values]\nReduce the current selection by removing elements based on the existence or absence of specified parameter values, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Auswahl durch Existenz von Parameterwerten reduzieren]\nReduzieren Sie die aktuelle Auswahl, indem Sie Elemente basierend auf der Existenz oder Abwesenheit bestimmter Parameterwerte entfernen, und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[کاهش انتخاب بر اساس وجود مقادیر پارامترها]\nانتخاب فعلی را با حذف المان‌ها بر اساس وجود یا عدم وجود مقادیر مشخص پارامترها کاهش دهید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Уменьшить выбор по существованию значений параметров]\nУменьшите текущий выбор, удалив элементы на основе наличия или отсутствия указанных значений параметров, и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Reducir selección por existencia de valores de parámetros]\nReduzca la selección actual eliminando elementos basados en la existencia o ausencia de valores de parámetros específicos y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[根据参数值的存在减少选择]\n通过移除具有或不具有指定参数值的元素来减少当前选择，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[매개변수 값 존재 여부에 따른 선택 축소]\n지정된 매개변수 값의 존재 여부에 따라 요소를 제거하여 현재 선택을 축소하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_20(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Delete Elements by ID]\nDelete elements based on their specified IDs, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Elemente nach ID löschen]\nLöschen Sie Elemente basierend auf ihren angegebenen IDs und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[حذف المان ها بر اساس شناسه]\nبر اساس شناسه‌های مشخص‌شده، المان‌ها را حذف کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Удалить элементы по ID]\nУдалите элементы на основе их указанных идентификаторов и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Eliminar elementos por ID]\nElimine elementos basados en sus identificadores especificados y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[按ID删除元素]\n根据指定的ID删除元素，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[ID로 요소 삭제]\n지정된 ID를 기반으로 요소를 삭제하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Delete Elements by IDs from Excel]\nImport element IDs from an Excel file, delete elements based on these IDs, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Elemente nach IDs aus Excel löschen]\nImportieren Sie Element-IDs aus einer Excel-Datei, löschen Sie Elemente basierend auf diesen IDs und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[حذف المان ها بر اساس شناسه‌ها از اکسل]\nشناسه‌های المان‌ها را از یک فایل اکسل وارد کنید، بر اساس این شناسه‌ها المان‌ها را حذف کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Удалить элементы по ID из Excel]\nИмпортируйте идентификаторы элементов из файла Excel, удалите элементы на основе этих идентификаторов и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Eliminar elementos por IDs desde Excel]\nImporte identificadores de elementos desde un archivo de Excel, elimine elementos basados en estos identificadores y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[按来自Excel的ID删除元素]\n从Excel文件中导入元素ID，根据这些ID删除元素，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[Excel에서 ID로 요소 삭제]\nExcel 파일에서 요소 ID를 가져오고, 이러한 ID를 기반으로 요소를 삭제한 후 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_22(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Delete Elements by Type Filter]\nFilter elements by category, family, and type, delete elements based on the filter criteria, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Elemente nach Typfilter löschen]\nFiltern Sie Elemente nach Kategorie, Familie und Typ, löschen Sie Elemente basierend auf den Filterkriterien und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[حذف المان ها بر اساس فیلتر نوع]\nالمان‌ها را بر اساس دسته‌بندی، خانواده و نوع فیلتر کنید، بر اساس معیارهای فیلتر المان‌ها را حذف کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Удалить элементы по фильтру типа]\nФильтруйте элементы по категории, семейству и типу, удаляйте элементы на основе критериев фильтра и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Eliminar elementos por filtro de tipo]\nFiltre elementos por categoría, familia y tipo, elimine elementos basados en los criterios del filtro y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[按类型过滤器删除元素]\n按类别、族和类型过滤元素，根据过滤条件删除元素，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[유형 필터로 요소 삭제]\n카테고리, 패밀리 및 유형별로 요소를 필터링하고, 필터 기준에 따라 요소를 삭제한 후 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_23(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Delete All DirectShape Elements]\nCollect and delete all DirectShape elements in the model, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Alle DirectShape-Elemente löschen]\nSammeln und löschen Sie alle DirectShape-Elemente im Modell und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[حذف تمام المان های DirectShape]\nتمام المان‌های DirectShape در مدل را جمع‌آوری و حذف کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Удалить все элементы DirectShape]\nСоберите и удалите все элементы DirectShape в модели и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Eliminar todos los elementos DirectShape]\nRecopile y elimine todos los elementos DirectShape en el modelo y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[删除所有 DirectShape 元素]\n收集并删除模型中的所有 DirectShape 元素，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[모든 DirectShape 요소 삭제]\n모델의 모든 DirectShape 요소를 수집 및 삭제하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_tip_24(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Delete All Elements of OST Category]\nCollect and delete all elements of the selected OST category, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Alle Elemente der OST-Kategorie löschen]\nSammeln und löschen Sie alle Elemente der ausgewählten OST-Kategorie und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[حذف تمام المان های دسته‌بندی‌های OST]\nتمام المان‌های دسته‌بندی‌های انتخاب‌شده OST را جمع‌آوری و حذف کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Удалить все элементы категории OST]\nСоберите и удалите все элементы выбранной категории OST и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Eliminar todos los elementos de la categoría OST]\nRecopile y elimine todos los elementos de la categoría OST seleccionada y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[删除OST类别的所有元素]\n收集并删除所选OST类别的所有元素，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[OST 카테고리의 모든 요소 삭제]\n선택한 OST 카테고리의 모든 요소를 수집 및 삭제하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_25(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Search Values of Parameters by Filter]\nFilter elements by category, family, and type, display parameter values for selected elements, and show the results in a report tab."
            elif first_line == "deutsch":
                return "[Werte von Parametern nach Filter suchen]\nFiltern Sie Elemente nach Kategorie, Familie und Typ, zeigen Sie Parameterwerte für ausgewählte Elemente an und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[جستجوی مقادیر پارامترها بر اساس فیلتر]\nالمان‌ها را بر اساس دسته‌بندی، خانواده و نوع فیلتر کنید، مقادیر پارامترها را برای المان‌های انتخاب‌شده نمایش دهید و نتایج را در یک تب گزارش نشان دهید"
            elif first_line == "russian":
                return "[Поиск значений параметров по фильтру]\nФильтруйте элементы по категории, семейству и типу, отображайте значения параметров для выбранных элементов и показывайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Buscar valores de parámetros por filtro]\nFiltre elementos por categoría, familia y tipo, muestre los valores de los parámetros para los elementos seleccionados y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[按筛选器搜索参数值]\n按类别、族和类型过滤元素，显示所选元素的参数值，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[필터로 매개변수 값 검색]\n카테고리, 패밀리 및 유형별로 요소를 필터링하고, 선택한 요소의 매개변수 값을 표시한 후 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_tip_26(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Search Values of Parameters by Filter for Family Document]\nFilter elements by category, family, and type, display parameter values for selected elements in family documents, and show the results in a report tab."
            elif first_line == "deutsch":
                return "[Werte von Parametern nach Filter für Familien-Dokument suchen]\nFiltern Sie Elemente nach Kategorie, Familie und Typ, zeigen Sie Parameterwerte für ausgewählte Elemente in Familien-Dokumenten an und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[جستجوی مقادیر پارامترها بر اساس فیلتر برای سند خانواده]\nالمان‌ها را بر اساس دسته‌بندی، خانواده و نوع فیلتر کنید، مقادیر پارامترها را برای المان‌های انتخاب‌شده در اسناد خانواده نمایش دهید و نتایج را در یک تب گزارش نشان دهید"
            elif first_line == "russian":
                return "[Поиск значений параметров по фильтру для семейного документа]\nФильтруйте элементы по категории, семейству и типу, отображайте значения параметров для выбранных элементов в семейных документах и показывайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Buscar valores de parámetros por filtro para documento de familia]\nFiltre elementos por categoría, familia y tipo, muestre los valores de los parámetros para los elementos seleccionados en documentos de familia y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[按筛选器搜索家族文档的参数值]\n按类别、族和类型过滤元素，显示家族文档中所选元素的参数值，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[가족 문서에 대한 필터로 매개변수 값 검색]\n카테고리, 패밀리 및 유형별로 요소를 필터링하고, 가족 문서에서 선택한 요소의 매개변수 값을 표시한 후 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_27(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Snipe Parameter Value]\nSelect and display parameter values (both instance and type) for a specific element, and show the results in a report tab."
            elif first_line == "deutsch":
                return "[Parameterwert anvisieren]\nWählen Sie Parameterwerte (sowohl Instanz als auch Typ) für ein bestimmtes Element aus und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[اسنایپ مقدارپارامتر]\nمقادیر پارامترها (هم نمونه و هم نوع) را برای یک المان خاص انتخاب و نمایش دهید و نتایج را در یک تب گزارش نشان دهید"
            elif first_line == "russian":
                return "[Нацеливание на значение параметра]\nВыберите и отобразите значения параметров (как экземпляра, так и типа) для конкретного элемента и покажите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Apuntar al valor del parámetro]\nSeleccione y muestre los valores de los parámetros (tanto de instancia como de tipo) para un elemento específico y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[瞄准参数值]\n选择并显示特定元素的参数值（实例和类型），并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[파라미터 값 조준]\n특정 요소에 대한 파라미터 값(인스턴스 및 유형)을 선택 및 표시하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_28(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Snipe Parameter Value for Family Document]\nSelect and display parameter values (both instance and type) for a specific element in a family document, and show the results in a report tab."
            elif first_line == "deutsch":
                return "[Parameterwert für Familien-Dokument anvisieren]\nWählen Sie Parameterwerte (sowohl Instanz als auch Typ) für ein bestimmtes Element in einem Familien-Dokument aus und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[اسنایپ مقدار پارامتر برای سند خانواده]\nمقادیر پارامترها (هم نمونه و هم نوع) را برای یک المان خاص در سند خانواده انتخاب و نمایش دهید و نتایج را در یک تب گزارش نشان دهید"
            elif first_line == "russian":
                return "[Нацеливание на значение параметра для семейного документа]\nВыберите и отобразите значения параметров (как экземпляра, так и типа) для конкретного элемента в семейном документе и покажите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Apuntar al valor del parámetro para documento de familia]\nSeleccione y muestre los valores de los parámetros (tanto de instancia como de tipo) para un elemento específico en un documento de familia y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[针对家庭文档瞄准参数值]\n选择并显示家庭文档中特定元素的参数值（实例和类型），并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[가족 문서의 파라미터 값 조준]\n가족 문서에서 특정 요소에 대한 파라미터 값(인스턴스 및 유형)을 선택 및 표시하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_29(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Dictionary]\nRetrieve instance and type parameters for a selected element, display parameter details (name, type, value, etc.), and show the results in a report tab."
            elif first_line == "deutsch":
                return "[Wörterbuch]\nRufen Sie Instanz- und Typ-Parameter für ein ausgewähltes Element ab, zeigen Sie Parameterdetails (Name, Typ, Wert usw.) an und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[دیکشنری]\nپارامترهای نمونه و نوع را برای یک المان انتخاب‌شده بازیابی کنید، جزئیات پارامترها (نام، نوع، مقدار و غیره) را نمایش دهید و نتایج را در یک تب گزارش نشان دهید"
            elif first_line == "russian":
                return "[Словарь]\nПолучите параметры экземпляра и типа для выбранного элемента, отобразите детали параметров (имя, тип, значение и т.д.) и покажите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Diccionario]\nRecupere los parámetros de instancia y tipo para un elemento seleccionado, muestre los detalles del parámetro (nombre, tipo, valor, etc.) y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[字典]\n检索所选元素的实例和类型参数，显示参数详细信息（名称、类型、值等），并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[사전]\n선택한 요소에 대한 인스턴스 및 유형 매개변수를 검색하고, 매개변수 세부 정보(이름, 유형, 값 등)를 표시한 후 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_30(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Check Existence of Parameter Values]\nCheck parameter values for all elements, elements with values, or elements without values, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Existenz von Parameterwerten überprüfen]\nÜberprüfen Sie Parameterwerte für alle Elemente, Elemente mit Werten oder Elemente ohne Werte und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[بررسی وجود مقادیر پارامترها]\nمقادیر پارامترها را برای تمام المان‌ها، المان‌های دارای مقدار یا المان‌های بدون مقدار بررسی کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Проверить наличие значений параметров]\nПроверьте значения параметров для всех элементов, элементов со значениями или элементов без значений и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Comprobar existencia de valores de parámetros]\nCompruebe los valores de los parámetros para todos los elementos, elementos con valores o elementos sin valores y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[检查参数值的存在性]\n检查所有元素、有值的元素或无值的元素的参数值，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[매개변수 값 존재 여부 확인]\n모든 요소, 값이 있는 요소 또는 값이 없는 요소에 대한 매개변수 값을 확인하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_tip_31(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Check Parameter Against Category]\nCheck if parameters exist in selected categories, display results in a grid view, save results to Excel, and load data from CSV or SJD files."
            elif first_line == "deutsch":
                return "[Parameter mit Kategorie abgleichen]\nÜberprüfen Sie, ob Parameter in ausgewählten Kategorien vorhanden sind, zeigen Sie die Ergebnisse in einer Rasteransicht an, speichern Sie die Ergebnisse in Excel und laden Sie Daten aus CSV- oder SJD-Dateien."
            elif first_line == "farsi":
                return "[بررسی پارامتر با دسته بندی]\nبررسی کنید که آیا پارامترها در دسته‌بندی‌های انتخاب‌شده وجود دارند، نتایج را در یک نمای جدولی نمایش دهید، نتایج را در اکسل ذخیره کنید و داده‌ها را از فایل‌های CSV یا SJD بارگیری کنید"
            elif first_line == "russian":
                return "[Проверить параметр с категорией]\nПроверьте, существуют ли параметры в выбранных категориях, отобразите результаты в виде сетки, сохраните результаты в Excel и загрузите данные из файлов CSV или SJD."
            elif first_line == "spanish":
                return "[Comprobar parámetro contra categoría]\nCompruebe si los parámetros existen en las categorías seleccionadas, muestre los resultados en una vista de cuadrícula, guarde los resultados en Excel y cargue datos desde archivos CSV o SJD."
            elif first_line == "chinese":
                return "[检查参数与类别]\n检查参数是否存在于所选类别中，在网格视图中显示结果，将结果保存到Excel，并从CSV或SJD文件加载数据。"
            elif first_line == "korean":
                return "[카테고리와 매개변수 확인]\n선택한 카테고리에 매개변수가 존재하는지 확인하고, 결과를 그리드 뷰로 표시하고, 결과를 Excel에 저장하고, CSV 또는 SJD 파일에서 데이터를 로드합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_32(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Delete Parameter Completely from Model]\nDelete parameters from specific elements, all elements in a category, or all elements in the model, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Parameter vollständig aus dem Modell löschen]\nLöschen Sie Parameter von bestimmten Elementen, allen Elementen in einer Kategorie oder allen Elementen im Modell und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[حذف کامل پارامتر از مدل]\nپارامترها را از المان‌های خاص، تمام المان‌های یک دسته‌بندی یا تمام المان‌های مدل حذف کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Полностью удалить параметр из модели]\nУдалите параметры из конкретных элементов, всех элементов в категории или всех элементов в модели и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Eliminar completamente el parámetro del modelo]\nElimine parámetros de elementos específicos, todos los elementos en una categoría o todos los elementos en el modelo y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[完全从模型中删除参数]\n从特定元素、类别中的所有元素或模型中的所有元素中删除参数，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[모델에서 파라미터 완전히 삭제]\n특정 요소, 카테고리의 모든 요소 또는 모델의 모든 요소에서 파라미터를 삭제하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_33(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Search for Value of Instance Parameters]\nSearch for specific instance parameter values across predefined categories and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Nach Wert von Instanzparametern suchen]\nSuchen Sie nach spezifischen Instanzparameterwerten in vordefinierten Kategorien und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[جستجوی مقدار پارامترهای نمونه]\nمقادیر خاص پارامترهای نمونه را در دسته‌بندی‌های از پیش تعریف‌شده جستجو کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Поиск значения параметров экземпляра]\nИщите конкретные значения параметров экземпляра в предопределенных категориях и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Buscar el valor de los parámetros de instancia]\nBusque valores específicos de parámetros de instancia en categorías predefinidas y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[搜索实例参数的值]\n在预定义类别中搜索特定实例参数值，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[인스턴스 매개변수 값 검색]\n미리 정의된 카테고리에서 특정 인스턴스 매개변수 값을 검색하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_34(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Search for Any Value]\nSearch for any value of a specified parameter in selected elements and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Nach beliebigem Wert suchen]\nSuchen Sie nach einem beliebigen Wert eines bestimmten Parameters in ausgewählten Elementen und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[جستجو برای هر مقدار]\nهر مقدار از یک پارامتر مشخص را در المان‌های انتخاب‌شده جستجو کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Поиск любого значения]\nИщите любое значение указанного параметра в выбранных элементах и отображайте результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Buscar cualquier valor]\nBusque cualquier valor de un parámetro especificado en los elementos seleccionados y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[搜索任何值]\n在选定元素中搜索指定参数的任意值，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[모든 값 검색]\n선택한 요소에서 지정된 매개변수의 모든 값을 검색하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_35(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Pair Comparer]\nCompare instance and type parameters of two elements or views and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Paar-Vergleicher]\nVergleichen Sie Instanz- und Typ-Parameter von zwei Elementen oder Ansichten und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[جفت مقایسه کننده]\nپارامترهای نمونه و نوع دو المان یا نما را مقایسه کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Сравнение пар]\nСравните параметры экземпляра и типа двух элементов или видов и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Comparador de pares]\nCompare los parámetros de instancia y tipo de dos elementos o vistas y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[对比器]\n比较两个元素或视图的实例和类型参数，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[쌍 비교기]\n두 요소 또는 뷰의 인스턴스 및 유형 매개변수를 비교하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_tip_36(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Comparer of Multiple Elements]\nCompare parameters across multiple elements and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Vergleicher mehrerer Elemente]\nVergleichen Sie Parameter über mehrere Elemente hinweg und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[مقایسه کننده چندین المان]\nپارامترها را در چندین المان مقایسه کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Сравнение нескольких элементов]\nСравните параметры нескольких элементов и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Comparador de múltiples elementos]\nCompare parámetros entre varios elementos y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[多元素对比器]\n比较多个元素的参数，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[다중 요소 비교기]\n여러 요소 간의 매개변수를 비교하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_37(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Same Value for All Selected Elements]\nSet the same parameter value for all selected elements and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Gleicher Wert für alle ausgewählten Elemente]\nSetzen Sie den gleichen Parameterwert für alle ausgewählten Elemente und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[مقدار یکسان برای تمام المان‌های انتخاب شده]\nمقدار یکسان پارامتر را برای تمام المان‌های انتخاب‌شده تنظیم کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Одинаковое значение для всех выбранных элементов]\nУстановите одинаковое значение параметра для всех выбранных элементов и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Mismo valor para todos los elementos seleccionados]\nEstablezca el mismo valor de parámetro para todos los elementos seleccionados y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[所有选定元素的相同值]\n为所有选定元素设置相同的参数值，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[선택된 모든 요소에 대한 동일한 값]\n선택한 모든 요소에 동일한 매개변수 값을 설정하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_tip_38(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Copy from One Parameter to Another Parameter]\nCopy parameter values from a source parameter to a target parameter and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Kopieren von einem Parameter zu einem anderen Parameter]\nKopieren Sie Parameterwerte von einem Quellparameter zu einem Zielparameter und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[کپی از یک پارامتر به پارامتر دیگر]\nمقادیر پارامترها را از یک پارامتر مبدأ به یک پارامتر مقصد کپی کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Копировать из одного параметра в другой параметр]\nСкопируйте значения параметров из исходного параметра в целевой параметр и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Copiar de un parámetro a otro parámetro]\nCopie los valores de los parámetros de un parámetro de origen a un parámetro de destino y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[从一个参数复制到另一个参数]\n将参数值从源参数复制到目标参数，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[하나의 파라미터에서 다른 파라미터로 복사]\n소스 파라미터에서 대상 파라미터로 파라미터 값을 복사하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_tip_39(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[List Maker of Values from Excel]\nImport data from Excel files, set parameter values based on the imported data, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Listenmacher für Werte aus Excel]\nImportieren Sie Daten aus Excel-Dateien, setzen Sie Parameterwerte basierend auf den importierten Daten und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[ابزار فهرست‌سازی مقادیر از اکسل]\nداده‌ها را از فایل‌های اکسل وارد کنید، مقادیر پارامترها را بر اساس داده‌های وارد‌شده تنظیم کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Создатель списка значений из Excel]\nИмпортируйте данные из файлов Excel, установите значения параметров на основе импортированных данных и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Creador de listas de valores desde Excel]\nImporte datos desde archivos de Excel, establezca valores de parámetros basados en los datos importados y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[从Excel列出值的工具]\n从Excel文件导入数据，根据导入的数据设置参数值，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[Excel에서 값의 목록 생성기]\nExcel 파일에서 데이터를 가져오고, 가져온 데이터를 기반으로 매개변수 값을 설정한 후 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_40(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Batch Parameter Set using Dataset]\nSet parameter values for multiple elements using dataset IDs, convert data types for parameter values, and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Stapel-Parameter setzen mit Datensatz]\nSetzen Sie Parameterwerte für mehrere Elemente mit Datensatz-IDs, konvertieren Sie Datentypen für Parameterwerte und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[تنظیم دسته‌ای پارامتر با استفاده از مجموعه داده]\nمقادیر پارامترها را برای چندین المان با استفاده از شناسه‌های مجموعه داده تنظیم کنید، انواع داده‌ها را برای مقادیر پارامترها تبدیل کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Пакетная настройка параметров с использованием набора данных]\nУстановите значения параметров для нескольких элементов с использованием идентификаторов набора данных, преобразуйте типы данных для значений параметров и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Conjunto de parámetros por lotes usando conjunto de datos]\nEstablezca valores de parámetros para varios elementos utilizando ID de conjuntos de datos, convierta tipos de datos para valores de parámetros y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[使用数据集批量设置参数]\n使用数据集ID为多个元素设置参数值，转换参数值的数据类型，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[데이터셋을 사용한 배치 파라미터 설정]\n데이터셋 ID를 사용하여 여러 요소에 대한 매개변수 값을 설정하고, 매개변수 값의 데이터 유형을 변환한 후 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_41(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[ID Generator]\nGenerate unique IDs for elements using various methods (count, random numbers, strings, etc.) and display the results in a report tab."
            elif first_line == "deutsch":
                return "[ID-Generator]\nGenerieren Sie eindeutige IDs für Elemente mit verschiedenen Methoden (Zählung, Zufallszahlen, Zeichenketten usw.) und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[تولید کننده شناسه]\nشناسه‌های منحصر به فرد برای المان‌ها با استفاده از روش‌های مختلف (شمارش، اعداد تصادفی، رشته‌ها و غیره) تولید کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Генератор ID]\nСгенерируйте уникальные идентификаторы для элементов с использованием различных методов (счетчик, случайные числа, строки и т.д.) и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Generador de ID]\nGenere ID únicos para elementos utilizando varios métodos (contador, números aleatorios, cadenas, etc.) y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[ID生成器]\n使用各种方法（计数、随机数、字符串等）为元素生成唯一ID，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[ID 생성기]\n다양한 방법(카운트, 난수, 문자열 등)을 사용하여 요소에 대한 고유 ID를 생성하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_42(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Parameter Value Editor]\nEdit parameter values using various methods (replace, prefix, suffix, and math operations) and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Parameterwert-Editor]\nBearbeiten Sie Parameterwerte mit verschiedenen Methoden (Ersetzen, Präfix, Suffix und mathematische Operationen) und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[ویرایشگر مقدار پارامتر]\nمقادیر پارامترها را با استفاده از روش‌های مختلف (جایگزینی، پیشوند، پسوند و عملیات ریاضی) ویرایش کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Редактор значения параметра]\nРедактируйте значения параметров с использованием различных методов (замена, префикс, суффикс и математические операции) и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Editor de valor de parámetro]\nEdite valores de parámetros utilizando varios métodos (reemplazar, prefijo, sufijo y operaciones matemáticas) y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[参数值编辑器]\n使用各种方法（替换、前缀、后缀和数学运算）编辑参数值，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[파라미터 값 편집기]\n다양한 방법(교체, 접두사, 접미사 및 수학 연산)을 사용하여 매개변수 값을 편집하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_tip_43(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Parameter Value Editor for Special Characters]\nEdit parameter values for special characters (e.g., replace commas and umlauts) and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Parameterwert-Editor für Sonderzeichen]\nBearbeiten Sie Parameterwerte für Sonderzeichen (z.B. Ersetzen von Kommas und Umlauten) und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[ویرایشگر مقدار پارامتر برای کاراکترهای خاص]\nمقادیر پارامترها را برای کاراکترهای خاص (مانند جایگزینی کاما و اوملاوت) ویرایش کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Редактор значения параметра для специальных символов]\nРедактируйте значения параметров для специальных символов (например, замена запятых и умлаутов) и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Editor de valor de parámetro para caracteres especiales]\nEdite valores de parámetros para caracteres especiales (por ejemplo, reemplazar comas y diéresis) y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[特殊字符参数值编辑器]\n编辑特殊字符的参数值（例如替换逗号和变音符号），并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[특수 문자 매개변수 값 편집기]\n특수 문자(예: 쉼표 및 움라우트 교체)에 대한 매개변수 값을 편집하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_44(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Value of Parameter for Selected Elements]\nDelete parameter values for selected elements based on storage type and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Wert des Parameters für ausgewählte Elemente]\nLöschen Sie Parameterwerte für ausgewählte Elemente basierend auf dem Speichertyp und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[مقدار پارامتر برای المان‌های انتخاب شده]\nمقادیر پارامترها را برای المان‌های انتخاب‌شده بر اساس نوع ذخیره‌سازی حذف کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Значение параметра для выбранных элементов]\nУдалите значения параметров для выбранных элементов на основе типа хранения и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Valor del parámetro para los elementos seleccionados]\nElimine los valores de los parámetros para los elementos seleccionados según el tipo de almacenamiento y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[所选元素的参数值]\n根据存储类型删除所选元素的参数值，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[선택된 요소의 파라미터 값]\n저장 유형에 따라 선택한 요소의 매개변수 값을 삭제하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def tool_tip_45(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Desired Character in Value of Parameter for Selected Elements]\nDelete specific characters from parameter values for selected elements and display the results in a report tab."
            elif first_line == "deutsch":
                return "[Gewünschtes Zeichen im Parameterwert für ausgewählte Elemente]\nLöschen Sie bestimmte Zeichen aus den Parameterwerten für ausgewählte Elemente und zeigen Sie die Ergebnisse in einem Berichtstab an."
            elif first_line == "farsi":
                return "[کاراکتر مورد نظر در مقدار پارامتر برای المان‌های انتخاب شده]\nکاراکترهای خاص را از مقادیر پارامترها برای المان‌های انتخاب‌شده حذف کنید و نتایج را در یک تب گزارش نمایش دهید"
            elif first_line == "russian":
                return "[Желаемый символ в значении параметра для выбранных элементов]\nУдалите определенные символы из значений параметров для выбранных элементов и отобразите результаты в вкладке отчета."
            elif first_line == "spanish":
                return "[Carácter deseado en el valor del parámetro para los elementos seleccionados]\nElimine caracteres específicos de los valores de los parámetros para los elementos seleccionados y muestre los resultados en una pestaña de informe."
            elif first_line == "chinese":
                return "[所选元素的参数值中的所需字符]\n从所选元素的参数值中删除特定字符，并在报告选项卡中显示结果。"
            elif first_line == "korean":
                return "[선택된 요소의 파라미터 값에서 원하는 문자]\n선택한 요소의 매개변수 값에서 특정 문자를 삭제하고 결과를 보고서 탭에 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_46(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "[Information]\nRetrieve and display detailed information about the model, including its categories, elements, and project details."
            elif first_line == "deutsch":
                return "[Information]\nErmitteln und zeigen Sie detaillierte Informationen zum Modell an, einschließlich seiner Kategorien, Elemente und Projektdetails."
            elif first_line == "farsi":
                return "[اطلاعات]\nاطلاعات دقیق درباره مدل، از جمله دسته‌بندی‌ها، المان‌ها و جزئیات پروژه را بازیابی و نمایش دهید"
            elif first_line == "russian":
                return "[Информация]\nПолучите и отобразите подробную информацию о модели, включая её категории, элементы и детали проекта."
            elif first_line == "spanish":
                return "[Información]\nRecupere y muestre información detallada sobre el modelo, incluidas sus categorías, elementos y detalles del proyecto."
            elif first_line == "chinese":
                return "[信息]\n检索并显示模型的详细信息，包括其类别、元素和项目细节。"
            elif first_line == "korean":
                return "[정보]\n모델에 대한 자세한 정보(카테고리, 요소 및 프로젝트 세부 정보 포함)를 검색하고 표시합니다."
            else:
                return "[Unknown language]\nThe language specified in the file is not recognized."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_47(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Load selected elements from memory"
            elif first_line == "deutsch":
                return "Ausgewählte Elemente aus dem Speicher laden"
            elif first_line == "farsi":
                return "بارگذاری المان‌های انتخاب شده از حافظه"
            elif first_line == "russian":
                return "Загрузить выбранные элементы из памяти"
            elif first_line == "spanish":
                return "Cargar elementos seleccionados desde la memoria"
            elif first_line == "chinese":
                return "从内存加载选定的元素"
            elif first_line == "korean":
                return "메모리에서 선택한 요소 로드"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_48(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Load elements and reduce the selection"
            elif first_line == "deutsch":
                return "Elemente laden und Auswahl reduzieren"
            elif first_line == "farsi":
                return "بارگذاری المان‌ها و کاهش انتخاب"
            elif first_line == "russian":
                return "Загрузить элементы и сократить выбор"
            elif first_line == "spanish":
                return "Cargar elementos y reducir la selección"
            elif first_line == "chinese":
                return "加载元素并减少选择"
            elif first_line == "korean":
                return "요소를 로드하고 선택 줄이기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_49(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Import Selection from XML"
            elif first_line == "deutsch":
                return "Auswahl aus XML importieren"
            elif first_line == "farsi":
                return "XML ایمپورت انتخاب از "
            elif first_line == "russian":
                return "Импорт выбора из XML"
            elif first_line == "spanish":
                return "Importar selección desde XML"
            elif first_line == "chinese":
                return "从 XML 导入选择"
            elif first_line == "korean":
                return "XML에서 선택 가져오기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_50(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Import HTML"
            elif first_line == "deutsch":
                return "HTML importieren"
            elif first_line == "farsi":
                return "HTML وارد کردن از "
            elif first_line == "russian":
                return "Импорт HTML"
            elif first_line == "spanish":
                return "Importar HTML"
            elif first_line == "chinese":
                return "导入 HTML"
            elif first_line == "korean":
                return "HTML 가져오기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_51(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Export Selection to XML"
            elif first_line == "deutsch":
                return "Auswahl in XML exportieren"
            elif first_line == "farsi":
                return "XML اکسپورت انتخاب به "
            elif first_line == "russian":
                return "Экспорт выбора в XML"
            elif first_line == "spanish":
                return "Exportar selección a XML"
            elif first_line == "chinese":
                return "导出选择到 XML"
            elif first_line == "korean":
                return "선택 항목을 XML로 내보내기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tool_tip_52(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Export Selection to CSV"
            elif first_line == "deutsch":
                return "Auswahl in CSV exportieren"
            elif first_line == "farsi":
                return "CSV اکسپورت انتخاب به "
            elif first_line == "russian":
                return "Экспорт выбора в CSV"
            elif first_line == "spanish":
                return "Exportar selección a CSV"
            elif first_line == "chinese":
                return "导出选择到 CSV"
            elif first_line == "korean":
                return "선택 항목을 CSV로 내보내기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"




































