# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#fc.py

# Imports
import os
from pyrevit import revit, forms
from Autodesk.Revit.DB import ElementId
from System.Collections.Generic import List
import sys

uidoc = revit.uidoc  
doc = revit.doc 

def fcat(title, button_name, cancel_alert, element_alert_title, element_alert):
    """
    Filter elements by category.

    Args:
        title (str): The title for the selection dialog.
        button_name (str): The name of the button in the dialog.
        cancel_alert (str): The alert message if the operation is canceled.
        element_alert_title (str): The title for the element alert.
        element_alert (str): The alert message if no elements are found.

    Returns:
        list: The selected category names.
    """
    selection = uidoc.Selection.GetElementIds()
    category_names = set()
    for element_id in selection:
        element = doc.GetElement(element_id)
        category = element.Category
        if category is not None:
            category_names.add(category.Name)
    selected_category = forms.SelectFromList.show(
        sorted(category_names),
        title=title,
        button_name=button_name,
        multiselect=True
    )
    if selected_category is None:
        forms.alert(cancel_alert)
        sys.exit()
    else:
        filtered_element_ids = []
        for element_id in selection:
            element = doc.GetElement(element_id)
            category = element.Category
            if category is not None and category.Name in selected_category:
                filtered_element_ids.append(element_id)
        if len(filtered_element_ids) < 1:
            forms.alert(element_alert, title=element_alert_title)
        else:
            uidoc.Selection.SetElementIds(List[ElementId](filtered_element_ids))
            revit.uidoc.ShowElements(List[ElementId](filtered_element_ids))

    return selected_category
