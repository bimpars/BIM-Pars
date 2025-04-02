# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_unbound_rooms.py

def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "is unbound."
            elif first_line == "deutsch":
                return "ist nicht gebunden."
            elif first_line == "farsi":
                return "متصل نیست"
            elif first_line == "russian":
                return "не связано."
            elif first_line == "spanish":
                return "no está vinculado."
            elif first_line == "chinese":
                return "未绑定。"
            elif first_line == "korean":
                return "바인딩되지 않았습니다."
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
                return "Unbound Rooms"
            elif first_line == "deutsch":
                return "Ungebundene Räume"
            elif first_line == "farsi":
                return "اتاق‌های غیرمتصل"
            elif first_line == "russian":
                return "Непривязанные помещения"
            elif first_line == "spanish":
                return "Habitaciones sin vincular"
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
    
def str_3(file_path):
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
    
def str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Room Name" 
            elif first_line == "deutsch":
                return "Raumname"
            elif first_line == "farsi":
                return "نام اتاق"
            elif first_line == "russian":
                return "Название помещения"
            elif first_line == "spanish":
                return "Nombre de la habitación"
            elif first_line == "chinese":
                return "房间名称"
            elif first_line == "korean":
                return "방 이름"
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
                return "Unbound rooms"
            elif first_line == "deutsch":
                return "Ungebundene Räume"
            elif first_line == "farsi":
                return "اتاق های محدودنشده"
            elif first_line == "russian":
                return "Свободные комнаты"
            elif first_line == "spanish":
                return "Habitaciones sin restricciones"
            elif first_line == "chinese":
                return "无限制的房间"
            elif first_line == "korean":
                return "무제한 공간"
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