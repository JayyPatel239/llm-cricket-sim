"""
Test script to verify the cricket simulation environment setup.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

def main():
    """Test function to verify all imports are working."""
    print("Environment setup testing...")
    
    # Create a simple DataFrame
    data = pd.DataFrame({
        'Batsman': ['Kohli', 'Rohit', 'Smith', 'Williamson', 'Root'],
        'Runs': [74, 83, 92, 67, 89],
        'Strike_Rate': [125.4, 148.2, 110.8, 105.6, 115.3]
    })
    
    print("\nSample Cricket Data:")
    print(data)
    
    # Use NumPy for calculations
    print("\nAverage runs:", np.mean(data['Runs']))
    
    print("\nAll packages imported successfully!")
    print("Cricket simulation environment is ready!")

if __name__ == "__main__":
    main()
