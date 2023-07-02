from interface import Ui_MainWindow as Interface
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import re
import traceback
import sys
import subprocess
import os
import shutil

class Importer(QMainWindow, Interface):
    def __init__(self):
        super().__init__()

        self.vmf_default_path = "C:\\"
        self.csgo_basefolder = None
        self.vmf_folder = None
        self.addon = None
        self.map_name = None

        self.setupUi(self)
        self.set_tooltips()
        self.set_stylesheets()
        self.get_addon()
        self.get_launch_options()

        self.load_from_cfg()

        self.csgo_button.clicked.connect(self.select_csgo_folder)
        self.vmf_button.clicked.connect(self.select_vmf)
        self.addon_edit.textChanged.connect(self.get_addon)
        self.launch_options_edit.textChanged.connect(self.get_launch_options)
        self.go_button.clicked.connect(self.go)

    def set_stylesheets(self):
        self.csgo_label.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.vmf_label.setStyleSheet("background-color:rgb(255, 0, 0)")

    def set_tooltips(self):
        self.csgo_button.setToolTip('Use "Counter-Strike Global Offensive" folder or any folder inside it.')
        self.vmf_button.setToolTip('Does not need to be in a "maps" folder, one will be created then deleted afterwards if necessary.')
        self.config_checkbox.setToolTip('Auto-selects CSGO folder, auto-selects .VMF folder when you open the dialog, and auto-fills launch options for next time.')

    def select_csgo_folder(self):
        path = QFileDialog.getExistingDirectory(self, "Select a folder:", "C:\\", QFileDialog.ShowDirsOnly)
        if not path:
            return
        
        path = re.split("(/Counter-Strike Global Offensive/)", path)
        path.append("") # to add a second element incase there isnt one, occurs if selected base folder not a subfolder i.e. csgo/cfg
        
        path = path[0] + path[1]
        self.set_csgo_folder(path)

    def set_csgo_folder(self, path):
        self.csgo_basefolder = path
        self.csgo_label.setText(path)
        self.csgo_label.setStyleSheet("background-color:rgb(0, 255, 0)")

    def select_vmf(self):
        path = QFileDialog.getOpenFileName(self, "Select a VMF", self.vmf_default_path, "VMF files (*.vmf)")[0]
        if not path:
            return
        
        temp = path.split("/")
        self.map_name = temp.pop().split(".vmf")[0]
        self.vmf_folder = "/".join(temp) + "/"

        if self.vmf_folder.endswith("/maps/"):
            self.vmf_folder = "/".join(self.vmf_folder.split("/")[:-2])
        else:
            maps_dir = f"{self.vmf_folder}/maps/"
            os.mkdir(maps_dir)
            copy_from = self.vmf_folder + self.map_name + ".vmf"
            shutil.copy(copy_from, maps_dir)


        self.vmf_label.setText(path)
        self.vmf_label.setStyleSheet("background-color:rgb(0, 255, 0)")

    def get_addon(self):
        self.addon = self.addon_edit.text()

    def get_launch_options(self):
        self.launch_options = self.launch_options_edit.text()

    def set_launch_options(self, text):
        self.launch_options_edit.setText(text)

    def save_to_cfg(self): 
        temp = f"""{self.launch_options}
{self.csgo_basefolder}
{self.vmf_folder}"""
        
        with open("cs2importer.cfg", "w") as f:
            f.write(temp)

    def load_from_cfg(self):
        with open("cs2importer.cfg", "r") as f:
            temp = f.readlines()
            print(temp)
            if not temp:
                return

        self.set_launch_options(temp[0].strip())
        self.set_csgo_folder(temp[1].strip())
        self.vmf_default_path = temp[2].strip()

    def go(self):
        try:
            if bool(self.config_checkbox.checkState()):
                self.save_to_cfg()

            cd = self.csgo_basefolder + '/game/csgo/import_scripts'
            command = "python import_map_community.py "
            command += '"' + self.csgo_basefolder + '/csgo/' + '" '
            command += '"' + self.vmf_folder + '" '
            command += '"' + self.csgo_basefolder + '/game/csgo' + '" '
            command += '"' + self.addon + '" '
            command += '"' + self.map_name + '" '
            command += self.launch_options

            print(command)
            subprocess.Popen(command, cwd=cd)

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Error", str(traceback.format_exc()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    imp = Importer()
    imp.show()
    sys.exit(app.exec_())