# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#ff.py

# Imports
from pyrevit import revit, forms
from Autodesk.Revit.DB import ElementId
from System.Collections.Generic import List
import sys

uidoc = revit.uidoc  
doc = revit.doc 

def ffamily(title, button_name, cancel_alert, noelement_alert, noelementtitle_alert):
    """
    Filter elements by family.

    Args:
        title (str): The title for the selection dialog.
        button_name (str): The name of the button in the dialog.
        cancel_alert (str): The alert message if the operation is canceled.
        noelement_alert (str): The alert message if no elements are found.
        noelementtitle_alert (str): The title for the no element alert.

    Returns:
        list: The selected family names.
    """
    selection = uidoc.Selection.GetElementIds()
    family_names = set()
    for element_id in selection:
        element = doc.GetElement(element_id)
        family_name = doc.GetElement(element.GetTypeId()).FamilyName
        family_names.add(family_name)
    selected_family = forms.SelectFromList.show(
        sorted(family_names),
        title=title,
        button_name=button_name,
        multiselect=True
    )
    if selected_family is None:
        forms.alert(cancel_alert)
        sys.exit()
    else:
        filtered_element_ids = []
        for element_id in selection:
            element = doc.GetElement(element_id)
            family_name = doc.GetElement(element.GetTypeId()).FamilyName
            if family_name in selected_family:
                filtered_element_ids.append(element_id)
        if len(filtered_element_ids) < 1:
            forms.alert(noelement_alert, title=noelementtitle_alert)
        else:
            uidoc.Selection.SetElementIds(List[ElementId](filtered_element_ids))
            revit.uidoc.ShowElements(List[ElementId](filtered_element_ids))
    return selected_family
