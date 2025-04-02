# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#fl.py

# Imports
from pyrevit import revit, forms
from Autodesk.Revit.DB import FilteredElementCollector, ElementLevelFilter, ElementId, LogicalOrFilter
from System.Collections.Generic import List
import sys

uidoc = revit.uidoc  
doc = revit.doc  

def flevel(title, button_name, cancel_alert):
    """
    Filter elements by level.

    Args:
        title (str): The title for the level selection dialog.
        button_name (str): The name of the button in the dialog.
        cancel_alert (str): The alert message if the operation is canceled.

    Returns:
        list: The selected levels.
    """
    selection = uidoc.Selection.GetElementIds()
    level_ids = set()
    for element_id in selection:
        element = doc.GetElement(element_id)
        level_id = element.LevelId
        if level_id != ElementId.InvalidElementId:
            level_ids.add(level_id)
    selected_levels = forms.select_levels(
        title=title,
        button_name=button_name,
        width=500,
        multiple=True,
        filterfunc=lambda level: level.Id in level_ids,
        doc=doc,
        use_selection=False
    )
    if selected_levels is None:
        forms.alert(cancel_alert)
        sys.exit()
    else:
        filters = []
        for level in selected_levels:
            level_filter = ElementLevelFilter(level.Id)
            filters.append(level_filter)
        combined_filter = LogicalOrFilter(filters)
        filtered_elements = FilteredElementCollector(doc).WherePasses(combined_filter)
        filtered_element_ids = [element_id for element_id in filtered_elements.ToElementIds()]
        uidoc.Selection.SetElementIds(List[ElementId](filtered_element_ids))

    return selected_levels

