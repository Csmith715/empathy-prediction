import streamlit as st
import openpyxl
import pandas as pd
from io import BytesIO
from base64 import b64encode
from openpyxl.styles import Font, PatternFill
from openpyxl.styles.colors import Color

def main():
    st.title("Excel File Converter")
    # Create a button for file upload
    uploaded_file = st.file_uploader("Upload Excel file", type=["xls", "xlsx"])
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file, sheet_name='Client Summary', usecols='E', header=None)
            rows_to_delete = [i for i, x in enumerate(df[4][:56], start=1) if x == 0]
            table1_delete_count = len([r for r in rows_to_delete if r < 28])
            table2_delete_count = len([r for r in rows_to_delete if 31 < r < 54])
            table3_delete_count = len([r for r in rows_to_delete if 57 < r < 66])
            table1_equation_val = 27 - table1_delete_count
            table1_eq1 = f'=SUM(E13:E{table1_equation_val})'
            table1_eq2 = f'=SUM(F13:F{table1_equation_val})'

            table2_start_val = 32 - table1_delete_count
            table2_equation_val = 53 - table1_delete_count - table2_delete_count
            table2_eq1 = f'=SUM(E{table2_start_val}:E{table2_equation_val})'
            table2_eq2 = f'=SUM(F{table2_start_val}:F{table2_equation_val})'

            table3_start_val = 58 - table1_delete_count - table2_delete_count
            table3_equation_val = 65 - table1_delete_count - table2_delete_count - table3_delete_count
            # table3_eq1 = f'=SUM(E{table3_start_val}:E{table3_equation_val})'
            workbook = openpyxl.load_workbook(uploaded_file)

            # Get the worksheet you want to delete rows from
            worksheet = workbook['Client Summary']

            for row_index in reversed(rows_to_delete):
                worksheet.delete_rows(row_index)

            # Modify Excel Formulas to account for deleted cells
            worksheet[f'E{table1_equation_val + 1}'] = table1_eq1
            worksheet[f'F{table1_equation_val + 1}'] = table1_eq2
            worksheet[f'E{table2_equation_val + 1}'] = table2_eq1
            worksheet[f'F{table2_equation_val + 1}'] = table2_eq2
            # worksheet[f'E{table3_equation_val + 1}'] = table3_eq1

            copy_row_format(10, table1_equation_val + 2, worksheet)
            # copy_row_format(11, table1_equation_val + 2, worksheet)
            # copy_row_format(12, table1_equation_val + 3, worksheet)
            copy_row_format(10, table2_equation_val + 2, worksheet)
            copy_row_format(10, table3_equation_val + 2, worksheet)
            # copy_row_format(11, table2_equation_val + 2, worksheet)
            # copy_row_format(12, table2_equation_val + 3, worksheet)
            # Save the modified workbook to a BytesIO object
            output = BytesIO()
            workbook.save(output)
            xlsx_data = output.getvalue()
            output.seek(0)

            # Generate download link
            href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64encode(xlsx_data).decode()}" download="Modified.xlsx">Download Excel File</a>'
            st.markdown(href, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")

def copy_row_format(source_row, target_row, ws):
    source_row_height = ws.row_dimensions[source_row].height
    ws.row_dimensions[target_row].height = source_row_height


if __name__ == "__main__":
    main()
