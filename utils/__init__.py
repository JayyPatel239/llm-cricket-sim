"""
Utility functions for cricket simulation.

This module contains helper functions used across the project.
"""

import random
import numpy as np


def weighted_choice(options, weights):
    """
    Select an option based on weights.
    
    Args:
        options (list): List of options to choose from
        weights (list): Corresponding weights for each option
        
    Returns:
        Selected option
    """
    return random.choices(options, weights=weights, k=1)[0]


def calculate_run_rate(runs, overs):
    """
    Calculate the run rate.
    
    Args:
        runs (int): Total runs scored
        overs (float): Overs completed
        
    Returns:
        float: Run rate
    """
    if overs == 0:
        return 0.0
    return runs / overs


def calculate_required_rate(target, current_score, total_overs, overs_completed):
    """
    Calculate required run rate.
    
    Args:
        target (int): Target score
        current_score (int): Current score
        total_overs (float): Total overs in the innings
        overs_completed (float): Overs completed
        
    Returns:
        float: Required run rate
    """
    runs_required = target - current_score
    overs_remaining = total_overs - overs_completed
    
    if overs_remaining <= 0:
        return float('inf')
    
    return runs_required / overs_remaining


def over_to_balls(overs):
    """
    Convert overs to balls.
    
    Args:
        overs (float): Number of overs
        
    Returns:
        int: Number of balls
    """
    full_overs = int(overs)
    partial_over = overs - full_overs
    balls = full_overs * 6 + int(partial_over * 10)
    return balls
