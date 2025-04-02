# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#fte.py

#Imports
from pyrevit import revit, forms
from Autodesk.Revit.DB import ElementId
from System.Collections.Generic import List
uidoc = revit.uidoc  
doc = revit.doc 

def ftypeel():
    """
    Filter elements by their type from the currently selected elements in Revit.

    This function allows the user to select elements based on their type
    and updates the selection in the Revit UI accordingly.
    
    Returns:
        None
    """
    selection = uidoc.Selection.GetElementIds()
    type_names = set()
    for element_id in selection:
        element = doc.GetElement(element_id)
        type_name = element.GetType().Name
        type_names.add(type_name)
    selected_type = forms.SelectFromList.show(
        sorted(type_names),
        button_name="Select Type of elements"
    )

    if selected_type is None:
        forms.alert("Operation canceled.")
    else:
        filtered_element_ids = []
        for element_id in selection:
            element = doc.GetElement(element_id)
            type_name = element.GetType().Name
            if type_name == selected_type:
                filtered_element_ids.append(element_id)
        if len(filtered_element_ids) < 1:
            forms.alert("No elements with the selected type found.", title="Information")
        else:
            uidoc.Selection.SetElementIds(List[ElementId](filtered_element_ids))