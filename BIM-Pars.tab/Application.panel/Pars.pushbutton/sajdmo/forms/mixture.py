# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#mixture.py

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
from System.Windows.Forms import Form, Label, TextBox, Button, DialogResult, PictureBox, ComboBox, ComboBoxStyle, RadioButton, Cursors
from System import Array
import Autodesk.Revit.DB as DB


def mix_input1_radio2(icon_path, search_image_path, ok_icon_path, cancel_icon_path, radio_label, radio_op1, radio_op2, parameter_label, window_name, url):
    """
    Displays a form with radio buttons and a text input field for user interaction.

    This function creates a modal dialog that allows the user to select one of two options 
    via radio buttons and enter a corresponding value in a text box. The dialog includes 
    OK and Cancel buttons, and it can open a specified URL when a label is clicked.

    Parameters:
    - icon_path (str): The file path to the icon displayed in the form.
    - search_image_path (str): The file path to the image displayed in the PictureBox.
    - ok_icon_path (str): The file path to the icon for the OK button.
    - cancel_icon_path (str): The file path to the icon for the Cancel button.
    - radio_label (str): The label text for the radio button section.
    - radio_op1 (str): The text for the first radio button option.
    - radio_op2 (str): The text for the second radio button option.
    - parameter_label (str): The label text for the text input field.
    - window_name (str): The title of the dialog window.
    - url (str): The URL to open when the created_by label is clicked.

    Returns:
    - tuple: A tuple containing:
        - user_input (str or None): The text entered by the user in the text box, or None if not applicable.
        - selected_option (str or None): The selected radio button option ("option 1" or "option 2"), or None if no option is selected.
    """
    #Initialization
    class InputForm(Form):
        def __init__(self):
            
            self.Text = window_name
            self.Width = 300
            self.Height = 475
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
            self.label1.Location = Point(40, 240)
            self.label1.AutoSize = True
            self.label1.Font = Font(self.label1.Font, FontStyle.Bold)
            self.label1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label1)

            self.label2 = Label()
            self.label2.Text = radio_label
            self.label2.Location = Point(40, 125)
            self.label2.AutoSize = True
            self.label2.Font = Font(self.label2.Font, FontStyle.Bold)
            self.label2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label2)

            self.radioButton01 = RadioButton()
            self.radioButton01.Appearance = 0  
            self.radioButton01.Text = radio_op1
            self.radioButton01.Width = 50
            self.radioButton01.Height = 30
            self.radioButton01.Left = 40
            self.radioButton01.Top = 150
            self.radioButton01.CheckedChanged += self.RadioChanged
            self.radioButton01.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton01)

            self.radioButton2 = RadioButton()
            self.radioButton2.Appearance = 0
            self.radioButton2.Text = radio_op2
            self.radioButton2.Width = 50
            self.radioButton2.Height = 30
            self.radioButton2.Left = 40
            self.radioButton2.Top = 175
            self.radioButton2.CheckedChanged += self.RadioChanged
            self.radioButton2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton2)

            self.textbox1 = TextBox()
            self.textbox1.Width = 200
            self.textbox1.Location = Point(40, 265)
            self.textbox1.TextChanged += self.textbox_TextChanged
            self.textbox1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox1)
            self.textbox1.Enabled = False

            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(100, 325)
            self.ok_button.Width = 35
            self.ok_button.Height = 35
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

            self.cancel_button = Button()
            self.cancel_button.DialogResult = DialogResult.Cancel
            self.cancel_button.Location = Point(140, 325)
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
            
            self.user_input = None
            self.selected_option = None

        def Label_Click(self, sender, event):
            webbrowser.open(url)

        def RadioChanged(self, sender, e):
            if self.radioButton01.Checked:
                self.textbox1.Enabled = True
                self.selected_option = "option 1"
            elif self.radioButton2.Checked:
                self.textbox1.Enabled = True
                self.selected_option = "option 2"
            else:
                self.textbox1.Enabled = False
                self.selected_option = None

        def textbox_TextChanged(self, sender, e):
            if self.textbox1.Text:
                self.ok_button.Enabled = True
                self.user_input = self.textbox1.Text
            else:
                self.ok_button.Enabled = False
                self.user_input = None
    
    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()

        if dialog_result == DialogResult.OK:
            user_input = input_form.user_input
            selected_option = input_form.selected_option
        elif dialog_result == DialogResult.Cancel:
            user_input = None
            selected_option = None
            sys.exit()
        
    except StopIteration:
        pass
    except Exception:
        pass
    except SystemExit:
        pass

    return user_input, selected_option

def mix_input2_radio4(icon_path, search_image_path, ok_icon_path, cancel_icon_path, radio_label, radio_op1, radio_op2, radio_label2, radio_op3, radio_op4, parameter_label, window_name, url):
    """
    Displays a form with multiple radio buttons and two text input fields for user interaction.

    This function creates a modal dialog that allows the user to select one of two options 
    via the first set of radio buttons and one of two options via the second set of radio buttons. 
    The dialog includes two text boxes for user input and OK and Cancel buttons. 
    It can also open a specified URL when a label is clicked.

    Parameters:
    - icon_path (str): The file path to the icon displayed in the form.
    - search_image_path (str): The file path to the image displayed in the PictureBox.
    - ok_icon_path (str): The file path to the icon for the OK button.
    - cancel_icon_path (str): The file path to the icon for the Cancel button.
    - radio_label (str): The label text for the first set of radio buttons.
    - radio_op1 (str): The text for the first radio button option in the first set.
    - radio_op2 (str): The text for the second radio button option in the first set.
    - radio_label2 (str): The label text for the second set of radio buttons.
    - radio_op3 (str): The text for the first radio button option in the second set.
    - radio_op4 (str): The text for the second radio button option in the second set.
    - parameter_label (str): The label text for the first text input field.
    - window_name (str): The title of the dialog window.
    - url (str): The URL to open when the created_by label is clicked.

    Returns:
    - tuple: A tuple containing:
        - user_input1 (str or None): The text entered by the user in the first text box, or None if not applicable.
        - user_input2 (str or None): The text entered by the user in the second text box, or None if not applicable.
        - selected_option1 (str or None): The selected option from the first set of radio buttons ("C1R1" or "C1R2"), or None if no option is selected.
        - selected_option2 (str or None): The selected option from the second set of radio buttons ("C2R1" or "C2R2"), or None if no option is selected.
    """
    #Initializations
    class InputForm(Form):
        def __init__(self):
            self.Text = window_name
            self.Width = 300
            self.Height = 475
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
            self.label1.Location = Point(40, 240)
            self.label1.AutoSize = True
            self.label1.Font = Font(self.label1.Font, FontStyle.Bold)
            self.label1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label1)

            self.label2 = Label()
            self.label2.Text = radio_label
            self.label2.Location = Point(40, 125)
            self.label2.AutoSize = True
            self.label2.Font = Font(self.label2.Font, FontStyle.Bold)
            self.label2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label2)

            self.label2_append = Label()
            self.label2_append.Text = ""
            self.label2_append.Location = Point(100, 125)
            self.label2_append.AutoSize = True
            self.label2_append.Font = Font(self.label2_append.Font, FontStyle.Bold)
            self.label2_append.ForeColor = Color.Red
            self.label2_append.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label2_append)

            self.label3 = Label()
            self.label3.Text = radio_label2
            self.label3.Location = Point(140, 125)
            self.label3.AutoSize = True
            self.label3.Font = Font(self.label3.Font, FontStyle.Bold)
            self.label3.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label3)

            self.label3_append = Label()
            self.label3_append.Text = ""
            self.label3_append.Location = Point(240, 125)
            self.label3_append.AutoSize = True
            self.label3_append.Font = Font(self.label3_append.Font, FontStyle.Bold)
            self.label3_append.ForeColor = Color.Red
            self.label3_append.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label3_append)

            self.label4 = Label()
            self.label4.Text = radio_label2
            self.label4.Location = Point(40, 300)
            self.label4.AutoSize = True
            self.label4.Font = Font(self.label4.Font, FontStyle.Bold)
            self.label4.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)

            self.radioButton01 = RadioButton()
            self.radioButton01.Appearance = 0  
            self.radioButton01.Text = radio_op1
            self.radioButton01.Width = 50
            self.radioButton01.Height = 30
            self.radioButton01.Left = 40
            self.radioButton01.Top = 150
            self.radioButton01.CheckedChanged += self.RadioChanged1
            self.radioButton01.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton01)

            self.radioButton2 = RadioButton()
            self.radioButton2.Appearance = 0  
            self.radioButton2.Text = radio_op2
            self.radioButton2.Width = 50
            self.radioButton2.Height = 30
            self.radioButton2.Left = 40
            self.radioButton2.Top = 175
            self.radioButton2.CheckedChanged += self.RadioChanged1
            self.radioButton2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton2)
            self.radioButton2.Enabled = False

            self.radioButton3 = RadioButton()
            self.radioButton3.Appearance = 0  
            self.radioButton3.Text = radio_op3
            self.radioButton3.Width = 50
            self.radioButton3.Height = 30
            self.radioButton3.Left = 140
            self.radioButton3.Top = 150
            self.radioButton3.CheckedChanged += self.RadioChanged2
            self.radioButton3.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton3)
            self.radioButton3.Enabled = False
                
            self.radioButton4 = RadioButton()
            self.radioButton4.Appearance = 0
            self.radioButton4.Text = radio_op4
            self.radioButton4.Width = 50
            self.radioButton4.Height = 30
            self.radioButton4.Left = 140
            self.radioButton4.Top = 175
            self.radioButton4.CheckedChanged += self.RadioChanged2
            self.radioButton4.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton4)
            self.radioButton4.Enabled = False

            self.textbox1 = TextBox()
            self.textbox1.Width = 200
            self.textbox1.Location = Point(40, 265)
            self.textbox1.TextChanged += self.textbox_TextChanged
            self.textbox1.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.textbox1)
            self.textbox1.Enabled = False

            self.textbox2 = TextBox()
            self.textbox2.Width = 200
            self.textbox2.Location = Point(40, 325)
            self.textbox2.TextChanged += self.textbox_TextChanged2
            self.textbox2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)
            
            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(100, 365)
            self.ok_button.Width = 35
            self.ok_button.Height = 35
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

            self.cancel_button = Button()
            self.cancel_button.DialogResult = DialogResult.Cancel
            self.cancel_button.Location = Point(140, 365)
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

            self.user_input = None
            self.user_input2 = None
            self.selected_option1 = None
            self.selected_option2 = None

        def Label_Click(self, sender, event):
            webbrowser.open(url)

        def RadioChanged1(self, sender, e):
            if self.radioButton01.Checked:
                self.radioButton3.Enabled = True
                self.radioButton4.Enabled = True
                self.selected_option1 = "C1R1"
                self.radioButton01.Enabled = False
                self.radioButton2.Enabled = False
                self.radioButton01.Checked = True
                self.label2_append.Text = radio_op1
            elif self.radioButton2.Checked:
                self.radioButton3.Enabled = True
                self.radioButton4.Enabled = True
                self.selected_option1 = "C1R2"
                self.radioButton01.Enabled = False
                self.radioButton2.Enabled = False
                self.radioButton2.Checked = True
                self.label2_append.Text = radio_op2

        def RadioChanged2(self, sender, e):
            if self.radioButton3.Checked:
                self.textbox2.Enabled = True
                self.selected_option2 = "C2R1"
                self.label3_append.Text = radio_op3

                self.Controls.Add(self.textbox2)
                self.Controls.Add(self.label4)

                self.radioButton3.Enabled = False
                self.radioButton4.Enabled = False

            elif self.radioButton4.Checked:
                self.textbox1.Enabled = True
                self.selected_option2 = "C2R2"
                self.label3_append.Text = radio_op4

                self.Controls.Remove(self.textbox2)
                self.textbox2.Enabled = False
                self.Controls.Remove(self.label4)

                self.radioButton3.Enabled = False
                self.radioButton4.Enabled = False
            else:
                self.textbox1.Enabled = False
                self.selected_option2 = None
                self.label3_append.Text = ""

        def textbox_TextChanged2(self, sender, e):
            if self.textbox2.Text:
                self.ok_button.Enabled = False
                self.textbox1.Enabled = True
                self.user_input2 = self.textbox2.Text
                self.textbox2.Enabled = True
            else:
                self.textbox1.Enabled = False
                self.user_input2 = None

        def textbox_TextChanged(self, sender, e):
            if self.textbox1.Text:
                self.ok_button.Enabled = True
                self.user_input1 = self.textbox1.Text
            else:
                self.ok_button.Enabled = False
                self.user_input1 = None
    
    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()

        if dialog_result == DialogResult.OK:
            user_input = input_form.user_input1
            user_input2 = input_form.user_input2
            selected_option1 = input_form.selected_option1
            selected_option2 = input_form.selected_option2
        elif dialog_result == DialogResult.Cancel:
            user_input = None
            user_input2 = None
            selected_option1 = None
            selected_option2 = None
            sys.exit()
        
    except StopIteration:
        pass
    except Exception:
        pass
    except SystemExit:
        pass

    return user_input, user_input2, selected_option1, selected_option2

def double_input(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, value_label, window_name, url):
    """
    Displays a form with two text input fields for user interaction.

    This function creates a modal dialog that allows the user to enter two values in separate text boxes. 
    The dialog includes OK and Cancel buttons, and it can open a specified URL when a label is clicked.

    Parameters:
    - icon_path (str): The file path to the icon displayed in the form.
    - search_image_path (str): The file path to the image displayed in the PictureBox.
    - ok_icon_path (str): The file path to the icon for the OK button.
    - cancel_icon_path (str): The file path to the icon for the Cancel button.
    - parameter_label (str): The label text for the first text input field.
    - value_label (str): The label text for the second text input field.
    - window_name (str): The title of the dialog window.
    - url (str): The URL to open when the created_by label is clicked.

    Returns:
    - tuple: A tuple containing:
        - user_input1 (str or None): The text entered by the user in the first text box, or None if not applicable.
        - user_input2 (str or None): The text entered by the user in the second text box, or None if not applicable.
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

def mix_input_combo(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, value_label, window_name, url):
    """
    Displays a form with a text input field and a combo box for user interaction.

    This function creates a modal dialog that allows the user to enter a value in a text box 
    and select an option from a combo box. The dialog includes OK and Cancel buttons, 
    and it can open a specified URL when a label is clicked.

    Parameters:
    - icon_path (str): The file path to the icon displayed in the form.
    - search_image_path (str): The file path to the image displayed in the PictureBox.
    - ok_icon_path (str): The file path to the icon for the OK button.
    - cancel_icon_path (str): The file path to the icon for the Cancel button.
    - parameter_label (str): The label text for the text input field.
    - value_label (str): The label text for the combo box.
    - window_name (str): The title of the dialog window.
    - url (str): The URL to open when the created_by label is clicked.

    Returns:
    - tuple: A tuple containing:
        - user_input1 (str or None): The text entered by the user in the text box, or None if not applicable.
        - user_input2 (str or None): The selected item from the combo box, or None if not applicable.
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

            self.selected_item = None

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

            options = [
                        '3 digits', 
                        '4 digits', 
                        '5 digits', 
                        '6 digits',
                        '7 digits',
                        '8 digits', 
                        '9 digits', 
                        '10 digits',
                        '11 digits', 
                        '12 digits', 
                        '13 digits', 
                        '14 digits', 
                        '15 digits', 
                        '16 digits', 
                    ]
            self.comboBox = ComboBox()
            self.comboBox.Width = 200
            self.comboBox.Left = 40
            self.comboBox.Top = 225
            self.comboBox.DropDownStyle = ComboBoxStyle.DropDownList
            self.comboBox.Items.AddRange(Array[object](options))
            self.comboBox.SelectedIndexChanged += self.comboBox_selected_index_changed
            self.Controls.Add(self.comboBox)
            self.comboBox.SelectedIndex = 13
        
        def Label_Click(self, sender, event):
            webbrowser.open(url)

        def textbox_TextChanged(self, sender, e):
            self.comboBox.Enabled = True
            if self.textbox1.Text and self.selected_item:
                self.ok_button.Enabled = True
            else:
                self.ok_button.Enabled = False
        def comboBox_selected_index_changed(self, sender, e):
            self.selected_item = self.comboBox.SelectedItem  

            if self.textbox1.Text and self.selected_item:
                self.ok_button.Enabled = True
            else:
                self.ok_button.Enabled = False
    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()

        if dialog_result == DialogResult.OK:
            user_input1 = input_form.textbox1.Text
            user_input2 = input_form.selected_item  
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

def mix_input_combo2(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, value_label, window_name, url):
    """
    Displays a form with a text input field and a combo box for user interaction.

    This function creates a modal dialog that allows the user to enter a value in a text box 
    and select an option from a combo box. The dialog includes OK and Cancel buttons, 
    and it can open a specified URL when a label is clicked.

    Parameters:
    - icon_path (str): The file path to the icon displayed in the form.
    - search_image_path (str): The file path to the image displayed in the PictureBox.
    - ok_icon_path (str): The file path to the icon for the OK button.
    - cancel_icon_path (str): The file path to the icon for the Cancel button.
    - parameter_label (str): The label text for the text input field.
    - value_label (str): The label text for the combo box.
    - window_name (str): The title of the dialog window.
    - url (str): The URL to open when the created_by label is clicked.

    Returns:
    - tuple: A tuple containing:
        - user_input1 (str or None): The text entered by the user in the text box, or None if not applicable.
        - user_input2 (str or None): The selected item from the combo box, or None if not applicable.
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

            self.selected_item = None

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

            options = [
                        '2 characters',
                        '3 characters',
                        '4 characters',
                        '5 characters',
                        '6 characters',
                        '7 characters',
                        '8 characters',
                        '9 characters',
                        '10 characters',
                        '11 characters',
                        '12 characters',
                        '13 characters',
                        '14 characters',
                        '15 characters',
                        '16 characters',
                    ]
            self.comboBox = ComboBox()
            self.comboBox.Width = 200
            self.comboBox.Left = 40
            self.comboBox.Top = 225
            self.comboBox.DropDownStyle = ComboBoxStyle.DropDownList
            self.comboBox.Items.AddRange(Array[object](options))
            self.comboBox.SelectedIndexChanged += self.comboBox_selected_index_changed
            self.Controls.Add(self.comboBox)
            self.comboBox.SelectedIndex = 14

        def Label_Click(self, sender, event):
            webbrowser.open(url)

        def textbox_TextChanged(self, sender, e):
            self.comboBox.Enabled = True
            if self.textbox1.Text and self.selected_item:
                self.ok_button.Enabled = True
            else:
                self.ok_button.Enabled = False
        def comboBox_selected_index_changed(self, sender, e):
            self.selected_item = self.comboBox.SelectedItem 

            if self.textbox1.Text and self.selected_item:
                self.ok_button.Enabled = True
            else:
                self.ok_button.Enabled = False

    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()

        if dialog_result == DialogResult.OK:
            user_input1 = input_form.textbox1.Text
            user_input2 = input_form.selected_item  
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

def mix_2input_1radio_combo(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, value_label, window_name, seprator_label, radio_op1, radio_op2, url):
    """
    Displays a form with two text input fields, a radio button group, and a combo box for user interaction.

    This function creates a modal dialog that allows the user to enter two values in separate text boxes, 
    select one of two options via radio buttons, and choose an option from a combo box. 
    The dialog includes OK and Cancel buttons, and it can open a specified URL when a label is clicked.

    Parameters:
    - icon_path (str): The file path to the icon displayed in the form.
    - search_image_path (str): The file path to the image displayed in the PictureBox.
    - ok_icon_path (str): The file path to the icon for the OK button.
    - cancel_icon_path (str): The file path to the icon for the Cancel button.
    - parameter_label (str): The label text for the first text input field.
    - value_label (str): The label text for the second text input field.
    - window_name (str): The title of the dialog window.
    - seprator_label (str): The label text for the separator between the radio buttons.
    - radio_op1 (str): The text for the first radio button option.
    - radio_op2 (str): The text for the second radio button option.
    - url (str): The URL to open when the created_by label is clicked.

    Returns:
    - tuple: A tuple containing:
        - user_input1 (str or None): The text entered by the user in the first text box, or None if not applicable.
        - user_input2 (str or None): The selected option from the radio buttons ("C1R1" or "C1R2"), or None if no option is selected.
        - user_input3 (str or None): The text entered by the user in the second text box, or None if not applicable.
        - user_input4 (str or None): The selected item from the combo box, or None if not applicable.
    """
    #Initialization
    class InputForm(Form):
        def __init__(self):
            self.Text = window_name
            self.Width = 300
            self.Height = 550
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
            self.label2.Location = Point(40, 325)
            self.label2.AutoSize = True
            self.label2.Font = Font(self.label2.Font, FontStyle.Bold)
            self.label2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label2)

            self.label3 = Label()
            self.label3.Text = seprator_label
            self.label3.Location = Point(40, 200)
            self.label3.AutoSize = True
            self.label3.Font = Font(self.label3.Font, FontStyle.Bold)
            self.label3.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label3)

            self.radioButton01 = RadioButton()
            self.radioButton01.Appearance = 0
            self.radioButton01.Text = radio_op1
            self.radioButton01.Width = 50
            self.radioButton01.Height = 30
            self.radioButton01.Left = 40
            self.radioButton01.Top = 225
            self.radioButton01.CheckedChanged += self.RadioChanged
            self.radioButton01.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton01)
            self.radioButton01.Enabled = False

            self.radioButton2 = RadioButton()
            self.radioButton2.Appearance = 0
            self.radioButton2.Text = radio_op2
            self.radioButton2.Width = 50
            self.radioButton2.Height = 30
            self.radioButton2.Left = 40
            self.radioButton2.Top = 250
            self.radioButton2.CheckedChanged += self.RadioChanged
            self.radioButton2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton2)
            self.radioButton2.Enabled = False

            self.textbox2 = TextBox()
            self.textbox2.Width = 200
            self.textbox2.Location = Point(40, 285)
            self.textbox2.TextChanged += self.textbox_TextChanged2
            self.textbox2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)

            self.selected_item = None  
            self.selected_option1 = None  

            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(100, 415)
            self.ok_button.Width = 35
            self.ok_button.Height = 35
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

            self.cancel_button = Button()
            self.cancel_button.DialogResult = DialogResult.Cancel
            self.cancel_button.Location = Point(140, 415)
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

            options = [
                        '3 digits', 
                        '4 digits', 
                        '5 digits', 
                        '6 digits',
                        '7 digits',
                        '8 digits', 
                        '9 digits', 
                        '10 digits',
                        '11 digits', 
                        '12 digits', 
                        '13 digits', 
                        '14 digits', 
                        '15 digits', 
                        '16 digits', 
                    ]
            self.comboBox = ComboBox()
            self.comboBox.Width = 200
            self.comboBox.Left = 40
            self.comboBox.Top = 350
            self.comboBox.DropDownStyle = ComboBoxStyle.DropDownList
            self.comboBox.Items.AddRange(Array[object](options))
            self.comboBox.SelectedIndexChanged += self.comboBox_selected_index_changed
            self.Controls.Add(self.comboBox)
            self.comboBox.SelectedIndex = 13
            self.comboBox.Enabled = False

        def Label_Click(self, sender, event):
            webbrowser.open(url)

        def RadioChanged (self, sender, e):
            if self.radioButton01.Checked:
                self.Controls.Add(self.textbox2)
                self.selected_option1 = "C1R1"
                self.radioButton01.Enabled = False
                self.radioButton2.Enabled = False
                self.radioButton01.Checked = True
                self.comboBox.Enabled = False
                self.textbox1.Enabled = False
            elif self.radioButton2.Checked:
                self.Controls.Remove(self.textbox2)
                self.selected_option1 = "C1R2"

                
                self.radioButton01.Enabled = False
                self.radioButton2.Enabled = False
                self.radioButton2.Checked = True
                self.comboBox.Enabled = True
                self.textbox1.Enabled = False

        def textbox_TextChanged2(self, sender, e):
            if self.textbox2.Text and self.textbox1.Text:
                self.comboBox.Enabled = True                
            else:
                self.comboBox.Enabled = False

        def textbox_TextChanged(self, sender, e):
            self.comboBox.Enabled = False
            if self.textbox1.Text :
                self.radioButton01.Enabled = True
                self.radioButton2.Enabled = True
            else:
                self.radioButton01.Enabled = False
                self.radioButton2.Enabled = False


        def comboBox_selected_index_changed(self, sender, e):
            self.selected_item = self.comboBox.SelectedItem 
            if self.radioButton2.Checked:
                if self.textbox1.Text and self.selected_item:
                    self.ok_button.Enabled = True
                    self.textbox1.Enabled = False
                    self.radioButton01.Enabled = False
                    self.radioButton2.Enabled = False                   
                else:
                    self.ok_button.Enabled = False
                    self.textbox1.Enabled = True
                    self.radioButton01.Enabled = True
                    self.radioButton2.Enabled = True
            elif self.radioButton01.Checked:
                if self.textbox1.Text and self.textbox2.Text and self.selected_item:
                    self.ok_button.Enabled = True
                    self.textbox1.Enabled = False
                    self.radioButton01.Enabled = False
                    self.radioButton2.Enabled = False
                    self.textbox2.Enabled = False
                else:
                    self.ok_button.Enabled = False
                    self.textbox1.Enabled = True
                    self.radioButton01.Enabled = True
                    self.radioButton2.Enabled = True
                    self.textbox2.Enabled = True
    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()

        if dialog_result == DialogResult.OK:
            user_input1 = input_form.textbox1.Text
            user_input2 = input_form.selected_option1
            user_input4 = input_form.selected_item  
            if input_form.textbox2.Text:
                user_input3 = input_form.textbox2.Text
            else:
                user_input3 = None
        elif dialog_result == DialogResult.Cancel:
            user_input1 = None
            user_input2 = None
            user_input3 = None
            user_input4 = None
            sys.exit()

    except StopIteration:
        pass
    except Exception:
        pass
    except SystemExit:
        pass
    return user_input1, user_input2, user_input3, user_input4

def mix_2input_1radio_combo2(icon_path, search_image_path, ok_icon_path, cancel_icon_path, parameter_label, value_label, window_name, seprator_label, radio_op1, radio_op2, url):
    """
    Creates a Windows Form dialog with multiple input controls for user interaction.

    This function displays a modal dialog that contains:
    - A text input field
    - Two radio button options
    - A conditional second text input field (appears when first radio button is selected)
    - A combo box with character length options (2-16 characters)
    - OK and Cancel buttons
    - A clickable BIM Pars label that opens a URL

    The dialog implements a specific flow:
    1. User enters text in first input field
    2. Radio buttons become enabled
    3. Based on radio selection:
        - Option 1: Shows second text input field
        - Option 2: Enables combo box directly
    4. Combo box selection enables OK button when all required fields are filled

    Parameters:
        icon_path (str): Path to the window icon file (.ico)
        search_image_path (str): Path to the image displayed at top of form (.gif)
        ok_icon_path (str): Path to the OK button icon file (.ico)
        cancel_icon_path (str): Path to the Cancel button icon file (.ico)
        parameter_label (str): Label text for the first text input field
        value_label (str): Label text for the combo box
        window_name (str): Title of the dialog window
        seprator_label (str): Label text above the radio buttons
        radio_op1 (str): Text for first radio button option
        radio_op2 (str): Text for second radio button option
        url (str): URL to open when BIM Pars label is clicked

    Returns:
        tuple: Contains four elements:
            - user_input1 (str or None): Text from first input field
            - user_input2 (str or None): Selected radio option ("C1R1" or "C1R2")
            - user_input3 (str or None): Text from second input field (if radio_op1 selected)
            - user_input4 (str or None): Selected combo box value (e.g. "16 characters")

    Notes:
        - Returns (None, None, None, None) if dialog is cancelled
        - Handles SystemExit when Cancel is clicked
        - Window size is fixed at 300x550 pixels
        - Combo box is pre-selected to "16 characters"
    """
    #Initialization
    class InputForm(Form):
        def __init__(self):
            self.Text = window_name
            self.Width = 300
            self.Height = 550
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
            self.label2.Location = Point(40, 325)
            self.label2.AutoSize = True
            self.label2.Font = Font(self.label2.Font, FontStyle.Bold)
            self.label2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label2)

            self.label3 = Label()
            self.label3.Text = seprator_label
            self.label3.Location = Point(40, 200)
            self.label3.AutoSize = True
            self.label3.Font = Font(self.label3.Font, FontStyle.Bold)
            self.label3.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label3)

            self.radioButton01 = RadioButton()
            self.radioButton01.Appearance = 0
            self.radioButton01.Text = radio_op1
            self.radioButton01.Width = 50
            self.radioButton01.Height = 30
            self.radioButton01.Left = 40
            self.radioButton01.Top = 225
            self.radioButton01.CheckedChanged += self.RadioChanged
            self.radioButton01.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton01)
            self.radioButton01.Enabled = False

            self.radioButton2 = RadioButton()
            self.radioButton2.Appearance = 0
            self.radioButton2.Text = radio_op2
            self.radioButton2.Width = 50
            self.radioButton2.Height = 30
            self.radioButton2.Left = 40
            self.radioButton2.Top = 250
            self.radioButton2.CheckedChanged += self.RadioChanged
            self.radioButton2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton2)
            self.radioButton2.Enabled = False

            self.textbox2 = TextBox()
            self.textbox2.Width = 200
            self.textbox2.Location = Point(40, 285)
            self.textbox2.TextChanged += self.textbox_TextChanged2
            self.textbox2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right)

            self.selected_item = None  
            self.selected_option1 = None  

            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(100, 415)
            self.ok_button.Width = 35
            self.ok_button.Height = 35
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

            self.cancel_button = Button()
            self.cancel_button.DialogResult = DialogResult.Cancel
            self.cancel_button.Location = Point(140, 415)
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

            options = [
                        '2 characters',
                        '3 characters',
                        '4 characters',
                        '5 characters',
                        '6 characters',
                        '7 characters',
                        '8 characters',
                        '9 characters',
                        '10 characters',
                        '11 characters',
                        '12 characters',
                        '13 characters',
                        '14 characters',
                        '15 characters',
                        '16 characters',
                    ]
            self.comboBox = ComboBox()
            self.comboBox.Width = 200
            self.comboBox.Left = 40
            self.comboBox.Top = 350
            self.comboBox.DropDownStyle = ComboBoxStyle.DropDownList
            self.comboBox.Items.AddRange(Array[object](options))
            self.comboBox.SelectedIndexChanged += self.comboBox_selected_index_changed
            self.Controls.Add(self.comboBox)
            self.comboBox.SelectedIndex = 14
            self.comboBox.Enabled = False

        def Label_Click(self, sender, event):
            webbrowser.open(url)

        def RadioChanged (self, sender, e):
            if self.radioButton01.Checked:
                self.Controls.Add(self.textbox2)
                self.selected_option1 = "C1R1"
                self.radioButton01.Enabled = False
                self.radioButton2.Enabled = False
                self.radioButton01.Checked = True
                self.comboBox.Enabled = False
                self.textbox1.Enabled = False
            elif self.radioButton2.Checked:
                self.Controls.Remove(self.textbox2)
                self.selected_option1 = "C1R2"
               
                self.radioButton01.Enabled = False
                self.radioButton2.Enabled = False
                self.radioButton2.Checked = True

                self.comboBox.Enabled = True
                self.textbox1.Enabled = False

        def textbox_TextChanged2(self, sender, e):
            if self.textbox2.Text and self.textbox1.Text:
                self.comboBox.Enabled = True                
            else:
                self.comboBox.Enabled = False

        def textbox_TextChanged(self, sender, e):
            self.comboBox.Enabled = False
            if self.textbox1.Text :
                self.radioButton01.Enabled = True
                self.radioButton2.Enabled = True
            else:
                self.radioButton01.Enabled = False
                self.radioButton2.Enabled = False

        def comboBox_selected_index_changed(self, sender, e):
            self.selected_item = self.comboBox.SelectedItem  

            if self.radioButton2.Checked:
                if self.textbox1.Text and self.selected_item:
                    self.ok_button.Enabled = True
                    self.textbox1.Enabled = False
                    self.radioButton01.Enabled = False
                    self.radioButton2.Enabled = False                   
                else:
                    self.ok_button.Enabled = False
                    self.textbox1.Enabled = True
                    self.radioButton01.Enabled = True
                    self.radioButton2.Enabled = True

            elif self.radioButton01.Checked:
                if self.textbox1.Text and self.textbox2.Text and self.selected_item:
                    self.ok_button.Enabled = True
                    self.textbox1.Enabled = False
                    self.radioButton01.Enabled = False
                    self.radioButton2.Enabled = False
                    self.textbox2.Enabled = False
                else:
                    self.ok_button.Enabled = False
                    self.textbox1.Enabled = True
                    self.radioButton01.Enabled = True
                    self.radioButton2.Enabled = True
                    self.textbox2.Enabled = True

    try:
        input_form = InputForm()

        dialog_result = input_form.ShowDialog()
        
        if dialog_result == DialogResult.OK:
            user_input1 = input_form.textbox1.Text
            user_input2 = input_form.selected_option1
            user_input4 = input_form.selected_item 
            if input_form.textbox2.Text:
                user_input3 = input_form.textbox2.Text
            else:
                user_input3 = None

        elif dialog_result == DialogResult.Cancel:
            user_input1 = None
            user_input2 = None
            user_input3 = None
            user_input4 = None
            sys.exit()

    except StopIteration:
        pass
    except Exception:
        pass
    except SystemExit:
        pass
    return user_input1, user_input2, user_input3, user_input4

