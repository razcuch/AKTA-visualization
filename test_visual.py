import pytest
import pandas as pd
from tkinter import Tk
from AKTA_vizualization import generate_graph
import matplotlib.pyplot as plt

def setup_data():
    test_data = pd.DataFrame({
        'ml1': [0, 50,100,150,200],
        'mAU1': [0,5,10,15,20],
        'ml2': [14.7, 15.7, 17.1,18.1,18.7],
        'fraction': ['5.F.1', '5.F.5', '5.F.10', '5.G.2', '5.G.5']
    })
    return test_data

def test_generate_graph_valid_data():
    """Test the generate_graph function with valid manually inserted data."""
    global data, ml_start_entry, ml_end_entry, fraction_start_entry, fraction_end_entry, fill_color

    data = setup_data()
    fill_color = "#ffcf8d"

    ml_start_entry = lambda: None
    ml_start_entry.get = lambda: "1"

    ml_end_entry = lambda: None
    ml_end_entry.get = lambda: "20"

    fraction_start_entry = lambda: None
    fraction_start_entry.get = lambda: "5.F.1"

    fraction_end_entry = lambda: None
    fraction_end_entry.get = lambda: "5.F.9"

    try:
        generate_graph()
        success = True
    except Exception as e:
        success = False
        print(f"Test failed: {e}")

    assert success, "generate_graph failed with valid manually inserted data"