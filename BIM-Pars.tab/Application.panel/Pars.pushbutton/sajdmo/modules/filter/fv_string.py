# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#fv_string.py

#Imports
import clr
clr.AddReference("RevitAPI")
import sys
from pyrevit import revit, DB, forms
import Autodesk.Revit.DB as DB
from System.Collections.Generic import List

def fvalue_string(selected_value,cancel_alert,noelementfound_alert,novalueinsert_alert):
    """Processes the selected value and alerts the user based on the selection results.

    Args:
        selected_value: The value to be matched against element parameters.
        cancel_alert: Message to display if the operation is canceled.
        noelementfound_alert: Message to display if no elements match the selected value.
        novalueinsert_alert: Message to display if no value is inserted.
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
            for element_id in selected_elements_ids:
                element = revit.doc.GetElement(element_id)
                parameters = element.Parameters
                for parameter in parameters:
                    if parameter.HasValue:
                        parameter_value = parameter.AsString()
                        if parameter_value == selected_value:
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
            forms.alert(novalueinsert_alert)
