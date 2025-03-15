#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MedTime GUI - User interface for timeline calculations
-----------------------------------------------------
This module provides the graphical user interface for mediation timeline calculations.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.lang import Builder

from datetime import datetime
from pathlib import Path  # Import pathlib for modern path handling
from typing import Optional, Dict

from .calculator import MediationTimeCalculator

# Import necessary classes for drawing
from kivy.graphics import Color, Rectangle, Line


def add_border_to_widget(widget, color=(1, 1, 1, 1), line_width=1.5):
    """Add a white border to any widget"""
    # Function to ensure border is redrawn when widget changes
    def update_border(*args):
        widget.canvas.after.clear()
        with widget.canvas.after:
            Color(*color)
            Line(rectangle=(widget.x, widget.y, widget.width, widget.height), width=line_width)

    widget.bind(pos=update_border, size=update_border)
    update_border()
    return widget


# Load the KV file at module level using pathlib
try:
    kv_path = Path(__file__).parent / 'mediationtime.kv'
    Builder.load_file(str(kv_path))  # Convert Path to string for Kivy compatibility
except Exception as e:
    print(f"Error loading KV file: {e}")


class MediationTimeGUI(BoxLayout):
    """GUI class for mediation timeline calculations"""
    
    def __init__(self, **kwargs):
        """Initialize GUI components"""
        # Initialize parent class first using the old-style call which is more reliable
        BoxLayout.__init__(self, **kwargs)
        
        # Initialize calculator
        self.calculator = MediationTimeCalculator()
        
        # Initialize other attributes
        self.table_layout = None
        self.data_cells = {}
        self.target_dates = None
        self.table_initialized = False
        
        # Setup table with a delay to ensure widgets are ready
        Clock.schedule_once(self._setup_table, 0.1)
        
        # Set the date entry to today's date immediately
        Clock.schedule_once(self._set_today_date, 0.1)
        
        # Perform an initial calculation on startup
        Clock.schedule_once(self.calculate, 0.3)
        
    def _setup_table(self, dt):
        """Setup the table layout after the widget tree is constructed"""
        self.table_layout = self.ids.table_layout

        # Ensure the table layout is only created once
        if self.table_initialized:
            return

        self.table_layout.clear_widgets()
        self.table_layout.cols = len(self.calculator.get_all_weeks()) + 1  

        # Add table headers
        header_dispute = Label(
            text="Dispute Subject", 
            size_hint_x=None, width=dp(400),  
            size_hint_y=None, height=dp(40),
            bold=True, halign='left',
            valign='middle',
            text_size=(dp(390), dp(40)),  
            color=[0, 0, 0.6, 1]
        )
        add_border_to_widget(header_dispute)
        self.table_layout.add_widget(header_dispute)

        # Add week headers
        self.week_headers = []
        for week in self.calculator.get_all_weeks():
            header_week = Label(
                text=f"Week {week}", 
                size_hint_x=None, width=dp(100),
                size_hint_y=None, height=dp(40),
                bold=True,
                color=[0, 0, 0.6, 1]
            )
            add_border_to_widget(header_week)
            self.table_layout.add_widget(header_week)
            self.week_headers.append(header_week)

        # Store cell references for direct updates
        self.data_cells = {}

        for dispute in self.calculator.get_dispute_types():
            dispute_label = Label(
                text=dispute.name, 
                size_hint_x=None, width=dp(400),
                size_hint_y=None, height=dp(40),
                halign='left',
                valign='middle',
                text_size=(dp(390), dp(40)),
                padding_x=dp(10),
                color=[0, 0, 0.6, 1]
            )
            add_border_to_widget(dispute_label)
            self.table_layout.add_widget(dispute_label)

            for week in self.calculator.get_all_weeks():
                cell_label = Label(
                    text="-",
                    size_hint_x=None, width=dp(100),
                    size_hint_y=None, height=dp(40),
                    halign='center',
                    valign='middle',
                    color=[0.5, 0.5, 0.5, 1]
                )
                add_border_to_widget(cell_label)
                self.table_layout.add_widget(cell_label)

                # Store cell reference using (dispute_name, week) as key
                self.data_cells[(dispute.name, week)] = cell_label

        # Ensure dates update properly
        self.table_initialized = True
        Clock.schedule_once(lambda dt: self.update_table_dates(), 0.3)

    def update_table_dates(self, dt=None):
        """Update only date values in existing table cells, clearing previous error messages."""
        if not self.target_dates:
            return
        
        for (dispute_name, week), cell_label in self.data_cells.items():
            # Check if this cell should show a calculation based on dispute type and week
            should_calculate = self.calculator.should_calculate(dispute_name, week)
            
            if should_calculate and week in self.target_dates:
                # This is a cell that should be calculated
                cell_label.text = self.target_dates[week].strftime("%d.%m.%Y")
                cell_label.color = [0, 0.5, 0, 1]  # Dark green text color
            else:
                # This is a cell that should not be calculated
                cell_label.text = "-"  # Show dash for non-calculated cells
                cell_label.color = [0.5, 0.5, 0.5, 1]  # Gray color (non-calculated)

    def update_error_message(self, error_msg="Invalid date"):
        """Update table cells with error message"""
        if not self.data_cells:
            return
            
        for (dispute_name, week), cell_label in self.data_cells.items():
            # Only show error in cells that should be calculated
            if self.calculator.should_calculate(dispute_name, week):
                cell_label.text = error_msg
                cell_label.color = [0.8, 0, 0, 1]  # Red text color for errors
            else:
                cell_label.text = "-"  # Non-calculated cells still show dash
                cell_label.color = [0.5, 0.5, 0.5, 1]  # Gray color

    def _set_today_date(self, dt):
        """Set today's date in the date entry field"""
        if hasattr(self, 'ids') and 'date_entry' in self.ids:
            self.ids.date_entry.text = datetime.now().strftime("%d.%m.%Y")

    def format_date_input(self, date_str):
        """Format date input to handle different formats"""
        # Check if string is empty
        if not date_str or date_str.strip() == "":
            # Return today's date as default
            return datetime.now().strftime("%d.%m.%Y")
            
        # Remove any non-digit characters
        digits_only = ''.join(filter(str.isdigit, date_str))
        
        # If we have 8 digits (DDMMYYYY), format it properly
        if len(digits_only) == 8:
            return f"{digits_only[:2]}.{digits_only[2:4]}.{digits_only[4:]}"
        
        return date_str
    
    def calculate(self, instance=None):
        """Calculate mediation dates and update the table dynamically"""
        try:
            date_str = self.ids.date_entry.text.strip()

            # If date is empty, use today's date
            if not date_str:
                date_str = datetime.now().strftime("%d.%m.%Y")

            formatted_date = self.format_date_input(date_str)
            self.ids.date_entry.text = formatted_date

            # Parse input date
            start_date = datetime.strptime(formatted_date, "%d.%m.%Y")

            # Calculate dates and store in `self.target_dates`
            self.target_dates = self.calculator.calculate_dates(start_date)

            # Only update date values instead of recreating the entire table
            self.update_table_dates()

        except ValueError as e:
            print(f"Date conversion error: {e}")
            # Show error message for invalid date format in existing cells
            self.update_error_message("Invalid date")

        except Exception as e:
            print(f"General error: {e}")
            # Show general error message in existing cells
            self.update_error_message(f"Error: {str(e)[:10]}")


class MediationTimeApp(App):
    """Standalone application class for the Mediation Time Calculator"""
    
    def build(self):
        """Build the application"""
        Window.size = (1200, 600)
        Window.clearcolor = (0, 0, 0, 0)  # Completely transparent background
        return MediationTimeGUI()


# Standalone execution
if __name__ == "__main__":
    MediationTimeApp().run()