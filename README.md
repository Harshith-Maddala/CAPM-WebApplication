# CAPM-WebApplication
CAPM calculation along with Beta and Return for stocks using python and streamlit
Project was created in VisualStudioCode and CAPMmain.py is the main file.
link to access th streamlit app - https://capm-webapplication-k9jrtfmu6hudlufdjiwkg4.streamlit.app/   and https://capm-webapplication-83gzkxp5tubkqnmazm3hw3.streamlit.app/

Certainly! Here's a revised version that sounds like documentation:

---

## Streamlit CAPM Analysis Documentation

### 1. Library Import:
   - Essential libraries, including Streamlit, Pandas, yfinance, and datetime, are imported to facilitate data analysis and visualization.

### 2. Streamlit Configuration:
   - The Streamlit page is configured with a specified title, icon, and layout to enhance the user interface.

### 3. User Input:
   - Users can interactively choose up to four stocks and specify the number of years for historical data analysis.

### 4. Data Download:
   - Historical data for the S&P 500 index is retrieved using the `pandas_datareader` library for comprehensive market analysis.

### 5. Data Preparation:
   - A DataFrame is created to organize and store closing prices of selected stocks and the S&P 500.
   - Data cleaning and merging processes ensure a coherent dataset for subsequent analysis.

### 6. Data Display:
   - Streamlit is leveraged to showcase the head and tail of the DataFrame, providing users with a snapshot of the dataset.

### 7. Interactive Charts:
   - Utilizing a custom module, interactive line charts are generated to visually represent stock prices.

### 8. Beta and Alpha Calculation:
   - Daily returns are computed for each stock, and beta and alpha values are calculated to assess risk and performance.

### 9. Displaying Beta Values:
   - Calculated beta values for selected stocks are presented in a clear and concise DataFrame for user reference.
