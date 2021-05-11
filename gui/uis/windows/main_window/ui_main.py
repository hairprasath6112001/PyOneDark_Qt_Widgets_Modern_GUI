# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import sys

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# IMPORT SETUP MAIN WINDOW
# ///////////////////////////////////////////////////////////////
from . setup_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # SET INITIAL PARAMETERS
        parent.setMinimumSize(self.settings["startup_size"][0], self.settings["startup_size"][1])

        # SET CENTRAL WIDGET
        # Add central widget to app
        # ///////////////////////////////////////////////////////////////
        self.central_widget = QWidget()
        self.central_widget_layout = QVBoxLayout(self.central_widget)
        if self.settings["custom_title_bar"]:
            self.central_widget_layout.setContentsMargins(10,10,10,10)
        else:
            self.central_widget_layout.setContentsMargins(0,0,0,0)
        
        # LOAD PY WINDOW CUSTOM WIDGET
        # Add inside PyWindow "layout" all Widgets
        # ///////////////////////////////////////////////////////////////
        self.window = PyWindow(
            parent,
            bg_color = self.themes["app_color"]["bg_one"],
            border_color = self.themes["app_color"]["bg_two"],
            text_color = self.themes["app_color"]["text_foreground"]
        )
        
        # If disable custom title bar
        if not self.settings["custom_title_bar"]:
            self.window.set_stylesheet(border_radius = 0, border_size = 0)
        
        # ADD PY WINDOW TO CENTRAL WIDGET
        self.central_widget_layout.addWidget(self.window)

        # ADD FRAME LEFT MENU
        # Add here the custom left menu bar
        # ///////////////////////////////////////////////////////////////
        self.left_menu_frame = QFrame()
        self.left_menu_frame.setMaximumSize(50, 17280)
        self.left_menu_frame.setMinimumSize(self.settings["menu_size"]["minimum"], 0)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QHBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setContentsMargins(0,0,0,0)

        # ADD LEFT MENU
        # Add custom left menu here
        # ///////////////////////////////////////////////////////////////
        self.left_menu = PyLeftMenu(
            parent = self.left_menu_frame,
            dark_one = self.themes["app_color"]["dark_one"]
        )
        self.left_menu_layout.addWidget(self.left_menu)
        print(self.themes["app_color"]["dark_one"])

        # ADD RIGHT WIDGETS
        # Add here the right widgets
        # ///////////////////////////////////////////////////////////////
        self.right_app_frame = QFrame()

        # ADD RIGHT APP LAYOUT
        self.right_app_layout = QVBoxLayout(self.right_app_frame)
        self.right_app_layout.setContentsMargins(0,0,0,0)
        self.right_app_layout.setSpacing(6)

        # ADD TITLE BAR FRAME
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setMaximumHeight(40)
        self.title_bar_frame.setMaximumHeight(40)
        self.title_bar_frame.setStyleSheet("background: #f00")

        # ADD CONTENT AREA
        self.content_area_frame = QFrame()
        self.content_area_frame.setStyleSheet("background: transparent")

        # CREDITS / BOTTOM APP FRAME
        self.credits_frame = QFrame()
        self.credits_frame.setMaximumHeight(26)
        self.credits_frame.setMaximumHeight(26)
        self.credits_frame.setStyleSheet("background: transparent")

        # ADD WIDGETS TO RIGHT LAYOUT
        self.right_app_layout.addWidget(self.title_bar_frame)
        self.right_app_layout.addWidget(self.content_area_frame)
        self.right_app_layout.addWidget(self.credits_frame)
        
        # ADD WIDGETS TO "PyWindow"
        # Add here your custom widgets or default widgets
        # ///////////////////////////////////////////////////////////////
        self.window.layout.addWidget(self.left_menu_frame)
        self.window.layout.addWidget(self.right_app_frame)

        # ADD CENTRAL WIDGET AND SET CONTENT MARGINS
        # ///////////////////////////////////////////////////////////////
        parent.setCentralWidget(self.central_widget)