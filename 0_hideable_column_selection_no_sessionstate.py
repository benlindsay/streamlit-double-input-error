import pandas as pd
import streamlit as st

st.info(
    "## Instructions:\n"
    + "1. Upload simple csv (like `data.csv` from this repo)\n"
    + "2. Check the box to choose column names\n"
    + "3. Change the column names selection and see the dataframe update in response\n"
    + "4. Uncheck the box to exit column name selection and see the dataframe go back to its previous state\n"
)

csv_file = st.file_uploader("File", type="csv")

if csv_file is not None:
    dataframe = pd.read_csv(csv_file)
    all_columns = list(dataframe.columns)
    if st.checkbox("Select Columns", False):
        columns = st.multiselect(
            "Columns", all_columns, all_columns
        )
    else:
        columns = all_columns
    st.write(dataframe.filter(columns))
