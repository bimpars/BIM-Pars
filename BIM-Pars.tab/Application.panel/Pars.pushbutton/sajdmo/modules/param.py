# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#param.py

import os
import sys
import clr
clr.AddReference("RevitAPI")
from collections import defaultdict

def get_parameter_value(element, param_definition):
    """
    Get the value of a specified parameter from an element.

    Args:
        element: The Revit element to retrieve the parameter from.
        param_definition: The parameter definition to look up.

    Returns:
        str or None: The value of the parameter as a string, or None if not found.
    """
    param_value = None
    param = element.LookupParameter(param_definition.Name)
    if param and param.HasValue:
        param_value = param.AsValueString()
    return param_value

def map(element):
    """
    Map instance and type parameters for a given element.

    Args:
        element: The Revit element to map parameters for.

    Returns:
        tuple: A tuple containing instance and type parameter maps.
    """
    inst_map = dic(element)
    type_map = None
    if "Symbol" in dir(element):
        elem_symbol = element.Symbol
        type_map = dic(elem_symbol)
    return inst_map, type_map

def dic(param_element):
    """
    Create a dictionary of parameters for a given element.

    Args:
        param_element: The Revit element to retrieve parameters from.

    Returns:
        dict: A dictionary mapping parameter names to their values.
    """
    parameters = param_element.Parameters
    param_dict = defaultdict(list)
    for param in parameters:
        param_dict[param.Definition.Name].append(param.StorageType.ToString().split(".")[-1])
        param_dict[param.Definition.Name].append(param.HasValue)
        param_value = None
        if param.HasValue:
            if param.StorageType.ToString() == "ElementId":
                param_value = param.AsElementId().IntegerValue
            elif param.StorageType.ToString() == "Integer":
                param_value = param.AsInteger()
            elif param.StorageType.ToString() == "Double":
                param_value = param.AsDouble()
            elif param.StorageType.ToString() == "String":
                param_value = param.AsString()
        param_dict[param.Definition.Name].append(str(param_value))
    return param_dict