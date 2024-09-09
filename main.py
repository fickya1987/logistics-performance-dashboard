import streamlit as st
import pandas as pd

# Load the dataset
file_path = 'data.xlsx'
df = pd.read_excel(file_path)

# Make the first row the new header
df.columns = df.iloc[0]
df = df[1:]


def main():
    st.title("LPI Scores by Country")

    # List of columns for selection
    metrics = ['LPI Score', 'Customs Score', 'Infrastructure Score',
               'International shipments Score', 'Logistics competence Score',
               'Tracking & tracing Score', 'Timeliness Score']

    # Select which metric to visualize
    selected_metric = st.selectbox("Select the metric to visualize:", metrics)

    # Update the DataFrame based on the selected metric
    df_sorted = df.sort_values(by=selected_metric, ascending=False)

    # Add a selection box for choosing visualization type
    vis_type = st.selectbox("Select the type of visualization:", [
                            "Bar Chart", "CSV Table"])

    # Slider for the number of countries to display
    num_countries = st.slider(
        "Number of Countries to Display", 1, len(df_sorted), 10)

    # Filter the data to display the selected number of countries
    df_display = df_sorted[:num_countries]

    if vis_type == "Bar Chart":
        # Create a bar chart using Streamlit
        st.bar_chart(df_display.set_index('Country')[selected_metric])

    elif vis_type == "CSV Table":
        # Create a CSV Table using Streamlit
        st.write("CSV Table")
        st.write(df_display)
        st.plotly_chart(
            df_display.set_index('Country').reset_index(
            ).plot.scatter(x='Country', y=selected_metric),
            use_container_width=True
        )


if __name__ == "__main__":
    main()
