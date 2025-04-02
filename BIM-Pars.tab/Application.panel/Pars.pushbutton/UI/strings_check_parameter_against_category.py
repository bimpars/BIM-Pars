# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_check_parameter_against_category.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameters Agains Category"
            elif first_line == "deutsch":
                return "Parameter gegen Kategorie"
            elif first_line == "farsi":
                return "پارامتر در مقابل دسته بندی"
            elif first_line == "russian":
                return "Параметры против категории"
            elif first_line == "spanish":
                return "Parámetros contra la categoría"
            elif first_line == "chinese":
                return "与类别的参数"
            elif first_line == "korean":
                return "카테고리 대비 매개변수"
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
    
def str_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Categories Included:Architectural Elements: Walls, Doors, Windows, Roofs, Floors, Ceilings, Ramps.Structural Elements: Columns, Framing, Foundations, Trusses.MEP (Mechanical, Electrical, Plumbing): Ducts, Pipes, Electrical Fixtures, Sprinklers, Mechanical Equipment, Air Terminals.Other Elements: Furniture, Planting, Casework, Security Devices, Specialty Equipment.Systems: Cable Trays, Conduit, Curtain Walls.Annotations and Rooms: Rooms.Reinforcement: Area Reinforcement, Path Reinforcement, Rebar.Communications: Communication Devices, Telephone Devices, Nurse Call Devices, Data Devices."
            elif first_line == "deutsch":
                return "Kategorien enthalten:Architektonische Elemente: Wände, Türen, Fenster, Dächer, Böden, Decken, Rampen.Strukturelle Elemente: Säulen, Rahmen, Fundamente, Fachwerke.MEP (Mechanik, Elektrik, Sanitär): Kanäle, Rohre, elektrische Geräte, Sprinkler, mechanische Geräte, Luftauslässe.Andere Elemente: Möbel, Bepflanzung, Tischlerarbeiten, Sicherheitsgeräte, Spezialgeräte.Systeme: Kabelrinnen, Leitungen, Vorhangwände.Anmerkungen und Räume: Räume.Verstärkung: Flächenverstärkung, Pfadverstärkung, Bewehrungsstahl.Kommunikation: Kommunikationsgeräte, Telefondgeräte, Rufgeräte, Datengeräte."
            elif first_line == "farsi":
                return ".دسته‌بندی‌ها شامل:المان های معماری: دیوارها، درها، پنجره‌ها، سقف‌ها، کف‌ها، بام ها، رمپ‌ها.المان های سازه‌ای: ستون‌ها، قاب‌ها، پی‌ها، تیرک‌ها.ام ای پی (مکانیکی، الکتریکی، لوله‌کشی): کانال‌ها، لوله‌ها، تجهیزات الکتریکی، آب‌پاش‌ها، تجهیزات مکانیکی، ترمینال‌های هوایی.المان های دیگر: مبلمان، کاشت، کارهای چوبی، دستگاه‌های امنیتی، تجهیزات تخصصی.سیستم‌ها: سینی‌های کابل، لوله، دیوارهای پرده‌ای.توضیحات و اتاق‌ها: اتاق‌ها.تقویت‌کننده: تقویت منطقه‌ای، تقویت مسیر، میلگرد.ارتباطات: دستگاه‌های ارتباطی، دستگاه‌های تلفن، دستگاه‌های فراخوان پرستار، دستگاه‌های داده"
            elif first_line == "russian":
                return "Включенные категории:Архитектурные элементы: стены, двери, окна, крыши, полы, потолки, пандусы.Структурные элементы: колонны, рамы, фундаменты, фермы.MEP (Механические, Электрические, Сантехнические): каналы, трубы, электрические установки, спринклеры, механическое оборудование, воздуховоды.Другие элементы: мебель, озеленение, столярные изделия, средства безопасности, специализированное оборудование.Системы: кабельные лотки, трубопроводы, занавесочные стены.Аннотации и помещения: помещения.Укрепление: усиление площади, усиление пути, арматура.Связь: устройства связи, телефонные устройства, устройства вызова медсестры, устройства данных."
            elif first_line == "spanish":
                return "Categorías Incluidas:Elementos arquitectónicos: Paredes, Puertas, Ventanas, Techos, Pisos, Techos, Rampas.Elementos estructurales: Columnas, Estructuras, Fundaciones, Cerchas.MEP (Mecánico, Eléctrico, Fontanería): Conductos, Tuberías, Instalaciones eléctricas, Rociadores, Equipos mecánicos, Terminales de aire.Otros elementos: Muebles, Plantación, Carpintería, Dispositivos de seguridad, Equipos especializados.Sistemas: Bandejas de cables, Conductos, Muros cortina.Anotaciones y habitaciones: Habitaciones.Refuerzo: Refuerzo de área, Refuerzo de camino, Varilla de refuerzo.Comunicaciones: Dispositivos de comunicación, Dispositivos telefónicos, Dispositivos de llamada de enfermera, Dispositivos de datos."
            elif first_line == "chinese":
                return "包含的类别：建筑元素：墙、门、窗、屋顶、地板、天花板、坡道。结构元素：柱、框架、基础、桁架。MEP（机械、电气、管道）：风管、管道、电气设备、喷头、机械设备、空气终端。其他元素：家具、种植、木工、安全设备、专业设备。系统：电缆槽、导管、幕墙。注释和房间：房间。加固：区域加固、路径加固、钢筋。通信：通信设备、电话设备、护士呼叫设备、数据设备。"
            elif first_line == "korean":
                return "포함된 카테고리:건축 요소: 벽, 문, 창문, 지붕, 바닥, 천장, 경사로.구조 요소: 기둥, 프레임, 기초, 트러스.MEP(기계, 전기, 배관): 덕트, 파이프, 전기 기구, 스프링클러, 기계 장비, 공기 단말기.기타 요소: 가구, 식재, 캐비닛, 보안 장치, 전문 장비.시스템: 케이블 트레이, 관, 커튼 월.주석 및 방: 방.보강: 면 보강, 경로 보강, 철근.통신: 통신 장치, 전화 장치, 간호사 호출 장치, 데이터 장치."
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
                return "参数"
            elif first_line == "korean":
                return "매개변수"
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
                return "Categories with missing parameter"
            elif first_line == "deutsch":
                return "Kategorien mit fehlendem Parameter"
            elif first_line == "farsi":
                return "دسته بندی هایی که پارامترهایی از آنها موجود نمی باشد"
            elif first_line == "russian":
                return "Категории с отсутствующим параметром"
            elif first_line == "spanish":
                return "Categorías con parámetro faltante"
            elif first_line == "chinese":
                return "缺少参数的类别"
            elif first_line == "korean":
                return "매개변수가 누락된 카테고리"
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
    
def str_8(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Some parameters are missing for categories."
            elif first_line == "deutsch":
                return "Einige Parameter fehlen für die Kategorien."
            elif first_line == "farsi":
                return "برخی پارامترها برای دسته‌بندی‌های موردنظرموجودنمیباشد"
            elif first_line == "russian":
                return "Некоторые параметры отсутствуют для категорий."
            elif first_line == "spanish":
                return "Faltan algunos parámetros para las categorías."
            elif first_line == "chinese":
                return "某些类别缺少参数。"
            elif first_line == "korean":
                return "카테고리에 일부 매개변수가 누락되었습니다."
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
                return "An error occurred: {0}"
            elif first_line == "deutsch":
                return "Ein Fehler ist aufgetreten: {0}"
            elif first_line == "farsi":
                return "یک خطا رخ داد: {0}"
            elif first_line == "russian":
                return "Произошла ошибка: {0}"
            elif first_line == "spanish":
                return "Ocurrió un error: {0}"
            elif first_line == "chinese":
                return "发生错误: {0}"
            elif first_line == "korean":
                return "오류가 발생했습니다: {0}"
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
                return "Filter"
            elif first_line == "deutsch":
                return "Filter"
            elif first_line == "farsi":
                return "فیلتر"
            elif first_line == "russian":
                return "Фильтр"
            elif first_line == "spanish":
                return "Filtro"
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
    
def str_11(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Column:"
            elif first_line == "deutsch":
                return "Spalte:"
            elif first_line == "farsi":
                return "ستون:"
            elif first_line == "russian":
                return "Столбец:"
            elif first_line == "spanish":
                return "Columna:"
            elif first_line == "chinese":
                return "列:"
            elif first_line == "korean":
                return "열:"
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
                return "An error occurred while applying the filter: {}"
            elif first_line == "deutsch":
                return "Ein Fehler ist beim Anwenden des Filters aufgetreten: {}"
            elif first_line == "farsi":
                return "در حین اعمال فیلتر خطایی رخ داد: {}"
            elif first_line == "russian":
                return "Произошла ошибка при применении фильтра: {}"
            elif first_line == "spanish":
                return "Ocurrió un error al aplicar el filtro: {}"
            elif first_line == "chinese":
                return "应用过滤器时发生错误: {}"
            elif first_line == "korean":
                return "필터를 적용하는 동안 오류가 발생했습니다: {}"
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
                return "No missing parameter found."
            elif first_line == "deutsch":
                return "Kein fehlender Parameter gefunden."
            elif first_line == "farsi":
                return " .پارامتر ناموجودی پیدا نشد"
            elif first_line == "russian":
                return "Не найдено отсутствующих параметров."
            elif first_line == "spanish":
                return "No se encontró ningún parámetro faltante."
            elif first_line == "chinese":
                return "未找到缺失的参数。"
            elif first_line == "korean":
                return "누락된 매개변수가 없습니다."
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
                return "##Check is complete.##"
            elif first_line == "deutsch":
                return "##Überprüfung abgeschlossen.##"
            elif first_line == "farsi":
                return "##بررسی کامل شد.##"
            elif first_line == "russian":
                return "##Проверка завершена.##"
            elif first_line == "spanish":
                return "##La verificación está completa.##"
            elif first_line == "chinese":
                return "##检查完成。##"
            elif first_line == "korean":
                return "##검사가 완료되었습니다.##"
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
                return "An error occurred: "
            elif first_line == "deutsch":
                return "Ein Fehler ist aufgetreten: "
            elif first_line == "farsi":
                return "یک خطا رخ داده است: "
            elif first_line == "russian":
                return "Произошла ошибка: "
            elif first_line == "spanish":
                return "Se produjo un error: "
            elif first_line == "chinese":
                return "发生错误："
            elif first_line == "korean":
                return "오류가 발생했습니다: "
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
                return "Selection complete."
            elif first_line == "deutsch":
                return "Auswahl abgeschlossen."
            elif first_line == "farsi":
                return "انتخاب کامل شد"
            elif first_line == "russian":
                return "Выбор завершён."
            elif first_line == "spanish":
                return "Selección completa."
            elif first_line == "chinese":
                return "选择完成。"
            elif first_line == "korean":
                return "선택이 완료되었습니다."
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
                return "File name:"
            elif first_line == "deutsch":
                return "Dateiname:"
            elif first_line == "farsi":
                return "نام فایل:"
            elif first_line == "russian":
                return "Имя файла:"
            elif first_line == "spanish":
                return "Nombre del archivo:"
            elif first_line == "chinese":
                return "文件名:"
            elif first_line == "korean":
                return "파일 이름:"
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
                return "Save as Excel"
            elif first_line == "deutsch":
                return "Als Excel speichern"
            elif first_line == "farsi":
                return "ذخیره به عنوان اکسل"
            elif first_line == "russian":
                return "Сохранить как Excel"
            elif first_line == "spanish":
                return "Guardar como Excel"
            elif first_line == "chinese":
                return "另存为 Excel"
            elif first_line == "korean":
                return "Excel로 저장"
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
                return "Excel file saved successfully at "
            elif first_line == "deutsch":
                return "Excel-Datei erfolgreich gespeichert unter "
            elif first_line == "farsi":
                return "فایل اکسل با موفقیت در آدرس ذخیره شد "
            elif first_line == "russian":
                return "Файл Excel успешно сохранён по адресу "
            elif first_line == "spanish":
                return "Archivo de Excel guardado con éxito en "
            elif first_line == "chinese":
                return "Excel 文件成功保存于 "
            elif first_line == "korean":
                return "Excel 파일이 성공적으로 저장되었습니다 "
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
                return "Save operation canceled."
            elif first_line == "deutsch":
                return "Speichervorgang abgebrochen."
            elif first_line == "farsi":
                return "عملیات ذخیره سازی لغو شد"
            elif first_line == "russian":
                return "Операция сохранения отменена."
            elif first_line == "spanish":
                return "Operación de guardado cancelada."
            elif first_line == "chinese":
                return "保存操作已取消。"
            elif first_line == "korean":
                return "저장 작업이 취소되었습니다."
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
                return "An error occurred while saving the Excel file: "
            elif first_line == "deutsch":
                return "Ein Fehler ist beim Speichern der Excel-Datei aufgetreten: "
            elif first_line == "farsi":
                return "در حین ذخیره فایل اکسل خطایی رخ داد: "
            elif first_line == "russian":
                return "Произошла ошибка при сохранении файла Excel: "
            elif first_line == "spanish":
                return "Ocurrió un error al guardar el archivo de Excel: "
            elif first_line == "chinese":
                return "保存 Excel 文件时发生错误: "
            elif first_line == "korean":
                return "Excel 파일을 저장하는 동안 오류가 발생했습니다: "
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
                return "An error occurred while deleting rows: "
            elif first_line == "deutsch":
                return "Ein Fehler ist beim Löschen der Zeilen aufgetreten: "
            elif first_line == "farsi":
                return "در حین حذف ردیف‌ها خطایی رخ داد: "
            elif first_line == "russian":
                return "Произошла ошибка при удалении строк: "
            elif first_line == "spanish":
                return "Ocurrió un error al eliminar filas: "
            elif first_line == "chinese":
                return "删除行时发生错误: "
            elif first_line == "korean":
                return "행을 삭제하는 동안 오류가 발생했습니다: "
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
                return "No elements found."
            elif first_line == "deutsch":
                return "Keine Elemente gefunden."
            elif first_line == "farsi":
                return ".هیچ المانی پیدا نشد"
            elif first_line == "russian":
                return "Элементы не найдены."
            elif first_line == "spanish":
                return "No se encontraron elementos."
            elif first_line == "chinese":
                return "未找到元素。"
            elif first_line == "korean":
                return "요소가 발견되지 않았습니다."
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
                return "Error: "
            elif first_line == "deutsch":
                return "Fehler: "
            elif first_line == "farsi":
                return "خطا: "
            elif first_line == "russian":
                return "Ошибка: "
            elif first_line == "spanish":
                return "Error: "
            elif first_line == "chinese":
                return "错误："
            elif first_line == "korean":
                return "오류: "
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
                return "Parameters"
            elif first_line == "deutsch":
                return "Parameter"
            elif first_line == "farsi":
                return "پارامترها"
            elif first_line == "russian":
                return "Параметры"
            elif first_line == "spanish":
                return "Parámetros"
            elif first_line == "chinese":
                return "参数"
            elif first_line == "korean":
                return "매개변수"
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
                return "Category1"
            elif first_line == "deutsch":
                return "Kategorie1"
            elif first_line == "farsi":
                return "دسته‌بندی1"
            elif first_line == "russian":
                return "Категория1"
            elif first_line == "spanish":
                return "Categoría1"
            elif first_line == "chinese":
                return "类别1"
            elif first_line == "korean":
                return "카테고리1"
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
                return "Category2"
            elif first_line == "deutsch":
                return "Kategorie2"
            elif first_line == "farsi":
                return "دسته‌بندی2"
            elif first_line == "russian":
                return "Категория2"
            elif first_line == "spanish":
                return "Categoría2"
            elif first_line == "chinese":
                return "类别2"
            elif first_line == "korean":
                return "카테고리2"
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
                return "Category3"
            elif first_line == "deutsch":
                return "Kategorie3"
            elif first_line == "farsi":
                return "دسته‌بندی3"
            elif first_line == "russian":
                return "Категория3"
            elif first_line == "spanish":
                return "Categoría3"
            elif first_line == "chinese":
                return "类别3"
            elif first_line == "korean":
                return "카테고리3"
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
                return "Category 1"
            elif first_line == "deutsch":
                return "Kategorie 1"
            elif first_line == "farsi":
                return "دسته‌بندی 1"
            elif first_line == "russian":
                return "Категория 1"
            elif first_line == "spanish":
                return "Categoría 1"
            elif first_line == "chinese":
                return "类别 1"
            elif first_line == "korean":
                return "카테고리 1"
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
                return "Category 2"
            elif first_line == "deutsch":
                return "Kategorie 2"
            elif first_line == "farsi":
                return "دسته‌بندی 2"
            elif first_line == "russian":
                return "Категория 2"
            elif first_line == "spanish":
                return "Categoría 2"
            elif first_line == "chinese":
                return "类别 2"
            elif first_line == "korean":
                return "카테고리 2"
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
                return "Category 3"
            elif first_line == "deutsch":
                return "Kategorie 3"
            elif first_line == "farsi":
                return "دسته‌بندی 3"
            elif first_line == "russian":
                return "Категория 3"
            elif first_line == "spanish":
                return "Categoría 3"
            elif first_line == "chinese":
                return "类别 3"
            elif first_line == "korean":
                return "카테고리 3"
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
                return "No element selected"
            elif first_line == "deutsch":
                return "Kein Element ausgewählt"
            elif first_line == "farsi":
                return "هیچ المانی انتخاب نشده"
            elif first_line == "russian":
                return "Элемент не выбран"
            elif first_line == "spanish":
                return "Ningún elemento seleccionado"
            elif first_line == "chinese":
                return "未选择任何元素"
            elif first_line == "korean":
                return "선택된 요소가 없습니다"
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
                return "select"
            elif first_line == "deutsch":
                return "auswählen"
            elif first_line == "farsi":
                return "انتخاب کنید"
            elif first_line == "russian":
                return "выбрать"
            elif first_line == "spanish":
                return "seleccionar"
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
    
def str_34(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Unsupported file type."
            elif first_line == "deutsch":
                return "Nicht unterstützter Dateityp."
            elif first_line == "farsi":
                return "نوع فایل پشتیبانی نمی‌شود"
            elif first_line == "russian":
                return "Неподдерживаемый тип файла."
            elif first_line == "spanish":
                return "Tipo de archivo no soportado."
            elif first_line == "chinese":
                return "不支持的文件类型。"
            elif first_line == "korean":
                return "지원되지 않는 파일 형식입니다."
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
                return "An error occurred: "
            elif first_line == "deutsch":
                return "Ein Fehler ist aufgetreten: "
            elif first_line == "farsi":
                return "یک خطا رخ داده است: "
            elif first_line == "russian":
                return "Произошла ошибка: "
            elif first_line == "spanish":
                return "Se produjo un error: "
            elif first_line == "chinese":
                return "发生错误："
            elif first_line == "korean":
                return "오류가 발생했습니다: "
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
                return "\n\n\nTry other formats."
            elif first_line == "deutsch":
                return "\n\n\nVersuchen Sie andere Formate."
            elif first_line == "farsi":
                return "\n\n\nفرمت‌های دیگر را امتحان کنید."
            elif first_line == "russian":
                return "\n\n\nПопробуйте другие форматы."
            elif first_line == "spanish":
                return "\n\n\nPrueba otros formatos."
            elif first_line == "chinese":
                return "\n\n\n尝试其他格式。"
            elif first_line == "korean":
                return "\n\n\n다른 형식을 시도해 보세요."
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
    
def str_38(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Missing Parameter"
            elif first_line == "deutsch":
                return "Fehlender Parameter"
            elif first_line == "farsi":
                return "پارامترغایب"
            elif first_line == "russian":
                return "Отсутствующий параметр"
            elif first_line == "spanish":
                return "Parámetro faltante"
            elif first_line == "chinese":
                return "缺失的参数"
            elif first_line == "korean":
                return "누락된 매개변수"
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
                return "No missing parameters found."
            elif first_line == "deutsch":
                return "Keine fehlenden Parameter gefunden."
            elif first_line == "farsi":
                return ".هیچ پارامتر غایبی پیدا نشد"
            elif first_line == "russian":
                return "Не найдено отсутствующих параметров."
            elif first_line == "spanish":
                return "No se encontraron parámetros faltantes."
            elif first_line == "chinese":
                return "未找到缺失的参数。"
            elif first_line == "korean":
                return "누락된 매개변수가 없습니다."
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
    