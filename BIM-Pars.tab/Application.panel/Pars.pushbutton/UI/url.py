# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#url.py

def parsweb(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()
        if first_line:
            return first_line 
        else:
            return "None"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"