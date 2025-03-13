#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MedTime Demo - Demonstration of the MedTime module
-------------------------------------------------
This script demonstrates how to use the MedTime module both standalone
and as an embedded component.
"""

import tkinter as tk
from tkinter import ttk

# Import the MedTime module
try:
    from modules.core.medTime.calculator import MediationTimeCalculator
    from modules.core.medTime.gui import MediationTimeGUI
except ImportError:
    import sys
    sys.path.append("..")  # Üst dizini ekleyerek aramaya yardımcı olur
    from calculator import MediationTimeCalculator
    from gui import MediationTimeGUI

def standalone_demo():
    """Run MedTime as a standalone application"""
    print("Running MedTime as standalone application...")
    app = MediationTimeGUI()
    # No need to run mainloop here as it's handled in the GUI class when standalone=True

def embedded_demo():
    """Demonstrate how to embed MedTime in another application"""
    print("Running MedTime as embedded component...")
    
    # Create the main application window
    root = tk.Tk()
    root.title("MediaCalc - Embedded Demo")
    root.geometry("800x600")
    
    # Create a notebook for tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Create tabs
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    
    notebook.add(tab1, text="Süre Hesaplama")
    notebook.add(tab2, text="Diğer İşlemler")
    
    # Embed MedTime in the first tab
    medtime_gui = MediationTimeGUI(tab1, standalone=False)
    
    # Add some content to the second tab
    ttk.Label(tab2, text="Bu alan diğer modüller için ayrılmıştır.", 
             font=("Arial", 12)).pack(pady=50)
    
    # Run the application
    root.mainloop()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--embedded":
        embedded_demo()
    else:
        standalone_demo()