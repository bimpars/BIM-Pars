# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
#option.py

#Imports
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from System.Windows.Forms import Form, Label, TextBox, Button, DialogResult, PictureBox, Cursors, ComboBox, ComboBoxStyle, RadioButton
from System.Drawing import Point, Size, Bitmap, Color, Icon, Font, FontStyle, Image, GraphicsUnit
from RevitServices.Persistence import DocumentManager
from structure.root import comparev_back, comparee_back, comparetwo_icon, lan_path, cuslogo_path, logo_path, id_back, submit_icon, cancel_icon, ok_icon, compare_icon, searchbar_icon, searchbar_back, math_back, math_icon, rannumber_icon, rannumber_back, ranstring_icon, ranstring_back, editor_icon, editor_back, replace_back, prefix_back, suffix_back, borcomma_back 
import os
import sys
import webbrowser
import System.Windows.Forms as WinForms
import System.Drawing as Drawing
from System import Array
import Autodesk.Revit.DB as DB

doc = DocumentManager.Instance.CurrentDBDocument 

def pick(window_name, op1, op2, window_icon, button_icon, op1_pic, op2_pic, url):
    """
    Displays a modal form with two radio button options and an action button.

    This function creates a form that allows the user to select between two options 
    (op1 and op2) represented by radio buttons. The form includes images for each option, 
    a button that becomes enabled when an option is selected, and a label indicating 
    the creator of the form. The form can be customized with a title, icons, and images.

    Parameters:
    - window_name (str): The title of the form window.
    - op1 (str): The text for the first radio button option.
    - op2 (str): The text for the second radio button option.
    - window_icon (str): The file path to the icon for the form window.
    - button_icon (str): The file path to the icon for the action button.
    - op1_pic (str): The file path to the image for the first option.
    - op2_pic (str): The file path to the image for the second option.
    - url (str): The URL to open when the creator label is clicked.

    Returns:
    - str: The text of the selected radio button option if the user clicks the action button; 
           otherwise, returns None.
    """
    #Initialization
    class MyForm(Form):
        def __init__(self, doc):
            self.Text = window_name
            self.Width = 330
            self.Height = 350
            self.BackColor = Color.White
            self.doc = doc
            self.CenterToScreen()
            self.Icon = Icon(window_icon)

            self.radioButton01 = RadioButton()
            self.radioButton01.Appearance = 0
            self.radioButton01.Text = op1
            self.radioButton01.Width = 100
            self.radioButton01.Height = 30
            self.radioButton01.Left = 50
            self.radioButton01.Top = 10
            self.radioButton01.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.radioButton01.CheckedChanged += self.radioButton_checked_changed
            
            self.radioButton2 = RadioButton()
            self.radioButton2.Appearance = 0
            self.radioButton2.Text = op2
            self.radioButton2.Width = 100
            self.radioButton2.Height = 30
            self.radioButton2.Left = 175
            self.radioButton2.Top = 10
            self.radioButton2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.radioButton2.CheckedChanged += self.radioButton_checked_changed

            self.button = Button()
            self.button.Width = 40
            self.button.Height = 40
            self.button.Left = (self.Width - self.button.Width - 10) // 2
            self.button.Top = 220
            icon_button = button_icon
            self.button.Image = Icon(icon_button).ToBitmap()
            self.button.Click += self.button_click
            self.button.Enabled = False
            self.button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)

            self.pictureBox = PictureBox()
            self.pictureBox.Location = Point(50, 50)
            self.pictureBox.Size = Size(100, 100)  
            icon_path = op1_pic
            image = Bitmap(icon_path)
            self.pictureBox.Image = image
            self.pictureBox.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)

            self.pictureBox2 = PictureBox()
            self.pictureBox2.Location = Point(175, 50)
            self.pictureBox2.Size = Size(100, 100) 
            icon_path2 = op2_pic 
            image2 = Bitmap(icon_path2)
            self.pictureBox2.Image = image2
            self.pictureBox2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)

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
         
            self.Controls.Add(self.radioButton01)
            self.Controls.Add(self.radioButton2)
            self.Controls.Add(self.pictureBox)
            self.Controls.Add(self.pictureBox2)
            self.Controls.Add(self.button)
            self.checked_radiobutton = None
        
        def Label_Click(self, sender, event):
            webbrowser.open(url)

        def radioButton_checked_changed(self, sender, e):
            radiobutton = sender
            if radiobutton.Checked:
                self.button.Enabled = True
                self.checked_radiobutton = radiobutton

        def button_click(self, sender, e):
            if self.checked_radiobutton is not None:
                self.selected_radio_button_text = self.checked_radiobutton.Text
                self.DialogResult = DialogResult.OK

    form = MyForm(doc)
    result = form.ShowDialog()
    if result == DialogResult.OK:
        return form.selected_radio_button_text
    else:
        return None

def pick3_dyn(window_name, op1, op2, op3, window_icon, button_icon, op1_pic, op2_pic, op3_pic, dyn1, dyn2, dyn3, url):
    """
    Displays a modal form with three radio button options and an action button.

    This function creates a form that allows the user to select between three options 
    (op1, op2, and op3) represented by radio buttons. The form includes images for each option, 
    a button that becomes enabled when an option is selected, and a label indicating 
    the creator of the form. Additionally, the form displays dynamic descriptions based on 
    the selected radio button. The form can be customized with a title, icons, and images.

    Parameters:
    - window_name (str): The title of the form window.
    - op1 (str): The text for the first radio button option.
    - op2 (str): The text for the second radio button option.
    - op3 (str): The text for the third radio button option.
    - window_icon (str): The file path to the icon for the form window.
    - button_icon (str): The file path to the icon for the action button.
    - op1_pic (str): The file path to the image for the first option.
    - op2_pic (str): The file path to the image for the second option.
    - op3_pic (str): The file path to the image for the third option.
    - dyn1 (str): The dynamic description for the first option.
    - dyn2 (str): The dynamic description for the second option.
    - dyn3 (str): The dynamic description for the third option.
    - url (str): The URL to open when the creator label is clicked.

    Returns:
    - str: The text of the selected radio button option if the user clicks the action button; 
           otherwise, returns None.
    """
    #Initializations
    class MyForm(Form):
        def __init__(self, doc):
            self.Text = window_name
            self.Width = 475
            self.Height = 450
            self.BackColor = Color.White
            self.doc = doc
            self.CenterToScreen()
            self.Icon = Icon(window_icon)

            self.radioButton01 = RadioButton()
            self.radioButton01.Appearance = 0
            self.radioButton01.Text = op1
            self.radioButton01.Width = 100
            self.radioButton01.Height = 30
            self.radioButton01.Left = 50
            self.radioButton01.Top = 10
            self.radioButton01.CheckedChanged += self.radioButton_checked_changed
            self.radioButton01.CheckedChanged += self.dyn_descriptin
            self.radioButton01.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)

            self.radioButton2 = RadioButton()
            self.radioButton2.Appearance = 0
            self.radioButton2.Text = op2
            self.radioButton2.Width = 100
            self.radioButton2.Height = 30
            self.radioButton2.Left = 175
            self.radioButton2.Top = 10
            self.radioButton2.CheckedChanged += self.radioButton_checked_changed
            self.radioButton2.CheckedChanged += self.dyn_descriptin2
            self.radioButton2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)

            self.radioButton3 = RadioButton()
            self.radioButton3.Appearance = 0
            self.radioButton3.Text = op3
            self.radioButton3.Width = 100
            self.radioButton3.Height = 30
            self.radioButton3.Left = 300
            self.radioButton3.Top = 10
            self.radioButton3.CheckedChanged += self.radioButton_checked_changed
            self.radioButton3.CheckedChanged += self.dyn_descriptin3
            self.radioButton3.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)

            self.button = Button()
            self.button.Width = 40
            self.button.Height = 40
            self.button.Left = (self.Width - self.button.Width - 10) // 2
            self.button.Top = 320
            icon_button = button_icon
            self.button.Image = Icon(icon_button).ToBitmap()
            self.button.Click += self.button_click
            self.button.Enabled = False
            self.button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)

            self.pictureBox = PictureBox()
            self.pictureBox.Location = Point(50, 50)
            self.pictureBox.Size = Size(100, 100)  
            icon_path = op1_pic
            image = Bitmap(icon_path)
            self.pictureBox.Image = image
            self.pictureBox.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)

            self.pictureBox2 = PictureBox()
            self.pictureBox2.Location = Point(175, 50)
            self.pictureBox2.Size = Size(100, 100)  
            icon_path2 = op2_pic 
            image2 = Bitmap(icon_path2)
            self.pictureBox2.Image = image2
            self.pictureBox2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)

            self.pictureBox3 = PictureBox()
            self.pictureBox3.Location = Point(300, 50)
            self.pictureBox3.Size = Size(100, 100)  
            icon_path3 = op3_pic 
            image3 = Bitmap(icon_path3)
            self.pictureBox3.Image = image3
            self.pictureBox3.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)

            self.label = Label()
            self.label.Text = ""
            self.label.AutoSize = True
            self.label.Left = 50
            self.label.Top = 200
            self.label.ForeColor = Color.Black
            self.label.MaximumSize = Size(375, 200)
            self.label.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Right)
            self.Controls.Add(self.label)

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
        
            self.Controls.Add(self.radioButton01)
            self.Controls.Add(self.radioButton2)
            self.Controls.Add(self.radioButton3)
            self.Controls.Add(self.pictureBox)
            self.Controls.Add(self.pictureBox2)
            self.Controls.Add(self.pictureBox3)
            self.Controls.Add(self.button)
            self.checked_radiobutton = None
        def Label_Click(self, sender, event):
            webbrowser.open(url)

        def radioButton_checked_changed(self, sender, e):
            radiobutton = sender
            if radiobutton.Checked:
                self.button.Enabled = True
                self.checked_radiobutton = radiobutton

        def dyn_descriptin(self, sender, e):
            if self.radioButton01:
                self.label.Text = ""
                self.label.Text = dyn1

        def dyn_descriptin2(self, sender, e):
            if self.radioButton2:
                self.label.Text = ""
                self.label.Text = dyn2

        def dyn_descriptin3(self, sender, e):
            if self.radioButton3:
                self.label.Text = ""
                self.label.Text += dyn3
            
        def button_click(self, sender, e):
            if self.checked_radiobutton is not None:
                self.selected_radio_button_text = self.checked_radiobutton.Text
                self.DialogResult = DialogResult.OK

    form = MyForm(doc)
    result = form.ShowDialog()
    if result == DialogResult.OK:
        return form.selected_radio_button_text
    else:
        return None

def Filter(icon_path, search_image_path, ok_icon_path, radio_label, radio_op1, radio_op2, radio_label2, radio_op3, radio_op4, window_name, url):
    """
    Displays a modal form with radio button options and an action button for filtering.

    This function creates a form that allows the user to select between multiple options 
    represented by radio buttons. The form includes images, labels for each option, and 
    a button that becomes enabled when an option is selected. The form can be customized 
    with a title, icons, and images. It also provides dynamic feedback based on the 
    selected options.

    Parameters:
    - icon_path (str): The file path to the icon for the form window.
    - search_image_path (str): The file path to the image displayed in the form.
    - ok_icon_path (str): The file path to the icon for the action button.
    - radio_label (str): The label for the first set of radio buttons.
    - radio_op1 (str): The text for the first radio button option.
    - radio_op2 (str): The text for the second radio button option.
    - radio_label2 (str): The label for the second set of radio buttons.
    - radio_op3 (str): The text for the third radio button option.
    - radio_op4 (str): The text for the fourth radio button option.
    - window_name (str): The title of the form window.
    - url (str): The URL to open when the creator label is clicked.

    Returns:
    - tuple: A tuple containing the selected options (selected_option1, selected_option2) 
             if the user clicks the action button; otherwise, returns (None, None).
    """
    #Initializations
    class InputForm(Form):
        def __init__(self):
            self.Text = window_name
            self.Width = 500
            self.Height = 600
            self.BackColor = Color.White
            self.CenterToScreen()
            self.Icon = Drawing.Icon(icon_path)

            self.pictureBoxSFIPV = PictureBox()
            self.pictureBoxSFIPV.Location = Point(self.Width // 2 - 200, -90)
            self.pictureBoxSFIPV.Size = Size(300,300)
            imageSFIPV = Image.FromFile(search_image_path)
            self.pictureBoxSFIPV.Image = imageSFIPV
            self.pictureBoxSFIPV.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.pictureBoxSFIPV)

            self.label2 = Label()
            self.label2.Text = radio_label
            self.label2.Location = Point(40, 230)
            self.label2.AutoSize = True
            self.label2.Font = Font(self.label2.Font, FontStyle.Bold)
            self.label2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label2)

            self.label2_append = Label()
            self.label2_append.Text = ""
            self.label2_append.Location = Point(100, 230)
            self.label2_append.AutoSize = True
            self.label2_append.Font = Font(self.label2_append.Font, FontStyle.Bold)
            self.label2_append.ForeColor = Color.Red
            self.label2_append.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label2_append)

            self.label3 = Label()
            self.label3.Text = radio_label2
            self.label3.Location = Point(40, 330)
            self.label3.AutoSize = True
            self.label3.Font = Font(self.label3.Font, FontStyle.Bold)
            self.label3.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label3)

            self.label3_append = Label()
            self.label3_append.Text = ""
            self.label3_append.Location = Point(100, 330)
            self.label3_append.AutoSize = True
            self.label3_append.Font = Font(self.label3_append.Font, FontStyle.Bold)
            self.label3_append.ForeColor = Color.Red
            self.label3_append.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.label3_append)

            self.radioButton01 = RadioButton()
            self.radioButton01.Appearance = 0
            self.radioButton01.Text = radio_op1
            self.radioButton01.Width = 150
            self.radioButton01.Height = 30
            self.radioButton01.Left = 40
            self.radioButton01.Top = 255
            self.radioButton01.CheckedChanged += self.RadioChanged1
            self.radioButton01.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton01)

            self.radioButton2 = RadioButton()
            self.radioButton2.Appearance = 0
            self.radioButton2.Text = radio_op2
            self.radioButton2.Width = 150
            self.radioButton2.Height = 30
            self.radioButton2.Left = 40
            self.radioButton2.Top = 280
            self.radioButton2.CheckedChanged += self.RadioChanged1
            self.radioButton2.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton2)

            self.radioButton3 = RadioButton()
            self.radioButton3.Appearance = 0
            self.radioButton3.Text = radio_op3
            self.radioButton3.Width = 150
            self.radioButton3.Height = 30
            self.radioButton3.Left = 40
            self.radioButton3.Top = 355
            self.radioButton3.CheckedChanged += self.RadioChanged2
            self.radioButton3.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton3)
            self.radioButton3.Enabled = False
                
            self.radioButton4 = RadioButton()
            self.radioButton4.Appearance = 0
            self.radioButton4.Text = radio_op4
            self.radioButton4.Width = 150
            self.radioButton4.Height = 30
            self.radioButton4.Left = 40
            self.radioButton4.Top = 380
            self.radioButton4.CheckedChanged += self.RadioChanged2
            self.radioButton4.Anchor = (WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.radioButton4)
            self.radioButton4.Enabled = False

            self.ok_button = Button()
            self.ok_button.DialogResult = DialogResult.OK
            self.ok_button.Location = Point(225, 450)
            self.ok_button.Width = 40
            self.ok_button.Height = 40
            self.ok_button.Image = Icon(ok_icon_path).ToBitmap()
            self.ok_button.Enabled = False
            self.ok_button.Anchor = (WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left)
            self.Controls.Add(self.ok_button)

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
                self.selected_option2 = "C2R1"
                self.label3_append.Text = radio_op3
                self.radioButton3.Enabled = False
                self.radioButton4.Enabled = False
                self.ok_button.Enabled = True
            elif self.radioButton4.Checked:
                self.selected_option2 = "C2R2"
                self.label3_append.Text = radio_op4                
                self.radioButton3.Enabled = False
                self.radioButton4.Enabled = False
                self.ok_button.Enabled = True
    try:
        input_form = InputForm()
        dialog_result = input_form.ShowDialog()
        if dialog_result == DialogResult.OK:
            selected_option1 = input_form.selected_option1
            selected_option2 = input_form.selected_option2
        elif dialog_result == DialogResult.Cancel:
            selected_option1 = None
            selected_option2 = None
            sys.exit()
        
    except StopIteration:
        pass
    except Exception:
        pass
    except SystemExit:
        pass

    return  selected_option1, selected_option2




