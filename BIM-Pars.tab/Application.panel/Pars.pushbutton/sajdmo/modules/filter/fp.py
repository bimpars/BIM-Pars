# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#fp.py

# Imports
import clr
from pyrevit import revit, forms
from Autodesk.Revit.DB import ElementId
from System.Collections.Generic import List
import sys

def fparam(selected_parameter, cancel_alert, noelement_alert, noparameterinsert_alert):
    """
    Get the value of a specified parameter for selected elements.

    Args:
        selected_parameter (str): The name of the parameter to retrieve.
        cancel_alert (str): The alert message if the operation is canceled.
        noelement_alert (str): The alert message if no elements are found.
        noparameterinsert_alert (str): The alert message if no parameter is inserted.

    Returns:
        str: The selected parameter name.
    """
    selected_parameter = selected_parameter
    if selected_parameter is None:
        forms.alert(cancel_alert)
        sys.exit()
    if selected_parameter:
        def generate_table(selected_elements_ids):
            table_data = []
            selected_ids = [] 
            for element_id in selected_elements_ids:
                element = revit.doc.GetElement(element_id)
                parameter = element.LookupParameter(selected_parameter)
                if parameter:
                    parameter_value = parameter.AsValueString() if parameter.HasValue else "Does not have value"
                    table_data.append([element_id.ToString(), selected_parameter, parameter_value])
                    selected_ids.append(element_id)  
            return table_data, selected_ids
        
        selected_elements_ids = revit.uidoc.Selection.GetElementIds()
        table_data, selected_ids = generate_table(selected_elements_ids)
        if not selected_ids:
            forms.alert(noelement_alert)
        else:
            revit_elements = List[ElementId]()
            for element_id in selected_ids:
                revit_elements.Add(element_id)
            revit.uidoc.Selection.SetElementIds(revit_elements)
            revit.uidoc.ShowElements(revit_elements)
    else:
        forms.alert(noparameterinsert_alert)
    
    return selected_parameter
