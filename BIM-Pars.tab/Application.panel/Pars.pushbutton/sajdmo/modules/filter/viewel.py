# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#viewel.py

#Imports
from Autodesk.Revit.DB import FilteredElementCollector, ElementId
from System.Collections.Generic import List

def curr_viewel(uidoc):
    """Retrieve the element IDs of all elements in the current active view.

    Args:
        uidoc: The active UIDocument from which to retrieve the view elements.

    Returns:
        List[ElementId]: A list of ElementId objects representing the elements in the active view.
    """
    active_view = uidoc.ActiveView
    elements = FilteredElementCollector(uidoc.Document, active_view.Id).WhereElementIsNotElementType().ToElements()
    element_ids = List[ElementId]([element.Id for element in elements])
    return element_ids
    
def curr_viewname(uidoc):
    """Retrieve the name of the current active view.

    Args:
        uidoc: The active UIDocument from which to retrieve the view name.

    Returns:
        str: The name of the active view.
    """
    active_view = uidoc.ActiveView
    view_name = active_view.Name
    return view_name