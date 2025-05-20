"""
UI module for cricket simulation.

This module handles the user interface components for
displaying match progress, statistics, and interactive elements.
"""

import streamlit as st

class Dashboard:
    """Main dashboard for cricket simulation UI."""
    
    def __init__(self):
        self.title = "Cricket Simulator"
    
    def initialize(self):
        """Set up the initial UI structure."""
        st.set_page_config(
            page_title=self.title,
            page_icon="🏏",
            layout="wide"
        )
        st.title(self.title)
    
    def display_match_summary(self, match_data):
        """Display current match summary."""
        st.header("Match Summary")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(match_data.get("team1_name", "Team 1"))
            st.metric("Score", match_data.get("team1_score", "0/0"))
            
        with col2:
            st.subheader(match_data.get("team2_name", "Team 2"))
            st.metric("Score", match_data.get("team2_score", "0/0"))
    
    def display_commentary(self, commentary_list):
        """Display recent commentary."""
        st.header("Commentary")
        for comment in commentary_list:
            st.text(comment)
    
    def display_scorecard(self, batting_data, bowling_data):
        """Display detailed scorecard."""
        pass


def run_dashboard(match_simulator):
    """Run the Streamlit dashboard with a match simulator."""
    dashboard = Dashboard()
    dashboard.initialize()
    
    # Main app logic would go here, updating the UI based on match state
    
    # Example usage:
    # match_data = match_simulator.get_current_state()
    # dashboard.display_match_summary(match_data)
    # dashboard.display_commentary(match_simulator.get_recent_commentary())
    
    st.sidebar.button("Start New Match")
