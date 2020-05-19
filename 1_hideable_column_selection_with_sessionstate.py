import pandas as pd
import streamlit as st

import SessionState

session = SessionState.get(columns=None)

st.info(
    "## Instructions:\n"
    + "1. Upload simple csv (like `data.csv` from this repo)\n"
    + "2. Check the box to choose column names\n"
    + "3. Deselect one of the column names\n"
    + "4. Try to add that column name back, note that it takes two tries\n"
)

csv_file = st.file_uploader("File", type="csv")

if csv_file is not None:
    dataframe = pd.read_csv(csv_file)
    all_columns = list(dataframe.columns)
    if session.columns is None:
        session.columns = all_columns.copy()
    if st.checkbox("Select Columns", False):
        session.columns = st.multiselect(
            "Columns", all_columns, session.columns
        )
    st.write(dataframe.filter(list(session.columns)))
