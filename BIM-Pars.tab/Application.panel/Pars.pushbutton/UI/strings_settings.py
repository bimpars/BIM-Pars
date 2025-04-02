# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_settings.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Mode "
            elif first_line == "deutsch":
                return "Modus "
            elif first_line == "farsi":
                return "حالت " 
            elif first_line == "russian":
                return "Режим " 
            elif first_line == "spanish":
                return "Modo "  
            elif first_line == "chinese":
                return "模式 "  
            elif first_line == "korean":
                return "모드 "  
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
                return "Language "
            elif first_line == "deutsch":
                return "Sprache "
            elif first_line == "farsi":
                return "زبان " 
            elif first_line == "russian":
                return "Язык "
            elif first_line == "spanish":
                return "Idioma "
            elif first_line == "chinese":
                return "语言 " 
            elif first_line == "korean":
                return "언어 "  
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
                return "Logo "
            elif first_line == "deutsch":
                return "Logo "
            elif first_line == "farsi":
                return  "لوگو " 
            elif first_line == "russian":
                return "Логотип " 
            elif first_line == "spanish":
                return "Logotipo " 
            elif first_line == "chinese":
                return "标志 "
            elif first_line == "korean":
                return  "로고 "  
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
                return "Cool Mode"
            elif first_line == "deutsch":
                return "Lustiger Modus"
            elif first_line == "farsi":
                return  "حالت شوخ طبع" 
            elif first_line == "russian":
                return "Забавный режим" 
            elif first_line == "spanish":
                return "Modo divertido" 
            elif first_line == "chinese":
                return "有趣模式"
            elif first_line == "korean":
                return   "재미있는 모드" 
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
                return "Standard"
            elif first_line == "deutsch":
                return "Standard"
            elif first_line == "farsi":
                return  "استاندارد"
            elif first_line == "russian":
                return  "Стандартный"
            elif first_line == "spanish":
                return "Estándar"
            elif first_line == "chinese":
                return "标准"
            elif first_line == "korean":
                return "표준"
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
                return "Default"
            elif first_line == "deutsch":
                return "Standard"  
            elif first_line == "farsi":
                return "پیش فرض"  
            elif first_line == "russian":
                return "По умолчанию" 
            elif first_line == "spanish":
                return "Predeterminado"  
            elif first_line == "chinese":
                return "默认"  
            elif first_line == "korean":
                return "기본값"  
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
                return "New"
            elif first_line == "deutsch":
                return "Neu"
            elif first_line == "farsi":
                return  "جدید" 
            elif first_line == "russian":
                return  "Новый"
            elif first_line == "spanish":
                return "Nuevo"
            elif first_line == "chinese":
                return "新"
            elif first_line == "korean":
                return   "새로운" 
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
                return "Operation canceled."
            elif first_line == "deutsch":
                return "Vorgang abgebrochen."
            elif first_line == "farsi":
                return  "عملیات لغو شد." 
            elif first_line == "russian":
                return  "Операция отменена."
            elif first_line == "spanish":
                return "Operación cancelada."
            elif first_line == "chinese":
                return  "操作已取消。"
            elif first_line == "korean":
                return   "작업이 취소되었습니다." 
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
                return "Setting logo was successful."
            elif first_line == "deutsch":
                return  "Das Setzen des Logos war erfolgreich."
            elif first_line == "farsi":
                return   "تنظیم لوگو با موفقیت انجام شد" 
            elif first_line == "russian":
                return  "Установка логотипа прошла успешно."
            elif first_line == "spanish":
                return "La configuración del logotipo se realizó con éxito."
            elif first_line == "chinese":
                return  "设置标志成功。"
            elif first_line == "korean":
                return "로고 설정이 성공했습니다." 
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
                return "No file selected."
            elif first_line == "deutsch":
                return  "Keine Datei ausgewählt."
            elif first_line == "farsi":
                return   "فایلی انتخاب نشده است" 
            elif first_line == "russian":
                return  "Файл не выбран."
            elif first_line == "spanish":
                return "No se ha seleccionado ningún archivo."
            elif first_line == "chinese":
                return   "未选择文件。"
            elif first_line == "korean":
                return "선택된 파일이 없습니다." 
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
                return "Coldnt delete logo. please close revit and try again."
            elif first_line == "deutsch":
                return   "Logo konnte nicht gelöscht werden. Bitte schließen Sie Revit und versuchen Sie es erneut."
            elif first_line == "farsi":
                return   "لوگو حذف نشد. لطفا رویت را ببندید و دوباره امتحان کنید"
            elif first_line == "russian":
                return  "Не удалось удалить логотип. Пожалуйста, закройте Revit и попробуйте еще раз."
            elif first_line == "spanish":
                return "No se pudo eliminar el logotipo. Por favor, cierre Revit e intente nuevamente."
            elif first_line == "chinese":
                return   "无法删除标志。请关闭 Revit，然后重试。"
            elif first_line == "korean":
                return "로고를 삭제할 수 없습니다. Revit을 닫고 다시 시도해주세요."
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
                return "Settings"
            elif first_line == "deutsch":
                return "Einstellungen"
            elif first_line == "farsi":
                return "تنظیمات"
            elif first_line == "russian":
                return "Настройки"
            elif first_line == "spanish":
                return "Configuración"
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
    
def str_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "License Key"
            elif first_line == "deutsch":
                return "Lizenzschlüssel"
            elif first_line == "farsi":
                return "کلید "
            elif first_line == "russian":
                return "Лицензионный ключ"
            elif first_line == "spanish":
                return "Clave de licencia"
            elif first_line == "chinese":
                return "许可证密钥"
            elif first_line == "korean":
                return "라이센스 키"
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
                return "Check License"
            elif first_line == "deutsch":
                return "Lizenz überprüfen"
            elif first_line == "farsi":
                return "بررسی مجوز"
            elif first_line == "russian":
                return "Проверить лицензию"
            elif first_line == "spanish":
                return "Verificar licencia"
            elif first_line == "chinese":
                return "检查许可证"
            elif first_line == "korean":
                return "라이센스 확인하기"
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
                return "Save Key"
            elif first_line == "deutsch":
                return "Schlüssel speichern"
            elif first_line == "farsi":
                return "ذخیره کلید"
            elif first_line == "russian":
                return "Сохранить ключ"
            elif first_line == "spanish":
                return "Guardar clave"
            elif first_line == "chinese":
                return "保存密钥"
            elif first_line == "korean":
                return "키 저장하기"
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

def str_17(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Key saved successfully!"
            elif first_line == "deutsch":
                return "Schlüssel erfolgreich gespeichert!"
            elif first_line == "farsi":
                return "!کلید با موفقیت ذخیره شد"
            elif first_line == "russian":
                return "Ключ успешно сохранён!"
            elif first_line == "spanish":
                return "¡Clave guardada con éxito!"
            elif first_line == "chinese":
                return "密钥成功保存！"
            elif first_line == "korean":
                return "키가 성공적으로 저장되었습니다!"
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
    
def str_19(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Close and reopen the app to reset selected mode or language."
            elif first_line == "deutsch":
                return "Schließen Sie die App und öffnen Sie sie erneut, um den ausgewählten Modus oder die Sprache zurückzusetzen."
            elif first_line == "farsi":
                return ".برنامه را ببندید و دوباره باز کنید تا حالت یا زبان انتخاب شده بازنشانی شود"
            elif first_line == "russian":
                return "Закройте и снова откройте приложение, чтобы сбросить выбранный режим или язык."
            elif first_line == "spanish":
                return "Cierra y vuelve a abrir la aplicación para restablecer el modo o el idioma seleccionado."
            elif first_line == "chinese":
                return "关闭并重新打开应用以重置所选模式或语言。"
            elif first_line == "korean":
                return "선택한 모드나 언어를 재설정하려면 앱을 닫았다가 다시 열어주세요."
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