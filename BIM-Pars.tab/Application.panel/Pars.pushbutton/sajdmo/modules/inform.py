# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#inform.py

import os
import sys
from pyrevit import script, revit, DB
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, FamilyInstance, ElementId, BuiltInParameter, ElementLevelFilter, LogicalOrFilter

def category_andId(doc, cat_str, id_str):
    """
    Retrieve category names and IDs for selected elements.

    Args:
        doc: The Revit document.
        cat_str: The string format for category names.
        id_str: The string format for element IDs.

    Returns:
        list: A list of tuples containing formatted category names and IDs.
    """
    uidoc = __revit__.ActiveUIDocument
    selection = uidoc.Selection
    selected_element_ids = selection.GetElementIds()
    if selected_element_ids:
        info = []
        for element_id in selected_element_ids:
            selected_element = doc.GetElement(element_id)
            category_name = selected_element.Category.Name
            element_id = selected_element.Id.IntegerValue
            info.append((cat_str.format(category_name), id_str.format(element_id)))
        return info
    return None

def category_and_id(doc):
    """
    Retrieve category names and IDs for selected elements.

    Args:
        doc: The Revit document.

    Returns:
        list: A list of tuples containing category names and IDs.
    """
    uidoc = __revit__.ActiveUIDocument
    selection = uidoc.Selection
    selected_element_ids = selection.GetElementIds()
    if selected_element_ids:
        info = []
        for element_id in selected_element_ids:
            selected_element = doc.GetElement(element_id)
            category_name = selected_element.Category.Name
            element_id = selected_element.Id.IntegerValue
            info.append(("Category: {0}".format(category_name), "ID: {0}".format(element_id)))
        return info
    return None

def category_and_id_link(doc):
    """
    Retrieve linkified category names and IDs for selected elements.

    Args:
        doc: The Revit document.

    Returns:
        list: A list of tuples containing category names and linkified IDs.
    """
    uidoc = __revit__.ActiveUIDocument
    selection = uidoc.Selection
    selected_element_ids = selection.GetElementIds()
    if selected_element_ids:
        info_Linkified = []
        for element_id in selected_element_ids:
            selected_element = doc.GetElement(element_id)
            category_name = selected_element.Category.Name
            element_id = selected_element.Id
            formatted_id = script.get_output().linkify(element_id)
            info_Linkified.append(("{0}".format(category_name), "{0}".format(formatted_id)))
        return info_Linkified
    return None

def count_elements_in_categories(view):
    """
    Count elements in each category for a given view.

    Args:
        view: The Revit view to count elements in.

    Returns:
        list: A list of category names, IDs, and element counts.
    """
    categories = BuiltInCategory.GetValues(BuiltInCategory)
    category_counts = []
    for category in categories:
        category_id = int(category)
        category_name = category.ToString()
        element_count = len(FilteredElementCollector(view.Document, view.Id).OfCategory(category).ToElements())
        if element_count > 0:  
            category_counts.append([category_name, category_id, element_count])
    return category_counts

def count_elements_in_categories2(view):
    """
    Count elements in each category for a given view, returning only category names.

    Args:
        view: The Revit view to count elements in.

    Returns:
        list: A list of category names.
    """
    categories = list(BuiltInCategory.GetValues(BuiltInCategory)) 
    category_counts = []
    for category in categories:
        category_id = int(category)
        category_name = category.ToString()
        element_count = len(FilteredElementCollector(view.Document, view.Id).OfCategory(category).ToElements())
        if element_count > 0:  
            category_counts.append(category_name)
    return category_counts

def count_elements_in_categories3(view, level_ids):
    """
    Count elements in each category for a given view and level IDs.

    Args:
        view: The Revit view to count elements in.
        level_ids: List of level IDs to filter elements.

    Returns:
        dict: A dictionary mapping category names to their IDs.
    """
    categories = list(BuiltInCategory.GetValues(BuiltInCategory))
    category_counts = {}
    for category in categories:
        category_id = int(category)
        category_name = category.ToString()
        element_count = len(FilteredElementCollector(view.Document, view.Id).OfCategory(category).WhereElementIsNotElementType().WherePasses(LogicalOrFilter([ElementLevelFilter(level_id) for level_id in level_ids])).ToElements())
        if element_count > 0:
            category_counts[category_name] = category
    return category_counts

def familytree(view):
    """
    Retrieve family types for walls in a given view.

    Args:
        view: The Revit view to retrieve wall family types from.

    Returns:
        list: A list of family type details for walls.
    """
    categories = BuiltInCategory.GetValues(BuiltInCategory)
    category_counts = [] 
    walls_collector = FilteredElementCollector(view.Document, view.Id).OfCategory(BuiltInCategory.OST_Walls)
    walls = walls_collector.ToElements()
    wall_family_types = {}  
    for wall in walls:
        wall_type_id = wall.GetTypeId()
        if wall_type_id != ElementId.InvalidElementId:
            wall_type = view.Document.GetElement(wall_type_id)
            family_name = wall_type.FamilyName
            if family_name not in wall_family_types:
                wall_family_types[family_name] = set()
            name_param = wall_type.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM)
            if name_param is not None:
                wall_type_name = name_param.AsString()
                wall_family_types[family_name].add((wall_type_id, wall_type_name))
    for category in categories:
        category_id = int(category)
        category_name = category.ToString()
        if category_name == "INVALID":
            continue
        elements = FilteredElementCollector(view.Document, view.Id).OfCategory(category).ToElements()
        element_count = len(elements)
        if element_count > 0: 
            families_and_types = set([(element.Symbol.FamilyName, element.Symbol.Family.Id, element.Name, element.Symbol.Id) for element in elements if isinstance(element, FamilyInstance)])
            for family, family_id, family_type, family_type_id in families_and_types:
                category_counts.append([category_name, category_id, family, family_id, family_type, family_type_id])
    for family_name, types in wall_family_types.items():
        for wall_type_id, wall_type_name in types:
            wall_category_id = int(BuiltInCategory.OST_Walls)
            category_counts.append(['Walls', wall_category_id, family_name, family_id.IntegerValue, wall_type_name, wall_type_id])
    return category_counts

def catch_project_parameters():
    """
    Retrieve project parameters from the Revit document.

    Returns:
        list: A list of project parameter names and values.
    """
    doc = revit.doc
    collector = DB.FilteredElementCollector(doc).OfClass(DB.ProjectInfo)
    project_info = collector.FirstElement()
    if project_info:
        project_params = project_info.Parameters
        param_data = []
        for param in project_params:
            param_name = param.Definition.Name
            param_value = param.AsValueString()
            if param_name != "PrintManagerSettings":
                param_data.append([param_name, param_value])
        return param_data
    else:
        return None

def get_print_manager_settings():
    """
    Retrieve the print manager settings from the project info.

    Returns:
        str: The print manager settings as a string.
    """
    doc = revit.doc
    collector = DB.FilteredElementCollector(doc).OfClass(DB.ProjectInfo)
    project_info = collector.FirstElement()
    if project_info:
        param = project_info.LookupParameter("PrintManagerSettings")
        if param:
            return param.AsString()
    return "N/A"

def count_elements_in_categories_all_views():
    """
    Count elements in each category across all views.

    Returns:
        tuple: A dictionary of category counts and the total element count.
    """
    doc = __revit__.ActiveUIDocument.Document
    categories = BuiltInCategory.GetValues(BuiltInCategory)
    category_counts = {}
    total_element_count = 0
    for category in categories:
        category_id = int(category)
        category_name = category.ToString()
        if category_name != "INVALID":
            element_count = len(FilteredElementCollector(doc).OfCategory(category).WhereElementIsNotElementType().ToElements())
            if element_count > 0:  
                category_counts[category_id] = [category_name, element_count]
                total_element_count += element_count
    return category_counts, total_element_count

def count_elements_in_categories_for_view(view):
    """
    Count elements in each category for a specific view.

    Args:
        view: The Revit view to count elements in.

    Returns:
        list: A list of category names, IDs, and element counts.
    """
    if view.IsTemplate:
        return []  
    categories = BuiltInCategory.GetValues(BuiltInCategory)
    category_counts = []
    for category in categories:
        category_id = int(category)
        category_name = category.ToString()
        element_count = len(FilteredElementCollector(view.Document, view.Id).OfCategory(category).ToElements())
        if element_count > 0:  
            category_counts.append([category_name, category_id, element_count])
    return category_counts

def catch_family_names_and_types_for_category(view, category_name):
    """
    Retrieve family names and types for a specific category in a view.

    Args:
        view: The Revit view to search in.
        category_name (str): The name of the category to filter by.

    Returns:
        dict: A dictionary mapping family names to their types and IDs.
    """
    category = BuiltInCategory.Parse(BuiltInCategory, category_name)
    elements = FilteredElementCollector(view.Document, view.Id).OfCategory(category).WhereElementIsNotElementType().ToElements()
    if elements:
        family_info = {}
        for element in elements:
            type_name = view.Document.GetElement(element.GetTypeId()).get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString()
            family_name = view.Document.GetElement(element.GetTypeId()).get_Parameter(BuiltInParameter.SYMBOL_FAMILY_NAME_PARAM).AsString()
            if family_name and type_name:
                if family_name not in family_info:
                    family_info[family_name] = []
                family_info[family_name].append((type_name, element.Id))  
        if family_info:
            return family_info
    return None

def category_name(doc, element_id):
    """
    Retrieve the category name of a specific element.

    Args:
        doc: The Revit document.
        element_id: The ID of the element.

    Returns:
        str or None: The category name of the element, or None if not found.
    """
    doc = __revit__.ActiveUIDocument.Document
    if doc:
        selected_element = doc.GetElement(element_id)
        if selected_element:
            return selected_element.Category.Name
    return None

def catch_families_for_levels(view, level_ids, selected_category):
    """
    Retrieve family names for elements in a specific category and level IDs.

    Args:
        view: The Revit view to search in.
        level_ids: List of level IDs to filter elements.
        selected_category (str): The category to filter by.

    Returns:
        dict: A dictionary mapping family names to their element IDs.
    """
    family_info = {}
    category = BuiltInCategory.Parse(BuiltInCategory, selected_category)
    for level_id in level_ids:
        level_filter = ElementLevelFilter(level_id)
        elements_on_level = (FilteredElementCollector(view.Document, view.Id).OfCategory(category).WhereElementIsNotElementType().WherePasses(level_filter).ToElements())
        for element in elements_on_level:
            family_name = (view.Document.GetElement(element.GetTypeId()).get_Parameter(BuiltInParameter.SYMBOL_FAMILY_NAME_PARAM).AsString())
            if family_name:
                if family_name not in family_info:
                    family_info[family_name] = []
                family_info[family_name].append(element.Id)
    return family_info

def catch_types_for_family(view, level_ids, selected_category, selected_family):
    """
    Retrieve types for a specific family in a category and level IDs.

    Args:
        view: The Revit view to search in.
        level_ids: List of level IDs to filter elements.
        selected_category (str): The category to filter by.
        selected_family (str): The family to filter by.

    Returns:
        dict: A dictionary mapping type names to their element IDs.
    """
    type_info = {}
    category = BuiltInCategory.Parse(BuiltInCategory, selected_category)
    for level_id in level_ids:
        level_filter = ElementLevelFilter(level_id)
        elements_on_level = (FilteredElementCollector(view.Document, view.Id).OfCategory(category).WhereElementIsNotElementType().WherePasses(level_filter).ToElements())
        for element in elements_on_level:
            family_name = (view.Document.GetElement(element.GetTypeId()).get_Parameter(BuiltInParameter.SYMBOL_FAMILY_NAME_PARAM).AsString())
            if family_name == selected_family:
                type_name = (view.Document.GetElement(element.GetTypeId()).get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString())
                if type_name:
                    if type_name not in type_info:
                        type_info[type_name] = []
                    type_info[type_name].append(element.Id)
    return type_info