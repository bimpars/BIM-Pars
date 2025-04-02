# -*- coding: utf-8 -*-
# __author__ = "Mohammad Sajjad Mortazavi"
#tables.py

from pyrevit import revit, DB, script, forms
output = script.get_output()

def id_param_value(category_name, get_element_ids_func, selected_parameter, selected_value):
    """
    Searches for the value of instance parameters.

    Args:
        category_name (str): The name of the category.
        get_element_ids_func (function): Function to get element IDs.
        selected_parameter (str): The parameter to search for.
        selected_value (str): The value to match.

    Returns:
        list: A list of matching parameter values.
    """
    element_ids = get_element_ids_func()                
    table_data = []
    for element_id in element_ids:
        element = revit.doc.GetElement(element_id)
        parameter = element.LookupParameter(selected_parameter)
        if parameter and parameter.HasValue:
            parameter_value = parameter.AsValueString()
            if parameter_value == selected_value:
                table_data.append([output.linkify(element_id), selected_parameter, parameter_value])
    return table_data

def int_id_param_value(category_name, get_element_ids_func, selected_parameter, selected_value):
    """
    Searches for integer ID values of instance parameters.

    Args:
        category_name (str): The name of the category.
        get_element_ids_func (function): Function to get element IDs.
        selected_parameter (str): The parameter to search for.
        selected_value (str): The value to match.

    Returns:
        list: A list of matching parameter values.
    """
    element_ids = get_element_ids_func()                
    table_data = []
    for element_id in element_ids:
        element = revit.doc.GetElement(element_id)
        parameter = element.LookupParameter(selected_parameter)
        if parameter and parameter.HasValue:
            parameter_value = parameter.AsValueString()
            if parameter_value == selected_value:
                table_data.append([str(element_id), selected_parameter, parameter_value])
    return table_data

def intig_id_param_value(get_element_ids_func, selected_parameter, selected_value):
    """
    Searches for integer ID values and additional element information.

    Args:
        get_element_ids_func (function): Function to get element IDs.
        selected_parameter (str): The parameter to search for.
        selected_value (str): The value to match.

    Returns:
        list: A list of matching parameter values with additional information.
    """
    element_ids = get_element_ids_func()                
    table_data = []
    for element_id in element_ids:
        element = revit.doc.GetElement(element_id)
        element_name = element.Name  
        element_category = element.Category.Name  
        parameter = element.LookupParameter(selected_parameter)
        if parameter and parameter.HasValue:
            parameter_value = parameter.AsValueString()
            if parameter_value == selected_value:
                table_data.append([str(element_id), element_name, element_category, selected_parameter, parameter_value])
    return table_data



            

