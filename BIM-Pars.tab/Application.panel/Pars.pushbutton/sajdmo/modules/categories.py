# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#categories.py

import clr
clr.AddReference("RevitAPI")
from rpw import doc
from pyrevit import DB


def Doors():
    doors = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Doors)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return doors
door_ids = Doors()

def Viewers():
    views = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Views)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return views
view_ids = Viewers()

def Windows():
    windows = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Windows)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return windows
window_ids = Windows()

def Walls():
    walls = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Walls)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return walls
wall_ids = Walls()

def AirTerminals():
    air_terminals = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_DuctTerminal)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return air_terminals
air_terminal_ids = AirTerminals()

def CableTrayFittings():
    cable_tray_fittings = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_CableTrayFitting)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return cable_tray_fittings
cable_tray_fitting_ids = CableTrayFittings()

def CableTrays():
    cable_trays = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_CableTray)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return cable_trays
cable_tray_ids = CableTrays()

def Casework():
    casework = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Casework)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return casework
casework_ids = Casework()

def Ceilings():
    ceilings = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Ceilings)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return ceilings
ceiling_ids = Ceilings()

def Columns():
    columns = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Columns)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return columns
column_ids = Columns()

def CommunicationDevices():
    communication_devices = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_CommunicationDevices)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return communication_devices
communication_device_ids = CommunicationDevices()

def ConduitFitting():
    conduit_fittings = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_ConduitFitting)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return conduit_fittings
conduit_fitting_ids = ConduitFitting()

def Conduit():
    conduits = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Conduit)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return conduits
conduit_ids = Conduit()

def CurtainWallPanels():
    cw_panels = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_CurtainWallPanels)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return cw_panels
curtain_wall_panel_ids = CurtainWallPanels()

def CurtainWallMullions():
    cw_mullions = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_CurtainWallMullions)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return cw_mullions
curtain_wall_mullion_ids = CurtainWallMullions()

def DataDevices():
    data_devices = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_DataDevices)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return data_devices
data_device_ids = DataDevices()

def DuctAccessory():
    duct_accessories = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_DuctAccessory)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return duct_accessories
duct_accessory_ids = DuctAccessory()

def DuctFitting():
    duct_fittings = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_DuctFitting)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return duct_fittings
duct_fitting_ids = DuctFitting()

def DuctInsulations():
    duct_insuations = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_DuctInsulations)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return duct_insuations
duct_insulation_ids = DuctInsulations()

def DuctLinings():
    duct_linings = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_DuctLinings)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return duct_linings
duct_lining_ids = DuctLinings()

def DuctCurves():
    duct_curves = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_DuctCurves)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return duct_curves
duct_curve_ids = DuctCurves()

def ElectricalEquipment():
    electrical_equipment = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_ElectricalEquipment)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return electrical_equipment
electrical_equipment_ids = ElectricalEquipment()

def ElectricalFixtures():
    electrical_fixtures = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_ElectricalFixtures)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return electrical_fixtures
electrical_fixture_ids = ElectricalFixtures()

def FireAlarmDevices():
    fire_alarm_devices = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_FireAlarmDevices)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return fire_alarm_devices
fire_alarm_device_ids = FireAlarmDevices()

def FlexDuctCurves():
    flex_duct_curves = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_FlexDuctCurves)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return flex_duct_curves
flex_duct_curve_ids = FlexDuctCurves()

def FlexPipeCurves():
    flex_pipe_curves = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_FlexPipeCurves)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return flex_pipe_curves
flex_pipe_curve_ids = FlexPipeCurves()

def Floors():
    floors = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Floors)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return floors
floor_ids = Floors()

def Furniture():
    furniture = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Furniture)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return furniture
furniture_ids = Furniture()

def FurnitureSystems():
    furniture_systems = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_FurnitureSystems)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return furniture_systems
furniture_system_ids = FurnitureSystems()

def GenericModel():
    generic_models = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_GenericModel)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return generic_models
generic_model_ids = GenericModel()

def LightingDevices():
    lighting_devices = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_LightingDevices)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return lighting_devices
lighting_device_ids = LightingDevices()

def LightingFixtures():
    lighting_fixtures = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_LightingFixtures)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return lighting_fixtures
lighting_fixture_ids = LightingFixtures()

def MechanicalEquipment():
    mechanical_equipment = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_MechanicalEquipment)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return mechanical_equipment
mechanical_equipment_ids = MechanicalEquipment()

def NurseCallDevices():
    nurse_call_devices = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_NurseCallDevices)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return nurse_call_devices
nurse_call_device_ids = NurseCallDevices()

def PipeAccessory():
    pipe_accessories = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_PipeAccessory)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return pipe_accessories
pipe_accessory_ids = PipeAccessory()

def PipeFitting():
    pipe_fittings = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_PipeFitting)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return pipe_fittings
pipe_fitting_ids = PipeFitting()

def PipeInsulations():
    pipe_insuations = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_PipeInsulations)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return pipe_insuations
pipe_insulation_ids = PipeInsulations()

def PipeCurves():
    pipe_curves = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_PipeCurves)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return pipe_curves
pipe_curve_ids = PipeCurves()

def Planting():
    planting = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Planting)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return planting
planting_ids = Planting()

def PlumbingFixtures():
    plumbing_fixtures = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_PlumbingFixtures)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return plumbing_fixtures
plumbing_fixture_ids = PlumbingFixtures()

def StairsRailing():
    stairs_railing = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_StairsRailing)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return stairs_railing
stairs_railing_ids = StairsRailing()

def Ramps():
    ramps = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Ramps)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return ramps
ramp_ids = Ramps()

def Roofs():
    roofs = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Roofs)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return roofs
roof_ids = Roofs()

def Rooms():
    rooms = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Rooms)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return rooms
room_ids = Rooms()

def SecurityDevices():
    security_devices = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_SecurityDevices)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return security_devices
security_device_ids = SecurityDevices()

def Site():
    site = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Site)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return site
site_ids = Site()

def SpecialityEquipment():
    speciality_equipment = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_SpecialityEquipment)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return speciality_equipment
speciality_equipment_ids = SpecialityEquipment()

def Sprinklers():
    sprinklers = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Sprinklers)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return sprinklers
sprinkler_ids = Sprinklers()

def Stairs():
    stairs = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Stairs)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return stairs
stairs_ids = Stairs()

def AreaRein():
    area_rein = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_AreaRein)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return area_rein
area_rein_ids = AreaRein()

def StructuralColumns():
    structural_columns = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_StructuralColumns)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return structural_columns
structural_column_ids = StructuralColumns()

def StructConnections():
    struct_connections = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_StructConnections)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return struct_connections
struct_connection_ids = StructConnections()

def StructuralFoundation():
    structural_foundation = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_StructuralFoundation)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return structural_foundation
structural_foundation_ids = StructuralFoundation()

def StructuralFraming():
    structural_framing = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_StructuralFraming)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return structural_framing
structural_framing_ids = StructuralFraming()

def PathRein():
    path_rein = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_PathRein)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return path_rein
path_rein_ids = PathRein()

def Rebar():
    rebar = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_Rebar)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return rebar
rebar_ids = Rebar()

def StructuralStiffener():
    structural_stiffener = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_StructuralStiffener)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return structural_stiffener
structural_stiffener_ids = StructuralStiffener()

def StructuralTruss():
    structural_truss = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_StructuralTruss)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return structural_truss
structural_truss_ids = StructuralTruss()

def TelephoneDevices():
    telephone_devices = (
        DB.FilteredElementCollector(doc)
        .OfCategory(DB.BuiltInCategory.OST_TelephoneDevices)
        .WhereElementIsNotElementType()
        .ToElementIds()
    )
    return telephone_devices
telephone_device_ids = TelephoneDevices()