# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#get_lan.py

import xml.etree.ElementTree as ET

def lan(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        language = root.find('Language')
        if language is not None:
            return language.text
        else:
            return "Language tag not found."
    except Exception as e:
        return "Error reading XML file: " + str(e)

file_path = "app_setup.xml" 
language = lan(file_path)
