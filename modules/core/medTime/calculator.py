#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MedTime Calculator - Core calculation functionality
--------------------------------------------------
This module provides the core calculation functionality for mediation timelines.
"""

from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Dict, List, Tuple, Set, Optional


@dataclass
class DisputeType:
    """Data class for storing dispute types and their associated timeframes"""
    name: str
    week_intervals: List[int]


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
            DisputeType("Tarımsal Üretim Sözleşmesinden Kaynaklanan Uyuşmazlıklar", [2, 3]),
        ]
        
        # All possible week values
        self.all_weeks = [2, 3, 4, 6, 8]

    def calculate_dates(self, start_date: datetime) -> Dict[int, datetime]:
        """Calculate target dates based on the given start date
        
        Args:
            start_date: The date from which to start calculations
            
        Returns:
            Dict[int, datetime]: Dictionary mapping week numbers to target dates
        """
        return {
            week: start_date + timedelta(weeks=week)
            for week in self.all_weeks
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