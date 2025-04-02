# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#pset.py

import clr
import Autodesk.Revit.DB as DB
from Autodesk.Revit.DB import ElementId
from pyrevit import forms, script
import sys
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
doc = __revit__.ActiveUIDocument.Document

def pvset_text(parameter_name, value):
    """
    Set the same value for all selected elements.

    Args:
        parameter_name (str): The name of the parameter to set.
        value: The value to set for the parameter.
    """
    selection = __revit__.ActiveUIDocument.Selection.GetElementIds()
    if len(selection) == 0:
        sys.exit()
    elements = [doc.GetElement(element_id) for element_id in selection]
    param_type = elements[0].LookupParameter(parameter_name).Definition.ParameterType
    if param_type:                
        if param_type == DB.ParameterType.Text or param_type == DB.ParameterType.Integer or param_type == DB.ParameterType.Number:
            while True:
                if value is None: 
                    sys.exit()
                with DB.Transaction(doc, 'Set Parameter Value') as trans:
                    trans.Start()
                    valid_value = True  
                    for element in elements:
                        param = element.LookupParameter(parameter_name)
                        if param is None:
                            continue
                        if param.StorageType == DB.StorageType.String:
                            param.Set(value)
                        elif param.StorageType == DB.StorageType.Integer:
                            try:
                                param.Set(int(value))
                            except ValueError:
                                forms.alert('Invalid value for Integer type. Please enter a valid Integer.')
                                valid_value = False  
                                break
                        elif param.StorageType == DB.StorageType.Double:
                            try:
                                param.Set(float(value))
                            except ValueError:
                                forms.alert('Invalid value for Number type. Please enter a valid Number.')
                                valid_value = False  
                                break
                        elif param.StorageType == DB.StorageType.ElementId:
                            pass
                        elif param.StorageType == DB.StorageType.Boolean:
                            try:
                                param.Set(bool(value))
                            except ValueError:
                                forms.alert('Invalid value for Boolean type. Please enter a valid Boolean.')
                                valid_value = False 
                                break
                        elif param.StorageType == DB.StorageType.None:
                            pass
                    trans.Commit()
                    if valid_value:
                        break

def p_values(selection, parameter_name, doc):
    """
    Retrieve values of a specified parameter for a list of selected elements.

    Args:
        selection: List of ElementId objects representing selected elements.
        parameter_name (str): The name of the parameter to retrieve values for.
        doc: The Revit Document object to access elements.

    Returns:
        list: List of parameter values.
    """
    values = []
    for element_id in selection:
        if isinstance(element_id, ElementId):
            element = doc.GetElement(element_id)
            if element:
                param = element.LookupParameter(parameter_name)
                if param:
                    values.append(param.AsValueString())
                else:
                    values.append(None)
    return values

def link_ids(selection, doc):
    """
    Retrieve linkified IDs of selected elements.

    Args:
        selection: List of ElementId objects representing selected elements.
        doc: The Revit Document object to access elements.

    Returns:
        list: List of linkified element IDs as strings.
    """
    output = script.get_output()
    linkified_ids = []
    for element_id in selection:
        if isinstance(element_id, ElementId):
            linkified_id = output.linkify(element_id)
            linkified_ids.append(linkified_id)
    return linkified_ids

def print_table_from_lists(list1, list2, list3, columns, title):
    """
    Print a table with three columns using the provided lists.

    Args:
        list1: List of values for the first column.
        list2: List of values for the second column.
        list3: List of values for the third column.
        title (str): Title of the table.
    """
    output = script.get_output()
    if not (len(list1) == len(list2) == len(list3)):
        raise ValueError("An error occurred.")
    data = list(zip(list1, list2, list3))
    formats = ['', '', '']
    output.print_table(table_data=data, title=title, columns=columns, formats=formats)

def print_table_from_4lists(list1, list2, list3, list4, columns, title):
    """
    Print a table with four columns using the provided lists.

    Args:
        list1: List of values for the first column.
        list2: List of values for the second column.
        list3: List of values for the third column.
        list4: List of values for the fourth column.
        title (str): Title of the table.
    """
    output = script.get_output()
    if not (len(list1) == len(list2) == len(list3) == len(list4)):
        raise ValueError("An error occurred.")
    data = list(zip(list1, list2, list3, list4))
    formats = ['', '', '', '']
    output.print_table(table_data=data, title=title, columns=columns, formats=formats)

def int_ids(selection, doc):
    """
    Retrieve integer IDs of selected elements.

    Args:
        selection: List of ElementId objects representing selected elements.
        doc: The Revit Document object to access elements.

    Returns:
        list: List of integer IDs of elements.
    """
    int_ids_list = []
    for element_id in selection:
        if isinstance(element_id, ElementId):
            int_id = element_id.IntegerValue
            int_ids_list.append(int_id)
    return int_ids_list

def c_name(int_ids, doc):
    """
    Retrieve names of elements based on their integer IDs.

    Args:
        int_ids: List of integer IDs representing the elements.
        doc: The Revit Document object to access elements.

    Returns:
        list: List of names of elements as strings.
    """
    element_names = []
    for int_id in int_ids:
        element = doc.GetElement(ElementId(int_id))
        if element is not None:
            element_name = element.Name
            element_names.append(element_name)
        else:
            element_names.append("Element not found")
    return element_names

def c_category(int_ids, doc):
    """
    Retrieve categories of elements based on their integer IDs.

    Args:
        int_ids: List of integer IDs representing the elements.
        doc: The Revit Document object to access elements.

    Returns:
        list: List of categories of elements as strings.
    """
    element_categories = []
    for int_id in int_ids:
        element = doc.GetElement(ElementId(int_id))
        if element is not None:
            category = element.Category
            if category is not None:
                element_categories.append(category.Name)
            else:
                element_categories.append("No category")
        else:
            element_categories.append("Element not found")
    return element_categories

def c_storage_type(param_names, element):
    """
    Retrieve the storage types of parameters based on their names for a given element.

    Args:
        param_names: List of parameter names as strings.
        element: The Revit element object to access parameters.

    Returns:
        list: List of storage types of the parameters as strings.
    """
    storage_types = []
    for param_name in param_names:
        parameter = element.LookupParameter(param_name)
        if parameter is not None:
            storage_type = parameter.StorageType
            storage_types.append(storage_type.ToString())
        else:
            storage_types.append("Parameter not found")
    return storage_types