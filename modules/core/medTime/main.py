#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MedTime - Kivy Application Main File
------------------------------------
This file is used to launch the Kivy application.
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
import sys

# UI scaling and window settings
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '600')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')  # Optimize mouse usage

# Settings for light blue background
Window.clearcolor = (0.8, 0.9, 1, 1)  # Light blue background

# Import the MedTime module
try:
    from modules.core.medTime.gui import MediationTimeGUI
except ImportError as e:
    print("\nError loading MedTime modules!")
    print(f"Reason: {e}")
    print("Make sure you are running the script from the correct directory.")
    print("Try running: `python3 -m modules.core.medTime.main`\n")
    sys.exit(1)  # Terminate the program safely

class MediationTimeApp(App):
    """Standalone application class for Mediation Time Calculator"""

    def build(self):
        """Build the application"""
        return MediationTimeGUI()

    def get_current_date(self):
        """Returns today's date in DD.MM.YYYY format for KV file"""
        from datetime import datetime
        return datetime.today().strftime("%d.%m.%Y")

if __name__ == "__main__":
    print("\n🚀 Starting MediationTimeApp... 🚀")
    try:
        MediationTimeApp().run()
    except Exception as e:
        print(f"\n⚠️ Unexpected Error: {e}")
        print("The application encountered an issue and needs to close.\n")
    finally:
        print("\nMediationTimeApp has exited.")