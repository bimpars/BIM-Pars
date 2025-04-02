# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#cau.py

# Imports
from pyrevit import revit

def caunt():
    """
    Count the number of selected elements in the Revit document.

    Returns:
        str: The count of selected elements as a string.
    """
    selection = revit.uidoc.Selection
    selected_elements = selection.GetElementIds()
    caunt = str(len(selected_elements))
    return caunt