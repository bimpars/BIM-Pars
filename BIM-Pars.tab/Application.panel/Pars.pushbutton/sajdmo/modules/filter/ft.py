# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#ft.py

# Imports
from pyrevit import revit, forms
from Autodesk.Revit.DB import ElementId
from System.Collections.Generic import List
import sys

def ftype(title, button_name, cancel_alert, noelementtitle_alert, noelement_alert):
    """
    Filter elements by type.

    Args:
        title (str): The title for the type selection dialog.
        button_name (str): The name of the button in the dialog.
        cancel_alert (str): The alert message if the operation is canceled.
        noelementtitle_alert (str): The title for the no element alert.
        noelement_alert (str): The alert message if no elements are found.

    Returns:
        list: The selected type names.
    """
    selection = revit.uidoc.Selection.GetElementIds()
    type_names = set()
    for element_id in selection:
        element = revit.doc.GetElement(element_id)
        type_name = element.Name
        type_names.add(type_name)
    
    selected_type = forms.SelectFromList.show(
        sorted(type_names),
        title=title,
        button_name=button_name,
        multiselect=True
    )
    
    if selected_type is None:
        forms.alert(cancel_alert)
        sys.exit()
    else:
        filtered_element_ids = []
        for element_id in selection:
            element = revit.doc.GetElement(element_id)
            type_name = element.Name
            if type_name in selected_type:
                filtered_element_ids.append(element_id)
        
        if len(filtered_element_ids) < 1:
            forms.alert(noelement_alert, title=noelementtitle_alert)
        else:
            revit.uidoc.Selection.SetElementIds(List[ElementId](filtered_element_ids))
            revit.uidoc.ShowElements(List[ElementId](filtered_element_ids))

    return selected_type
