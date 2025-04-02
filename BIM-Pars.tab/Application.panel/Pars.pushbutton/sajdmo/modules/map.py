# -*- coding: utf-8 -*-
# __author__ = "Mohammad Sajjad Mortazavi"
#map.py

import clr
clr.AddReference("RevitAPI")
import Autodesk.Revit.DB as DB
import os
import sys
def category():
    category_map = {
        'Walls': DB.BuiltInCategory.OST_Walls,
        'OST_Walls': DB.BuiltInCategory.OST_Walls,
        
        'Doors': DB.BuiltInCategory.OST_Doors,
        'OST_Doors': DB.BuiltInCategory.OST_Doors,
        
        'Windows': DB.BuiltInCategory.OST_Windows,
        'OST_Windows': DB.BuiltInCategory.OST_Windows,
        
        'GenericModel': DB.BuiltInCategory.OST_GenericModel,
        'OST_GenericModel': DB.BuiltInCategory.OST_GenericModel,
        
        'Floors': DB.BuiltInCategory.OST_Floors,
        'OST_Floors': DB.BuiltInCategory.OST_Floors,
        
        'Roofs': DB.BuiltInCategory.OST_Roofs,
        'OST_Roofs': DB.BuiltInCategory.OST_Roofs,
        
        'Ceilings': DB.BuiltInCategory.OST_Ceilings,
        'OST_Ceilings': DB.BuiltInCategory.OST_Ceilings,
        
        'Stairs': DB.BuiltInCategory.OST_Stairs,
        'OST_Stairs': DB.BuiltInCategory.OST_Stairs,
        
        'Railings': DB.BuiltInCategory.OST_StairsRailing,
        'OST_StairsRailing': DB.BuiltInCategory.OST_StairsRailing,
        
        'StructuralColumns': DB.BuiltInCategory.OST_StructuralColumns,
        'OST_StructuralColumns': DB.BuiltInCategory.OST_StructuralColumns,
        
        'StructuralFraming': DB.BuiltInCategory.OST_StructuralFraming,
        'OST_StructuralFraming': DB.BuiltInCategory.OST_StructuralFraming,
        
        'StructuralFoundation': DB.BuiltInCategory.OST_StructuralFoundation,
        'OST_StructuralFoundation': DB.BuiltInCategory.OST_StructuralFoundation,
        
        'CurtainWallPanels': DB.BuiltInCategory.OST_CurtainWallPanels,
        'OST_CurtainWallPanels': DB.BuiltInCategory.OST_CurtainWallPanels,
        
        'CurtainWallMullions': DB.BuiltInCategory.OST_CurtainWallMullions,
        'OST_CurtainWallMullions': DB.BuiltInCategory.OST_CurtainWallMullions,
        
        'Casework': DB.BuiltInCategory.OST_Casework,
        'OST_Casework': DB.BuiltInCategory.OST_Casework,
        
        'Columns': DB.BuiltInCategory.OST_Columns,
        'OST_Columns': DB.BuiltInCategory.OST_Columns,
        
        'Furniture': DB.BuiltInCategory.OST_Furniture,
        'OST_Furniture': DB.BuiltInCategory.OST_Furniture,
        
        'FurnitureSystems': DB.BuiltInCategory.OST_FurnitureSystems,
        'OST_FurnitureSystems': DB.BuiltInCategory.OST_FurnitureSystems,
        
        'LightingFixtures': DB.BuiltInCategory.OST_LightingFixtures,
        'OST_LightingFixtures': DB.BuiltInCategory.OST_LightingFixtures,
        
        'LightingDevices': DB.BuiltInCategory.OST_LightingDevices,
        'OST_LightingDevices': DB.BuiltInCategory.OST_LightingDevices,
        
        'ElectricalEquipment': DB.BuiltInCategory.OST_ElectricalEquipment,
        'OST_ElectricalEquipment': DB.BuiltInCategory.OST_ElectricalEquipment,
        
        'ElectricalFixtures': DB.BuiltInCategory.OST_ElectricalFixtures,
        'OST_ElectricalFixtures': DB.BuiltInCategory.OST_ElectricalFixtures,
        
        'MechanicalEquipment': DB.BuiltInCategory.OST_MechanicalEquipment,
        'OST_MechanicalEquipment': DB.BuiltInCategory.OST_MechanicalEquipment,
        
        'PlumbingFixtures': DB.BuiltInCategory.OST_PlumbingFixtures,
        'OST_PlumbingFixtures': DB.BuiltInCategory.OST_PlumbingFixtures,
        
        'Pipes': DB.BuiltInCategory.OST_PipeCurves,
        'OST_PipeCurves': DB.BuiltInCategory.OST_PipeCurves,
        
        'PipeFittings': DB.BuiltInCategory.OST_PipeFitting,
        'OST_PipeFitting': DB.BuiltInCategory.OST_PipeFitting,
        
        'PipeAccessories': DB.BuiltInCategory.OST_PipeAccessory,
        'OST_PipeAccessory': DB.BuiltInCategory.OST_PipeAccessory,
        
        'Ducts': DB.BuiltInCategory.OST_DuctCurves,
        'OST_DuctCurves': DB.BuiltInCategory.OST_DuctCurves,
        
        'DuctFittings': DB.BuiltInCategory.OST_DuctFitting,
        'OST_DuctFitting': DB.BuiltInCategory.OST_DuctFitting,
        
        'DuctAccessories': DB.BuiltInCategory.OST_DuctAccessory,
        'OST_DuctAccessory': DB.BuiltInCategory.OST_DuctAccessory,
        
        #'HVACZones': DB.BuiltInCategory.OST_HVACZones,
        #'OST_HVACZones': DB.BuiltInCategory.OST_HVACZones,
        
        'Sprinklers': DB.BuiltInCategory.OST_Sprinklers,
        'OST_Sprinklers': DB.BuiltInCategory.OST_Sprinklers,
        
        'Views': DB.BuiltInCategory.OST_Views,
        'OST_Views': DB.BuiltInCategory.OST_Views,
        
        'Sheets': DB.BuiltInCategory.OST_Sheets,
        'OST_Sheets': DB.BuiltInCategory.OST_Sheets,
        
        'TitleBlocks': DB.BuiltInCategory.OST_TitleBlocks,
        'OST_TitleBlocks': DB.BuiltInCategory.OST_TitleBlocks,
        
        #'Annotations': DB.BuiltInCategory.OST_Annotations,
        #'OST_Annotations': DB.BuiltInCategory.OST_Annotations,
        
        'Dimensions': DB.BuiltInCategory.OST_Dimensions,
        'OST_Dimensions': DB.BuiltInCategory.OST_Dimensions,
        
        'Grids': DB.BuiltInCategory.OST_Grids,
        'OST_Grids': DB.BuiltInCategory.OST_Grids,
        
        'Levels': DB.BuiltInCategory.OST_Levels,
        'OST_Levels': DB.BuiltInCategory.OST_Levels,
        
        'Topography': DB.BuiltInCategory.OST_Topography,
        'OST_Topography': DB.BuiltInCategory.OST_Topography,
        
        'Parking': DB.BuiltInCategory.OST_Parking,
        'OST_Parking': DB.BuiltInCategory.OST_Parking,
        
        #'StairsComponents': DB.BuiltInCategory.OST_StairsComponents,
        #'OST_StairsComponents': DB.BuiltInCategory.OST_StairsComponents,
        
        #'RailingsComponents': DB.BuiltInCategory.OST_RailingsComponents,
        #'OST_RailingsComponents': DB.BuiltInCategory.OST_RailingsComponents,

        'CommunicationDevices': DB.BuiltInCategory.OST_CommunicationDevices,
        'OST_CommunicationDevices': DB.BuiltInCategory.OST_CommunicationDevices,

        'FireAlarmDevices': DB.BuiltInCategory.OST_FireAlarmDevices,
        'OST_FireAlarmDevices': DB.BuiltInCategory.OST_FireAlarmDevices,
        
        'DataDevices': DB.BuiltInCategory.OST_DataDevices,
        'OST_DataDevices': DB.BuiltInCategory.OST_DataDevices,

        'Conduit': DB.BuiltInCategory.OST_Conduit,
        'OST_Conduit': DB.BuiltInCategory.OST_Conduit,
        
        'ConduitFittings': DB.BuiltInCategory.OST_ConduitFitting,
        'OST_ConduitFitting': DB.BuiltInCategory.OST_ConduitFitting,
        
        'CableTray': DB.BuiltInCategory.OST_CableTray,
        'OST_CableTray': DB.BuiltInCategory.OST_CableTray,
        
        'CableTrayFittings': DB.BuiltInCategory.OST_CableTrayFitting,
        'OST_CableTrayFitting': DB.BuiltInCategory.OST_CableTrayFitting,

        'Doors': DB.BuiltInCategory.OST_Doors,
        'OST_Doors': DB.BuiltInCategory.OST_Doors,

        'Windows': DB.BuiltInCategory.OST_Windows,
        'OST_Windows': DB.BuiltInCategory.OST_Windows,

        'Walls': DB.BuiltInCategory.OST_Walls,
        'OST_Walls': DB.BuiltInCategory.OST_Walls,

        'AirTerminals': DB.BuiltInCategory.OST_DuctTerminal,
        'OST_AirTerminals': DB.BuiltInCategory.OST_DuctTerminal,

        'CableTrayFittings': DB.BuiltInCategory.OST_CableTrayFitting,
        'OST_CableTrayFittings': DB.BuiltInCategory.OST_CableTrayFitting,

        'CableTrays': DB.BuiltInCategory.OST_CableTray,
        'OST_CableTrays': DB.BuiltInCategory.OST_CableTray,

        'Casework': DB.BuiltInCategory.OST_Casework,
        'OST_Casework': DB.BuiltInCategory.OST_Casework,

        'Ceilings': DB.BuiltInCategory.OST_Ceilings,
        'OST_Ceilings': DB.BuiltInCategory.OST_Ceilings,

        'Columns': DB.BuiltInCategory.OST_Columns,
        'OST_Columns': DB.BuiltInCategory.OST_Columns,

        'CommunicationDevices': DB.BuiltInCategory.OST_CommunicationDevices,
        'OST_CommunicationDevices': DB.BuiltInCategory.OST_CommunicationDevices,

        'ConduitFitting': DB.BuiltInCategory.OST_ConduitFitting,
        'OST_ConduitFitting': DB.BuiltInCategory.OST_ConduitFitting,

        'Conduit': DB.BuiltInCategory.OST_Conduit,
        'OST_Conduit': DB.BuiltInCategory.OST_Conduit,

        'CurtainWallPanels': DB.BuiltInCategory.OST_CurtainWallPanels,
        'OST_CurtainWallPanels': DB.BuiltInCategory.OST_CurtainWallPanels,

        'CurtainWallMullions': DB.BuiltInCategory.OST_CurtainWallMullions,
        'OST_CurtainWallMullions': DB.BuiltInCategory.OST_CurtainWallMullions,

        'DataDevices': DB.BuiltInCategory.OST_DataDevices,
        'OST_DataDevices': DB.BuiltInCategory.OST_DataDevices,

        'DuctAccessory': DB.BuiltInCategory.OST_DuctAccessory,
        'OST_DuctAccessory': DB.BuiltInCategory.OST_DuctAccessory,

        'DuctFitting': DB.BuiltInCategory.OST_DuctFitting,
        'OST_DuctFitting': DB.BuiltInCategory.OST_DuctFitting,

        'DuctInsulations': DB.BuiltInCategory.OST_DuctInsulations,
        'OST_DuctInsulations': DB.BuiltInCategory.OST_DuctInsulations,

        'DuctLinings': DB.BuiltInCategory.OST_DuctLinings,
        'OST_DuctLinings': DB.BuiltInCategory.OST_DuctLinings,

        'DuctCurves': DB.BuiltInCategory.OST_DuctCurves,
        'OST_DuctCurves': DB.BuiltInCategory.OST_DuctCurves,

        'ElectricalEquipment': DB.BuiltInCategory.OST_ElectricalEquipment,
        'OST_ElectricalEquipment': DB.BuiltInCategory.OST_ElectricalEquipment,

        'ElectricalFixtures': DB.BuiltInCategory.OST_ElectricalFixtures,
        'OST_ElectricalFixtures': DB.BuiltInCategory.OST_ElectricalFixtures,

        'FireAlarmDevices': DB.BuiltInCategory.OST_FireAlarmDevices,
        'OST_FireAlarmDevices': DB.BuiltInCategory.OST_FireAlarmDevices,

        'FlexDuctCurves': DB.BuiltInCategory.OST_FlexDuctCurves,
        'OST_FlexDuctCurves': DB.BuiltInCategory.OST_FlexDuctCurves,

        'FlexPipeCurves': DB.BuiltInCategory.OST_FlexPipeCurves,
        'OST_FlexPipeCurves': DB.BuiltInCategory.OST_FlexPipeCurves,

        'Floors': DB.BuiltInCategory.OST_Floors,
        'OST_Floors': DB.BuiltInCategory.OST_Floors,

        'Furniture': DB.BuiltInCategory.OST_Furniture,
        'OST_Furniture': DB.BuiltInCategory.OST_Furniture,

        'FurnitureSystems': DB.BuiltInCategory.OST_FurnitureSystems,
        'OST_FurnitureSystems': DB.BuiltInCategory.OST_FurnitureSystems,

        'GenericModel': DB.BuiltInCategory.OST_GenericModel,
        'OST_GenericModel': DB.BuiltInCategory.OST_GenericModel,

        'LightingDevices': DB.BuiltInCategory.OST_LightingDevices,
        'OST_LightingDevices': DB.BuiltInCategory.OST_LightingDevices,

        'LightingFixtures': DB.BuiltInCategory.OST_LightingFixtures,
        'OST_LightingFixtures': DB.BuiltInCategory.OST_LightingFixtures,

        'MechanicalEquipment': DB.BuiltInCategory.OST_MechanicalEquipment,
        'OST_MechanicalEquipment': DB.BuiltInCategory.OST_MechanicalEquipment,

        'NurseCallDevices': DB.BuiltInCategory.OST_NurseCallDevices,
        'OST_NurseCallDevices': DB.BuiltInCategory.OST_NurseCallDevices,

        'PipeAccessory': DB.BuiltInCategory.OST_PipeAccessory,
        'OST_PipeAccessory': DB.BuiltInCategory.OST_PipeAccessory,

        'PipeFitting': DB.BuiltInCategory.OST_PipeFitting,
        'OST_PipeFitting': DB.BuiltInCategory.OST_PipeFitting,

        'PipeInsulations': DB.BuiltInCategory.OST_PipeInsulations,
        'OST_PipeInsulations': DB.BuiltInCategory.OST_PipeInsulations,

        'PipeCurves': DB.BuiltInCategory.OST_PipeCurves,
        'OST_PipeCurves': DB.BuiltInCategory.OST_PipeCurves,

        'Planting': DB.BuiltInCategory.OST_Planting,
        'OST_Planting': DB.BuiltInCategory.OST_Planting,

        'PlumbingFixtures': DB.BuiltInCategory.OST_PlumbingFixtures,
        'OST_PlumbingFixtures': DB.BuiltInCategory.OST_PlumbingFixtures,

        'StairsRailing': DB.BuiltInCategory.OST_StairsRailing,
        'OST_StairsRailing': DB.BuiltInCategory.OST_StairsRailing,

        'Ramps': DB.BuiltInCategory.OST_Ramps,
        'OST_Ramps': DB.BuiltInCategory.OST_Ramps,

        'Roofs': DB.BuiltInCategory.OST_Roofs,
        'OST_Roofs': DB.BuiltInCategory.OST_Roofs,

        'Rooms': DB.BuiltInCategory.OST_Rooms,
        'OST_Rooms': DB.BuiltInCategory.OST_Rooms,

        'SecurityDevices': DB.BuiltInCategory.OST_SecurityDevices,
        'OST_SecurityDevices': DB.BuiltInCategory.OST_SecurityDevices,

        'Site': DB.BuiltInCategory.OST_Site,
        'OST_Site': DB.BuiltInCategory.OST_Site,

        'SpecialityEquipment': DB.BuiltInCategory.OST_SpecialityEquipment,
        'OST_SpecialityEquipment': DB.BuiltInCategory.OST_SpecialityEquipment,

        'Sprinklers': DB.BuiltInCategory.OST_Sprinklers,
        'OST_Sprinklers': DB.BuiltInCategory.OST_Sprinklers,

        'Stairs': DB.BuiltInCategory.OST_Stairs,
        'OST_Stairs': DB.BuiltInCategory.OST_Stairs,

        'AreaRein': DB.BuiltInCategory.OST_AreaRein,
        'OST_AreaRein': DB.BuiltInCategory.OST_AreaRein,

        'StructuralColumns': DB.BuiltInCategory.OST_StructuralColumns,
        'OST_StructuralColumns': DB.BuiltInCategory.OST_StructuralColumns,

        'StructConnections': DB.BuiltInCategory.OST_StructConnections,
        'OST_StructConnections': DB.BuiltInCategory.OST_StructConnections,

        'StructuralFoundation': DB.BuiltInCategory.OST_StructuralFoundation,
        'OST_StructuralFoundation': DB.BuiltInCategory.OST_StructuralFoundation,

        'StructuralFraming': DB.BuiltInCategory.OST_StructuralFraming,
        'OST_StructuralFraming': DB.BuiltInCategory.OST_StructuralFraming,

        'PathRein': DB.BuiltInCategory.OST_PathRein,
        'OST_PathRein': DB.BuiltInCategory.OST_PathRein,

        'Rebar': DB.BuiltInCategory.OST_Rebar,
        'OST_Rebar': DB.BuiltInCategory.OST_Rebar,

        'StructuralStiffener': DB.BuiltInCategory.OST_StructuralStiffener,
        'OST_StructuralStiffener': DB.BuiltInCategory.OST_StructuralStiffener,

        'StructuralTruss': DB.BuiltInCategory.OST_StructuralTruss,
        'OST_StructuralTruss': DB.BuiltInCategory.OST_StructuralTruss,

        'TelephoneDevices': DB.BuiltInCategory.OST_TelephoneDevices,
        'OST_TelephoneDevices': DB.BuiltInCategory.OST_TelephoneDevices,

    }
    
    return category_map