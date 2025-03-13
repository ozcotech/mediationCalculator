#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MedTime GUI - User interface for timeline calculations
-----------------------------------------------------
This module provides the graphical user interface for mediation timeline calculations.
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from typing import Optional, Dict, Any

from .calculator import MediationTimeCalculator


class MediationTimeGUI:
    """GUI class for mediation timeline calculations"""
    
    def __init__(self, master=None, standalone=True):
        """Initialize GUI components
        
        Args:
            master: Parent window if embedded in another application
            standalone: Whether this GUI should run as a standalone application
        """
        self.calculator = MediationTimeCalculator()
        self.master = master or tk.Tk()
        
        if standalone:
            self.master.title("Arabuluculuk Süre Hesaplama")
            self.master.geometry("1500x500") 
        
        # Main frame
        self.frame = ttk.Frame(self.master, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Date input field and calculate button
        self.date_frame = ttk.Frame(self.frame)
        self.date_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(self.date_frame, text="Başlangıç Tarihi (GG.AA.YYYY):").pack(side=tk.LEFT, padx=5)
        self.date_entry = ttk.Entry(self.date_frame, width=10)
        self.date_entry.pack(side=tk.LEFT, padx=5)
        self.date_entry.insert(0, datetime.now().strftime("%d.%m.%Y"))
        
        ttk.Button(self.date_frame, text="Hesapla", command=self.calculate).pack(side=tk.LEFT, padx=5)
        
        # Results table
        self.table_frame = ttk.Frame(self.frame)
        self.table_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Table headers
        dispute_types = self.calculator.get_dispute_types()
        all_weeks = self.calculator.get_all_weeks()
        week_columns = [f"{week}_week" for week in all_weeks]
        
        self.table = ttk.Treeview(self.table_frame, columns=week_columns, 
                           show="tree headings", height=len(dispute_types))
        
        # Column headers
        for week in all_weeks:
            self.table.heading(f"{week}_week", text=f"{week}. Hafta")
            self.table.column(f"{week}_week", width=30, minwidth=30, anchor=tk.CENTER)
            # Add heading for the first column (Dispute Type)
            self.table.heading("#0", text="Uyuşmazlık Konusu")
            self.table.column("#0", width=300, minwidth=150)
        
        # Scrollbars
        scrollbar_y = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar_y.set)
        
        # Place the table
        self.table_frame.pack_propagate(False) # Prevent resizing
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Calculate automatically on startup
        self.calculate()
        
        if standalone:
            try:
                self.master.mainloop()
            except Exception as e:
                print(f"GUI error: {e}")
            
    def get_frame(self) -> ttk.Frame:
        """Get the main frame for external applications
        
        Returns:
            ttk.Frame: The main frame of this GUI
        """
        return self.frame
            
    def calculate(self) -> None:
        """Get date from the interface, calculate timelines and update the table"""
        # Clear the table
        for item in self.table.get_children():
            self.table.delete(item)
            
        try:
            # Parse input date
            date_str = self.date_entry.get()
            start_date = datetime.strptime(date_str, "%d.%m.%Y")
            
            # Calculate dates
            target_dates = self.calculator.calculate_dates(start_date)
            
            # Fill the table
            for dispute in self.calculator.get_dispute_types():
                # Prepare row values (for all week values)
                row_values = {}
                for week in self.calculator.get_all_weeks():
                    if week in dispute.week_intervals:
                        row_values[f"{week}_week"] = target_dates[week].strftime("%d.%m.%Y")
                    else:
                        row_values[f"{week}_week"] = "-"
                
                # Add row to the table
                self.table.insert("", tk.END, text=dispute.name, values=[
                    row_values[f"{week}_week"] for week in self.calculator.get_all_weeks()
                ])
                
        except ValueError:
            # Show error message for invalid date format
            for dispute in self.calculator.get_dispute_types():
                self.table.insert("", tk.END, text=dispute.name, 
                                  values=["Hatalı tarih"] * len(self.calculator.get_all_weeks()))
                                  

# Standalone execution
if __name__ == "__main__":
    MediationTimeGUI()