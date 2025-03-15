#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MedTime Demo - Demonstration of the MedTime module
-------------------------------------------------
This script demonstrates how to use the MedTime module both standalone
and as an embedded component.
"""

import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.window import Window

# Import the MedTime module
try:
    from modules.core.medTime.calculator import MediationTimeCalculator
    from modules.core.medTime.gui import MediationTimeGUI
except ImportError as e:
    print("\nError loading MedTime modules!")
    print(f"Reason: {e}")
    print("Make sure you are running the script from the correct directory.")
    print("Try running: `python3 -m modules.core.medTime.demo`\n")
    sys.exit(1)  # Terminate safely

def standalone_demo():
    """Run MedTime as a standalone application"""
    print("\n🚀 Running MedTime as standalone application... 🚀")
    
    class StandaloneApp(App):
        def build(self):
            Window.size = (1200, 600)
            Window.clearcolor = (0.8, 0.9, 1, 1)  # Light blue background
            return MediationTimeGUI()
    
    try:
        StandaloneApp().run()
    except Exception as e:
        print(f"\n⚠️ Unexpected Error: {e}")
        print("The application encountered an issue and needs to close.\n")
    finally:
        print("\nMediationTimeApp has exited.")

def embedded_demo():
    """Demonstrate how to embed MedTime in another application"""
    print("\n🖥️ Running MedTime as an embedded component... 🖥️")
    
    class EmbeddedApp(App):
        def build(self):
            Window.size = (1200, 600)
            Window.clearcolor = (0.8, 0.9, 1, 1)  # Light blue background
            
            main_layout = BoxLayout(orientation='vertical')
            tab_panel = TabbedPanel(do_default_tab=False, size_hint=(1, 1))
            
            # Create the first tab with MedTime
            tab1 = TabbedPanelItem(text='Duration Calculation')
            medtime_gui = MediationTimeGUI()  
            tab1.add_widget(medtime_gui)
            tab_panel.add_widget(tab1)
            
            # Create the second tab
            tab2 = TabbedPanelItem(text='Other Operations')
            other_layout = BoxLayout(orientation='vertical', padding=[20])
            other_label = Label(text="This area is reserved for other modules.", font_size=20)
            other_layout.add_widget(other_label)
            tab2.add_widget(other_layout)
            tab_panel.add_widget(tab2)
            
            main_layout.add_widget(tab_panel)
            return main_layout
    
    try:
        EmbeddedApp().run()
    except Exception as e:
        print(f"\n⚠️ Unexpected Error: {e}")
        print("The application encountered an issue and needs to close.\n")
    finally:
        print("\nEmbedded MediationTimeApp has exited.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--embedded":
        embedded_demo()
    else:
        standalone_demo()