import streamlit as st
import pandas as pd
import yfinance as yf
import time

msft = yf.Ticker('^GSPC')
info = msft.info
low = info['fiftyTwoWeekLow']
print('Extracted: ', low)
#news=msft.news
#css=
'''
<style>
.banner {
   Width:970px;
   Height:250px;
}
<style>

if len(news)!=0:
    news1=news[-1]
    ref_news='Latest Headline: \n'+news1['title']
    st.info(ref_news, icon='📰')
'''
# check multiple clicks
password = st.text_input(placeholder='', label='passkey')
if password == st.secrets['password']:
   df = pd.DataFrame({'test':['csv1']})
   df1 = pd.DataFrame({'test':['csv1']})

   # Define a function to convert the DataFrame to CSV format
   @st.cache_data
   def convert_df(df):
      return df.to_csv(index=False).encode("utf-8")

   # Convert the DataFrame to CSV
   csv = convert_df(df)
   csv1 = convert_df(df1)
  # Create the download button
   st.download_button("Press to Download", csv, "file.csv", "text/csv", key="download-csv")
   st.download_button("Press to Download", csv1, "file.csv", "text/csv", key="download-csv-new")
else:
   st.info('Passkey is unavailable')
