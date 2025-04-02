# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#strings_delete_parameter_completely_from_model.py
    
def str_1(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Insert Name"
            elif first_line == "deutsch":
                return "Namen einfügen"
            elif first_line == "farsi":
                return "نام را وارد کنید"
            elif first_line == "russian":
                return "Вставьте имя"
            elif first_line == "spanish":
                return "Ingresar nombre"
            elif first_line == "chinese":
                return "插入姓名"
            elif first_line == "korean":
                return "이름을 입력하세요"
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
    
def str_3(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Element"
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
    
def str_4(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter (separate by comma):"
            elif first_line == "deutsch":
                return "Parameter (durch Komma getrennt):"
            elif first_line == "farsi":
                return "(پارامتر (با کاما جدا کنید:"
            elif first_line == "russian":
                return "Параметры (разделите запятой):"
            elif first_line == "spanish":
                return "Parámetros (separados por coma):"
            elif first_line == "chinese":
                return "参数（用逗号分隔）："
            elif first_line == "korean":
                return "매개변수 (쉼표로 구분):"
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
                return "Operation canceled."
            elif first_line == "deutsch":
                return "Operation abgebrochen."
            elif first_line == "farsi":
                return "عملیات لغو شد."
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
    
def str_6(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Parameter '{}' does not exist."
            elif first_line == "deutsch":
                return "Parameter '{}' existiert nicht."
            elif first_line == "farsi":
                return "پارامتر '{}' وجود ندارد"
            elif first_line == "russian":
                return "Параметр '{}' не существует."
            elif first_line == "spanish":
                return "El parámetro '{}' no existe."
            elif first_line == "chinese":
                return "参数'{}'不存在。"
            elif first_line == "korean":
                return "매개변수 '{}'가 존재하지 않습니다."
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
                return "deleted"
            elif first_line == "deutsch":
                return "gelöscht"
            elif first_line == "farsi":
                return "حذف شد"
            elif first_line == "russian":
                return "удалено"
            elif first_line == "spanish":
                return "eliminado"
            elif first_line == "chinese":
                return "已删除"
            elif first_line == "korean":
                return "삭제됨"
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
                return "can not be deleted"
            elif first_line == "deutsch":
                return "Kann nicht gelöscht werden"
            elif first_line == "farsi":
                return "نمی‌توان حذف کرد"
            elif first_line == "russian":
                return "Невозможно удалить"
            elif first_line == "spanish":
                return "No se puede eliminar"
            elif first_line == "chinese":
                return "无法删除"
            elif first_line == "korean":
                return "삭제할 수 없습니다"
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
                return "Parameters and their status regarding deletion"
            elif first_line == "deutsch":
                return "Parameter und ihr Status bezüglich Löschung"
            elif first_line == "farsi":
                return "پارامترها و وضعیت آنها درباره حذف"
            elif first_line == "russian":
                return "Параметры и их статус относительно удаления"
            elif first_line == "spanish":
                return "Parámetros y su estado con respecto a la eliminación"
            elif first_line == "chinese":
                return "参数及其删除状态"
            elif first_line == "korean":
                return "매개변수 및 삭제 상태"
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
    
def str_11(file_path):
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
    
def str_12(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Categories"
            elif first_line == "deutsch":
                return "Kategorien"
            elif first_line == "farsi":
                return "دسته‌بندی‌ها"
            elif first_line == "russian":
                return "Категории"
            elif first_line == "spanish":
                return "Categorías"
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

def str_13(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "Select"
            elif first_line == "deutsch":
                return "Auswählen"
            elif first_line == "farsi":
                return "انتخاب کردن"
            elif first_line == "russian":
                return "Выбрать"
            elif first_line == "spanish":
                return "Seleccionar"
            elif first_line == "chinese":
                return "选择"
            elif first_line == "korean":
                return "선택"
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

def str_15(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return  "Select one element"
            elif first_line == "deutsch":
                return "Wählen Sie ein Element aus"
            elif first_line == "farsi":
                return "یک المان را انتخاب کنید"
            elif first_line == "russian":
                return "Выберите один элемент"
            elif first_line == "spanish":
                return "Selecciona un elemento"
            elif first_line == "chinese":
                return "选择一个元素"
            elif first_line == "korean":
                return "하나의 요소를 선택하세요"
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
                return "Please select exactly one element."
            elif first_line == "deutsch":
                return "Bitte wählen Sie genau ein Element aus."
            elif first_line == "farsi":
                return "لطفاً دقیقاً یک المان را انتخاب کنید"
            elif first_line == "russian":
                return "Пожалуйста, выберите ровно один элемент."
            elif first_line == "spanish":
                return "Por favor, selecciona exactamente un elemento."
            elif first_line == "chinese":
                return "请选择一个元素。"
            elif first_line == "korean":
                return "정확히 하나의 요소를 선택하십시오."
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
                return "Information"
            elif first_line == "deutsch":
                return "Informationen"
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
 
def str_18(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "In this method, you can directly insert the name of the parameter that you want to delete entirely from your model."
            elif first_line == "deutsch":
                return "In dieser Methode können Sie direkt den Namen des Parameters eingeben, den Sie vollständig aus Ihrem Modell löschen möchten."
            elif first_line == "farsi":
                return "در این روش، شما می‌توانید مستقیماً نام پارامتری را که می‌خواهید به طور کامل از مدل خود حذف کنید، وارد کنید"
            elif first_line == "russian":
                return "В этом методе вы можете непосредственно вставить имя параметра, который вы хотите полностью удалить из вашей модели."
            elif first_line == "spanish":
                return "En este método, puedes insertar directamente el nombre del parámetro que deseas eliminar por completo de tu modelo."
            elif first_line == "chinese":
                return "在这种方法中，您可以直接插入要从模型中完全删除的参数名称。"
            elif first_line == "korean":
                return "이 방법에서는 모델에서 완전히 삭제하려는 매개변수의 이름을 직접 입력할 수 있습니다."
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
                return "In this method, you can select the category that the parameter is assigned to and delete the parameter entirely from the model. Note that the parameter will be deleted entirely from the model and not only for the selected category."
            elif first_line == "deutsch":
                return "In dieser Methode können Sie die Kategorie auswählen, der der Parameter zugeordnet ist, und den Parameter vollständig aus dem Modell löschen. Beachten Sie, dass der Parameter vollständig aus dem Modell gelöscht wird und nicht nur für die ausgewählte Kategorie."
            elif first_line == "farsi":
                return "در این روش، شما می‌توانید دسته‌بندی را که پارامتر به آن تعلق دارد را انتخاب کنید و پارامتر را به طور کامل از مدل حذف کنید. توجه داشته باشید که پارامتر به طور کامل از مدل حذف خواهد شد و نه فقط برای دسته‌بندی انتخاب شده"
            elif first_line == "russian":
                return "В этом методе вы можете выбрать категорию, к которой относится параметр, и полностью удалить параметр из модели. Обратите внимание, что параметр будет полностью удален из модели, а не только для выбранной категории."
            elif first_line == "spanish":
                return "En este método, puedes seleccionar la categoría a la que se asigna el parámetro y eliminar el parámetro por completo del modelo. Ten en cuenta que el parámetro se eliminará por completo del modelo y no solo para la categoría seleccionada."
            elif first_line == "chinese":
                return "在这种方法中，您可以选择参数所属的类别，并将该参数从模型中完全删除。请注意，该参数将从模型中完全删除，而不仅仅是对于所选类别。"
            elif first_line == "korean":
                return "이 방법에서는 매개변수가 할당된 카테고리를 선택하고 모델에서 매개변수를 완전히 삭제할 수 있습니다. 매개변수는 선택한 카테고리에만 삭제되는 것이 아니라 모델 전체에서 완전히 삭제된다는 점을 유의하세요."
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
                return "In this method, select one element which you are sure that it contains that parameter and delete the parameter entirely from the model. Note that the parameter will be deleted entirely from the model and not only for the selected category."
            elif first_line == "deutsch":
                return "In dieser Methode wählen Sie ein Element aus, von dem Sie sicher sind, dass es diesen Parameter enthält, und löschen den Parameter vollständig aus dem Modell. Beachten Sie, dass der Parameter vollständig aus dem Modell gelöscht wird und nicht nur für die ausgewählte Kategorie."
            elif first_line == "farsi":
                return "در این روش، یک المان را انتخاب کنید که مطمئن هستید حاوی آن پارامتر است و پارامتر را به طور کامل از مدل حذف کنید. توجه داشته باشید که پارامتر به طور کامل از مدل حذف خواهد شد و نه فقط برای دسته‌بندی انتخاب شده"
            elif first_line == "russian":
                return "В этом методе выберите один элемент, в котором вы уверены, что он содержит этот параметр, и полностью удалите параметр из модели. Обратите внимание, что параметр будет полностью удален из модели, а не только для выбранной категории."
            elif first_line == "spanish":
                return "En este método, selecciona un elemento del cual estés seguro de que contiene ese parámetro y elimina el parámetro por completo del modelo. Ten en cuenta que el parámetro se eliminará por completo del modelo y no solo para la categoría seleccionada."
            elif first_line == "chinese":
                return "在这种方法中，选择一个你确信包含该参数的元素，并将该参数从模型中完全删除。请注意，该参数将从模型中完全删除，而不仅仅是对于所选类别。"
            elif first_line == "korean":
                return "이 방법에서는 해당 매개변수가 포함되어 있는 것으로 확신하는 요소 하나를 선택하고 모델에서 매개변수를 완전히 삭제합니다. 매개변수는 선택한 카테고리에만 삭제되는 것이 아니라 모델 전체에서 완전히 삭제된다는 점을 유의하세요."
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
                return "Delete parameter from model"
            elif first_line == "deutsch":
                return "Parameter aus Modell löschen"
            elif first_line == "farsi":
                return "حذف پارامتر از مدل"
            elif first_line == "russian":
                return "Удалить параметр из модели"
            elif first_line == "spanish":
                return "Eliminar parámetro del modelo"
            elif first_line == "chinese":
                return "从模型中删除参数"
            elif first_line == "korean":
                return "모델에서 매개변수 삭제"
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
    
def str_23(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()

            if first_line == "english":
                return "No parameters processed."
            elif first_line == "deutsch":
                return "Keine Parameter verarbeitet."
            elif first_line == "farsi":
                return ".هیچ پارامتری پردازش نشد"
            elif first_line == "russian":
                return "Нет обработанных параметров."
            elif first_line == "spanish":
                return "No se procesaron parámetros."
            elif first_line == "chinese":
                return "未处理任何参数。"
            elif first_line == "korean":
                return "처리된 매개변수가 없습니다."
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
                return "No elements found in the model."
            elif first_line == "deutsch":
                return "Keine Elemente im Modell gefunden."
            elif first_line == "farsi":
                return ".هیچ المانی در مدل پیدا نشد"
            elif first_line == "russian":
                return "В модели не найдено элементов."
            elif first_line == "spanish":
                return "No se encontraron elementos en el modelo."
            elif first_line == "chinese":
                return "模型中未找到任何元素。"
            elif first_line == "korean":
                return "모델에서 요소를 찾을 수 없습니다."
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