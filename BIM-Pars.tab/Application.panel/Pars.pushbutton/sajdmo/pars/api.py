# -*- coding: utf-8 -*-
# __author__ = "Mohammad Sajjad Mortazavi"
#api.py

import clr  
import json
import codecs
from System import Array, Object
from System.Windows.Forms import DataGridView, DataGridViewAutoSizeColumnsMode, AnchorStyles

def app_string(file_path, json_data, key):
    """
    Retrieve a localized string from a JSON data structure based on the file's language.

    Args:
        file_path (str): The path to the file containing the language identifier.
        json_data (dict): A dictionary containing language-specific strings.
        key (str): The key for the desired string in the specified language.

    Returns:
        str: The localized string if found, otherwise an error message.
    """
    try:
        with codecs.open(file_path, 'r', encoding='utf-8') as file:
            language = file.readline().strip().lower()

        if language in json_data:
            if key in json_data[language]:
                return json_data[language][key]
            else:
                return "String not found for the given key."
        else:
            return "Language not found in the data."
    except Exception:
        pass  

def check_key(json_path):
    """
    Retrieve the license key from a JSON file.

    Args:
        json_path (str): The path to the JSON file containing the license key.

    Returns:
        str or None: The license key if found, otherwise None.
    """
    try:
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)  
            return data.get("license_key", None)  

        return None
    except Exception as e:
        return None

def to_dotnet_array(py_list):
    """
    Convert a Python list to a .NET array of Object type.

    Args:
        py_list (list): The Python list to convert.

    Returns:
        Array[Object]: A .NET array containing the elements of the Python list.
    """
    return Array[Object](py_list) 

def create_data_grid(position, size, column_headers, data, editable_columns):
    """
    Create and configure a DataGridView control.

    Args:
        position (Point): The location of the DataGridView on the form.
        size (Size): The size of the DataGridView.
        column_headers (list): A list of column header names.
        data (list of lists): A list of lists containing the data for each column.
        editable_columns (list): A list of booleans indicating which columns are editable.

    Returns:
        DataGridView: The configured DataGridView control.
    """
    dataGridView = DataGridView()
    dataGridView.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill
    dataGridView.AllowUserToAddRows = False
    dataGridView.Location = position
    dataGridView.Width, dataGridView.Height = size
    dataGridView.Anchor = (AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right)

    for i, header in enumerate(column_headers):
        column = dataGridView.Columns.Add(header, header)
        dataGridView.Columns[column].ReadOnly = not editable_columns[i]

    row_count = len(data[0])  
    for i in range(row_count):
        row_data = [col[i] for col in data]  
        dotnet_row = to_dotnet_array(row_data)  
        dataGridView.Rows.Add(dotnet_row)

    return dataGridView

def load_config_json(url):
    """
    Load button states from a JSON URL.

    Args:
        url (str): The URL to fetch the JSON data from.

    Returns:
        dict: The loaded JSON data as a dictionary, or an empty dictionary if an error occurs.
    """
    try:
        clr.AddReference('System.Net.Http')  
        from System.Net.Http import HttpClient  
        from System.IO import StreamReader  
        import json 

        client = HttpClient()  
        response = client.GetAsync(url).Result  

        if response.IsSuccessStatusCode:
            content = response.Content.ReadAsStringAsync().Result 
            return json.loads(content)  
        else:
            return {}  

    except Exception as e:
        return {}
