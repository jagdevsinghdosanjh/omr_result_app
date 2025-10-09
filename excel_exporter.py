# Exports results to Excel
import pandas as pd

def export_to_excel(results, filename="class_results.xlsx"):
    df = pd.DataFrame(results)
    df.to_excel(filename, index=False)
