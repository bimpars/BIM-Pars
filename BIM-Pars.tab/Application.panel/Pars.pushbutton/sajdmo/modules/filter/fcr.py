# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#fcr.py

# Imports
from pyrevit import revit, forms
from Autodesk.Revit.DB import ElementId
from System.Collections.Generic import List
import sys
import os

def fcreator(emptyselectiontitle_alert, emptyselection_alert, title, button_name, noelement_alert, nocreatorselected_alert, nonamefound_alert):
    """
    Create a filtered selection based on the creator of elements.

    Args:
        emptyselectiontitle_alert (str): Title for the empty selection alert.
        emptyselection_alert (str): Message for the empty selection alert.
        title (str): Title for the selection dialog.
        button_name (str): The name of the button in the dialog.
        noelement_alert (str): Message if no elements are found.
        nocreatorselected_alert (str): Message if no creator is selected.
        nonamefound_alert (str): Message if no creator names are found.

    Returns:
        str or None: The selected creator name or None if not found.
    """
    selection = revit.get_selection()
    if len(selection) < 1:
        forms.alert(emptyselection_alert, title=emptyselectiontitle_alert)
    else:
        def get_creator_names():
            creator_names = set()  
            for element in selection:
                eh = revit.query.get_history(element)
                creator_names.add(eh.creator)
            if creator_names:
                return list(creator_names) 
            else:
                return None
        creator_names = get_creator_names()
        if creator_names:
            selected_creator = forms.SelectFromList.show(creator_names, title=title, multiselect=False, button_name=button_name)
            if selected_creator is None:
                sys.exit()
            if selected_creator:
                filtered_element_ids = []
                for element in selection:
                    eh = revit.query.get_history(element)
                    if eh.creator == selected_creator:
                        filtered_element_ids.append(element.Id)
                if len(filtered_element_ids) > 0:
                    revit.uidoc.Selection.SetElementIds(List[ElementId](filtered_element_ids))
                    revit.uidoc.ShowElements(List[ElementId](filtered_element_ids))
                else:
                    forms.alert(noelement_alert)
            else:
                forms.alert(nocreatorselected_alert)
        else:
            forms.alert(nonamefound_alert)

    return selected_creator
