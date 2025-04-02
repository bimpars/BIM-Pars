# -*- coding: utf-8 -*-
# __author__ = "Mohammad Sajjad Mortazavi"
#delete.py

import os
import sys
import pyrevit
from pyrevit import revit, DB, forms
from Autodesk.Revit.UI import (TaskDialog, TaskDialogCommonButtons, TaskDialogCommandLinkId, TaskDialogResult)

def selection_delete_el(tit_msg, succ_msg, unsucc_msg):
    """
    Deletes selected elements in Revit.

    Args:
        tit_msg (str): Title for the dialog.
        succ_msg (str): Success message to display.
        unsucc_msg (str): Message to display if no elements are selected.
    """
    selection = revit.uidoc.Selection
    selected_ids = selection.GetElementIds()
    if selected_ids:
        with revit.Transaction("Delete Elements"):
            for element_id in selected_ids:
                element = revit.doc.GetElement(element_id)
                revit.doc.Delete(element.Id)
        title = tit_msg
        dialog = TaskDialog(title)
        dialog.MainContent = succ_msg
        dialog.TitleAutoPrefix = False
        dialog.AllowCancellation = True
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.DefaultButton = TaskDialogResult.None
        result = dialog.Show()
        if result == TaskDialogResult.Ok:
            sys.exit()
        if result == TaskDialogResult.Cancel:
            sys.exit()
    else:
        title = tit_msg
        dialog = TaskDialog(title)
        dialog.MainContent = unsucc_msg
        dialog.TitleAutoPrefix = False
        dialog.AllowCancellation = True
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.DefaultButton = TaskDialogResult.None
        result = dialog.Show()
        if result == TaskDialogResult.Ok:
            sys.exit()
        if result == TaskDialogResult.Cancel:
            sys.exit()
