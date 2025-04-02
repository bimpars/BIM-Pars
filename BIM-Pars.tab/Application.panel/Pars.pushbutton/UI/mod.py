# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#mod.py

def check_mode(file_path):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()
            if first_line == "cool":
                return "Cool Mode"
            elif first_line == "boring":
                return "Boring Mode"
            else:
                return "Unknown Mode"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"