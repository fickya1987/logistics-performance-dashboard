# Logistics Performance Dashboard

An interactive dashboard built with [Streamlit](https://streamlit.io/) to visualize logistics performance metrics such as the Logistics Performance Index (LPI). This dashboard helps to easily identify the best-performing countries in logistics by allowing users to adjust the number of countries displayed and select various metrics.

## Features

- **Interactive Metric Selection**: Choose from multiple logistics metrics like LPI Score, Customs Score, Infrastructure Score, etc.
- **Customizable Visualizations**: Use sliders to limit the number of countries visualized.
- **Multiple Visualization Types**: Display data as a bar chart or a CSV table.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AhmedHeshamEG/logistics-performance-dashboard.git
    cd logistics-performance-dashboard
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure the dataset (`data.xlsx`) is in the project directory.
2. Run the Streamlit application:
    ```bash
    streamlit run main.py
    ```
3. Open your browser and navigate to `http://localhost:8501` to interact with the dashboard.

## Dataset

The dataset used in this dashboard is sourced from the [World Bank's Logistics Performance Index (LPI)](https://lpi.worldbank.org/international/global).

## Contributing

Contributions are welcome! Please fork the repository and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
