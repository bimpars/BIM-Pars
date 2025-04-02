# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#fv_integer.py

#Imports
import clr
clr.AddReference("RevitAPI")
import sys
from pyrevit import revit, DB, forms
import Autodesk.Revit.DB as DB
from System.Collections.Generic import List

def fvalue_integer(selected_value, cancel_alert, noelementfound_alert, novalueinsert_alert):
    """
    Filters Revit elements based on a specified integer value and updates the selection in the Revit UI.

    This function checks if the provided selected_value is valid and alerts the user if it is not.
    It then filters the currently selected Revit elements to find those whose parameter values 
    match the specified integer value within a defined tolerance. If matching elements are found, 
    they are selected in the Revit UI; otherwise, an alert is shown.

    Parameters:
    selected_value (str or None): The integer value to filter elements by. If None, an alert is shown.
    cancel_alert (str): The message to display if the operation is canceled.
    noelementfound_alert (str): The message to display if no elements are found with the specified value.
    novalueinsert_alert (str): The message to display if no value is inserted.

    Returns:
    None
    """
    selected_value = selected_value
    if selected_value is None:
        forms.alert(cancel_alert)
        sys.exit()
    if selected_value:
        def generate_table(selected_elements_ids, selected_parameter):
            table_data = []
            selected_ids = [] 
            for element_id in selected_elements_ids:
                element = revit.doc.GetElement(element_id)
                table_data.append([element_id.ToString(), selected_parameter, selected_value])
                selected_ids.append(element_id)  
            return table_data, selected_ids
        selected_elements_ids = revit.uidoc.Selection.GetElementIds()
        filtered_element_ids = []
        tolerance = 0.0001  
        for element_id in selected_elements_ids:
            element = revit.doc.GetElement(element_id)
            parameters = element.Parameters
            for parameter in parameters:
                if parameter.HasValue and parameter.StorageType == DB.StorageType.Double:
                    parameter_value = parameter.AsDouble()
                    if abs(parameter_value - float(selected_value)) <= tolerance:
                        filtered_element_ids.append(element_id)
                        break
        table_data, selected_ids = generate_table(filtered_element_ids, selected_value)
        if not selected_ids:
            forms.alert(noelementfound_alert)
        else:
            revit_elements = List[DB.ElementId]()
            for element_id in selected_ids:
                revit_elements.Add(element_id)
            revit.uidoc.Selection.SetElementIds(revit_elements)
            revit.uidoc.ShowElements(revit_elements)
    else:
        forms.alert(noelementfound_alert)
