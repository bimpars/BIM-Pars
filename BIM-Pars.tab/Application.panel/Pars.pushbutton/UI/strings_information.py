# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_information.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Model Information"
            elif first_line == "deutsch":
                return "Modellinformationen"
            elif first_line == "farsi":
                return "اطلاعات مدل" 
            elif first_line == "russian":
                return "Информация о модели" 
            elif first_line == "spanish":
                return "Información del modelo" 
            elif first_line == "chinese":
                return "模型信息" 
            elif first_line == "korean":
                return "모델 정보"  
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
                return "Category Element Counts(Current View)"
            elif first_line == "deutsch":
                return "Anzahl der Elemente in der Kategorie (aktuelle Ansicht)"
            elif first_line == "farsi":
                return "تعداد المان های دسته‌بندی (نمای فعلی)" 
            elif first_line == "russian":
                return "Количество элементов категории (текущий вид)" 
            elif first_line == "spanish":
                return "Cantidad de elementos de la categoría (vista actual)"
            elif first_line == "chinese":
                return "类别元素数量（当前视图）"
            elif first_line == "korean":
                return "카테고리 요소 수 (현재 보기)"
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
                return "Family Tree"
            elif first_line == "deutsch":
                return "Familienbaum"
            elif first_line == "farsi":
                return "درخت خانواده"
            elif first_line == "russian":
                return "Семейное дерево"
            elif first_line == "spanish":
                return "Árbol familiar"
            elif first_line == "chinese":
                return "族谱"
            elif first_line == "korean":
                return "가족 트리"
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
                return "Project Information"
            elif first_line == "deutsch":
                return "Projektinformation"
            elif first_line == "farsi":
                return "اطلاعات پروژه"
            elif first_line == "russian":
                return "Информация о проекте"
            elif first_line == "spanish":
                return "Información del proyecto"
            elif first_line == "chinese":
                return "项目信息"
            elif first_line == "korean":
                return "프로젝트 정보"
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
                return "Project Information/Print Manager Settings"
            elif first_line == "deutsch":
                return "Projektinformation/Druckmanager-Einstellungen"
            elif first_line == "farsi":
                return "اطلاعات پروژه/تنظیمات مدیر چاپ"
            elif first_line == "russian":
                return "Информация о проекте/Настройки менеджера печати"
            elif first_line == "spanish":
                return "Información del proyecto/Configuración del administrador de impresión"
            elif first_line == "chinese":
                return "项目信息/打印管理器设置"
            elif first_line == "korean":
                return "프로젝트 정보/인쇄 관리자 설정"
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
                return "All Categories in Model"
            elif first_line == "deutsch":
                return "Alle Kategorien im Modell"
            elif first_line == "farsi":
                return "تمام دسته‌بندی‌ها در مدل"
            elif first_line == "russian":
                return "Все категории в модели"
            elif first_line == "spanish":
                return "Todas las categorías en el modelo"
            elif first_line == "chinese":
                return "模型中的所有类别"
            elif first_line == "korean":
                return "모델의 모든 카테고리"
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
                return "All Categories and relevant views"
            elif first_line == "deutsch":
                return "Alle Kategorien und relevante Ansichten"
            elif first_line == "farsi":
                return "تمام دسته‌بندی‌ها و نمای مرتبط"
            elif first_line == "russian":
                return "Все категории и соответствующие виды"
            elif first_line == "spanish":
                return "Todas las categorías y vistas relevantes"
            elif first_line == "chinese":
                return "所有类别和相关视图"
            elif first_line == "korean":
                return "모든 카테고리와 관련된 뷰"
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
                return "Model Path"
            elif first_line == "deutsch":
                return "Modellpfad"
            elif first_line == "farsi":
                return "مسیر مدل"
            elif first_line == "russian":
                return "Путь модели"
            elif first_line == "spanish":
                return "Ruta del modelo"
            elif first_line == "chinese":
                return "模型路径"
            elif first_line == "korean":
                return "모델 경로"
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
                return "Model Name"
            elif first_line == "deutsch":
                return "Modellname"
            elif first_line == "farsi":
                return "نام مدل"
            elif first_line == "russian":
                return "Имя модели"
            elif first_line == "spanish":
                return "Nombre del modelo"
            elif first_line == "chinese":
                return "模型名称"
            elif first_line == "korean":
                return "모델 이름"
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
                return "Current User"
            elif first_line == "deutsch":
                return "Aktueller Benutzer"
            elif first_line == "farsi":
                return "کاربر فعلی"
            elif first_line == "russian":
                return "Текущий пользователь"
            elif first_line == "spanish":
                return "Usuario actual"
            elif first_line == "chinese":
                return "当前用户"
            elif first_line == "korean":
                return "현재 사용자"
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
                return "Property"
            elif first_line == "deutsch":
                return "Eigenschaft"
            elif first_line == "farsi":
                return "ویژگی"
            elif first_line == "russian":
                return "Свойство"
            elif first_line == "spanish":
                return "Propiedad"
            elif first_line == "chinese":
                return "属性"
            elif first_line == "korean":
                return "속성"
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
                return "Value"
            elif first_line == "deutsch":
                return "Wert"
            elif first_line == "farsi":
                return "مقدار"
            elif first_line == "russian":
                return "Значение"
            elif first_line == "spanish":
                return "Valor"
            elif first_line == "chinese":
                return "值"
            elif first_line == "korean":
                return "값"
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
                return "Category Name"
            elif first_line == "deutsch":
                return "Kategoriename"
            elif first_line == "farsi":
                return "نام دسته‌بندی"
            elif first_line == "russian":
                return "Название категории"
            elif first_line == "spanish":
                return "Nombre de la categoría"
            elif first_line == "chinese":
                return "类别名称"
            elif first_line == "korean":
                return "카테고리 이름"
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
                return "Category ID"
            elif first_line == "deutsch":
                return "Kategorie-ID"
            elif first_line == "farsi":
                return "شناسه دسته‌بندی"
            elif first_line == "russian":
                return "Идентификатор категории"
            elif first_line == "spanish":
                return "ID de categoría"
            elif first_line == "chinese":
                return "类别ID"
            elif first_line == "korean":
                return "카테고리 ID"
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
                return "Element Count"
            elif first_line == "deutsch":
                return "Elementanzahl"
            elif first_line == "farsi":
                return "تعداد المان ها"
            elif first_line == "russian":
                return "Количество элементов"
            elif first_line == "spanish":
                return "Número de elementos"
            elif first_line == "chinese":
                return "元素数量"
            elif first_line == "korean":
                return "요소 수"
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
                return "Family Name"
            elif first_line == "deutsch":
                return "Familiennamen"
            elif first_line == "farsi":
                return "نام خانواده"
            elif first_line == "russian":
                return "Фамилия семейства"
            elif first_line == "spanish":
                return "Nombre de familia"
            elif first_line == "chinese":
                return "族谱名称"
            elif first_line == "korean":
                return "패밀리 이름"
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
                return "Family ID"
            elif first_line == "deutsch":
                return "Familien-ID"
            elif first_line == "farsi":
                return "شناسه خانواده"
            elif first_line == "russian":
                return "Идентификатор семейства"
            elif first_line == "spanish":
                return "ID de familia"
            elif first_line == "chinese":
                return "族谱ID"
            elif first_line == "korean":
                return "패밀리 ID"
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
                return "Family Type"
            elif first_line == "deutsch":
                return "Familientyp"
            elif first_line == "farsi":
                return "نوع خانواده"
            elif first_line == "russian":
                return "Тип семейства"
            elif first_line == "spanish":
                return "Tipo de familia"
            elif first_line == "chinese":
                return "族谱类型"
            elif first_line == "korean":
                return "패밀리 유형"
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
                return "Family Type ID"
            elif first_line == "deutsch":
                return "Familientyp-ID"
            elif first_line == "farsi":
                return "شناسه نوع خانواده"
            elif first_line == "russian":
                return "Идентификатор типа семейства"
            elif first_line == "spanish":
                return "ID del tipo de familia"
            elif first_line == "chinese":
                return "族谱类型ID"
            elif first_line == "korean":
                return "패밀리 유형 ID"
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
    
def str_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter Value"
            elif first_line == "deutsch":
                return "Parameterwert"
            elif first_line == "farsi":
                return "مقدار پارامتر"
            elif first_line == "russian":
                return "Значение параметра"
            elif first_line == "spanish":
                return "Valor del parámetro"
            elif first_line == "chinese":
                return "参数值"
            elif first_line == "korean":
                return "매개변수 값"
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
                return "Total"
            elif first_line == "deutsch":
                return "Gesamt"
            elif first_line == "farsi":
                return "مجموع"
            elif first_line == "russian":
                return "Всего"
            elif first_line == "spanish":
                return "Total"
            elif first_line == "chinese":
                return "总计"
            elif first_line == "korean":
                return "총계"
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
                return "View Name"
            elif first_line == "deutsch":
                return "Ansichtsname"
            elif first_line == "farsi":
                return "نام نما"
            elif first_line == "russian":
                return "Название вида"
            elif first_line == "spanish":
                return "Nombre de la vista"
            elif first_line == "chinese":
                return "视图名称"
            elif first_line == "korean":
                return "뷰 이름"
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
                return "No project parameters found in the current project."
            elif first_line == "deutsch":
                return "In diesem Projekt wurden keine Projektparameter gefunden."
            elif first_line == "farsi":
                return "در این پروژه پارامترهای پروژه‌ای یافت نشدند"
            elif first_line == "russian":
                return "В текущем проекте не найдено ни одного параметра проекта."
            elif first_line == "spanish":
                return "No se encontraron parámetros de proyecto en el proyecto actual."
            elif first_line == "chinese":
                return "在当前项目中找不到项目参数。"
            elif first_line == "korean":
                return "현재 프로젝트에서 프로젝트 매개변수를 찾을 수 없습니다."
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
    
def str_26(file_path):
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
    
def str_27(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Setting"
            elif first_line == "deutsch":
                return "Einstellung"
            elif first_line == "farsi":
                return "تنظیم"
            elif first_line == "russian":
                return "Настройка"
            elif first_line == "spanish":
                return "Ajuste"
            elif first_line == "chinese":
                return "设置"
            elif first_line == "korean":
                return "설정"
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