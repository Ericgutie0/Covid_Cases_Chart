#!/bin/python3

import urllib.request
import json
import pygal


sauce = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'

file_obj = urllib.request.urlopen(sauce)

# transfrom into string
content = file_obj.read()

# covid_data is 'content' , now in dict format
covid_data = json.loads(content)

country_list_of_tuples = []




for i in covid_data:
  #i would be the country name
  
  country_list = covid_data[i]
  
  # Data is ACCUMLATIVE, so last_index, confirmed key value
  # capturing today's data, or any future date
  last_index = country_list[-1]
  
  
  last_confirmed = last_index["confirmed"]
  
  # creating a tuple that holds the country name, and accumlative confimred value
  # ('Syria', 19), is format
  solo_country_tuple = (i,last_confirmed)
  
  
  # appending that tuple before overwritten with other data
  country_list_of_tuples.append(solo_country_tuple)
  

# sorting the tuple according to their 1st index,'comfirmed', greatest to lowest
sorted_country_tuples = sorted(country_list_of_tuples, key=lambda c: c[1], reverse=True)



#######################################################################################
# Intention: Build a program that charts corona virus cases for the top x countries, 
# ..where x is an integer entered by user input. 


print("Chart the top 'x' countries with COVID-19 cases")
print('-----------------------------------------------\n')


# user's 'X' input -----------------------------------------
while True:
  try:
    x = int(input('Enter an integer between 1 and 187: '))
    print('\n')
    if(x <= 0 or x > 187):
      print('Your input needs to be an integer between 1 and 187.')
      x = int(input('Please, enter again: '))
      print('\n')
  except:
    print("That's not an integer...\n")
  else:
    break
  
# ---------------------------------------------------------



# WIDTH AND HEIGHT ASSIGNMENT ------------------------------
# The value of x determines the width and height of the chart

if(x<11):
  width = 1000
  height = 800
elif(x >= 11 or x < 50):
  width = 1200
  height = 1000
elif(x >= 50 or x < 101):
  width = 1400
  height = 1300
else:
  width = 1500
  height = 1500

chart = pygal.Line(width=width,height=height)

# ---------------------------------------------------------


chart.title = "COVID-19 CASES"



# PLOT POINTS ----------------------------------------------

# will equal to the number of 'x' indexes
top_x_tuples = sorted_country_tuples[:x]

for i in range(x):
  
  # holds all the confirmed case values for 'x' countries
  temp_lst = [] 
  
  #access the name of the country
  for j in range(len(covid_data[top_x_tuples[i][0]])): 
  
    # gets ALL the confirmed values
    temp_lst.append(covid_data[top_x_tuples[i][0]][j]["confirmed"]) 
  
  
  # make a series for the country and the temp_lst as that country's data
  chart.add(top_x_tuples[i][0],temp_lst) 
  
# ---------------------------------------------------------

chart.render()
