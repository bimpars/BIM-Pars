# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#select.py

#Imports
import Autodesk.Revit.DB as DB
from pyrevit import revit
from System.Collections.Generic import List

def selectlist(element_ids):
    """
    Selects elements in the Revit UI based on a list of element IDs.

    Args:
        element_ids (list): A list of element IDs to be selected in the Revit document.

    This function converts the provided element IDs into ElementId objects,
    sets them as the current selection in the Revit UI, and displays the selected
    elements.
    """
    doc = revit.doc
    element_id_objects = List[DB.ElementId]()
    for element_id in element_ids:
        element_id_object = DB.ElementId(element_id)
        element_id_objects.Add(element_id_object)
    revit.uidoc.Selection.SetElementIds(element_id_objects)
    revit.uidoc.ShowElements(element_id_objects)
