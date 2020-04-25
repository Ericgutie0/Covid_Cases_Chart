#!/bin/python3

import urllib.request
import json
import pygal

#data from the web
sauce = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'

#retrive with urllib.request
f = urllib.request.urlopen(sauce)

#transfrom into string
content = f.read()
# print(type(content))

#covid_data is the 'content' but a dictionary
covid_data = json.loads(content)


#going to hold a list of tuples
country_list_of_tuples = []

for i in covid_data:
  #i would be the country name
  
  #country_list is the dictionary at 'i' index in covid_data
  country_list = covid_data[i]
  
  #capturing today's data, or any future date
  last_index = country_list[-1]
  #Data is ACCUMLATIVE, so last_index, confirmed key value
  #.. does it 
  last_confirmed = last_index["confirmed"]
  
  #creating a tuple that holds the country name, and ..
  #accumlative confimred value
  solo_country_tuple = (i,last_confirmed)
  # ('Syria', 19), is format
  
  #appending that tuple before overwritten with other data
  country_list_of_tuples.append(solo_country_tuple)
  

#this sorts the tuple acoording to their 1st index (the lambda allows that)
#.. from greatest to lowest , reverse = True
sorted_country_tuples = sorted(country_list_of_tuples, key=lambda c: c[1], reverse=True)


#######################################################################################
# Q: We want to build a program that charts corona virus cases for the top x countries, 
# ..where x is an integer entered by user input. 


x = int(input("How many countries do you want to chart?:"))



#our chart
chart = pygal.Line(width=3000, height=400)
chart.title = "COVID-19 CASES"

#will equal to the number of x indexs the user plugs in
top_x_tuples = sorted_country_tuples[:x]

for i in range(x):
  temp_lst = [] #this will hold all the confirmed case values for each country user wants
  # print(covid_data[top_x_tuples[i][0]])
  for j in range(len(covid_data[top_x_tuples[i][0]])): #accesses the name of the country
    
    # print(i,"i",j,"j")
    # print(covid_data[top_x_tuples[i][0]][j]['confirmed'])
    
   
    temp_lst.append(covid_data[top_x_tuples[i][0]][j]["confirmed"]) #gets ALL the confirmed values
  
  chart.add(top_x_tuples[i][0],temp_lst) #we make a series for the country..
                                        #and and the temp_lst as that country's data
  #

chart.render()
  
