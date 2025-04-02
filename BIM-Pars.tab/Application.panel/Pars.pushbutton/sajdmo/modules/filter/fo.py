# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#fo.py

# Imports
from pyrevit import revit, forms
from Autodesk.Revit.DB import ElementId
from System.Collections.Generic import List
import os
import sys

def fowner(emptyselectiontitle_alert, emptyselection_alert, title, button_name, cancel_alert, noelement_alert, noownerselect_alert, nonamefound):
    """
    Get the owner names for selected elements.

    Args:
        emptyselectiontitle_alert (str): Title for the empty selection alert.
        emptyselection_alert (str): Message for the empty selection alert.
        title (str): Title for the selection dialog.
        button_name (str): The name of the button in the dialog.
        cancel_alert (str): The alert message if the operation is canceled.
        noelement_alert (str): Message if no elements are found.
        noownerselect_alert (str): Message if no owner is selected.
        nonamefound (str): Message if no owner names are found.

    Returns:
        str or None: The selected owner name or None if not found.
    """
    selection = revit.get_selection()
    if len(selection) < 1:
        forms.alert(emptyselection_alert, title=emptyselectiontitle_alert)
    else:
        def get_owner_names():
            owner_names = set()  
            for element in selection:
                eh = revit.query.get_history(element)
                owner_names.add(eh.owner)
            if owner_names:
                return list(owner_names) 
            else:
                return None
        owner_names = get_owner_names()
        if owner_names:
            selected_owner = forms.SelectFromList.show(owner_names, title=title, multiselect=False, button_name=button_name)
            if selected_owner is None:
                forms.alert(cancel_alert)
                sys.exit()
            if selected_owner:
                filtered_element_ids = []
                for element in selection:
                    eh = revit.query.get_history(element)
                    if eh.owner == selected_owner:
                        filtered_element_ids.append(element.Id)
                if len(filtered_element_ids) > 0:
                    revit.uidoc.Selection.SetElementIds(List[ElementId](filtered_element_ids))
                    revit.uidoc.ShowElements(List[ElementId](filtered_element_ids))
                else:
                    forms.alert(noelement_alert)
            else:
                forms.alert(noownerselect_alert)
        else:
            forms.alert(nonamefound)

    return selected_owner
