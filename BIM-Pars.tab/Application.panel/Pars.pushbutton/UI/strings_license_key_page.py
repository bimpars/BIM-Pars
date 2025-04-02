# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_license_key_page.py

def str_1(file_path):
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
    
def str_2(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "To use the BIM Pars app, you need an active key. You can create an account to obtain a new key or renew your key if it has expired. Please select one of the options below:"
            elif first_line == "deutsch":
                return "Um die BIM Pars-App zu nutzen, benötigen Sie einen aktiven Schlüssel. Sie können ein Konto erstellen, um einen neuen Schlüssel zu erhalten oder Ihren Schlüssel zu erneuern, wenn er abgelaufen ist. Bitte wählen Sie eine der folgenden Optionen aus:"
            elif first_line == "farsi":
                return "برای استفاده از اپلیکیشن بیم پارس، به یک کلید فعال نیاز دارید. می‌توانید یک حساب کاربری ایجاد کنید تا یک کلید جدید دریافت کنید یا در صورتی که کلید شما منقضی شده باشد، آن را تجدید کنید. لطفاً یکی از گزینه‌های زیر را انتخاب کنید:"
            elif first_line == "russian":
                return "Чтобы использовать приложение BIM Pars, вам нужен активный ключ. Вы можете создать учетную запись, чтобы получить новый ключ или продлить свой ключ, если он истек. Пожалуйста, выберите один из вариантов ниже:"
            elif first_line == "spanish":
                return "Para usar la aplicación BIM Pars, necesitas una clave activa. Puedes crear una cuenta para obtener una nueva clave o renovar tu clave si ha expirado. Por favor, selecciona una de las opciones a continuación:"
            elif first_line == "chinese":
                return "要使用BIM Pars应用，您需要一个有效的密钥。您可以创建一个帐户来获取新密钥，或在密钥过期时续订您的密钥。请从以下选项中选择一个："
            elif first_line == "korean":
                return "BIM Pars 앱을 사용하려면 활성화된 키가 필요합니다. 새 키를 얻거나 키가 만료된 경우 갱신하기 위해 계정을 만들 수 있습니다. 아래 옵션 중 하나를 선택하세요:"
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
                return "Create an account"
            elif first_line == "deutsch":
                return "Ein Konto erstellen"
            elif first_line == "farsi":
                return "یک حساب کاربری ایجاد کنید"
            elif first_line == "russian":
                return "Создать учетную запись"
            elif first_line == "spanish":
                return "Crear una cuenta"
            elif first_line == "chinese":
                return "创建账户"
            elif first_line == "korean":
                return "계정 만들기"
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
                return "Renew your key"
            elif first_line == "deutsch":
                return "Ihren Schlüssel erneuern"
            elif first_line == "farsi":
                return "کلید جدید دریافت کنید"
            elif first_line == "russian":
                return "Продлить ваш ключ"
            elif first_line == "spanish":
                return "Renovar tu clave"
            elif first_line == "chinese":
                return "续订您的密钥"
            elif first_line == "korean":
                return "키 갱신하기"
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
                return "Saving new key was successful."
            elif first_line == "deutsch":
                return "Speichern des neuen Schlüssels war erfolgreich."
            elif first_line == "farsi":
                return ".ذخیره کلید جدید با موفقیت انجام شد"
            elif first_line == "russian":
                return "Сохранение нового ключа прошло успешно."
            elif first_line == "spanish":
                return "Guardar la nueva clave fue exitoso."
            elif first_line == "chinese":
                return "新密钥保存成功。"
            elif first_line == "korean":
                return "새 키 저장이 성공적으로 완료되었습니다."
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
                return "URL file not found."
            elif first_line == "deutsch":
                return "URL-Datei nicht gefunden."
            elif first_line == "farsi":
                return ".فایل لینکها پیدا نشد"
            elif first_line == "russian":
                return "Файл URL не найден."
            elif first_line == "spanish":
                return "Archivo URL no encontrado."
            elif first_line == "chinese":
                return "未找到 URL 文件。"
            elif first_line == "korean":
                return "URL 파일을 찾을 수 없습니다."
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
    
def str_8(file_path):
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
