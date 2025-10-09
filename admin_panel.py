# School-wide dashboard and export
import streamlit as st
import pandas as pd
from excel_exporter import export_to_excel

def launch_admin_panel(results, theme="constellation"):
    # Use theme to customize visuals, badge overlays, etc.
    st.subheader("🏫 School-Wide Dashboard")
# def launch_admin_panel(results):
#     st.header("🏫 School-Wide Dashboard")

    df = pd.DataFrame(results)
    st.dataframe(df)

    st.subheader("📊 Leaderboard")
    top_students = df.sort_values(by="Score", ascending=False).head(10)
    st.table(top_students[["Name", "Roll No", "Score"]])

    st.subheader("📤 Export Full School Results")
    export_to_excel(results, "school_results.xlsx")
    with open("school_results.xlsx", "rb") as f:
        st.download_button("Download School Results", f, file_name="school_results.xlsx")
