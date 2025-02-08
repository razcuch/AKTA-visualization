import pytest
import pandas as pd
import os
from qPCR_data_analysis_with_errorbars import qPCRApp  

def setup_qpcr_analysis(tmp_path):
    """Setup qPCRApp with test parameters and process data."""
    excel_path = "qPCR_results.xls"
    output_path = tmp_path / "test_output"
    skiplines = 47
    config_path = "config_file.yaml"
    show_plot = False

    # Create qPCRApp instance
    app = qPCRApp(None, excel_path, str(output_path), skiplines, gui=False, show_plot=show_plot)

    # Process data using config file
    app.process_from_config(config_path)

    return output_path

def test_output_files_created(setup_qpcr_analysis):
    """Test if expected output files are generated."""
    table_path = str(setup_qpcr_analysis) + "_table.csv"
    plot_path = str(setup_qpcr_analysis) + ".jpg"

    assert os.path.exists(table_path), "Output table file was not created"
    assert os.path.exists(plot_path), "Plot file was not created"

    df = pd.read_csv(table_path)
    assert df.shape[0] > 0, "Output table is empty"

def test_expected_columns_exist(setup_qpcr_analysis):
    """Test if the expected columns exist in the output table."""
    table_path = str(setup_qpcr_analysis) + "_table.csv"
    df = pd.read_csv(table_path)

    expected_columns = ['Treatment', 'Sample', 'Target Gene', 'Cq Reference Gene', 'Cq Target', 
                        '∆Cq', '∆Cq Expression', 'Mean ∆Cq Expression', '∆Cq Expression stdev', 
                        '∆∆Cq Expression', '∆∆Cq Expression stdev', '% KD']
    
    missing_columns = [col for col in expected_columns if col not in df.columns]
    assert not missing_columns, f"Missing columns: {missing_columns}"

def test_calculations_correctness(setup_qpcr_analysis):
    """Test if calculations such as ∆Cq, ∆Cq Expression, ∆∆Cq Expression, and % KD are correct."""
    table_path = str(setup_qpcr_analysis) + "_table.csv"
    df = pd.read_csv(table_path)

    sample_row = df.iloc[0]
    delta_cq = sample_row['Cq Target'] - sample_row['Cq Reference Gene']
    assert abs(sample_row['∆Cq'] - delta_cq) < 1e-6, "∆Cq calculation is incorrect"

    delta_cq_expression = 2 ** (-delta_cq)
    assert abs(sample_row['∆Cq Expression'] - delta_cq_expression) < 1e-6, "∆Cq Expression calculation is incorrect"

    control_expression = df[df['Treatment'] == 'Control']['Mean ∆Cq Expression'].values[0]
    delta_delta_cq_expression = sample_row['Mean ∆Cq Expression'] / control_expression
    assert abs(sample_row['∆∆Cq Expression'] - delta_delta_cq_expression) < 1e-6, "∆∆Cq Expression calculation is incorrect"

    kd_percentage = (1 - delta_delta_cq_expression) * 100
    assert abs(sample_row['% KD'] - kd_percentage) < 1e-6, "% KD calculation is incorrect"