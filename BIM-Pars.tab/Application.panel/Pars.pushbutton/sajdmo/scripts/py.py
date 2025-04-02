# -*- coding: utf-8 -*-
# __author__ = "Mohammad Sajjad Mortazavi"
#py.py

import os
from pyrevit import forms

def pathname():
    """
    Get the path of the current script.

    Returns:
        str: The path until the specified folder.
    """
    script_path = os.path.realpath(__file__)
    folder_name = 'BIM-Pars.tab'
    folder_index = script_path.lower().find(folder_name.lower())

    if folder_index != -1:
        script_path_until_folder = script_path[:folder_index + len(folder_name)]
        return script_path_until_folder
    else:
        raise ValueError('Folder name "{}" not found in the script path.'.format(folder_name))

def get_description(code):
    """
    Retrieve the description from the code.

    Args:
        code (str): The code to search for the description.

    Returns:
        str or None: The description if found, otherwise None.
    """
    lines = code.split('\n')
    for line in lines:
        if line.strip().startswith('#Description:'):
            description = line.strip().replace('#Description:', '').strip()
            return description
    return None

def execute_selected_file(selected_file):
    """
    Execute the selected Python file.

    Args:
        selected_file (str): The name of the selected file to execute.

    Returns:
        str or None: The description of the executed file if found.
    """
    script_path_until_folder = pathname()
    pylist_path = os.path.join(script_path_until_folder, 'data', 'pylist')
    file_path = os.path.join(pylist_path, selected_file)
    exec(open(file_path).read(), globals())
    if file_path:
        code = open(file_path).read()
        description = get_description(code)
        if description:              
            return description

def pylist_delete(title, button_name):
    """
    Delete a Python file from the list.

    Args:
        title (str): The title for the selection dialog.
        button_name (str): The name of the button in the dialog.

    Returns:
        str: The full path to the selected file.
    """
    script_path_until_folder = pathname()
    pylist_delete = os.path.join(script_path_until_folder, 'data', 'pylist')
    py_files = [f for f in os.listdir(pylist_delete) if f.endswith('.py')]
    selected_item = forms.SelectFromList.show(
        py_files,
        default=py_files[0] if py_files else None,
        title=title,
        button_name=button_name
    )
    return os.path.join(pylist_delete, selected_item)

def pylist_path_run(title, button_name):
    """
    Run a Python file from the list.

    Args:
        title (str): The title for the selection dialog.
        button_name (str): The name of the button in the dialog.

    Returns:
        str: The name of the selected item.
    """
    script_path_until_folder = pathname()
    pylist_path = os.path.join(script_path_until_folder, 'data', 'pylist')
    py_files = [f for f in os.listdir(pylist_path) if f.endswith('.py')]
    selected_item = forms.SelectFromList.show(
        py_files,
        default=py_files[0] if py_files else None,
        title=title,
        button_name=button_name
    )
    return selected_item