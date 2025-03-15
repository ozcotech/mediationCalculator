#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MedTime Calculator - Core calculation functionality
--------------------------------------------------
This module provides the core calculation functionality for mediation timelines.
"""

from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Set


@dataclass
class DisputeType:
    """Data class for storing dispute types and their associated timeframes"""
    name: str
    week_intervals: List[int]  # These are the only weeks that should be calculated for this dispute type


class MediationTimeCalculator:
    """Main class for calculating mediation timelines"""
    
    def __init__(self):
        """Initialize dispute types and time information"""
        self.dispute_types = [
            DisputeType("İş Hukuku Uyuşmazlıkları", [3, 4]),
            DisputeType("Ticaret Hukuku Uyuşmazlıkları", [6, 8]),
            DisputeType("Tüketici Hukuku Uyuşmazlıkları", [3, 4]),
            DisputeType("Kira İlişkisinden Kaynaklanan Uyuşmazlıklar", [3, 4]),
            DisputeType("Ortaklığın Giderilmesine İlişkin Uyuşmazlıklar", [3, 4]),
            DisputeType("Kat Mülkiyeti Kanunundan Kaynaklanan Uyuşmazlıklar", [3, 4]),
            DisputeType("Komşu Hukukundan Kaynaklanan Uyuşmazlıklar", [3, 4]),
            DisputeType("Tarımsal Üretim Sözleşmesinden Kaynaklanan Uyuşmazlıklar", [2, 3, 4]),
        ]
        
        # Automatically determine all unique week values across all dispute types
        self.all_weeks = sorted(set(week for dispute in self.dispute_types for week in dispute.week_intervals))

    def calculate_dates(self, start_date: Optional[datetime] = None) -> Dict[int, datetime]:
        """Calculate target dates based on the given start date for all possible weeks

        Args:
            start_date: The date from which to start calculations (defaults to today if None)
        
        Returns:
            Dict[int, datetime]: Dictionary mapping week numbers to target dates
        """
        # Use today's date if start_date is not provided
        start_date = datetime.today() if start_date is None else start_date

        # Convert start_date from string to datetime if needed
        if isinstance(start_date, str):
            try:
                start_date = datetime.strptime(start_date, "%d.%m.%Y")
            except ValueError:
                raise ValueError("Invalid date format. Expected format: DD.MM.YYYY")

        # Calculate dates for all weeks
        return {
            week: start_date + timedelta(weeks=week)
            for week in self.all_weeks if isinstance(week, int) and week > 0
        }
    
    def get_dispute_types(self) -> List[DisputeType]:
        """Return the list of dispute types
        
        Returns:
            List[DisputeType]: List of all dispute types
        """
        return self.dispute_types
    
    def get_all_weeks(self) -> List[int]:
        """Return all possible week values
        
        Returns:
            List[int]: List of all week values used in calculations
        """
        return self.all_weeks
        
    def should_calculate(self, dispute_name: str, week: int) -> bool:
        """Determine if a specific week should be calculated for a dispute type
        
        Args:
            dispute_name: The name of the dispute type
            week: The week number to check
            
        Returns:
            bool: True if the week should be calculated for this dispute, False otherwise
        """
        for dispute in self.dispute_types:
            if dispute.name == dispute_name and week in dispute.week_intervals:
                return True
        return False