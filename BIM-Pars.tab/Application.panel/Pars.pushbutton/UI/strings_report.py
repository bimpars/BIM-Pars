# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_report.py

def str_rep_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Report"
            elif first_line == "deutsch":
                return "Bericht"
            elif first_line == "farsi":
                return "گزارش"
            elif first_line == "russian":
                return "Отчет"
            elif first_line == "spanish":
                return "Informe"
            elif first_line == "chinese":
                return "展开树"
            elif first_line == "korean":
                return "报告"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Back to toolbox tab"
            elif first_line == "deutsch":
                return "Zurück zum Werkzeugkasten-Tab"
            elif first_line == "farsi":
                return "بازگشت به تب ابزارها"
            elif first_line == "russian":
                return "Назад к вкладке инструментов"
            elif first_line == "spanish":
                return "Volver a la pestaña de herramientas"
            elif first_line == "chinese":
                return "返回工具箱标签"
            elif first_line == "korean":
                return "도구 상자 탭으로 돌아가기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_3(file_path):
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
    
def str_rep_4(file_path):
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
    
def str_rep_5(file_path):
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
    
def str_rep_6(file_path):
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
    
def str_rep_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Color"
            elif first_line == "deutsch":
                return "Farbe"
            elif first_line == "farsi":
                return "رنگ"
            elif first_line == "russian":
                return "Цвет"
            elif first_line == "spanish":
                return "Color"
            elif first_line == "chinese":
                return "颜色"
            elif first_line == "korean":
                return "색상"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Clean"
            elif first_line == "deutsch":
                return "Reinigen"
            elif first_line == "farsi":
                return "پاک کردن"
            elif first_line == "russian":
                return "Очистить"
            elif first_line == "spanish":
                return "Limpiar"
            elif first_line == "chinese":
                return "清理"
            elif first_line == "korean":
                return "청소하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_9(file_path):
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
    
def str_rep_10(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "BIM Pars (coming soon.)"
            elif first_line == "deutsch":
                return "BIM Pars (kommt bald.)"
            elif first_line == "farsi":
                return "BIM Pars (به زودی)"
            elif first_line == "russian":
                return "BIM Pars (скоро.)"
            elif first_line == "spanish":
                return "BIM Pars (próximamente.)"
            elif first_line == "chinese":
                return "BIM Pars（敬请期待。）"
            elif first_line == "korean":
                return "BIM Pars (곧 출시됩니다.)"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    

def str_rep_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Add Column to Right"
            elif first_line == "deutsch":
                return "Spalte nach rechts hinzufügen"
            elif first_line == "farsi":
                return "اضافه کردن ستون به سمت راست"
            elif first_line == "russian":
                return "Добавить столбец справа"
            elif first_line == "spanish":
                return "Añadir columna a la derecha"
            elif first_line == "chinese":
                return "向右添加列"
            elif first_line == "korean":
                return "오른쪽에 열 추가하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_12(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Add Column to Left"
            elif first_line == "deutsch":
                return "Spalte nach links hinzufügen"
            elif first_line == "farsi":
                return "اضافه کردن ستون به سمت چپ"
            elif first_line == "russian":
                return "Добавить столбец слева"
            elif first_line == "spanish":
                return "Añadir columna a la izquierda"
            elif first_line == "chinese":
                return "向左添加列"
            elif first_line == "korean":
                return "왼쪽에 열 추가하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Add Row to Top"
            elif first_line == "deutsch":
                return "Zeile nach oben hinzufügen"
            elif first_line == "farsi":
                return "اضافه کردن ردیف به بالا"
            elif first_line == "russian":
                return "Добавить строку вверху"
            elif first_line == "spanish":
                return "Añadir fila en la parte superior"
            elif first_line == "chinese":
                return "在顶部添加行"
            elif first_line == "korean":
                return "상단에 행 추가하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_14(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Add Row to Bottom"
            elif first_line == "deutsch":
                return "Zeile nach unten hinzufügen"
            elif first_line == "farsi":
                return "اضافه کردن ردیف به پایین"
            elif first_line == "russian":
                return "Добавить строку внизу"
            elif first_line == "spanish":
                return "Añadir fila en la parte inferior"
            elif first_line == "chinese":
                return "在底部添加行"
            elif first_line == "korean":
                return "하단에 행 추가하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Assign Value"
            elif first_line == "deutsch":
                return "Wert zuweisen"
            elif first_line == "farsi":
                return "اختصاص مقدار"
            elif first_line == "russian":
                return "Назначить значение"
            elif first_line == "spanish":
                return "Asignar valor"
            elif first_line == "chinese":
                return "分配值"
            elif first_line == "korean":
                return "값 할당하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_16(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete Selected Rows"
            elif first_line == "deutsch":
                return "Ausgewählte Zeilen löschen"
            elif first_line == "farsi":
                return "حذف ردیف‌های انتخاب شده"
            elif first_line == "russian":
                return "Удалить выбранные строки"
            elif first_line == "spanish":
                return "Eliminar filas seleccionadas"
            elif first_line == "chinese":
                return "删除选定行"
            elif first_line == "korean":
                return "선택한 행 삭제하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_17(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete Selected Columns"
            elif first_line == "deutsch":
                return "Ausgewählte Spalten löschen"
            elif first_line == "farsi":
                return "حذف ستون‌های انتخاب شده"
            elif first_line == "russian":
                return "Удалить выбранные столбцы"
            elif first_line == "spanish":
                return "Eliminar columnas seleccionadas"
            elif first_line == "chinese":
                return "删除选定列"
            elif first_line == "korean":
                return "선택한 열 삭제하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete Hidden Cells"
            elif first_line == "deutsch":
                return "Versteckte Zellen löschen"
            elif first_line == "farsi":
                return "حذف سلول‌های پنهان"
            elif first_line == "russian":
                return "Удалить скрытые ячейки"
            elif first_line == "spanish":
                return "Eliminar celdas ocultas"
            elif first_line == "chinese":
                return "删除隐藏的单元格"
            elif first_line == "korean":
                return "숨겨진 셀 삭제하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_19(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Same Values Color"
            elif first_line == "deutsch":
                return "Farbe gleicher Werte"
            elif first_line == "farsi":
                return"رنگ مقادیر یکسان"
            elif first_line == "russian":
                return "Цвет одинаковых значений"
            elif first_line == "spanish":
                return "Color de valores iguales"
            elif first_line == "chinese":
                return "相同值颜色"
            elif first_line == "korean":
                return "같은 값 색상"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_20(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Same Values Color (Full Sheet)"
            elif first_line == "deutsch":
                return "Farbe gleicher Werte (Gesamtes Blatt)"
            elif first_line == "farsi":
                return "رنگ مقادیر یکسان (کل شیت)"
            elif first_line == "russian":
                return "Цвет одинаковых значений (Полный лист)"
            elif first_line == "spanish":
                return "Color de valores iguales (Hoja completa)"
            elif first_line == "chinese":
                return "相同值颜色（整张表）"
            elif first_line == "korean":
                return "같은 값 색상 (전체 시트)"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Numeric Gradient"
            elif first_line == "deutsch":
                return "Numerischer Verlauf"
            elif first_line == "farsi":
                return "گرادیان عددی"
            elif first_line == "russian":
                return "Числовой градиент"
            elif first_line == "spanish":
                return "Gradiente numérico"
            elif first_line == "chinese":
                return "数值渐变"
            elif first_line == "korean":
                return "수치 그라디언트"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_22(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Paint Selected Cells"
            elif first_line == "deutsch":
                return "Ausgewählte Zellen färben"
            elif first_line == "farsi":
                return "رنگ‌آمیزی سلول‌های انتخاب شده"
            elif first_line == "russian":
                return "Закрасить выбранные ячейки"
            elif first_line == "spanish":
                return "Pintar celdas seleccionadas"
            elif first_line == "chinese":
                return "涂色选定单元格"
            elif first_line == "korean":
                return "선택한 셀 색칠하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_23(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "HTML"
            elif first_line == "deutsch":
                return "HTML"
            elif first_line == "farsi":
                return "HTML"
            elif first_line == "russian":
                return "HTML"
            elif first_line == "spanish":
                return "HTML"
            elif first_line == "chinese":
                return "HTML"
            elif first_line == "korean":
                return "HTML"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_24(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "XLSX"
            elif first_line == "deutsch":
                return "XLSX"
            elif first_line == "farsi":
                return "XLSX"
            elif first_line == "russian":
                return "XLSX"
            elif first_line == "spanish":
                return "XLSX"
            elif first_line == "chinese":
                return "XLSX"
            elif first_line == "korean":
                return "XLSX"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_25(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "CSV"
            elif first_line == "deutsch":
                return "CSV"
            elif first_line == "farsi":
                return "CSV"
            elif first_line == "russian":
                return "CSV"
            elif first_line == "spanish":
                return "CSV"
            elif first_line == "chinese":
                return "CSV"
            elif first_line == "korean":
                return "CSV"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_26(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No data grid found in current tab"
            elif first_line == "deutsch":
                return "Kein Datengitter im aktuellen Tab gefunden"
            elif first_line == "farsi":
                return "جدول داده‌ای در برگه فعلی پیدا نشد"
            elif first_line == "russian":
                return "В текущей вкладке не найдено ни одной таблицы данных"
            elif first_line == "spanish":
                return "No se encontró ninguna cuadrícula de datos en la pestaña actual"
            elif first_line == "chinese":
                return "在当前选项卡中未找到数据网格"
            elif first_line == "korean":
                return "현재 탭에서 데이터 그리드를 찾을 수 없습니다"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_27(file_path):
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
    
def str_rep_28(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Save as HTML"
            elif first_line == "deutsch":
                return "Als HTML speichern"
            elif first_line == "farsi":
                return "HTML ذخیره به عنوان "
            elif first_line == "russian":
                return "Сохранить как HTML"
            elif first_line == "spanish":
                return "Guardar como HTML"
            elif first_line == "chinese":
                return "保存为HTML"
            elif first_line == "korean":
                return "HTML로 저장하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_29(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Save as HTML"
            elif first_line == "deutsch":
                return "Als HTML speichern"
            elif first_line == "farsi":
                return "HTML ذخیره به عنوان "
            elif first_line == "russian":
                return "Сохранить как HTML"
            elif first_line == "spanish":
                return "Guardar como HTML"
            elif first_line == "chinese":
                return "保存为HTML"
            elif first_line == "korean":
                return "HTML로 저장하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_30(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "HTML file created successfully."
            elif first_line == "deutsch":
                return "HTML-Datei erfolgreich erstellt."
            elif first_line == "farsi":
                return "فایل  با موفقیت ایجاد شد HTML"
            elif first_line == "russian":
                return "HTML файл успешно создан."
            elif first_line == "spanish":
                return "Archivo HTML creado con éxito."
            elif first_line == "chinese":
                return "HTML文件创建成功。"
            elif first_line == "korean":
                return "HTML 파일이 성공적으로 생성되었습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_31(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Success"
            elif first_line == "deutsch":
                return "Erfolg"
            elif first_line == "farsi":
                return "موفقیت"
            elif first_line == "russian":
                return "Успех"
            elif first_line == "spanish":
                return "Éxito"
            elif first_line == "chinese":
                return "成功"
            elif first_line == "korean":
                return "성공"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_32(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error creating HTML:"
            elif first_line == "deutsch":
                return "Fehler beim Erstellen von HTML:"
            elif first_line == "farsi":
                return"HTML خطا در ایجاد :"
            elif first_line == "russian":
                return "Ошибка при создании HTML:"
            elif first_line == "spanish":
                return "Error al crear HTML:"
            elif first_line == "chinese":
                return "创建HTML时出错："
            elif first_line == "korean":
                return "HTML 생성 중 오류: "
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_33(file_path):
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
                return "Error"
            elif first_line == "spanish":
                return "Éxito"
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
    
def str_rep_34(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Save Excel File"
            elif first_line == "deutsch":
                return "Excel-Datei speichern"
            elif first_line == "farsi":
                return "ذخیره فایل اکسل"
            elif first_line == "russian":
                return "Сохранить файл Excel"
            elif first_line == "spanish":
                return "Guardar archivo de Excel"
            elif first_line == "chinese":
                return "保存Excel文件"
            elif first_line == "korean":
                return "Excel 파일 저장하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_35(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Excel file created successfully."
            elif first_line == "deutsch":
                return "Excel-Datei erfolgreich erstellt."
            elif first_line == "farsi":
                return "فایل اکسل با موفقیت ایجاد شد"
            elif first_line == "russian":
                return "Файл Excel успешно создан."
            elif first_line == "spanish":
                return "Archivo de Excel creado con éxito."
            elif first_line == "chinese":
                return "Excel文件创建成功。"
            elif first_line == "korean":
                return "Excel 파일이 성공적으로 생성되었습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_36(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error exporting to Excel: {}"
            elif first_line == "deutsch":
                return "Fehler beim Exportieren nach Excel: {}"
            elif first_line == "farsi":
                return "خطا در اکسپوت به اکسل: {}"
            elif first_line == "russian":
                return "Ошибка при экспорте в Excel: {}"
            elif first_line == "spanish":
                return "Error al exportar a Excel: {}"
            elif first_line == "chinese":
                return "导出到Excel时出错：{}"
            elif first_line == "korean":
                return "Excel로 내보내는 중 오류: {}"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_37(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Save CSV File"
            elif first_line == "deutsch":
                return "CSV-Datei speichern"
            elif first_line == "farsi":
                return "CSV ذخیره فایل "
            elif first_line == "russian":
                return "Сохранить файл CSV"
            elif first_line == "spanish":
                return "Guardar archivo CSV"
            elif first_line == "chinese":
                return "保存CSV文件"
            elif first_line == "korean":
                return "CSV 파일 저장하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_38(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "CSV file created successfully."
            elif first_line == "deutsch":
                return "CSV-Datei erfolgreich erstellt."
            elif first_line == "farsi":
                return "فایل  با موفقیت ایجاد شد CSV"
            elif first_line == "russian":
                return "Файл CSV успешно создан."
            elif first_line == "spanish":
                return "Archivo CSV creado con éxito."
            elif first_line == "chinese":
                return "CSV文件创建成功。"
            elif first_line == "korean":
                return "CSV 파일이 성공적으로 생성되었습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def str_rep_39(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error exporting to CSV: {}"
            elif first_line == "deutsch":
                return "Fehler beim Exportieren nach CSV: {}"
            elif first_line == "farsi":
                return "CSV خطا در اکسپورت به : {}"
            elif first_line == "russian":
                return "Ошибка при экспорте в CSV: {}"
            elif first_line == "spanish":
                return "Error al exportar a CSV: {}"
            elif first_line == "chinese":
                return "导出到CSV时出错：{}"
            elif first_line == "korean":
                return "CSV로 내보내는 중 오류: {}"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_40(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Apply"
            elif first_line == "deutsch":
                return "Anwenden"
            elif first_line == "farsi":
                return "اعمال"
            elif first_line == "russian":
                return "Применить"
            elif first_line == "spanish":
                return "Aplicar"
            elif first_line == "chinese":
                return "应用"
            elif first_line == "korean":
                return "적용하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_41(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Groups"
            elif first_line == "deutsch":
                return "Gruppen"
            elif first_line == "farsi":
                return "گروه‌ها"
            elif first_line == "russian":
                return "Группы"
            elif first_line == "spanish":
                return "Grupos"
            elif first_line == "chinese":
                return "组"
            elif first_line == "korean":
                return "그룹"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_42(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Looking for:"
            elif first_line == "deutsch":
                return "Suche nach:"
            elif first_line == "farsi":
                return "در جستجوی:"
            elif first_line == "russian":
                return "Ищем:"
            elif first_line == "spanish":
                return "Buscando:"
            elif first_line == "chinese":
                return "寻找："
            elif first_line == "korean":
                return "찾고 있는:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_43(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Search Results"
            elif first_line == "deutsch":
                return "Suchergebnisse"
            elif first_line == "farsi":
                return "نتایج جستجو"
            elif first_line == "russian":
                return "Результаты поиска"
            elif first_line == "spanish":
                return "Resultados de búsqueda"
            elif first_line == "chinese":
                return "搜索结果"
            elif first_line == "korean":
                return "검색 결과"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_44(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Found and selected {} cell(s) with value '{}'"
            elif first_line == "deutsch":
                return "{} Zelle(n) mit dem Wert '{}' gefunden und ausgewählt"
            elif first_line == "farsi":
                return "{}پیدا و انتخاب شد  '{}' سلول با مقدار " 
            elif first_line == "russian":
                return "Найдены и выбраны {} ячейки со значением '{}'"
            elif first_line == "spanish":
                return "Se encontraron y seleccionaron {} celda(s) con el valor '{}'"
            elif first_line == "chinese":
                return "找到并选择了 {} 个值为 '{}' 的单元格"
            elif first_line == "korean":
                return "값이 '{}'인 {} 셀을 찾고 선택했습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_45(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No cells with value '{}' were found"
            elif first_line == "deutsch":
                return "Es wurden keine Zellen mit dem Wert '{}' gefunden"
            elif first_line == "farsi":
                return ".پیدا نشد '{}' هیچ سلولی با مقدار  "
            elif first_line == "russian":
                return "Ячейки со значением '{}' не найдены"
            elif first_line == "spanish":
                return "No se encontraron celdas con el valor '{}'"
            elif first_line == "chinese":
                return "未找到值为 '{}' 的单元格"
            elif first_line == "korean":
                return "값이 '{}'인 셀을 찾을 수 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_46(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "New Column"
            elif first_line == "deutsch":
                return "Neue Spalte"
            elif first_line == "farsi":
                return "ستون جدید"
            elif first_line == "russian":
                return "Новый столбец"
            elif first_line == "spanish":
                return "Nueva columna"
            elif first_line == "chinese":
                return "新列"
            elif first_line == "korean":
                return "새 열"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_47(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "New column added successfully. Double-click the header to rename."
            elif first_line == "deutsch":
                return "Neue Spalte erfolgreich hinzugefügt. Doppelklicken Sie auf den Header, um ihn umzubenennen."
            elif first_line == "farsi":
                return " .ستون جدید با موفقیت اضافه شد. برای تغییر نام، دو بار روی سرستون کلیک کنید"
            elif first_line == "russian":
                return "Новый столбец успешно добавлен. Дважды щелкните заголовок, чтобы переименовать."
            elif first_line == "spanish":
                return "Nueva columna añadida con éxito. Haga doble clic en el encabezado para renombrar."
            elif first_line == "chinese":
                return "新列成功添加。双击标题以重命名。"
            elif first_line == "korean":
                return "새 열이 성공적으로 추가되었습니다. 헤더를 두 번 클릭하여 이름을 변경하세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_48(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "New row added successfully."
            elif first_line == "deutsch":
                return "Neue Zeile erfolgreich hinzugefügt."
            elif first_line == "farsi":
                return ".ردیف جدید با موفقیت اضافه شد"
            elif first_line == "russian":
                return "Новая строка успешно добавлена."
            elif first_line == "spanish":
                return "Nueva fila añadida con éxito."
            elif first_line == "chinese":
                return "新行成功添加。"
            elif first_line == "korean":
                return "새 행이 성공적으로 추가되었습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_49(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please select cells to assign value."
            elif first_line == "deutsch":
                return "Bitte wählen Sie Zellen aus, um einen Wert zuzuweisen."
            elif first_line == "farsi":
                return ".لطفاً سلول‌هایی را برای اختصاص مقدار انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, выберите ячейки для назначения значения."
            elif first_line == "spanish":
                return "Por favor, seleccione celdas para asignar un valor."
            elif first_line == "chinese":
                return "请选择单元格以分配值。"
            elif first_line == "korean":
                return "값을 할당할 셀을 선택하세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_50(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please select cells to assign value."
            elif first_line == "deutsch":
                return "Bitte wählen Sie Zellen aus, um einen Wert zuzuweisen."
            elif first_line == "farsi":
                return ".لطفاً سلول‌هایی را برای اختصاص مقدار انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, выберите ячейки для назначения значения."
            elif first_line == "spanish":
                return "Por favor, seleccione celdas para asignar un valor."
            elif first_line == "chinese":
                return "请选择单元格以分配值。"
            elif first_line == "korean":
                return "값을 할당할 셀을 선택하세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_50(file_path):
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
                return "값："
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_51(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Assign"
            elif first_line == "deutsch":
                return "Zuweisen"
            elif first_line == "farsi":
                return "اختصاص دادن"
            elif first_line == "russian":
                return "Назначить"
            elif first_line == "spanish":
                return "Asignar"
            elif first_line == "chinese":
                return "分配"
            elif first_line == "korean":
                return "할당하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_52(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Value '{}' set for {} editable cell(s)"
            elif first_line == "deutsch":
                return "Wert '{}' für {} bearbeitbare Zelle(n) festgelegt"
            elif first_line == "farsi":
                return "'{}' \nبرای {} سلول قابل ویرایش تنظیم شد"
            elif first_line == "russian":
                return "Значение '{}' установлено для {} редактируемых ячеек"
            elif first_line == "spanish":
                return "Valor '{}' establecido para {} celda(s) editable(s)"
            elif first_line == "chinese":
                return "值 '{}' 为 {} 个可编辑单元格设置"
            elif first_line == "korean":
                return "값 '{}'가 {}개의 편집 가능한 셀에 설정되었습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_53(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No editable cells were found in selection."
            elif first_line == "deutsch":
                return "Es wurden keine bearbeitbaren Zellen in der Auswahl gefunden."
            elif first_line == "farsi":
                return ".هیچ سلول قابل ویرایشی در انتخاب پیدا نشد "
            elif first_line == "russian":
                return "В выбранной области не найдено редактируемых ячеек."
            elif first_line == "spanish":
                return "No se encontraron celdas editables en la selección."
            elif first_line == "chinese":
                return "在选择中未找到可编辑单元格。"
            elif first_line == "korean":
                return "선택 항목에서 편집 가능한 셀을 찾을 수 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_54(file_path):
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
                return "No se encontraron celdas editables en la selección."
            elif first_line == "chinese":
                return "在选择中未找到可编辑单元格。"
            elif first_line == "korean":
                return "선택 항목에서 편집 가능한 셀을 찾을 수 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_55(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error editing header:"
            elif first_line == "deutsch":
                return "Fehler beim Bearbeiten des Headers:"
            elif first_line == "farsi":
                return "خطا در ویرایش سربرگ:"
            elif first_line == "russian":
                return "Ошибка при редактировании заголовка:"
            elif first_line == "spanish":
                return "Error al editar el encabezado:"
            elif first_line == "chinese":
                return "编辑标题时出错："
            elif first_line == "korean":
                return "헤더 편집 중 오류:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_56(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Are you sure you want to delete the selected rows?"
            elif first_line == "deutsch":
                return "Sind Sie sicher, dass Sie die ausgewählten Zeilen löschen möchten?"
            elif first_line == "farsi":
                return "آیا مطمئن هستید که می‌خواهید ردیف‌های انتخاب شده را حذف کنید؟"
            elif first_line == "russian":
                return "Вы уверены, что хотите удалить выбранные строки?"
            elif first_line == "spanish":
                return "¿Está seguro de que desea eliminar las filas seleccionadas?"
            elif first_line == "chinese":
                return "您确定要删除选定的行吗？"
            elif first_line == "korean":
                return "선택한 행을 삭제하시겠습니까?"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_57(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Confirm Delete"
            elif first_line == "deutsch":
                return "Löschen bestätigen"
            elif first_line == "farsi":
                return "تأیید حذف"
            elif first_line == "russian":
                return "Подтвердить удаление"
            elif first_line == "spanish":
                return "Confirmar eliminación"
            elif first_line == "chinese":
                return "确认删除"
            elif first_line == "korean":
                return "삭제 확인"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_58(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Selected rows have been deleted."
            elif first_line == "deutsch":
                return "Ausgewählte Zeilen wurden gelöscht."
            elif first_line == "farsi":
                return ".ردیف‌های انتخاب شده حذف شدند"
            elif first_line == "russian":
                return "Выбранные строки были удалены."
            elif first_line == "spanish":
                return "Las filas seleccionadas han sido eliminadas."
            elif first_line == "chinese":
                return "选定的行已被删除。"
            elif first_line == "korean":
                return "선택한 행이 삭제되었습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_59(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error deleting rows:"
            elif first_line == "deutsch":
                return "Fehler beim Löschen der Zeilen:"
            elif first_line == "farsi":
                return "خطا در حذف ردیف‌ها:"
            elif first_line == "russian":
                return "Ошибка при удалении строк:"
            elif first_line == "spanish":
                return "Error al eliminar filas:"
            elif first_line == "chinese":
                return "删除行时出错："
            elif first_line == "korean":
                return "행 삭제 중 오류:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_60(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Selected columns have been deleted."
            elif first_line == "deutsch":
                return "Ausgewählte Spalten wurden gelöscht."
            elif first_line == "farsi":
                return ".ستون‌های انتخاب شده حذف شدند"
            elif first_line == "russian":
                return "Выбранные столбцы были удалены."
            elif first_line == "spanish":
                return "Las columnas seleccionadas han sido eliminadas."
            elif first_line == "chinese":
                return "选定的列已被删除。"
            elif first_line == "korean":
                return "선택한 열이 삭제되었습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_61(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please select at least one column to delete."
            elif first_line == "deutsch":
                return "Bitte wählen Sie mindestens eine Spalte zum Löschen aus."
            elif first_line == "farsi":
                return ".لطفاً حداقل یک ستون را برای حذف انتخاب کنید "
            elif first_line == "russian":
                return "Пожалуйста, выберите хотя бы один столбец для удаления."
            elif first_line == "spanish":
                return "Por favor, seleccione al menos una columna para eliminar."
            elif first_line == "chinese":
                return "请至少选择一列进行删除。"
            elif first_line == "korean":
                return "삭제할 열을 최소한 하나 선택하세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_62(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error deleting columns:"
            elif first_line == "deutsch":
                return "Fehler beim Löschen der Spalten:"
            elif first_line == "farsi":
                return "خطا در حذف ستون‌ها:"
            elif first_line == "russian":
                return "Ошибка при удалении столбцов:"
            elif first_line == "spanish":
                return "Error al eliminar columnas:"
            elif first_line == "chinese":
                return "删除列时出错："
            elif first_line == "korean":
                return "열 삭제 중 오류:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_63(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Are you sure you want to delete the selected columns?"
            elif first_line == "deutsch":
                return "Sind Sie sicher, dass Sie die ausgewählten Spalten löschen möchten?"
            elif first_line == "farsi":
                return "آیا مطمئن هستید که می‌خواهید ستون‌های انتخاب شده را حذف کنید؟"
            elif first_line == "russian":
                return "Вы уверены, что хотите удалить выбранные столбцы?"
            elif first_line == "spanish":
                return "¿Está seguro de que desea eliminar las columnas seleccionadas?"
            elif first_line == "chinese":
                return "您确定要删除选定的列吗？"
            elif first_line == "korean":
                return "선택한 열을 삭제하시겠습니까?"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_64(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No columns left in the table."
            elif first_line == "deutsch":
                return "Keine Spalten mehr in der Tabelle."
            elif first_line == "farsi":
                return ".هیچ ستونی در جدول باقی نمانده است"
            elif first_line == "russian":
                return "В таблице не осталось столбцов."
            elif first_line == "spanish":
                return "No quedan columnas en la tabla."
            elif first_line == "chinese":
                return "表中没有剩余列。"
            elif first_line == "korean":
                return "테이블에 남은 열이 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_65(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No rows left in the table."
            elif first_line == "deutsch":
                return "Keine Zeilen mehr in der Tabelle."
            elif first_line == "farsi":
                return ".هیچ ردیفی در جدول باقی نمانده است"
            elif first_line == "russian":
                return "В таблице не осталось строк."
            elif first_line == "spanish":
                return "No quedan filas en la tabla."
            elif first_line == "chinese":
                return "表中没有剩余行。"
            elif first_line == "korean":
                return "테이블에 남은 행이 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_66(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Are you sure you want to delete all hidden rows?\nThis action cannot be undone."
            elif first_line == "deutsch":
                return "Sind Sie sicher, dass Sie alle versteckten Zeilen löschen möchten?\nDiese Aktion kann nicht rückgängig gemacht werden."
            elif first_line == "farsi":
                return "آیا مطمئن هستید که می‌خواهید تمام ردیف‌های پنهان را حذف کنید؟\nاین عمل قابل بازگشت نیست"
            elif first_line == "russian":
                return "Вы уверены, что хотите удалить все скрытые строки?\nЭто действие нельзя отменить."
            elif first_line == "spanish":
                return "¿Está seguro de que desea eliminar todas las filas ocultas?\nEsta acción no se puede deshacer."
            elif first_line == "chinese":
                return "您确定要删除所有隐藏的行吗？\n此操作无法撤消。"
            elif first_line == "korean":
                return "모든 숨겨진 행을 삭제하시겠습니까?\n이 작업은 취소할 수 없습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_67(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Hidden rows have been removed.\nRemaining rows:"
            elif first_line == "deutsch":
                return "Versteckte Zeilen wurden entfernt.\nVerbleibende Zeilen:"
            elif first_line == "farsi":
                return "ردیف‌های پنهان حذف شدند.\nردیف‌های باقی‌مانده:"
            elif first_line == "russian":
                return "Скрытые строки были удалены.\nОставшиеся строки:"
            elif first_line == "spanish":
                return "Se han eliminado las filas ocultas.\nFilas restantes:"
            elif first_line == "chinese":
                return "隐藏的行已被删除。\n剩余行："
            elif first_line == "korean":
                return "숨겨진 행이 제거되었습니다.\n남은 행:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_68(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error deleting hidden rows:"
            elif first_line == "deutsch":
                return "Fehler beim Löschen versteckter Zeilen:"
            elif first_line == "farsi":
                return "خطا در حذف ردیف‌های پنهان:"
            elif first_line == "russian":
                return "Ошибка при удалении скрытых строк:"
            elif first_line == "spanish":
                return "Error al eliminar filas ocultas:"
            elif first_line == "chinese":
                return "删除隐藏行时出错："
            elif first_line == "korean":
                return "숨겨진 행 삭제 중 오류:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_69(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please select at least one cell in the columns first."
            elif first_line == "deutsch":
                return "Bitte wählen Sie zuerst mindestens eine Zelle in den Spalten aus."
            elif first_line == "farsi":
                return ".لطفاً ابتدا حداقل یک سلول در ستون‌ها را انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, сначала выберите хотя бы одну ячейку в столбцах."
            elif first_line == "spanish":
                return "Por favor, seleccione primero al menos una celda en las columnas."
            elif first_line == "chinese":
                return "请先在列中选择至少一个单元格。"
            elif first_line == "korean":
                return "먼저 열에서 최소한 하나의 셀을 선택하세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_70(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error applying colors:"
            elif first_line == "deutsch":
                return "Fehler beim Anwenden der Farben:"
            elif first_line == "farsi":
                return "خطا در اعمال رنگ‌ها:"
            elif first_line == "russian":
                return "Ошибка при применении цветов:"
            elif first_line == "spanish":
                return "Error al aplicar colores:"
            elif first_line == "chinese":
                return "应用颜色时出错："
            elif first_line == "korean":
                return "색상 적용 중 오류:"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_71(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please select a column first."
            elif first_line == "deutsch":
                return "Bitte wählen Sie zuerst eine Spalte aus."
            elif first_line == "farsi":
                return ".لطفاً ابتدا یک ستون را انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, сначала выберите столбец."
            elif first_line == "spanish":
                return "Por favor, seleccione primero una columna."
            elif first_line == "chinese":
                return "请先选择一列。"
            elif first_line == "korean":
                return "먼저 열을 선택하세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_72(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Selected column must contain numeric values only."
            elif first_line == "deutsch":
                return "Die ausgewählte Spalte darf nur numerische Werte enthalten."
            elif first_line == "farsi":
                return ".ستون انتخاب شده باید فقط شامل مقادیر عددی باشد"
            elif first_line == "russian":
                return "Выбранный столбец должен содержать только числовые значения."
            elif first_line == "spanish":
                return "La columna seleccionada debe contener solo valores numéricos."
            elif first_line == "chinese":
                return "选定的列必须仅包含数值。"
            elif first_line == "korean":
                return "선택한 열에는 숫자 값만 포함되어야 합니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_73(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error applying gradient"
            elif first_line == "deutsch":
                return "Fehler beim Anwenden des Verlaufs"
            elif first_line == "farsi":
                return "خطا در اعمال گرادیان"
            elif first_line == "russian":
                return "Ошибка при применении градиента"
            elif first_line == "spanish":
                return "Error al aplicar el degradado"
            elif first_line == "chinese":
                return "应用渐变时出错"
            elif first_line == "korean":
                return "그라디언트 적용 중 오류"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_74(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Please select cells to paint."
            elif first_line == "deutsch":
                return "Bitte wählen Sie Zellen zum Färben aus."
            elif first_line == "farsi":
                return ".لطفاً سلول‌هایی را برای رنگ‌آمیزی انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, выберите ячейки для окраски."
            elif first_line == "spanish":
                return "Por favor, seleccione celdas para pintar."
            elif first_line == "chinese":
                return "请选择要上色的单元格。"
            elif first_line == "korean":
                return "칠할 셀을 선택하세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_75(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error applying colors"
            elif first_line == "deutsch":
                return "Fehler beim Anwenden der Farben"
            elif first_line == "farsi":
                return "خطا در اعمال رنگ‌ها:"
            elif first_line == "russian":
                return "Ошибка при применении цветов"
            elif first_line == "spanish":
                return "Error al aplicar colores"
            elif first_line == "chinese":
                return "应用颜色时出错"
            elif first_line == "korean":
                return "색상 적용 중 오류"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_76(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "All cell colors have been cleared."
            elif first_line == "deutsch":
                return "Alle Zellfarben wurden gelöscht."
            elif first_line == "farsi":
                return ".تمام رنگ‌های سلول‌ها حذف شدند"
            elif first_line == "russian":
                return "Все цвета ячеек были сброшены."
            elif first_line == "spanish":
                return "Todos los colores de las celdas han sido eliminados."
            elif first_line == "chinese":
                return "所有单元格颜色已被清除。"
            elif first_line == "korean":
                return "모든 셀 색상이 지워졌습니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

def str_rep_77(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Error clearing colors."
            elif first_line == "deutsch":
                return "Fehler beim Löschen der Farben."
            elif first_line == "farsi":
                return ".خطا در حذف رنگ‌ها"
            elif first_line == "russian":
                return "Ошибка при очистке цветов."
            elif first_line == "spanish":
                return "Error al limpiar los colores."
            elif first_line == "chinese":
                return "清除颜色时出错。"
            elif first_line == "korean":
                return "색상 지우기 중 오류."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"

#tool tips
def tip_rep_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Back to toolbox tab"
            elif first_line == "deutsch":
                return "Zurück zum Werkzeugkasten-Tab"
            elif first_line == "farsi":
                return "بازگشت به تب ابزارها"
            elif first_line == "russian":
                return "Назад к вкладке инструментов"
            elif first_line == "spanish":
                return "Volver a la pestaña de herramientas"
            elif first_line == "chinese":
                return "返回工具箱标签"
            elif first_line == "korean":
                return "도구 상자 탭으로 돌아가기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_2(file_path):
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
    
def tip_rep_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Print"
            elif first_line == "deutsch":
                return "Drucken"
            elif first_line == "farsi":
                return "چاپ"
            elif first_line == "russian":
                return "Печать"
            elif first_line == "spanish":
                return "Imprimir"
            elif first_line == "chinese":
                return "打印"
            elif first_line == "korean":
                return "인쇄"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Export report table as HTML (colors preserved)"
            elif first_line == "deutsch":
                return "Berichtstabelle als HTML exportieren (Farben beibehalten)"
            elif first_line == "farsi":
                return "خروجی جدول گزارش به 'اچ تی ام ال' (رنگ‌ها حفظ می‌شوند)"
            elif first_line == "russian":
                return "Экспортировать таблицу отчета в HTML (цвета сохранены)"
            elif first_line == "spanish":
                return "Exportar tabla de informe como HTML (colores preservados)"
            elif first_line == "chinese":
                return "将报告表导出为HTML（保留颜色）"
            elif first_line == "korean":
                return "색상이 유지된 HTML로 보고서 테이블 내보내기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_5(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Export report table as Excel (colors preserved)"
            elif first_line == "deutsch":
                return "Berichtstabelle als Excel exportieren (Farben beibehalten)"
            elif first_line == "farsi":
                return "خروجی جدول گزارش به اکسل (رنگ‌ها حفظ می‌شوند)"
            elif first_line == "russian":
                return "Экспортировать таблицу отчета в Excel (цвета сохранены)"
            elif first_line == "spanish":
                return "Exportar tabla de informe como Excel (colores preservados)"
            elif first_line == "chinese":
                return "将报告表导出为Excel（保留颜色）"
            elif first_line == "korean":
                return "색상이 유지된 Excel로 보고서 테이블 내보내기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_6(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Export report table as CSV (colors not preserved)"
            elif first_line == "deutsch":
                return "Berichtstabelle als CSV exportieren (Farben nicht beibehalten)"
            elif first_line == "farsi":
                return "خروجی جدول گزارش به 'سی اس وی' (رنگ‌ها حفظ می‌شوند)"
            elif first_line == "russian":
                return "Экспортировать таблицу отчета в CSV (цвета не сохранены)"
            elif first_line == "spanish":
                return "Exportar tabla de informe como CSV (colores no preservados)"
            elif first_line == "chinese":
                return "将报告表导出为CSV（不保留颜色）"
            elif first_line == "korean":
                return "색상이 유지되지 않는 CSV로 보고서 테이블 내보내기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_7(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Print report table in pyRevit output window which can be saved as PDF or HTML."
            elif first_line == "deutsch":
                return "Berichtstabelle im pyRevit-Ausgabefenster drucken, die als PDF oder HTML gespeichert werden kann."
            elif first_line == "farsi":
                return "چاپ جدول گزارش در پنجره خروجی 'پای-رویت' که می‌توان آن را به عنوان 'پی دی اف' یا 'اچ تی ام ال' ذخیره کرد."
            elif first_line == "russian":
                return "Распечатать таблицу отчета в окне вывода pyRevit, которую можно сохранить как PDF или HTML."
            elif first_line == "spanish":
                return "Imprimir tabla de informe en la ventana de salida de pyRevit, que se puede guardar como PDF o HTML."
            elif first_line == "chinese":
                return "在pyRevit输出窗口中打印报告表，可以保存为PDF或HTML。"
            elif first_line == "korean":
                return "PDF 또는 HTML로 저장할 수 있는 pyRevit 출력 창에서 보고서 테이블 인쇄하기."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "BIM Pars print (Coming soon)"
            elif first_line == "deutsch":
                return "BIM Pars-Druck (kommt bald)"
            elif first_line == "farsi":
                return "چاپ بیم پارس (به زودی)"
            elif first_line == "russian":
                return "Печать BIM Pars (скоро)"
            elif first_line == "spanish":
                return "Impresión de BIM Pars (próximamente)"
            elif first_line == "chinese":
                return "BIM Pars 打印（敬请期待）"
            elif first_line == "korean":
                return "BIM Pars 인쇄 (곧 출시됩니다)"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_9(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Filter report table (Unnecessary data and cells will be hidden)"
            elif first_line == "deutsch":
                return "Berichtstabelle filtern (Unnötige Daten und Zellen werden ausgeblendet)"
            elif first_line == "farsi":
                return "فیلتر جدول گزارش (داده‌ها و سلول‌های غیرضروری پنهان خواهند شد)"
            elif first_line == "russian":
                return "Фильтровать таблицу отчета (Ненужные данные и ячейки будут скрыты)"
            elif first_line == "spanish":
                return "Filtrar la tabla de informe (los datos y celdas innecesarios se ocultarán)"
            elif first_line == "chinese":
                return "过滤报告表（不必要的数据和单元格将被隐藏）"
            elif first_line == "korean":
                return "보고서 테이블 필터링 (불필요한 데이터와 셀이 숨겨집니다)"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_10(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Search specific value inside report table and select their cells"
            elif first_line == "deutsch":
                return "Nach spezifischem Wert in der Berichtstabelle suchen und die entsprechenden Zellen auswählen"
            elif first_line == "farsi":
                return "جستجوی مقدار خاص در جدول گزارش و انتخاب سلول‌های آن"
            elif first_line == "russian":
                return "Искать конкретное значение в таблице отчета и выделять его ячейки"
            elif first_line == "spanish":
                return "Buscar un valor específico dentro de la tabla de informe y seleccionar sus celdas"
            elif first_line == "chinese":
                return "在报告表中搜索特定值并选择其单元格"
            elif first_line == "korean":
                return "보고서 테이블에서 특정 값을 검색하고 해당 셀 선택하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Add a new editable column to the right of selected column"
            elif first_line == "deutsch":
                return "Eine neue bearbeitbare Spalte rechts von der ausgewählten Spalte hinzufügen"
            elif first_line == "farsi":
                return "یک ستون جدید قابل ویرایش به سمت راست ستون انتخاب شده اضافه کنید"
            elif first_line == "russian":
                return "Добавить новый редактируемый столбец справа от выбранного столбца"
            elif first_line == "spanish":
                return "Añadir una nueva columna editable a la derecha de la columna seleccionada"
            elif first_line == "chinese":
                return "在选定列的右侧添加一个新的可编辑列"
            elif first_line == "korean":
                return "선택한 열의 오른쪽에 새로 편집 가능한 열 추가하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_12(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Add a new editable column to the left of selected column"
            elif first_line == "deutsch":
                return "Eine neue bearbeitbare Spalte links von der ausgewählten Spalte hinzufügen"
            elif first_line == "farsi":
                return "یک ستون جدید قابل ویرایش به سمت چپ ستون انتخاب شده اضافه کنید"
            elif first_line == "russian":
                return "Добавить новый редактируемый столбец слева от выбранного столбца"
            elif first_line == "spanish":
                return "Añadir una nueva columna editable a la izquierda de la columna seleccionada"
            elif first_line == "chinese":
                return "在选定列的左侧添加一个新的可编辑列"
            elif first_line == "korean":
                return "선택한 열의 왼쪽에 새로 편집 가능한 열 추가하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Add a new editable row above the selected row"
            elif first_line == "deutsch":
                return "Eine neue bearbeitbare Zeile über der ausgewählten Zeile hinzufügen"
            elif first_line == "farsi":
                return "یک ردیف جدید قابل ویرایش بالای ردیف انتخاب شده اضافه کنید"
            elif first_line == "russian":
                return "Добавить новую редактируемую строку выше выбранной строки"
            elif first_line == "spanish":
                return "Añadir una nueva fila editable encima de la fila seleccionada"
            elif first_line == "chinese":
                return "在选定行上方添加一个新的可编辑行"
            elif first_line == "korean":
                return "선택한 행 위에 새로 편집 가능한 행 추가하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_14(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Add a new editable row below the selected row"
            elif first_line == "deutsch":
                return "Eine neue bearbeitbare Zeile unter der ausgewählten Zeile hinzufügen"
            elif first_line == "farsi":
                return "یک ردیف جدید قابل ویرایش زیر ردیف انتخاب شده اضافه کنید"
            elif first_line == "russian":
                return "Добавить новую редактируемую строку под выбранной строкой"
            elif first_line == "spanish":
                return "Añadir una nueva fila editable debajo de la fila seleccionada"
            elif first_line == "chinese":
                return "在选定行下方添加一个新的可编辑行"
            elif first_line == "korean":
                return "선택한 행 아래에 새로 편집 가능한 행 추가하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Assign desired value for selected editable cells"
            elif first_line == "deutsch":
                return "Gewünschten Wert für ausgewählte bearbeitbare Zellen zuweisen"
            elif first_line == "farsi":
                return "مقدار مورد نظر را برای سلول‌های قابل ویرایش انتخاب شده اختصاص دهید"
            elif first_line == "russian":
                return "Назначить желаемое значение для выбранных редактируемых ячеек"
            elif first_line == "spanish":
                return "Asignar el valor deseado a las celdas editables seleccionadas"
            elif first_line == "chinese":
                return "为选定的可编辑单元格分配所需值"
            elif first_line == "korean":
                return "선택한 편집 가능한 셀에 원하는 값 할당하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_16(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete selected rows from the grid.\nTo select rows:\n- Click row header (leftmost cell)\n- Shift+Click for multiple rows\n- Ctrl+Click for non-adjacent rows"
            elif first_line == "deutsch":
                return "Ausgewählte Zeilen aus dem Raster löschen.\nUm Zeilen auszuwählen:\n- Klicken Sie auf den Zeilenkopf (linke Zelle)\n- Shift+Klicken für mehrere Zeilen\n- Ctrl+Klicken für nicht benachbarte Zeilen"
            elif first_line == "farsi":
                return "ردیف‌های انتخاب شده را از جدول حذف کنید.\nبرای انتخاب ردیف‌ها:\n- روی سرستون ردیف کلیک کنید (سلول سمت چپ)\n- برای انتخاب چند ردیف Shift+Click\n- برای انتخاب ردیف‌های غیرمجاور Ctrl+Click"
            elif first_line == "russian":
                return "Удалить выбранные строки из сетки.\nЧтобы выбрать строки:\n- Щелкните на заголовок строки (самая левая ячейка)\n- Shift+Щелчок для нескольких строк\n- Ctrl+Щелчок для разрозненных строк"
            elif first_line == "spanish":
                return "Eliminar filas seleccionadas de la cuadrícula.\nPara seleccionar filas:\n- Haga clic en el encabezado de la fila (la celda más a la izquierda)\n- Shift+clic para múltiples filas\n- Ctrl+clic para filas no adyacentes"
            elif first_line == "chinese":
                return "从网格中删除选定的行。\n选择行的方法：\n- 点击行标题（最左侧单元格）\n- Shift+点击选择多行\n- Ctrl+点击选择不相邻的行"
            elif first_line == "korean":
                return "그리드에서 선택한 행 삭제하기.\n행 선택 방법:\n- 행 헤더(가장 왼쪽 셀)를 클릭하세요.\n- 여러 행 선택을 위해 Shift+클릭하세요.\n- 비연속 행 선택을 위해 Ctrl+클릭하세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_17(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete selected columns from the grid.\nTo select columns:\n- Click column header\n- Click cells in column\n- Ctrl+Click for multiple columns"
            elif first_line == "deutsch":
                return "Ausgewählte Spalten aus dem Raster löschen.\nUm Spalten auszuwählen:\n- Klicken Sie auf den Spaltenkopf\n- Klicken Sie auf Zellen in der Spalte\n- Ctrl+Klicken für mehrere Spalten"
            elif first_line == "farsi":
                return "ستون‌های انتخاب شده را از جدول حذف کنید.\nبرای انتخاب ستون‌ها:\n- روی سرستون کلیک کنید\n- روی سلول‌های ستون کلیک کنید\n- برای انتخاب چند ستون Ctrl+Click"
            elif first_line == "russian":
                return "Удалить выбранные столбцы из сетки.\nЧтобы выбрать столбцы:\n- Щелкните на заголовок столбца\n- Щелкните на ячейки в столбце\n- Ctrl+Щелчок для нескольких столбцов"
            elif first_line == "spanish":
                return "Eliminar columnas seleccionadas de la cuadrícula.\nPara seleccionar columnas:\n- Haga clic en el encabezado de la columna\n- Haga clic en las celdas de la columna\n- Ctrl+clic para múltiples columnas"
            elif first_line == "chinese":
                return "从网格中删除选定的列。\n选择列的方法：\n- 点击列标题\n- 点击列中的单元格\n- Ctrl+点击选择多列"
            elif first_line == "korean":
                return "그리드에서 선택한 열 삭제하기.\n열 선택 방법:\n- 열 헤더를 클릭하세요.\n- 열의 셀을 클릭하세요.\n- 여러 열 선택을 위해 Ctrl+클릭하세요."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Delete hidden cells from the grid.\nAll the cells that are visible will remain and the rest will be removed from the grid."
            elif first_line == "deutsch":
                return "Versteckte Zellen aus dem Raster löschen.\nAlle sichtbaren Zellen bleiben erhalten, die restlichen werden aus dem Raster entfernt."
            elif first_line == "farsi":
                return ".سلول‌های پنهان را از جدول حذف کنید\nتمام سلول‌های قابل مشاهده باقی خواهند ماند و بقیه از جدول حذف خواهند شد"
            elif first_line == "russian":
                return "Удалить скрытые ячейки из сетки.\nВсе видимые ячейки останутся, а остальные будут удалены из сетки."
            elif first_line == "spanish":
                return "Eliminar celdas ocultas de la cuadrícula.\nTodas las celdas que son visibles permanecerán y el resto se eliminará de la cuadrícula."
            elif first_line == "chinese":
                return "从网格中删除隐藏的单元格。\n所有可见的单元格将保留，其余的将从网格中删除。"
            elif first_line == "korean":
                return "그리드에서 숨겨진 셀 삭제하기.\n모든 가시적인 셀은 남아 있고 나머지는 그리드에서 제거됩니다."
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_19(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Apply same random color to same values in selected columns"
            elif first_line == "deutsch":
                return "Den gleichen zufälligen Farbton auf gleiche Werte in den ausgewählten Spalten anwenden"
            elif first_line == "farsi":
                return "رنگ تصادفی یکسان را به مقادیر مشابه در ستون‌های انتخاب شده اعمال کنید"
            elif first_line == "russian":
                return "Применить один и тот же случайный цвет к одинаковым значениям в выбранных столбцах"
            elif first_line == "spanish":
                return "Aplicar el mismo color aleatorio a los mismos valores en las columnas seleccionadas"
            elif first_line == "chinese":
                return "将相同的随机颜色应用于选定列中的相同值"
            elif first_line == "korean":
                return "선택한 열의 동일한 값에 동일한 무작위 색상 적용하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_20(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Apply same random color to same values in sheet"
            elif first_line == "deutsch":
                return "Den gleichen zufälligen Farbton auf gleiche Werte im Blatt anwenden"
            elif first_line == "farsi":
                return "رنگ تصادفی یکسان را به مقادیر مشابه در شیت اعمال کنید"
            elif first_line == "russian":
                return "Применить один и тот же случайный цвет к одинаковым значениям на листе"
            elif first_line == "spanish":
                return "Aplicar el mismo color aleatorio a los mismos valores en la hoja"
            elif first_line == "chinese":
                return "将相同的随机颜色应用于工作表中的相同值"
            elif first_line == "korean":
                return "시트의 동일한 값에 동일한 무작위 색상 적용하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_21(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Apply gradient color from light to dark based on numeric values"
            elif first_line == "deutsch":
                return "Farbverlauf von hell nach dunkel basierend auf numerischen Werten anwenden"
            elif first_line == "farsi":
                return "رنگ گرادیان را از روشن به تیره بر اساس مقادیر عددی اعمال کنید"
            elif first_line == "russian":
                return "Применить градиентный цвет от светлого к темному на основе числовых значений"
            elif first_line == "spanish":
                return "Aplicar un color de degradado de claro a oscuro basado en valores numéricos"
            elif first_line == "chinese":
                return "根据数值从浅到深应用渐变颜色"
            elif first_line == "korean":
                return "숫자 값을 기반으로 밝은 색에서 어두운 색으로 그라디언트 색상 적용하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_22(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Choose a color to paint selected cells"
            elif first_line == "deutsch":
                return "Wählen Sie eine Farbe, um die ausgewählten Zellen zu färben"
            elif first_line == "farsi":
                return "یک رنگ برای رنگ‌آمیزی سلول‌های انتخاب شده انتخاب کنید"
            elif first_line == "russian":
                return "Выберите цвет для окраски выбранных ячеек"
            elif first_line == "spanish":
                return "Elija un color para pintar las celdas seleccionadas"
            elif first_line == "chinese":
                return "选择一个颜色来为选定的单元格上色"
            elif first_line == "korean":
                return "선택한 셀을 칠할 색상 선택하기"
            else:
                return "Unknown language"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"
    
def tip_rep_23(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Remove all colors from the data grid"
            elif first_line == "deutsch":
                return "Alle Farben aus dem Datengitter entfernen"
            elif first_line == "farsi":
                return "تمام رنگ‌ها را از جدول داده‌ها حذف کنید"
            elif first_line == "russian":
                return "Удалить все цвета из таблицы данных"
            elif first_line == "spanish":
                return "Eliminar todos los colores de la cuadrícula de datos"
            elif first_line == "chinese":
                return "从数据网格中删除所有颜色"
            elif first_line == "korean":
                return "데이터 그리드에서 모든 색상 제거하기"
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