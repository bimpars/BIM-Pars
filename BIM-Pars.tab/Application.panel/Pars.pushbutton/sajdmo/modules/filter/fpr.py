# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#fpr.py

# Imports
from Autodesk.Revit.DB import ElementId
from System.Collections.Generic import List
from pyrevit import revit, script

def fprint():
    """
    Print clickable links for selected elements in Revit.

    This function retrieves the selected elements in the active Revit document,
    generates clickable links for each element, and prints them to the console.
    """
    selection = revit.uidoc.Selection
    selected_elements = selection.GetElementIds()
    element_ids = List[ElementId](selected_elements)
    combined_ids = '+'.join(str(element_id.IntegerValue) for element_id in element_ids)
    
    for element_id in selected_elements:
        element = revit.doc.GetElement(element_id)
        clickable_link = script.get_output().linkify(element.Id)
        print(clickable_link)
    
    revit.uidoc.ShowElements(element_ids)