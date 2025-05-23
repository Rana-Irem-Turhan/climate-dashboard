from dash import Dash

app = Dash(__name__)

from .final_dashboard_with_ui_upgrade import *  # Import the main app code

# The app is initialized and can be run from the main file.