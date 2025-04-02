# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#fm.py

# Imports
from pyrevit import revit, forms
from Autodesk.Revit.DB import ElementId
from System.Collections.Generic import List
import sys

def fmodified(emptyselectiontitle_alert, emptyselection_alert, title, button_name, cancel_alert, noelement_alert, noownerselect_alert, nonamefound):
    """
    Get the last modified by names for selected elements.

    Args:
        emptyselectiontitle_alert (str): Title for the empty selection alert.
        emptyselection_alert (str): Message for the empty selection alert.
        title (str): Title for the selection dialog.
        button_name (str): The name of the button in the dialog.
        cancel_alert (str): The alert message if the operation is canceled.
        noelement_alert (str): Message if no elements are found.
        noownerselect_alert (str): Message if no owner is selected.
        nonamefound (str): Message if no names are found.

    Returns:
        str or None: The selected last modified by name or None if not found.
    """
    selection = revit.get_selection()
    if len(selection) < 1:
        forms.alert(emptyselection_alert, title=emptyselectiontitle_alert)
    else:
        def get_last_changed_by_names():
            last_changed_by_names = set()  
            for element in selection:
                eh = revit.query.get_history(element)
                last_changed_by_names.add(eh.last_changed_by)
            if last_changed_by_names:
                return list(last_changed_by_names) 
            else:
                return None
        last_changed_by_names = get_last_changed_by_names()
        if last_changed_by_names:
            selected_last_changed_by = forms.SelectFromList.show(last_changed_by_names, title=title, multiselect=False, button_name=button_name)
            if selected_last_changed_by is None:
                forms.alert(cancel_alert)
                sys.exit()
            if selected_last_changed_by:
                filtered_element_ids = []
                for element in selection:
                    eh = revit.query.get_history(element)
                    if eh.last_changed_by == selected_last_changed_by:
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

    return selected_last_changed_by
