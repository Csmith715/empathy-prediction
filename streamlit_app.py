import streamlit as st
import pandas as pd

def main():
    st.title("Excel File to Pandas DataFrame Converter")

    # Create a button for file upload
    uploaded_file = st.file_uploader("Upload Excel file", type=["xls", "xlsx"])

    if uploaded_file is not None:
        try:
            # Load the Excel file into a Pandas DataFrame
            df = pd.read_excel(uploaded_file, sheet_name='Client Summary')
            st.success("File uploaded successfully. DataFrame created.")

            # Display the DataFrame
            st.write(df)

            # Optionally, you can provide a button to download the DataFrame as a CSV
            st.markdown(get_csv_download_link(df), unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")

def get_csv_download_link(df):
    """Generates a link allowing the DataFrame to be downloaded as a CSV file."""
    csv = df.to_csv(index=False)
    href = f'<a href="data:file/csv;base64,{csv}" download="data.csv">Download CSV File</a>'
    return href

if __name__ == "__main__":
    main()
