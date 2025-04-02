# -*- coding: utf-8 -*-
# __author__ = "Mohammad Sajjad Mortazavi"
#select.py

import clr
clr.AddReference("RevitAPI")
import os
import sys
from pyrevit import revit, script, DB, forms
from System.Collections.Generic import List
from Autodesk.Revit.DB import ElementId, FilteredElementCollector, BuiltInCategory

output = script.get_output()

def category_id_param_value(category_name, get_element_ids_func, selected_parameter, selected_value):
    """
    Searches for value of instance parameters.

    Args:
        category_name (str): The name of the category.
        get_element_ids_func (function): Function to get element IDs.
        selected_parameter (str): The parameter to search for.
        selected_value (str): The value to match.

    Returns:
        list: A list of matching element IDs.
    """
    element_ids = get_element_ids_func()
    selected_element_ids = []
    for element_id in element_ids:
        element = revit.doc.GetElement(element_id)
        parameter = element.LookupParameter(selected_parameter)
        if parameter and parameter.HasValue:
            parameter_value = parameter.AsValueString()
            if parameter_value == selected_value:
                selected_element_ids.append(element_id)
    return selected_element_ids

def category_id_param(category_name, get_element_ids_func, selected_parameter):
    """
    Checks existence of parameter values.

    Args:
        category_name (str): The name of the category.
        get_element_ids_func (function): Function to get element IDs.
        selected_parameter (str): The parameter to check.

    Returns:
        tuple: A tuple containing table data and selected IDs.
    """
    element_ids = get_element_ids_func()
    table_data = []
    selected_ids = []
    for element_id in element_ids:
        element = revit.doc.GetElement(element_id)
        parameter = element.LookupParameter(selected_parameter)
        if parameter:
            if parameter.HasValue:
                parameter_value = parameter.AsValueString()
            else:
                parameter_value = "Does not have value"
            table_data.append([element_id.ToString(), selected_parameter, parameter_value])
            selected_ids.append(element_id)

    return table_data, selected_ids

def category_id_param2(category_name, get_element_ids_func, selected_parameter):
    """
    Retrieves only elements with parameter values.

    Args:
        category_name (str): The name of the category.
        get_element_ids_func (function): Function to get element IDs.
        selected_parameter (str): The parameter to check.

    Returns:
        list: A list of element IDs with values.
    """
    element_ids = get_element_ids_func()
    table_data = []
    for element_id in element_ids:
        element = revit.doc.GetElement(element_id)
        parameter = element.LookupParameter(selected_parameter)
        if parameter and parameter.HasValue:
            parameter_value = parameter.AsValueString()
            table_data.append([output.linkify(element_id), selected_parameter, parameter_value])

    if table_data:
        output.print_table(table_data=table_data,
                        title="Parameter Check for all the {}".format(category_name),
                        columns=["ID", "Target Parameter", "Value"])
    return [data[0] for data in table_data]

def category_id_param3(category_name, get_element_ids_func, selected_parameter):
    """
    Retrieves only elements without parameter values.

    Args:
        category_name (str): The name of the category.
        get_element_ids_func (function): Function to get element IDs.
        selected_parameter (str): The parameter to check.

    Returns:
        list: A list of element IDs without values.
    """
    element_ids = get_element_ids_func()
    selected_element_ids = []
    for element_id in element_ids:
        element = revit.doc.GetElement(element_id)
        parameter = element.LookupParameter(selected_parameter)
        if parameter:
            if not parameter.HasValue:
                selected_element_ids.append(element_id.IntegerValue)
            else:
                continue
    return selected_element_ids

def elements_of_category_all_views(category_id):
    """
    Selects individual elements of a category across all views.

    Args:
        category_id (ElementId): The ID of the category.

    Returns:
        List[ElementId]: A list of selected element IDs.
    """
    doc = __revit__.ActiveUIDocument.Document
    uidoc = __revit__.ActiveUIDocument
    elements = FilteredElementCollector(doc).OfCategory(category_id).WhereElementIsNotElementType().ToElements()
    element_ids = List[ElementId]()
    for element in elements:
        element_ids.Add(element.Id)
    uidoc.Selection.SetElementIds(element_ids)
    uidoc.ShowElements(element_ids)
    return element_ids

def select_all_elements_of_view(uidoc, view):
    """
    Selects all elements of a view.

    Args:
        uidoc: The active UIDocument.
        view: The view to select elements from.

    Returns:
        List[ElementId]: A list of element IDs.
    """
    elements = FilteredElementCollector(uidoc.Document, view.Id).WhereElementIsNotElementType().ToElements()
    element_ids = List[ElementId]([element.Id for element in elements])
    return element_ids

def idlist_inserted(id_str, ms_title, ms_allinvalid, ms_e_integer, ms_e_doc, ms_valid):
    """
    Selects elements by getting a list of integer IDs separated by commas.

    Args:
        id_str (str): The string of IDs.
        ms_title (str): Title for the message.
        ms_allinvalid (str): Message for all invalid IDs.
        ms_e_integer (str): Message for invalid integers.
        ms_e_doc (str): Message for invalid document IDs.
        ms_valid (str): Message for valid IDs.

    Returns:
        str: Message indicating the result of the operation.
    """
    if id_str is None:
        sys.exit()
    id_list = id_str.split(',')
    element_id_objects = List[DB.ElementId]()
    invalid_ids = []
    for id_str in id_list:
        try:
            element_id = int(id_str)
            element = revit.doc.GetElement(DB.ElementId(element_id))
            if element is None:
                invalid_ids.append(str(element_id))
            else:
                element_id_objects.Add(DB.ElementId(element_id))
        except ValueError:
            invalid_ids.append(id_str)
    doc = revit.doc
    invalid_ids_errors = []
    for element_id in element_id_objects:
        try:
            element = doc.GetElement(element_id)
            if element is None:
                invalid_ids_errors.append(str(element_id.IntegerValue))
            else:
                revit.uidoc.Selection.SetElementIds(element_id_objects)
                revit.uidoc.ShowElements(element_id_objects)
        except Exception:
            invalid_ids_errors.append(str(element_id.IntegerValue))
    msg = ms_valid
    if invalid_ids_errors:
        msg = ms_e_doc
        for error in invalid_ids_errors:
            msg += error + '\n'
    if invalid_ids:
        msg = ms_e_integer
        for invalid_id in invalid_ids:
            msg += invalid_id + '\n'
    if not element_id_objects:
        msg = ms_allinvalid
    return msg
