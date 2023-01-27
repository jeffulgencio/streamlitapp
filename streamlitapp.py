import streamlit

streamlit.title('My First Streamlit App')

streamlit.header('Test Header')

streamlit.text('Jeffry')

streamlit.text('Fulgencio')

streamlit.text('Test2')

streamlit.title('🥣')

streamlit.header('👻🧟')

import pandas as pd

df_fruitlist = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
df_fruitlist.set_index('Fruit',inplace=True)

selected_fruit = streamlit.multiselect('Pick some fruits:',list(df_fruitlist.index),['Avocado','Strawberries'])

fruit_toshow = df_fruitlist.loc[selected_fruit]

streamlit.dataframe(fruit_toshow)

