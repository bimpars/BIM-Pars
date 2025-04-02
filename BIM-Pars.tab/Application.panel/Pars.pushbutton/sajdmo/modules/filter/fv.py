# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#fv.py

#Imports
import clr
clr.AddReference("RevitAPI")
import sys
from pyrevit import revit, DB, forms
from System.Collections.Generic import List
from Autodesk.Revit.DB import ElementId

def fvalue(selected_parameter,selected_value,emptyselection_alert,noelement_alert,noelementwithvalue_alert,novalueinsert_alert,noparameterinsert_alert):
    """
    Filters Revit elements based on a specified parameter and value.

    This function retrieves elements from the active Revit document that match the 
    given parameter and value. It alerts the user if no elements are selected, 
    if no elements are found, or if the specified parameter or value is not provided.

    Parameters:
    selected_parameter (str): The name of the parameter to filter elements by.
    selected_value (str): The value of the parameter to match.
    emptyselection_alert (str): Alert message for no selected elements.
    noelement_alert (str): Alert message for no elements found.
    noelementwithvalue_alert (str): Alert message for no elements found with the specified value.
    novalueinsert_alert (str): Alert message for no specific value inserted.
    noparameterinsert_alert (str): Alert message for no parameter inserted.
    """
    doc = __revit__.ActiveUIDocument.Document
    selected_elements = __revit__.ActiveUIDocument.Selection.GetElementIds()
    if len(selected_elements) == 0:
        forms.alert(emptyselection_alert)
        sys.exit()
    selected_parameter = selected_parameter
    if selected_parameter is None:
        sys.exit()
    def generate_table(category):
        element_ids = DB.FilteredElementCollector(revit.doc).OfCategoryId(category.Id).ToElementIds()
        selected_element_ids = []  
        for element_id in element_ids:
            element = revit.doc.GetElement(element_id)
            parameter = element.LookupParameter(selected_parameter)
            if parameter and parameter.HasValue:
                parameter_value = parameter.AsValueString()
                if parameter_value == selected_value:
                    selected_element_ids.append(element_id) 
        return selected_element_ids
    if selected_parameter:
        selected_value = selected_value
        if selected_value is None:
            sys.exit()
        if selected_value:
            all_selected_element_ids = []  
            selected_ids_from_selected_elements = []  
            categories = doc.Settings.Categories  
            for category in categories:
                if category.AllowsBoundParameters:  
                    selected_element_ids = generate_table(category)
                    all_selected_element_ids.extend(selected_element_ids) 
                    selected_element_ids_from_selected = [id for id in selected_element_ids if id in revit.uidoc.Selection.GetElementIds()]
                    selected_ids_from_selected_elements.extend(selected_element_ids_from_selected)    
            if all_selected_element_ids:
                element_id_collection = List[ElementId](all_selected_element_ids) 
                revit.uidoc.Selection.SetElementIds(element_id_collection)
                revit.uidoc.ShowElements(element_id_collection)
                selected_ids_collection = List[ElementId](selected_ids_from_selected_elements)  
                revit.uidoc.Selection.SetElementIds(selected_ids_collection)
                if len(selected_ids_collection) == 0:
                    forms.alert(noelement_alert)
                else:
                    revit.uidoc.ShowElements(selected_ids_collection)
                all_selected_id_list = [element_id.IntegerValue for element_id in all_selected_element_ids if isinstance(element_id, ElementId)]
                selected_from_selected_id_list = [element_id.IntegerValue for element_id in selected_ids_from_selected_elements if isinstance(element_id, ElementId)]
            else:
                forms.alert(noelementwithvalue_alert)
        else:
            forms.alert(novalueinsert_alert)
    else:
        forms.alert(noparameterinsert_alert)
