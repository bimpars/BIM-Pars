# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#message.py

from Autodesk.Revit.UI import (TaskDialog, TaskDialogCommonButtons)

def mes(head, text):
    """
    Displays a message dialog with a specified header and text.

    Parameters:
    head (str): The main instruction or header of the message dialog.
    text (str): The main content or message to be displayed in the dialog.

    Returns:
    TaskDialogResult: The result of the dialog interaction, indicating which button was pressed.
    """
    title = 'Message'
    dialog = TaskDialog(title)
    dialog.MainInstruction = head
    dialog.MainContent = text
    dialog.TitleAutoPrefix = False
    dialog.AllowCancellation = True
    dialog.CommonButtons = TaskDialogCommonButtons.Ok
    result = dialog.Show()
    
pass
