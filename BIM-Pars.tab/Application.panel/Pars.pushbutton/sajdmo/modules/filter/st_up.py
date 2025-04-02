# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#st_up.py

#Imports
import clr
import os
import getpass
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, ElementId
from System.Collections.Generic import List
from pyrevit import revit, script

def storage():
    """
    Stores the IDs of selected elements in a specified file.

    This function retrieves the IDs of elements selected in the Revit UI,
    combines them into a single string, and writes them to a file. If the
    file already exists, it appends the new IDs to the existing ones. The
    file is named based on the current model's title and is stored in a
    designated folder structure.

    Raises:
        ValueError: If the expected folder name is not found in the script path.
    """
    selection = revit.uidoc.Selection
    selected_elements = selection.GetElementIds()
    element_ids = List[ElementId]()
    for element_id in selected_elements:
        element_ids.Add(element_id)
    combined_ids = '+'.join(str(element_id.IntegerValue) for element_id in element_ids)
    for element_id in selected_elements:
        element = revit.doc.GetElement(element_id)
        clickable_link = script.get_output().linkify(element.Id)
    model_path = revit.doc.PathName if revit.doc.PathName else ""
    model_name = revit.doc.Title
    current_user = getpass.getuser()
    file_name = 'MASTERFILTERSTORAGE'
    file_name = file_name + "_" + model_name
    import os
    def pathname():
        script_path = os.path.realpath(__file__)
        folder_name = 'BIM-Pars.tab'  
        folder_index = script_path.lower().find(folder_name.lower())
        if folder_index != -1:
            script_path_until_folder = script_path[:folder_index + len(folder_name)]
            return script_path_until_folder
        else:
            raise ValueError('Folder name "{}" not found in the script path.'.format(folder_name))
    def storage_path():
        script_path_until_folder = pathname()
        storage_path = os.path.join(script_path_until_folder, 'data', 'storage')
        return storage_path
    target_folder = storage_path()
    if target_folder:
        file_path = os.path.join(target_folder, file_name + '.sajdmo')
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                existing_ids = file.read()
            with open(file_path, 'w') as file:
                file.write(existing_ids.strip())
                if existing_ids.strip() != '':
                    file.write('+' + combined_ids)
                else:
                    file.write(combined_ids)
                file.write('//')
        else:
            with open(file_path, 'w') as file:
                file.write('%PATH#//' + (model_path if model_path else "") + '//\n')
                file.write('%NAME#//' + model_name + '//\n')
                file.write('%USER#//' + current_user + '//\n')
                file.write('%IDS#//' + combined_ids + '//\n')

def update():
    """
    Updates the IDs of selected elements in a specified file.

    This function retrieves the IDs of elements selected in the Revit UI,
    combines them into a single string, and writes them to a file. The file
    is named based on the current model's title and is stored in a designated
    folder structure. This function overwrites any existing file with the same
    name.

    Raises:
        ValueError: If the expected folder name is not found in the script path.
    """
    selection = revit.uidoc.Selection
    selected_elements = selection.GetElementIds()
    element_ids = List[ElementId]()
    for element_id in selected_elements:
        element_ids.Add(element_id)
    combined_ids = '+'.join(str(element_id.IntegerValue) for element_id in element_ids)
    for element_id in selected_elements:
        element = revit.doc.GetElement(element_id)
        clickable_link = script.get_output().linkify(element.Id)
    model_path = revit.doc.PathName if revit.doc.PathName else ""
    model_name = revit.doc.Title
    current_user = getpass.getuser()
    file_name = 'MASTERFILTERUPDATE'
    file_name = file_name + "_" + model_name
    import os
    def pathname():
        script_path = os.path.realpath(__file__)
        folder_name = 'BIM-Pars.tab'  
        folder_index = script_path.lower().find(folder_name.lower())
        if folder_index != -1:
            script_path_until_folder = script_path[:folder_index + len(folder_name)]
            return script_path_until_folder
        else:
            raise ValueError('Folder name "{}" not found in the script path.'.format(folder_name))
    def update_path():
        script_path_until_folder = pathname()
        update_path = os.path.join(script_path_until_folder, 'data', 'update')
        return update_path
    target_folder = update_path()
    if target_folder:
        file_path = os.path.join(target_folder, file_name + '.sajdmo')
        with open(file_path, 'w') as file:
            file.write('%PATH#//' + (model_path if model_path else "") + '//\n')
            file.write('%NAME#//' + model_name + '//\n')
            file.write('%USER#//' + current_user + '//\n')
            file.write('%IDS#//' + combined_ids + '//\n')