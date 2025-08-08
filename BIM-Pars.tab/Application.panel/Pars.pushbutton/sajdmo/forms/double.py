# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#double.py

#Imports
import clr
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


def double_input(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, value_label, window_name, url):
    """
    Displays a dialog for user input with two text fields.

    Parameters:
    icon_path (str): The file path to the icon to be displayed in the window.
    search_image_path (str): The file path to the image to be displayed in the PictureBox.
    ok_icon_path (str): The file path to the icon for the OK button.
    cancel_icon_path (str): The file path to the icon for the Cancel button.
    parameter_label (str): The label for the first input field.
    value_label (str): The label for the second input field.
    window_name (str): The title of the dialog window.
    url (str): The URL to be opened when the created_by_label is clicked.

    Returns:
    tuple: A tuple containing the user inputs from the two text boxes. 
           Returns (None, None) if the dialog is canceled.
    """
    #Initialization
    class InputForm(Form):
        def __init__(self):         
            self.Text = window_name
            self.Width = 300
            self.Height = 450
            self.BackColor = Color.White
            self.CenterToScreen()
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
            self.textbox1.Width = 200
            self.textbox1.Location = Point(40, 150)
            self.textbox1.TextChanged += self.textbox_TextChanged
            self.textbox1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox1)

            self.label2 = Label()
            self.label2.Text = value_label
            self.label2.Location = Point(40, 200)
            self.label2.AutoSize = True
            self.label2.Font = Font(self.label2.Font, FontStyle.Bold)
            self.label2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label2)

            self.textbox2 = TextBox()
            self.textbox2.Width = 200
            self.textbox2.Location = Point(40, 225)
            self.textbox2.TextChanged += self.textbox_TextChanged
            self.textbox2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox2)

            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(100, 300)
            self.ok_button.Width = 35
            self.ok_button.Height = 35
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

            self.cancel_button = Button()
            self.cancel_button.DialogResult = DialogResult.Cancel
            self.cancel_button.Location = Point(140, 300)
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
            if self.textbox1.Text and self.textbox2.Text:
                self.ok_button.Enabled = True
            else:
                self.ok_button.Enabled = False   
    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()

        if dialog_result == DialogResult.OK:
            user_input1 = input_form.textbox1.Text
            user_input2 = input_form.textbox2.Text
        elif dialog_result == DialogResult.Cancel:
            user_input1 = None
            user_input2 = None
            sys.exit()
        
    except StopIteration:
        pass
    except Exception:
        pass
    except SystemExit:
        pass
    return user_input1, user_input2

def double_input_plusnote(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, value_label, window_name, note, url):
    """
    Displays a dialog for user input with two text fields and an additional note.

    Parameters:
    icon_path (str): The file path to the icon to be displayed in the window.
    search_image_path (str): The file path to the image to be displayed in the PictureBox.
    ok_icon_path (str): The file path to the icon for the OK button.
    cancel_icon_path (str): The file path to the icon for the Cancel button.
    parameter_label (str): The label for the first input field.
    value_label (str): The label for the second input field.
    window_name (str): The title of the dialog window.
    note (str): A note to be displayed in the dialog.
    url (str): The URL to be opened when the created_by_label is clicked.

    Returns:
    tuple: A tuple containing the user inputs from the two text boxes. 
           Returns (None, None) if the dialog is canceled.
    """
    #Initialization
    class InputForm(Form):
        def __init__(self):
            self.Text = window_name
            self.Width = 300
            self.Height = 450
            self.BackColor = Color.White
            self.CenterToScreen()
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
            self.textbox1.Width = 200
            self.textbox1.Location = Point(40, 150)
            self.textbox1.TextChanged += self.textbox_TextChanged
            self.textbox1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox1)

            self.label2 = Label()
            self.label2.Text = value_label
            self.label2.Location = Point(40, 200)
            self.label2.AutoSize = True
            self.label2.Font = Font(self.label2.Font, FontStyle.Bold)
            self.label2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label2)

            self.textbox2 = TextBox()
            self.textbox2.Width = 200
            self.textbox2.Location = Point(40, 225)
            self.textbox2.TextChanged += self.textbox_TextChanged
            self.textbox2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox2)

            self.label3 = Label()
            self.label3.Text = note
            self.label3.Location = Point(40, 265)
            self.label3.AutoSize = True
            self.label3.MaximumSize =   Size(200, 150)
            self.label3.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label3)

            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(100, 350)
            self.ok_button.Width = 35
            self.ok_button.Height = 35
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

            self.cancel_button = Button()
            self.cancel_button.DialogResult = DialogResult.Cancel
            self.cancel_button.Location = Point(140, 350)
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
            if self.textbox1.Text and self.textbox2.Text:
                self.ok_button.Enabled = True
            else:
                self.ok_button.Enabled = False    
    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()

        if dialog_result == DialogResult.OK:
            user_input1 = input_form.textbox1.Text
            user_input2 = input_form.textbox2.Text
        elif dialog_result == DialogResult.Cancel:
            user_input1 = None
            user_input2 = None
            sys.exit()
        
    except StopIteration:
        pass
    except Exception:
        pass
    except SystemExit:
        pass
    return user_input1, user_input2

def double_input_plusnote_dynamiclabel(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, value_label, window_name, note, dyn, url):
    """
    Displays a dialog for user input with two text fields, an additional note, and a dynamic label.

    Parameters:
    icon_path (str): The file path to the icon to be displayed in the window.
    search_image_path (str): The file path to the image to be displayed in the PictureBox.
    ok_icon_path (str): The file path to the icon for the OK button.
    cancel_icon_path (str): The file path to the icon for the Cancel button.
    parameter_label (str): The label for the first input field.
    value_label (str): The label for the second input field.
    window_name (str): The title of the dialog window.
    note (str): A note to be displayed in the dialog.
    dyn (str): A dynamic label to be displayed based on user input.
    url (str): The URL to be opened when the created_by_label is clicked.

    Returns:
    tuple: A tuple containing the user inputs from the two text boxes and the dynamic parameter type. 
           Returns (None, None, None) if the dialog is canceled.
    """
    #Initialization
    class InputForm(Form):
        def __init__(self):
            
            self.Text = window_name
            self.Width = 300
            self.Height = 600
            self.BackColor = Color.White
            self.CenterToScreen()
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
            self.textbox1.Width = 200
            self.textbox1.Location = Point(40, 150)
            self.textbox1.TextChanged += self.textbox_TextChanged
            self.textbox1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox1)

            self.label2 = Label()
            self.label2.Text = value_label
            self.label2.Location = Point(40, 200)
            self.label2.AutoSize = True
            self.label2.Font = Font(self.label2.Font, FontStyle.Bold)
            self.label2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label2)

            self.textbox2 = TextBox()
            self.textbox2.Width = 200
            self.textbox2.Location = Point(40, 225)
            self.textbox2.TextChanged += self.textbox_TextChanged
            self.textbox2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox2)
            
            self.label3 = Label()
            self.label3.Text = note
            self.label3.Location = Point(40, 285)
            self.label3.AutoSize = True
            self.label3.MaximumSize =   Size(200, 300)
            self.label3.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label3)

            self.label4 = Label()
            self.label4.Text += ""
            self.label4.Location = Point(150, 265)
            self.label4.AutoSize = True
            self.label4.ForeColor = Color.Red
            self.label4.MaximumSize =   Size(400, 150)
            self.label4.Font = Font(self.label4.Font, FontStyle.Bold)
            self.label4.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label4)

            self.label5 = Label()
            self.label5.Text = dyn
            self.label5.Location = Point(40, 265)
            self.label5.AutoSize = True
            self.label5.ForeColor = Color.Black
            self.label5.MaximumSize =   Size(400, 150)
            self.label5.Font = Font(self.label5.Font, FontStyle.Bold)
            self.label5.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label5)

            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(100, 475)
            self.ok_button.Width = 35
            self.ok_button.Height = 35
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

            self.cancel_button = Button()
            self.cancel_button.DialogResult = DialogResult.Cancel
            self.cancel_button.Location = Point(140, 475)
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
            if self.textbox1.Text and self.textbox2.Text:
                self.ok_button.Enabled = True

                #LOGIC OF DYNAMIC LABEL
                self.textbox1.Enabled = False
                import clr
                import Autodesk.Revit.DB as DB
                from pyrevit import forms
                clr.AddReference('RevitAPI')
                clr.AddReference('RevitAPIUI')
                doc = __revit__.ActiveUIDocument.Document
                selection = __revit__.ActiveUIDocument.Selection.GetElementIds()
                parameter_name = self.textbox1.Text               
                elements = [doc.GetElement(element_id) for element_id in selection]

                invalid_elements = []
                for element in elements:
                    param = element.LookupParameter(parameter_name)
                    if param is None:
                        invalid_elements.append(element)
                    elif param.StorageType != DB.StorageType.String:
                        invalid_elements.append(element)

                if invalid_elements:
                    element_names = ', '.join([elem.Name for elem in invalid_elements])
                    message = "The parameter '{0}' does not exist or is not of type 'Text' for the following elements:\n{1}".format(parameter_name, element_names)
                    forms.alert(message)
                    self.Close()
                else:
                    self.param_type = elements[0].LookupParameter(parameter_name).StorageType
                                     
                    self.label4.Text = str(self.param_type)

            else:
                self.ok_button.Enabled = False
                self.textbox1.Enabled = True
                self.label4.Text = ""  
    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()

        if dialog_result == DialogResult.OK:
            user_input1 = input_form.textbox1.Text
            user_input2 = input_form.textbox2.Text
            user_input3 = input_form.param_type
        elif dialog_result == DialogResult.Cancel:
            user_input1 = None
            user_input2 = None
            user_input3 = None
            sys.exit()
        
    except StopIteration:
        pass
    except Exception:
        pass
    except SystemExit:
        pass
    return user_input1, user_input2, user_input3

def double_input_plusnote_dynamiclabel2(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, value_label, window_name, note, dyn, url):
    """
    Displays a dialog for user input with two text fields, an additional note, and a dynamic label.

    Parameters:
    icon_path (str): The file path to the icon to be displayed in the window.
    search_image_path (str): The file path to the image to be displayed in the PictureBox.
    ok_icon_path (str): The file path to the icon for the OK button.
    cancel_icon_path (str): The file path to the icon for the Cancel button.
    parameter_label (str): The label for the first input field.
    value_label (str): The label for the second input field.
    window_name (str): The title of the dialog window.
    note (str): A note to be displayed in the dialog.
    dyn (str): A dynamic label to be displayed based on user input.
    url (str): The URL to be opened when the created_by_label is clicked.

    Returns:
    tuple: A tuple containing the user inputs from the two text boxes and the dynamic parameter type. 
           Returns (None, None, None) if the dialog is canceled.
    """
    #Initialization
    class InputForm(Form):
        def __init__(self):
            self.Text = window_name
            self.Width = 300
            self.Height = 600
            self.BackColor = Color.White
            self.CenterToScreen()
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
            self.textbox1.Width = 200
            self.textbox1.Location = Point(40, 150)
            self.textbox1.TextChanged += self.textbox_TextChanged
            self.textbox1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox1)

            self.label2 = Label()
            self.label2.Text = value_label
            self.label2.Location = Point(40, 200)
            self.label2.AutoSize = True
            self.label2.Font = Font(self.label2.Font, FontStyle.Bold)
            self.label2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label2)

            self.textbox2 = TextBox()
            self.textbox2.Width = 200
            self.textbox2.Location = Point(40, 225)
            self.textbox2.TextChanged += self.textbox_TextChanged
            self.textbox2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox2)
            
            self.label3 = Label()
            self.label3.Text = note
            self.label3.Location = Point(40, 285)
            self.label3.AutoSize = True
            self.label3.MaximumSize =   Size(200, 300)
            self.label3.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label3)

            self.label4 = Label()
            self.label4.Text += ""
            self.label4.Location = Point(150, 265)
            self.label4.AutoSize = True
            self.label4.ForeColor = Color.Red
            self.label4.MaximumSize =   Size(400, 150)
            self.label4.Font = Font(self.label4.Font, FontStyle.Bold)
            self.label4.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label4)

            self.label5 = Label()
            self.label5.Text = dyn
            self.label5.Location = Point(40, 265)
            self.label5.AutoSize = True
            self.label5.ForeColor = Color.Black
            self.label5.MaximumSize =   Size(400, 150)
            self.label5.Font = Font(self.label5.Font, FontStyle.Bold)
            self.label5.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label5)

            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(100, 450)
            self.ok_button.Width = 35
            self.ok_button.Height = 35
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

            self.cancel_button = Button()
            self.cancel_button.DialogResult = DialogResult.Cancel
            self.cancel_button.Location = Point(140, 450)
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
            if self.textbox1.Text and self.textbox2.Text:
                self.ok_button.Enabled = True

                #LOGIC OF DYNAMIC LABEL
                self.textbox1.Enabled = False
                import clr
                import Autodesk.Revit.DB as DB
                from pyrevit import forms
                clr.AddReference('RevitAPI')
                clr.AddReference('RevitAPIUI')
                doc = __revit__.ActiveUIDocument.Document
                selection = __revit__.ActiveUIDocument.Selection.GetElementIds()
                parameter_name = self.textbox1.Text               
                elements = [doc.GetElement(element_id) for element_id in selection]

                invalid_elements = []
                for element in elements:
                    param = element.LookupParameter(parameter_name)
                    if param is None:
                        invalid_elements.append(element)
                    elif param.StorageType != DB.StorageType.Double:
                        invalid_elements.append(element)

                if invalid_elements:
                    element_names = ', '.join([elem.Name for elem in invalid_elements])
                    message = "The parameter '{0}' does not exist or is not of type 'Number' for the following elements:\n{1}".format(parameter_name, element_names)
                    forms.alert(message)
                    self.Close()
                else:
                    self.param_type = elements[0].LookupParameter(parameter_name).StorageType
                                     
                    self.label4.Text = str(self.param_type)

            else:
                self.ok_button.Enabled = False
                self.textbox1.Enabled = True
                self.label4.Text = ""
    
    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()

        if dialog_result == DialogResult.OK:
            user_input1 = input_form.textbox1.Text
            user_input2 = input_form.textbox2.Text
            user_input3 = input_form.param_type
        elif dialog_result == DialogResult.Cancel:
            user_input1 = None
            user_input2 = None
            user_input3 = None
            sys.exit()
        
    except StopIteration:
        pass
    except Exception:
        pass
    except SystemExit:
        pass
    return user_input1, user_input2, user_input3

