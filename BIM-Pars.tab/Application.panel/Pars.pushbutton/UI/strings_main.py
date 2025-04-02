# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_main.py

#window name 
def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "BIM Pars"
            elif first_line == "deutsch":
                return "BIM Pars"
            elif first_line == "farsi":
                return "بیم پارس"
            elif first_line == "russian":
                return "BIM Pars"
            elif first_line == "spanish":
                return "BIM Pars"
            elif first_line == "chinese":
                return "BIM Pars"
            elif first_line == "korean":
                return "BIM Pars"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
#tab name     
def str_2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Toolbox"
            elif first_line == "deutsch":
                return "Werkzeugkasten"
            elif first_line == "farsi":
                return "جعبه ابزار"
            elif first_line == "russian":
                return "Инструментальный ящик"
            elif first_line == "spanish":
                return "Caja de herramientas"
            elif first_line == "chinese":
                return "工具箱"
            elif first_line == "korean":
                return "도구 상자"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

#tree structure
def str_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "BIM Pars Tools"
            elif first_line == "deutsch":
                return "BIM Pars Werkzeuge"
            elif first_line == "farsi":
                return "ابزارهای بیم پارس"
            elif first_line == "russian":
                return "Инструменты BIM Pars"
            elif first_line == "spanish":
                return "Herramientas BIM Pars"
            elif first_line == "chinese":
                return "BIM Pars 工具"
            elif first_line == "korean":
                return "BIM Pars 도구"
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
                return "Info"
            elif first_line == "deutsch":
                return "Info"
            elif first_line == "farsi":
                return "اطلاعات"
            elif first_line == "russian":
                return "Информация"
            elif first_line == "spanish":
                return "Info"
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
    
def str_5(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Element Self"
            elif first_line == "deutsch":
                return "Element Selbst"
            elif first_line == "farsi":
                return "المان به تنها یی"
            elif first_line == "russian":
                return "Элемент Сам"
            elif first_line == "spanish":
                return "Elemento Propio"
            elif first_line == "chinese":
                return "元素自身"
            elif first_line == "korean":
                return "요소 자기"
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
                return "Select"
            elif first_line == "deutsch":
                return "Auswählen"
            elif first_line == "farsi":
                return "انتخاب"
            elif first_line == "russian":
                return "Выбрать"
            elif first_line == "spanish":
                return "Seleccionar"
            elif first_line == "chinese":
                return "选择"
            elif first_line == "korean":
                return "선택하다"
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
                return "Filter"
            elif first_line == "deutsch":
                return "Filter"
            elif first_line == "farsi":
                return "فیلتر"
            elif first_line == "russian":
                return "Фильтр"
            elif first_line == "spanish":
                return "Filtrar"
            elif first_line == "chinese":
                return "过滤器"
            elif first_line == "korean":
                return "필터"
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
                return "By Parameter"
            elif first_line == "deutsch":
                return "Nach Parameter"
            elif first_line == "farsi":
                return  "بر اساس پارامتر"
            elif first_line == "russian":
                return "По параметру"
            elif first_line == "spanish":
                return "Por parámetro"
            elif first_line == "chinese":
                return "按参数"
            elif first_line == "korean":
                return "매개변수로"
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
                return "All Elements"
            elif first_line == "deutsch":
                return "Alle Elemente"
            elif first_line == "farsi":
                return "همه المان‌ها"
            elif first_line == "russian":
                return "Все элементы"
            elif first_line == "spanish":
                return "Todos los elementos"
            elif first_line == "chinese":
                return "所有元素"
            elif first_line == "korean":
                return "모든 요소"
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
                return "Excel"
            elif first_line == "deutsch":
                return "Excel"
            elif first_line == "farsi":
                return "اکسل"
            elif first_line == "russian":
                return "Excel"
            elif first_line == "spanish":
                return "Excel"
            elif first_line == "chinese":
                return "Excel"
            elif first_line == "korean":
                return "엑셀"
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
                return "Reduce Selected"
            elif first_line == "deutsch":
                return "Ausgewählte reduzieren"
            elif first_line == "farsi":
                return "کاهش انتخاب شده ها"
            elif first_line == "russian":
                return "Уменьшить выбранное"
            elif first_line == "spanish":
                return "Reducir seleccionado"
            elif first_line == "chinese":
                return "减少选定"
            elif first_line == "korean":
                return "선택한 항목 줄이기"
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
                return "Delete"
            elif first_line == "deutsch":
                return "Löschen"
            elif first_line == "farsi":
                return "حذف"
            elif first_line == "russian":
                return "Удалить"
            elif first_line == "spanish":
                return "Eliminar"
            elif first_line == "chinese":
                return "删除"
            elif first_line == "korean":
                return "삭제"
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
                return "Element Parameter"
            elif first_line == "deutsch":
                return "Elementparameter"
            elif first_line == "farsi":
                return "پارامتر المان"
            elif first_line == "russian":
                return "Параметр элемента"
            elif first_line == "spanish":
                return "Parámetro del elemento"
            elif first_line == "chinese":
                return "元素参数"
            elif first_line == "korean":
                return "요소 매개변수"
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
                return "Parameter Self"
            elif first_line == "deutsch":
                return "Parameter Selbst"
            elif first_line == "farsi":
                return "پارامتر به تنها یی"
            elif first_line == "russian":
                return "Параметр Сам"
            elif first_line == "spanish":
                return "Parámetro Propio"
            elif first_line == "chinese":
                return "参数自身"
            elif first_line == "korean":
                return "매개변수 자기"
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
                return "Search"
            elif first_line == "deutsch":
                return "Suchen"
            elif first_line == "farsi":
                return "جستجو"
            elif first_line == "russian":
                return "Поиск"
            elif first_line == "spanish":
                return "Buscar"
            elif first_line == "chinese":
                return "搜索"
            elif first_line == "korean":
                return "검색"
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
                return "Check"
            elif first_line == "deutsch":
                return "Überprüfen"
            elif first_line == "farsi":
                return "بررسی"
            elif first_line == "russian":
                return "Проверить"
            elif first_line == "spanish":
                return "Verificar"
            elif first_line == "chinese":
                return "检查"
            elif first_line == "korean":
                return "확인"
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
    
def str_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Comparison Check"
            elif first_line == "deutsch":
                return "Vergleichsprüfung"
            elif first_line == "farsi":
                return "بررسی مقایسه ای"
            elif first_line == "russian":
                return "Проверка сравнения"
            elif first_line == "spanish":
                return "Verificación de comparación"
            elif first_line == "chinese":
                return "比较检查"
            elif first_line == "korean":
                return "비교 확인"
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
                return "Set"
            elif first_line == "deutsch":
                return "Setzen"
            elif first_line == "farsi":
                return "تنظیم"
            elif first_line == "russian":
                return "Установить"
            elif first_line == "spanish":
                return "Configurar"
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
    
def str_20(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Edit"
            elif first_line == "deutsch":
                return "Bearbeiten"
            elif first_line == "farsi":
                return "ویرایش"
            elif first_line == "russian":
                return "Редактировать"
            elif first_line == "spanish":
                return "Editar"
            elif first_line == "chinese":
                return "编辑"
            elif first_line == "korean":
                return "편집"
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
                return "Scripts"
            elif first_line == "deutsch":
                return "Scripts"
            elif first_line == "farsi":
                return "اسکریپت‌ها"
            elif first_line == "russian":
                return "Скрипты"
            elif first_line == "spanish":
                return "Scripts"
            elif first_line == "chinese":
                return "脚本"
            elif first_line == "korean":
                return "스크립트"
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
                return "Package"
            elif first_line == "deutsch":
                return "Paket"
            elif first_line == "farsi":
                return "بسته"
            elif first_line == "russian":
                return "Пакет"
            elif first_line == "spanish":
                return "Paquete"
            elif first_line == "chinese":
                return "包"
            elif first_line == "korean":
                return "패키지"
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
                return "Tools"
            elif first_line == "deutsch":
                return "Werkzeuge"
            elif first_line == "farsi":
                return "ابزارها"
            elif first_line == "russian":
                return "Инструменты"
            elif first_line == "spanish":
                return "Herramientas"
            elif first_line == "chinese":
                return "工具"
            elif first_line == "korean":
                return "도구"
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
                return "ID"
            elif first_line == "deutsch":
                return "ID"
            elif first_line == "farsi":
                return "شناسه"
            elif first_line == "russian":
                return "ID"
            elif first_line == "spanish":
                return "ID"
            elif first_line == "chinese":
                return "ID"
            elif first_line == "korean":
                return "ID"
            else:
                return "Unknown language"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {}".format(e)

def str_25(file_path):
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
                return "Room ID"
            elif first_line == "deutsch":
                return "Raum-ID"
            elif first_line == "farsi":
                return "شناسه اتاق"
            elif first_line == "russian":
                return "Идентификатор помещения"
            elif first_line == "spanish":
                return "ID de habitación"
            elif first_line == "chinese":
                return "房间标识"
            elif first_line == "korean":
                return "방 ID"
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
                return "Door ID"
            elif first_line == "deutsch":
                return "Tür-ID"
            elif first_line == "farsi":
                return "شناسه درب"
            elif first_line == "russian":
                return "Идентификатор двери"
            elif first_line == "spanish":
                return "ID de puerta"
            elif first_line == "chinese":
                return "门标识"
            elif first_line == "korean":
                return "도어 ID"
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
                return "Warning"
            elif first_line == "deutsch":
                return "Warnung"
            elif first_line == "farsi":
                return "هشدار"
            elif first_line == "russian":
                return "Предупреждение"
            elif first_line == "spanish":
                return "Advertencia"
            elif first_line == "chinese":
                return "警告"
            elif first_line == "korean":
                return "경고"
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
                return "No data grid found in current tab."
            elif first_line == "deutsch":
                return "Kein Datenraster im aktuellen Tab gefunden."
            elif first_line == "farsi":
                return ".هیچ جدول داده‌ای در برگه جاری پیدا نشد"
            elif first_line == "russian":
                return "В текущей вкладке не найдено ни одной таблицы данных."
            elif first_line == "spanish":
                return "No se encontró ninguna cuadrícula de datos en la pestaña actual."
            elif first_line == "chinese":
                return "当前选项卡中未找到数据网格。"
            elif first_line == "korean":
                return "현재 탭에서 데이터 그리드를 찾을 수 없습니다."
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
                return "Please select cells containing element IDs."
            elif first_line == "deutsch":
                return "Bitte wählen Sie Zellen mit Element-IDs aus."
            elif first_line == "farsi":
                return ".لطفاً سلول‌های حاوی شناسه‌های المان را انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, выберите ячейки, содержащие ID элементов."
            elif first_line == "spanish":
                return "Por favor, seleccione celdas que contengan IDs de elementos."
            elif first_line == "chinese":
                return "请选择包含元素ID的单元格。"
            elif first_line == "korean":
                return "요소 ID가 포함된 셀을 선택하세요."
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
                return "No valid element IDs found in selection."
            elif first_line == "deutsch":
                return "Keine gültigen Element-IDs in der Auswahl gefunden."
            elif first_line == "farsi":
                return ".هیچ شناسه المان معتبری در انتخاب پیدا نشد"
            elif first_line == "russian":
                return "В выбранном объекте не найдено действительных ID элементов."
            elif first_line == "spanish":
                return "No se encontraron IDs de elementos válidos en la selección."
            elif first_line == "chinese":
                return "在选择中未找到有效的元素ID。"
            elif first_line == "korean":
                return "선택 항목에서 유효한 요소 ID를 찾을 수 없습니다."
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
                return "No elements selected in the current view."
            elif first_line == "deutsch":
                return "Keine Elemente in der aktuellen Ansicht ausgewählt."
            elif first_line == "farsi":
                return ".هیچ المانی در نمای جاری انتخاب نشده است"
            elif first_line == "russian":
                return "В текущем представлении не выбрано ни одного элемента."
            elif first_line == "spanish":
                return "No se han seleccionado elementos en la vista actual."
            elif first_line == "chinese":
                return "当前视图中未选择任何元素。"
            elif first_line == "korean":
                return "현재 보기에서 선택된 요소가 없습니다."
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
                return "The view provided is not a 3D view."
            elif first_line == "deutsch":
                return "Die angegebene Ansicht ist keine 3D-Ansicht."
            elif first_line == "farsi":
                return ".نمای ارائه شده یک نمای سه بعدی نیست"
            elif first_line == "russian":
                return "Предоставленное представление не является 3D представлением."
            elif first_line == "spanish":
                return "La vista proporcionada no es una vista en 3D."
            elif first_line == "chinese":
                return "提供的视图不是3D视图。"
            elif first_line == "korean":
                return "제공된 뷰는 3D 뷰가 아닙니다."
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
                return "Solid fill pattern not found. Make sure a solid fill pattern exists."
            elif first_line == "deutsch":
                return "Füllmuster nicht gefunden. Stellen Sie sicher, dass ein Füllmuster vorhanden ist."
            elif first_line == "farsi":
                return ".الگو یافت نشد"
            elif first_line == "russian":
                return "Шаблон сплошной заливки не найден. Убедитесь, что существует шаблон сплошной заливки."
            elif first_line == "spanish":
                return "Patrón de relleno sólido no encontrado. Asegúrese de que existe un patrón de relleno sólido."
            elif first_line == "chinese":
                return "未找到实心填充图案。请确保存在实心填充图案。"
            elif first_line == "korean":
                return "솔리드 채우기 패턴을 찾을 수 없습니다. 솔리드 채우기 패턴이 존재하는지 확인하세요."
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
                return "No elements selected. Please select elements to override their color."
            elif first_line == "deutsch":
                return "Keine Elemente ausgewählt. Bitte wählen Sie Elemente aus, um ihre Farbe zu überschreiben."
            elif first_line == "farsi":
                return ".هیچ المانی انتخاب نشده است. لطفاً المان ها را برای تغییر رنگ آنها انتخاب کنید"
            elif first_line == "russian":
                return "Элементы не выбраны. Пожалуйста, выберите элементы, чтобы изменить их цвет."
            elif first_line == "spanish":
                return "No se han seleccionado elementos. Por favor, seleccione elementos para anular su color."
            elif first_line == "chinese":
                return "未选择任何元素。请选择元素以覆盖其颜色。"
            elif first_line == "korean":
                return "선택된 요소가 없습니다. 색상을 변경할 요소를 선택하세요."
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
                return "No elements selected. Please select elements to remove color overrides."
            elif first_line == "deutsch":
                return "Keine Elemente ausgewählt. Bitte wählen Sie Elemente aus, um Farbüberschreibungen zu entfernen."
            elif first_line == "farsi":
                return ".هیچ المانی انتخاب نشده است. لطفاً المان ها را برای حذف تغییرات رنگ انتخاب کنید"
            elif first_line == "russian":
                return "Элементы не выбраны. Пожалуйста, выберите элементы, чтобы удалить переопределения цвета."
            elif first_line == "spanish":
                return "No se han seleccionado elementos. Por favor, seleccione elementos para eliminar las anulaciones de color."
            elif first_line == "chinese":
                return "未选择任何元素。请选择元素以删除颜色覆盖。"
            elif first_line == "korean":
                return "선택된 요소가 없습니다. 색상 오버라이드를 제거할 요소를 선택하세요."
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
                return "Please select elements to remove their pin markers."
            elif first_line == "deutsch":
                return "Bitte wählen Sie Elemente aus, um ihre Pin-Markierungen zu entfernen."
            elif first_line == "farsi":
                return ".لطفاً المان ها را برای حذف نشانگرهای پین انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, выберите элементы, чтобы удалить их маркеры."
            elif first_line == "spanish":
                return "Por favor, seleccione elementos para eliminar sus marcadores."
            elif first_line == "chinese":
                return "请选择元素以删除它们的钉子标记。"
            elif first_line == "korean":
                return "핀 마커를 제거할 요소를 선택하세요."
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
                return "Error during operation: {}"
            elif first_line == "deutsch":
                return "Fehler während des Vorgangs: {}"
            elif first_line == "farsi":
                return "خطا در حین عملیات: {}"
            elif first_line == "russian":
                return "Ошибка во время операции: {}"
            elif first_line == "spanish":
                return "Error durante la operación: {}"
            elif first_line == "chinese":
                return "操作期间出错：{}"
            elif first_line == "korean":
                return "작업 중 오류: {}"
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
                return "Directory Error"
            elif first_line == "deutsch":
                return "Verzeichnisfehler"
            elif first_line == "farsi":
                return "خطا دایرکتوری"
            elif first_line == "russian":
                return "Ошибка каталога"
            elif first_line == "spanish":
                return "Error de directorio"
            elif first_line == "chinese":
                return "目录错误"
            elif first_line == "korean":
                return "디렉터리 오류"
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
                return "Script metadata file not found."
            elif first_line == "deutsch":
                return "Metadatendatei für das Skript nicht gefunden."
            elif first_line == "farsi":
                return ".فایل متادیتای اسکریپت پیدا نشد"
            elif first_line == "russian":
                return "Файл метаданных скрипта не найден."
            elif first_line == "spanish":
                return "Archivo de metadatos del script no encontrado."
            elif first_line == "chinese":
                return "未找到脚本元数据文件。"
            elif first_line == "korean":
                return "스크립트 메타데이터 파일을 찾을 수 없습니다."
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
                return "Error loading scripts:"
            elif first_line == "deutsch":
                return "Fehler beim Laden der Skripte:"
            elif first_line == "farsi":
                return "خطا در بارگذاری اسکریپت‌ها:"
            elif first_line == "russian":
                return "Ошибка при загрузке скриптов:"
            elif first_line == "spanish":
                return "Error al cargar los scripts:"
            elif first_line == "chinese":
                return "加载脚本时出错："
            elif first_line == "korean":
                return "스크립트를 로드하는 중 오류가 발생했습니다:"
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
                return "File Error"
            elif first_line == "deutsch":
                return "Dateifehler"
            elif first_line == "farsi":
                return "خطای فایل"
            elif first_line == "russian":
                return "Ошибка файла"
            elif first_line == "spanish":
                return "Error de archivo"
            elif first_line == "chinese":
                return "文件错误"
            elif first_line == "korean":
                return "파일 오류"
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
                return "Script file not found."
            elif first_line == "deutsch":
                return "Skriptdatei nicht gefunden."
            elif first_line == "farsi":
                return ".فایل اسکریپت پیدا نشد"
            elif first_line == "russian":
                return "Файл скрипта не найден."
            elif first_line == "spanish":
                return "Archivo de script no encontrado."
            elif first_line == "chinese":
                return "未找到脚本文件。"
            elif first_line == "korean":
                return "스크립트 파일을 찾을 수 없습니다."
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
                return "Error executing script:"
            elif first_line == "deutsch":
                return "Fehler beim Ausführen des Skripts:"
            elif first_line == "farsi":
                return "خطا در اجرای اسکریپت:"
            elif first_line == "russian":
                return "Ошибка при выполнении скрипта:"
            elif first_line == "spanish":
                return "Error al ejecutar el script:"
            elif first_line == "chinese":
                return "执行脚本时出错："
            elif first_line == "korean":
                return "스크립트를 실행하는 중 오류가 발생했습니다:"
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
                return "Script Error"
            elif first_line == "deutsch":
                return "Skriptfehler"
            elif first_line == "farsi":
                return "خطای اسکریپت"
            elif first_line == "russian":
                return "Ошибка скрипта"
            elif first_line == "spanish":
                return "Error de script"
            elif first_line == "chinese":
                return "脚本错误"
            elif first_line == "korean":
                return "스크립트 오류"
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
                return "Script metadata file not found at:"
            elif first_line == "deutsch":
                return "Metadatendatei für das Skript nicht gefunden unter:"
            elif first_line == "farsi":
                return "فایل متادیتای اسکریپت در آدرس زیر پیدا نشد:"
            elif first_line == "russian":
                return "Файл метаданных скрипта не найден по адресу:"
            elif first_line == "spanish":
                return "Archivo de metadatos del script no encontrado en:"
            elif first_line == "chinese":
                return "在以下位置未找到脚本元数据文件："
            elif first_line == "korean":
                return "다음 위치에서 스크립트 메타데이터 파일을 찾을 수 없습니다:"
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
                return "Configuration Error"
            elif first_line == "deutsch":
                return "Konfigurationsfehler"
            elif first_line == "farsi":
                return "خطای پیکربندی"
            elif first_line == "russian":
                return "Ошибка конфигурации"
            elif first_line == "spanish":
                return "Error de configuración"
            elif first_line == "chinese":
                return "配置错误"
            elif first_line == "korean":
                return "구성 오류"
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
                return "Error configuring script nodes:"
            elif first_line == "deutsch":
                return "Fehler bei der Konfiguration der Skriptnodes:"
            elif first_line == "farsi":
                return "خطا در پیکربندی گره‌های اسکریپت:"
            elif first_line == "russian":
                return "Ошибка при конфигурации узлов скрипта:"
            elif first_line == "spanish":
                return "Error al configurar los nodos del script:"
            elif first_line == "chinese":
                return "配置脚本节点时出错："
            elif first_line == "korean":
                return "스크립트 노드 구성 중 오류가 발생했습니다:"
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
                return "Script metadata file not found at: {}"
            elif first_line == "deutsch":
                return "Metadatendatei für das Skript nicht gefunden unter: {}"
            elif first_line == "farsi":
                return "فایل متادیتای اسکریپت در آدرس زیر پیدا نشد: {}"
            elif first_line == "russian":
                return "Файл метаданных скрипта не найден по адресу: {}"
            elif first_line == "spanish":
                return "Archivo de metadatos del script no encontrado en: {}"
            elif first_line == "chinese":
                return "在以下位置未找到脚本元数据文件：{}"
            elif first_line == "korean":
                return "다음 위치에서 스크립트 메타데이터 파일을 찾을 수 없습니다: {}"
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
                return "Error loading script metadata: {}"
            elif first_line == "deutsch":
                return "Fehler beim Laden der Skriptmetadaten: {}"
            elif first_line == "farsi":
                return "خطا در بارگذاری متادیتای اسکریپت: {}"
            elif first_line == "russian":
                return "Ошибка при загрузке метаданных скрипта: {}"
            elif first_line == "spanish":
                return "Error al cargar los metadatos del script: {}"
            elif first_line == "chinese":
                return "加载脚本元数据时出错：{}"
            elif first_line == "korean":
                return "스크립트 메타데이터를 로드하는 중 오류가 발생했습니다: {}"
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
                return "Server not respond."
            elif first_line == "deutsch":
                return "Server antwortet nicht."
            elif first_line == "farsi":
                return ".سرور پاسخ نمی‌دهد"
            elif first_line == "russian":
                return "Сервер не отвечает."
            elif first_line == "spanish":
                return "El servidor no responde."
            elif first_line == "chinese":
                return "服务器未响应。"
            elif first_line == "korean":
                return "서버가 응답하지 않습니다."
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
                return "URL not found."
            elif first_line == "deutsch":
                return "URL nicht gefunden."
            elif first_line == "farsi":
                return ".URL آدرس  پیدا نشد"
            elif first_line == "russian":
                return "URL не найден."
            elif first_line == "spanish":
                return "URL no encontrada."
            elif first_line == "chinese":
                return "未找到URL。"
            elif first_line == "korean":
                return "URL을 찾을 수 없습니다."
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
                return "Unknown icon clicked:"
            elif first_line == "deutsch":
                return "Unbekanntes Symbol angeklickt:"
            elif first_line == "farsi":
                return "آیکون ناشناخته کلیک شد:"
            elif first_line == "russian":
                return "Ícono desconocido clickeado:"
            elif first_line == "spanish":
                return "URL no encontrada."
            elif first_line == "chinese":
                return "点击了未知图标："
            elif first_line == "korean":
                return "알 수 없는 아이콘이 클릭되었습니다:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
#tool tips for tree structure toolstrip
def tip_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Expand Tree"
            elif first_line == "deutsch":
                return "Baum erweitern"
            elif first_line == "farsi":
                return "گسترش درخت"
            elif first_line == "russian":
                return "Развернуть дерево"
            elif first_line == "spanish":
                return "Expandir árbol"
            elif first_line == "chinese":
                return "展开树"
            elif first_line == "korean":
                return "트리 확장"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
    
def tip_2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Collapse Tree"
            elif first_line == "deutsch":
                return "Baum einklappen"
            elif first_line == "farsi":
                return "جمع کردن درخت"
            elif first_line == "russian":
                return "Свернуть дерево"
            elif first_line == "spanish":
                return "Colapsar árbol"
            elif first_line == "chinese":
                return "收起树"
            elif first_line == "korean":
                return "트리 축소"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Documentation"
            elif first_line == "deutsch":
                return "Dokumentation"
            elif first_line == "farsi":
                return "مستندات"
            elif first_line == "russian":
                return "Документация"
            elif first_line == "spanish":
                return "Documentación"
            elif first_line == "chinese":
                return "文档"
            elif first_line == "korean":
                return "문서"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Play Video"
            elif first_line == "deutsch":
                return "Video abspielen"
            elif first_line == "farsi":
                return "پخش ویدیو"
            elif first_line == "russian":
                return "Воспроизвести видео"
            elif first_line == "spanish":
                return "Reproducir video"
            elif first_line == "chinese":
                return "播放视频"
            elif first_line == "korean":
                return "비디오 재생"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_5(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Open GitHub"
            elif first_line == "deutsch":
                return "GitHub öffnen"
            elif first_line == "farsi":
                return "باز کردن گیت‌هاب"
            elif first_line == "russian":
                return "Открыть GitHub"
            elif first_line == "spanish":
                return "Abrir GitHub"
            elif first_line == "chinese":
                return "打开 GitHub"
            elif first_line == "korean":
                return "GitHub 열기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_6(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Report Bug"
            elif first_line == "deutsch":
                return "Fehler melden"
            elif first_line == "farsi":
                return "گزارش خرابی"
            elif first_line == "russian":
                return "Сообщить об ошибке"
            elif first_line == "spanish":
                return "Reportar error"
            elif first_line == "chinese":
                return "报告错误"
            elif first_line == "korean":
                return "버그 보고하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Save in Memory"
            elif first_line == "deutsch":
                return "Im Speicher speichern"
            elif first_line == "farsi":
                return "ذخیره در حافظه"
            elif first_line == "russian":
                return "Сохранить в памяти"
            elif first_line == "spanish":
                return "Guardar en memoria"
            elif first_line == "chinese":
                return "保存在内存中"
            elif first_line == "korean":
                return "메모리에 저장하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Load from Memory"
            elif first_line == "deutsch":
                return "Aus dem Speicher laden"
            elif first_line == "farsi":
                return "بارگذاری از حافظه"
            elif first_line == "russian":
                return "Загрузить из памяти"
            elif first_line == "spanish":
                return "Cargar desde memoria"
            elif first_line == "chinese":
                return "从内存加载"
            elif first_line == "korean":
                return "메모리에서 불러오기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_9(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Save"
            elif first_line == "deutsch":
                return "Speichern"
            elif first_line == "farsi":
                return "ذخیره"
            elif first_line == "russian":
                return "Сохранить"
            elif first_line == "spanish":
                return "Guardar"
            elif first_line == "chinese":
                return "保存"
            elif first_line == "korean":
                return "저장"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_10(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Load"
            elif first_line == "deutsch":
                return "Laden"
            elif first_line == "farsi":
                return "بارگذاری"
            elif first_line == "russian":
                return "Загрузить"
            elif first_line == "spanish":
                return "Cargar"
            elif first_line == "chinese":
                return "加载"
            elif first_line == "korean":
                return "불러오기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Import"
            elif first_line == "deutsch":
                return "Importieren"
            elif first_line == "farsi":
                return "ایمپورت"
            elif first_line == "russian":
                return "Импортировать"
            elif first_line == "spanish":
                return "Importar"
            elif first_line == "chinese":
                return "导入"
            elif first_line == "korean":
                return "가져오기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_12(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Export"
            elif first_line == "deutsch":
                return "Exportieren"
            elif first_line == "farsi":
                return "اکسپورت"
            elif first_line == "russian":
                return "Экспортировать"
            elif first_line == "spanish":
                return "Exportar"
            elif first_line == "chinese":
                return "导出"
            elif first_line == "korean":
                return "내보내기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Script Manager"
            elif first_line == "deutsch":
                return "Skript-Manager"
            elif first_line == "farsi":
                return "مدیریت اسکریپت"
            elif first_line == "russian":
                return "Менеджер скриптов"
            elif first_line == "spanish":
                return "Administrador de scripts"
            elif first_line == "chinese":
                return "脚本管理器"
            elif first_line == "korean":
                return "스크립트 관리자"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_14(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Run Directory"
            elif first_line == "deutsch":
                return "Ausführungsverzeichnis"
            elif first_line == "farsi":
                return "اجرای دایرکتوری"
            elif first_line == "russian":
                return "Каталог выполнения"
            elif first_line == "spanish":
                return "Directorio de ejecución"
            elif first_line == "chinese":
                return "运行目录"
            elif first_line == "korean":
                return "실행 디렉토리"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select elements"
            elif first_line == "deutsch":
                return "Elemente auswählen"
            elif first_line == "farsi":
                return "انتخاب المان‌ها"
            elif first_line == "russian":
                return "Выбрать элементы"
            elif first_line == "spanish":
                return "Seleccionar elementos"
            elif first_line == "chinese":
                return "选择元素"
            elif first_line == "korean":
                return "요소 선택하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_16(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Deselect elements"
            elif first_line == "deutsch":
                return "Elemente abwählen"
            elif first_line == "farsi":
                return "حذف انتخاب از المان‌ها"
            elif first_line == "russian":
                return "Снять выбор с элементов"
            elif first_line == "spanish":
                return "Deseleccionar elementos"
            elif first_line == "chinese":
                return "取消选择元素"
            elif first_line == "korean":
                return "요소 선택 해제"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_17(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Isolate elements"
            elif first_line == "deutsch":
                return "Elemente isolieren"
            elif first_line == "farsi":
                return "ایزوله کردن المان‌ها"
            elif first_line == "russian":
                return "Изолировать элементы"
            elif first_line == "spanish":
                return "Aislar elementos"
            elif first_line == "chinese":
                return "隔离元素"
            elif first_line == "korean":
                return "요소 분리하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Revoke Isolation"
            elif first_line == "deutsch":
                return "Isolierung aufheben"
            elif first_line == "farsi":
                return "لغو ایزولاسیون"
            elif first_line == "russian":
                return "Отменить изоляцию"
            elif first_line == "spanish":
                return "Revocar aislamiento"
            elif first_line == "chinese":
                return "撤销隔离"
            elif first_line == "korean":
                return "격리 해제하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_19(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Color elements"
            elif first_line == "deutsch":
                return "Elemente einfärben"
            elif first_line == "farsi":
                return "رنگ‌آمیزی المان‌ها"
            elif first_line == "russian":
                return "Окрасить элементы"
            elif first_line == "spanish":
                return "Colorear elementos"
            elif first_line == "chinese":
                return "为元素着色"
            elif first_line == "korean":
                return "요소 색칠하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_20(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Revoke color elements"
            elif first_line == "deutsch":
                return "Farbe der Elemente zurücknehmen"
            elif first_line == "farsi":
                return "لغو رنگ المان‌ها"
            elif first_line == "russian":
                return "Отменить цвет элементов"
            elif first_line == "spanish":
                return "Revocar color de elementos"
            elif first_line == "chinese":
                return "撤销元素颜色"
            elif first_line == "korean":
                return "요소 색상 해제하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Pin"
            elif first_line == "deutsch":
                return "Pin"
            elif first_line == "farsi":
                return "سنجاق"
            elif first_line == "russian":
                return "Пин"
            elif first_line == "spanish":
                return "Pin"
            elif first_line == "chinese":
                return "钉子"
            elif first_line == "korean":
                return "핀"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_22(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Remove pin"
            elif first_line == "deutsch":
                return "Pin entfernen"
            elif first_line == "farsi":
                return "حذف سنجاق"
            elif first_line == "russian":
                return "Удалить пин"
            elif first_line == "spanish":
                return "Quitar pin"
            elif first_line == "chinese":
                return "移除钉子"
            elif first_line == "korean":
                return "핀 제거하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

#information bars  
def str_bar_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "pyRevit"
            elif first_line == "deutsch":
                return "pyRevit"
            elif first_line == "farsi":
                return "پای-رویت"
            elif first_line == "russian":
                return "pyRevit"
            elif first_line == "spanish":
                return "pyRevit"
            elif first_line == "chinese":
                return "pyRevit"
            elif first_line == "korean":
                return "pyRevit"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_bar_2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return " User: Checking..."
            elif first_line == "deutsch":
                return " Benutzer: Überprüfen..."
            elif first_line == "farsi":
                return " ... کاربر: در حال بررسی"
            elif first_line == "russian":
                return " Пользователь: Проверка..."
            elif first_line == "spanish":
                return " Usuario: Comprobando..."
            elif first_line == "chinese":
                return " 用户：检查中..."
            elif first_line == "korean":
                return " 사용자: 확인 중..."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_bar_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return " Connection: Checking..."
            elif first_line == "deutsch":
                return " Verbindung: Überprüfen..."
            elif first_line == "farsi":
                return " ... اتصال: در حال بررسی"
            elif first_line == "russian":
                return " Подключение: Проверка..."
            elif first_line == "spanish":
                return " Conexión: Comprobando..."
            elif first_line == "chinese":
                return " 连接：检查中..."
            elif first_line == "korean":
                return " 연결: 확인 중..."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_bar_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Element: "
            elif first_line == "deutsch":
                return "Element: "
            elif first_line == "farsi":
                return "المان: "
            elif first_line == "russian":
                return "Элемент: "
            elif first_line == "spanish":
                return "Elemento: "
            elif first_line == "chinese":
                return "元素： "
            elif first_line == "korean":
                return "요소: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_bar_5(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return " User: "
            elif first_line == "deutsch":
                return " Benutzer: "
            elif first_line == "farsi":
                return " کاربر: "
            elif first_line == "russian":
                return " Пользователь: "
            elif first_line == "spanish":
                return " Usuario: "
            elif first_line == "chinese":
                return " 用户： "
            elif first_line == "korean":
                return " 사용자: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_bar_6(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Valid"
            elif first_line == "deutsch":
                return "Gültig"
            elif first_line == "farsi":
                return "معتبر"
            elif first_line == "russian":
                return "Действительный"
            elif first_line == "spanish":
                return "Válido"
            elif first_line == "chinese":
                return "有效"
            elif first_line == "korean":
                return "유효한"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_bar_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unvalid"
            elif first_line == "deutsch":
                return "Ungültig"
            elif first_line == "farsi":
                return "نامعتبر"
            elif first_line == "russian":
                return "Недействительный"
            elif first_line == "spanish":
                return "No válido"
            elif first_line == "chinese":
                return "无效"
            elif first_line == "korean":
                return "유효하지 않음"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_bar_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Do you have a license key?"
            elif first_line == "deutsch":
                return "Haben Sie einen Lizenzschlüssel?"
            elif first_line == "farsi":
                return "آیا شما یک کلید مجوز دارید؟"
            elif first_line == "russian":
                return "У вас есть лицензионный ключ?"
            elif first_line == "spanish":
                return "¿Tienes una clave de licencia?"
            elif first_line == "chinese":
                return "你有许可证密钥吗？"
            elif first_line == "korean":
                return "라이센스 키가 있나요?"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_bar_9(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "License"
            elif first_line == "deutsch":
                return "Lizenz"
            elif first_line == "farsi":
                return "مجوز"
            elif first_line == "russian":
                return "Лицензия"
            elif first_line == "spanish":
                return "Licencia"
            elif first_line == "chinese":
                return "许可证"
            elif first_line == "korean":
                return "라이센스"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_bar_10(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Online"
            elif first_line == "deutsch":
                return "Online"
            elif first_line == "farsi":
                return "آنلاین"
            elif first_line == "russian":
                return "Онлайн"
            elif first_line == "spanish":
                return "En línea"
            elif first_line == "chinese":
                return "在线"
            elif first_line == "korean":
                return "온라인"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_bar_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Offline"
            elif first_line == "deutsch":
                return "Offline"
            elif first_line == "farsi":
                return "آفلاین"
            elif first_line == "russian":
                return "Офлайн"
            elif first_line == "spanish":
                return "Fuera de línea"
            elif first_line == "chinese":
                return "离线"
            elif first_line == "korean":
                return "오프라인"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_bar_12(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Host unreachable: No internet connection."
            elif first_line == "deutsch":
                return "Host nicht erreichbar: Keine Internetverbindung."
            elif first_line == "farsi":
                return "میزبان قابل دسترسی نیست: اتصال اینترنتی وجود ندارد"
            elif first_line == "russian":
                return "Хост недоступен: Нет интернет-соединения."
            elif first_line == "spanish":
                return "Host inalcanzable: Sin conexión a Internet."
            elif first_line == "chinese":
                return "主机不可达：没有互联网连接。"
            elif first_line == "korean":
                return "호스트에 연결할 수 없습니다: 인터넷 연결이 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_bar_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Socket error occurred: {0}"
            elif first_line == "deutsch":
                return "Socket-Fehler aufgetreten: {0}"
            elif first_line == "farsi":
                return "خطای سوکت رخ داده است: {0}"
            elif first_line == "russian":
                return "Произошла ошибка сокета: {0}"
            elif first_line == "spanish":
                return "Ocurrió un error de socket: {0}"
            elif first_line == "chinese":
                return "发生了套接字错误：{0}"
            elif first_line == "korean":
                return "소켓 오류 발생: {0}"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_bar_14(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unexpected error occurred: {0}"
            elif first_line == "deutsch":
                return "Unerwarteter Fehler aufgetreten: {0}"
            elif first_line == "farsi":
                return "خطای غیرمنتظره رخ داده است: {0}"
            elif first_line == "russian":
                return "Произошла неожиданная ошибка: {0}"
            elif first_line == "spanish":
                return "Ocurrió un error inesperado: {0}"
            elif first_line == "chinese":
                return "发生了意外错误：{0}"
            elif first_line == "korean":
                return "예기치 않은 오류가 발생했습니다: {0}"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_bar_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return " Connection: "
            elif first_line == "deutsch":
                return " Verbindung: "
            elif first_line == "farsi":
                return " اتصال: "
            elif first_line == "russian":
                return " Подключение: "
            elif first_line == "spanish":
                return " Conexión: "
            elif first_line == "chinese":
                return " 连接： "
            elif first_line == "korean":
                return " 연결: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_bar_16(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Your current license key is not valid."
            elif first_line == "deutsch":
                return "Ihr aktueller Lizenzschlüssel ist nicht gültig."
            elif first_line == "farsi":
                return ".کلید مجوز فعلی شما معتبر نیست"
            elif first_line == "russian":
                return "Ваш текущий лицензионный ключ недействителен."
            elif first_line == "spanish":
                return "Su clave de licencia actual no es válida."
            elif first_line == "chinese":
                return "您的当前许可证密钥无效。"
            elif first_line == "korean":
                return "현재 라이선스 키가 유효하지 않습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

#heading   
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