# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#text.py

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

def text_input(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, window_name, url):
    """
    Displays a modal input form for user input with a specified icon and labels.

    This function creates a graphical user interface (GUI) that prompts the user to enter text.
    The form includes an icon, a label for the input field, and OK/Cancel buttons. The OK button
    is enabled only when the user has entered text in the input field.

    Parameters:
    - icon_path (str): The file path to the icon to be displayed in the form.
    - search_image_path (str): The file path to the image displayed in the form.
    - ok_icon_path (str): The file path to the icon for the OK button.
    - cancel_icon_path (str): The file path to the icon for the Cancel button.
    - parameter_label (str): The label text for the input field.
    - window_name (str): The title of the input form window.
    - url (str): The URL to be opened when the "BIM Pars" label is clicked.

    Returns:
    - str or None: The text entered by the user if the OK button is clicked; 
                   None if the Cancel button is clicked or the operation is canceled.
    """
#Initializations
    class InputForm(Form):
        def __init__(self):
            self.Text = window_name
            self.Width = 500
            self.Height = 500
            self.BackColor = Color.White
            self.CenterToScreen()
            self.TopMost = True  
            self.Icon = Drawing.Icon(icon_path)

            self.pictureBoxSFIPV = PictureBox()
            self.pictureBoxSFIPV.Location = Point(self.Width // 2 - 25, 50)
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
            self.textbox1.Width = self.Width - 80
            self.textbox1.Multiline = True
            self.textbox1.ScrollBars = WinForms.ScrollBars.Vertical
            self.textbox1.WordWrap = True
            self.textbox1.Height = self.Height // 3
            self.textbox1.Location = Point(40, 150)
            self.textbox1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.textbox1.TextChanged += self.textbox_TextChanged
            self.Controls.Add(self.textbox1)

            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(self.Width // 2 - 45, self.Height - 100)
            self.ok_button.Width = 35
            self.ok_button.Height = 35
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

            self.cancel_button = Button()
            self.cancel_button.DialogResult = DialogResult.Cancel
            self.cancel_button.Location = Point(self.Width // 2 + 5, self.Height - 100)
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

def text_2input(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, parameter_label2, window_name, url):
    """
    Displays a modal input form for user input with two text fields and specified icons and labels.

    This function creates a graphical user interface (GUI) that prompts the user to enter text in two separate fields.
    The form includes an icon, labels for each input field, and OK/Cancel buttons. The OK button is enabled
    only when the user has entered text in the second input field.

    Parameters:
    - icon_path (str): The file path to the icon to be displayed in the form.
    - search_image_path (str): The file path to the image displayed in the form.
    - ok_icon_path (str): The file path to the icon for the OK button.
    - cancel_icon_path (str): The file path to the icon for the Cancel button.
    - parameter_label (str): The label text for the first input field.
    - parameter_label2 (str): The label text for the second input field.
    - window_name (str): The title of the input form window.
    - url (str): The URL to be opened when the "BIM Pars" label is clicked.

    Returns:
    - tuple: A tuple containing the text entered by the user in both input fields if the OK button is clicked; 
             (None, None) if the Cancel button is clicked or the operation is canceled.
    """
    #Initializations
    class InputForm(Form):
        def __init__(self):
            
            self.Text = window_name
            self.Width = 500
            self.Height = 600
            self.BackColor = Color.White
            self.CenterToScreen()
            self.TopMost = True  
            self.Icon = Drawing.Icon(icon_path)

            self.pictureBoxSFIPV = PictureBox()
            self.pictureBoxSFIPV.Location = Point(self.Width // 2 - 25, 50)
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
            self.textbox1.Width = 400
            self.textbox1.Multiline = True
            self.textbox1.ScrollBars = WinForms.ScrollBars.Vertical
            self.textbox1.WordWrap = True
            self.textbox1.Height = 150
            self.textbox1.Location = Point(40, 150)
            self.textbox1.TextChanged += self.textbox_TextChanged
            self.textbox1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox1)

            self.label2 = Label()
            self.label2.Text = parameter_label2
            self.label2.Location = Point(40, 325)
            self.label2.AutoSize = True
            self.label2.Font = Font(self.label2.Font, FontStyle.Bold)
            self.Controls.Add(self.label2)

            self.textbox2 = TextBox()
            self.textbox2.Width = 400
            self.textbox2.Multiline = True
            self.textbox2.WordWrap = True
            self.textbox2.Height = 30
            self.textbox2.Location = Point(40, 350)
            self.textbox2.TextChanged += self.textbox_TextChanged
            self.textbox2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox2)

            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(200, 450)
            self.ok_button.Width = 35
            self.ok_button.Height = 35
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

            self.cancel_button = Button()
            self.cancel_button.DialogResult = DialogResult.Cancel
            self.cancel_button.Location = Point(240, 450)
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
            if self.textbox2.Text:
                self.ok_button.Enabled = True
            else:
                self.ok_button.Enabled = False
    
    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()

        if dialog_result == DialogResult.OK:
            user_input = input_form.textbox1.Text
            user_input2 = input_form.textbox2.Text
        elif dialog_result == DialogResult.Cancel:
            user_input = None
            user_input2 = None
            sys.exit()
        
    except StopIteration:
        pass
    except Exception:
        pass
    except SystemExit:
        pass
    return user_input, user_input2

