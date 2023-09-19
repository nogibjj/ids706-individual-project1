import pandas as pd
import matplotlib.pyplot as plt

def generate_data(file_path):
    """
    Read dataset from the provided file path. Supports both CSV and Excel files.
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

def describe_with_pandas(df):
    return df.describe()

def generate_scatter_plot(df, x_col, y_col):
    """
    Generate scatter plot for the specified columns.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col], color='blue', alpha=0.5)
    plt.title(f'Scatter plot of {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.tight_layout()
    # Save the scatter plot as an image
    plt.savefig('scatter_plot.png')
    plt.show()