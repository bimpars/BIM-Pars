# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#av.py

# Imports
from pyrevit import forms
from Autodesk.Revit.DB import FilteredElementCollector, ElementId
from System.Collections.Generic import List
import sys

def select_all_elements_of_view(uidoc, view):
    """
    Select all elements of a specified view.

    Args:
        uidoc: The active UIDocument.
        view: The view to select elements from.

    Returns:
        List[ElementId]: A list of element IDs.
    """
    elements = FilteredElementCollector(uidoc.Document, view.Id).WhereElementIsNotElementType().ToElements()
    element_ids = List[ElementId]([element.Id for element in elements])
    return element_ids

def ae(title, button_name, cancel_alert):
    """
    Execute the selection of views and set their elements.

    Args:
        title (str): The title for the view selection dialog.
        button_name (str): The name of the button in the dialog.
        cancel_alert (str): The alert message if the operation is canceled.

    Returns:
        list: The selected views.
    """
    selected_views = forms.select_views(title=title, button_name=button_name)
    if selected_views is None:
        forms.alert(cancel_alert)
        sys.exit()
    if selected_views:
        uidoc = __revit__.ActiveUIDocument
        for view in selected_views:
            element_ids = select_all_elements_of_view(uidoc, view)
            uidoc.ActiveView = view  
            uidoc.Selection.SetElementIds(element_ids)
    return selected_views

