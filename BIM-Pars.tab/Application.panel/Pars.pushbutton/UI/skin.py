# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#skin.py

def skin_mode(file_path, cool_skin, bor_skin):
    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()
            if first_line == "cool":
                return cool_skin
            elif first_line == "boring":
                return bor_skin
            else:
                return bor_skin
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An error occurred: {e}"