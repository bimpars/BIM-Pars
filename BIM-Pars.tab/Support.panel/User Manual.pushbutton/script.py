# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"

import os
import sys
import webbrowser
from pyrevit import forms, script
sys.path.append(os.path.dirname(__file__))
from structure.root import lan_path, usermanual_icon
from UI.strings import detect_language, str_1

# Initialization
lan = lan_path()
output = script.get_output()
output.set_height(720)
output.center()

# HTML 
html_file = os.path.join(os.path.dirname(__file__), detect_language(lan))
if not os.path.exists(html_file):
    sys.exit()

# Output window 
output.set_icon(usermanual_icon())
output.set_title(str_1(lan))
webbrowser.open(html_file)


