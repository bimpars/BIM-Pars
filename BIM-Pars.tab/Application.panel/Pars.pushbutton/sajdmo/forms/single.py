# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#single.py

#Imports
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
import os
import sys
import webbrowser
import System.Windows.Forms as WinForms
import System.Drawing as Drawing
from System.Drawing import Point, Image, Size, Color, Font, FontStyle, Icon, GraphicsUnit
from System.Windows.Forms import Form, Label, TextBox, Button, DialogResult, PictureBox, Cursors
import Autodesk.Revit.DB as DB

def single_input(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, window_name, url):
    """
    Displays a modal input form for user input with specified icons and labels.

    Parameters:
    icon_path (str): The file path to the icon displayed in the form's title bar.
    search_image_path (str): The file path to the image displayed in the form.
    ok_icon_path (str): The file path to the icon for the OK button.
    cancel_icon_path (str): The file path to the icon for the Cancel button.
    parameter_label (str): The label text that prompts the user for input.
    window_name (str): The title of the input form window.
    url (str): The URL to open when the "BIM Pars" label is clicked.

    Returns:
    str or None: The user input as a string if the OK button is clicked, 
                  or None if the operation is canceled.
    """
    #Initializations
    class InputForm(Form):
        def __init__(self):
            
            self.Text = window_name
            self.Width = 300
            self.Height = 325
            self.BackColor = Color.White
            self.CenterToScreen()
            self.Icon = Drawing.Icon(icon_path)

            self.pictureBoxSFIPV = PictureBox()
            self.pictureBoxSFIPV.Location = Point(self.Width // 2 - 25, 30)
            self.pictureBoxSFIPV.Size = Size(50, 50)
            imageSFIPV = Image.FromFile(search_image_path)
            self.pictureBoxSFIPV.Image = imageSFIPV
            self.pictureBoxSFIPV.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.pictureBoxSFIPV)

            self.label1 = Label()
            self.label1.Text = parameter_label
            self.label1.Location = Point(40, 125)
            self.label1.AutoSize = True
            self.label1.Font = Font(self.label1.Font, FontStyle.Bold)
            self.label1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label1)

            self.textbox1 = TextBox()
            self.textbox1.Width = 200
            self.textbox1.Location = Point(40, 150)
            self.textbox1.TextChanged += self.textbox_TextChanged
            self.textbox1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox1)

            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(100, 200)
            self.ok_button.Width = 35
            self.ok_button.Height = 35
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

            self.cancel_button = Button()
            self.cancel_button.DialogResult = DialogResult.Cancel
            self.cancel_button.Location = Point(140, 200)
            self.cancel_button.Width = 35
            self.cancel_button.Height = 35
            self.cancel_button.Image = Icon(cancel_icon_path).ToBitmap()
            self.cancel_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.cancel_button)

            self.created_by_label = Label()
            self.created_by_label.AutoSize = True
            self.created_by_label.Text = "BIM Pars"
            self.created_by_label.Location = Point(self.Width - 80, self.Height - 65)
            self.created_by_label.ForeColor = Color.Blue
            self.created_by_label.Font = Font(self.created_by_label.Font, FontStyle.Bold) 
            self.created_by_label.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Right)
            self.created_by_label.Font = Font(self.created_by_label.Font.FontFamily, self.created_by_label.Font.Size, FontStyle.Underline, GraphicsUnit.Point)  
            self.created_by_label.Cursor = Cursors.Hand  
            self.created_by_label.Click += self.Label_Click
            self.Controls.Add(self.created_by_label)

        def Label_Click(self, sender, event):            
            webbrowser.open(url)

        def textbox_TextChanged(self, sender, e):
            if self.textbox1.Text:
                self.ok_button.Enabled = True
            else:
                self.ok_button.Enabled = False
    
    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()

        if dialog_result == DialogResult.OK:
            user_input = input_form.textbox1.Text

        elif dialog_result == DialogResult.Cancel:
            user_input = None

            sys.exit()
        
    except StopIteration:
        pass
    except Exception:
        pass
    except SystemExit:
        pass
    return user_input


