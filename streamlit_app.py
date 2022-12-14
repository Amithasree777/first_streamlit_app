import streamlit

streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3&Blueberry oat Meal')
streamlit.text('Spinach,Kale & Rocket Smoothie')
streamlit.text('Hard-Boiled Free- Range EGG')


streamlit.title('My Moms New Healthy Dinner')
streamlit.header('Breakfast favorites')
streamlit.text('🥣Omega 3&Blueberry oat Meal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free- Range EGG')
  
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
streamlit.dataframe(my_fruit_list)


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("pick some fruits:", list (my_fruit_list.index),['Avocado','Strawberries'])
                 
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("pick some fruits:", list (my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)





                 
                 


                 
                 



