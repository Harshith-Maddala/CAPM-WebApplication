# Importing libraries

import streamlit as st
import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datetime
import graph_functions
# command to connect to streamlit --> python -m streamlit run CAPMmain.py

st.set_page_config(page_title = "CAMP",
    page_icon = "chart_with_upward_trend",
    layout = 'wide')

# use the command in cmd -- python -m streamlit run CAPMmain.py

st.title("Capital Asset Pricing Model 📈")

# getting input from user
# setting up sample companies along with a default value in the square brackets
# for making it more visually appealing, we make both of them in same column

col1, col2 = st.columns([1,1])

with col1:
    stocks_list = st.multiselect("Choose 4 stocks", ('TSLA','AAPL','NFLX','MSFT','MGM','AMZN','NVDA','GOOGL'),['TSLA','AAPL','AMZN','GOOGL'])
with col2:
    year = st.number_input("Number of years",1,10)

# downloading data for SP500

try:
    end = datetime.date.today()
    start = datetime.date(datetime.date.today().year-year, datetime.date.today().month, datetime.date.today().day)
    SP500 = web.DataReader(['sp500'],'fred',start,end)
    print(SP500.tail())

    # creating new DataFrame to obtain Cloade data for every syock

    stocks_df = pd.DataFrame()

    for stock in stocks_list:
        data = yf.download(stock, period = f'{year}y')
        stocks_df[f'{stock}'] = data['Close']

    stocks_df.reset_index(inplace = True)
    SP500.reset_index(inplace = True) 
    # changing the date to merge data
    SP500.columns = ['Date','sp500'] # changing names
    stocks_df['Date'] = stocks_df['Date'].astype('datetime64[ns]')
    stocks_df['Date'] = stocks_df['Date'].apply(lambda x:str(x)[:10])
    stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
    stocks_df = pd.merge(stocks_df, SP500, on = 'Date', how = 'inner') # merge

    # displaying first 5 last 5 rows

    col1,col2 = st.columns([1,1])
    with col1:
        st.markdown("### Dataframe head")
        st.dataframe(stocks_df.head(), use_container_width = True)
    with col2:
        st.markdown("### Dataframe head")
        st.dataframe(stocks_df.tail(), use_container_width = True)

    # creating chart in next python file

    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("### Price of all the Stocks")
        st.plotly_chart(graph_functions.interactive_plot(stocks_df))
    with col2:
    # print(graph_funtions.normalize(stocks_df)) -- if ypu want ot see the difference
        st.markdown("### Price of all the Stocks (After normaliztion)")
        st.plotly_chart(graph_functions.interactive_plot(graph_functions.normalize(stocks_df)))

    stocks_daily_return = graph_functions.daily_return(stocks_df)
    print(stocks_daily_return.head())

    beta = {}
    alpha = {}

    for i in stocks_daily_return.columns:

        # Ignoring the date and S&P500 Columns 
        if i !='Date' and i !='sp500':

            # calculate beta and alpha for all stocks
            b, a = graph_functions.cal_beta(stocks_daily_return, i)

            beta[i] = b
            alpha[i] = a
    print(beta, alpha)

    beta_df = pd.DataFrame(columns = ['Stock','Beta Value'])
    beta_df['Stock'] = beta.keys()
    beta_df['Beta Value'] = [str(round(i,2)) for i in beta.values()]

    with col1:
        st.markdown('### Calculated Beta Value')
        st.dataframe(beta_df, use_container_width= True)

    # Calculate return for any security using CAPM  
    rf = 0 # risk free rate of return
    rm = stocks_daily_return['sp500'].mean()*252 # market potfolio return

    return_df = pd.DataFrame()
    return_value = []
    for stock, value in beta.items():
                # calculate return
        return_value.append(str(round(rf+(value*(rm-rf)),2)))
    return_df['Stock'] = stocks_list

    return_df['Return Value'] = return_value

    with col2:
        st.markdown('### Calculated Return using CAPM')

        st.dataframe(return_df, use_container_width=True)
    
except:
    st.write("Please select valid input")
