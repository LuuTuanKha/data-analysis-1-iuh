#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
#DF

df_pop_london = pd.read_excel('C:/Users/84912/Downloads/central_trend_2017_base.xlsx')

print(df_pop_london)


# In[9]:


#bar chart
df_hackney = df_pop_london[['district', 2020]].query('district == "Hackney"')[[2020]].sum()
df_haringey = df_pop_london[['district', 2020]].query('district == "Haringey"')[[2020]].sum()

df_hackney_int = int(df_hackney)
df_haringey_int = int(df_haringey)
df_london_int = int(df_pop_london[['district', 2020]].query('district == "London"')[[2020]].sum())

array_pop_city = [df_hackney_int,df_haringey_int,df_london_int]

print(array_pop_city)


# In[7]:


#bar chart
df_male_london = pd.read_excel('C:/Users/84912/Downloads/central_trend_2017_base.xlsx', sheet_name=1)
df_female_london = pd.read_excel('C:/Users/84912/Downloads/central_trend_2017_base.xlsx', sheet_name=2)


df_bar_male = int(df_male_london[['district', 2020]].query('district == "London"')[[2020]].sum())
df_bar_male1 = int(df_male_london[['district', 2021]].query('district == "London"')[[2021]].sum())
df_bar_male2 = int(df_male_london[['district', 2022]].query('district == "London"')[[2022]].sum())
df_bar_male3 = int(df_male_london[['district', 2023]].query('district == "London"')[[2023]].sum())
df_bar_male4 = int(df_male_london[['district', 2024]].query('district == "London"')[[2024]].sum())
df_bar_male5 = int(df_male_london[['district', 2025]].query('district == "London"')[[2025]].sum())
df_bar_male6 = int(df_male_london[['district', 2026]].query('district == "London"')[[2026]].sum())
df_bar_male7 = int(df_male_london[['district', 2027]].query('district == "London"')[[2027]].sum())
df_bar_male8 = int(df_male_london[['district', 2028]].query('district == "London"')[[2028]].sum())
df_bar_male9 = int(df_male_london[['district', 2029]].query('district == "London"')[[2029]].sum())
df_bar_male10 = int(df_male_london[['district', 2030]].query('district == "London"')[[2030]].sum())
df_bar_male11 = int(df_male_london[['district', 2031]].query('district == "London"')[[2031]].sum())
arr_bar_male = [
    df_bar_male,df_bar_male1, df_bar_male2, df_bar_male3,
    df_bar_male4, df_bar_male5, df_bar_male6,
    df_bar_male7, df_bar_male8, df_bar_male9, df_bar_male10,df_bar_male11
]
for i in arr_bar_male:
    print(i)


# In[8]:




df_bar_female = int(df_female_london[['district', 2020]].query('district == "London"')[[2020]].sum())
df_bar_female1 = int(df_female_london[['district', 2021]].query('district == "London"')[[2021]].sum())
df_bar_female2 = int(df_female_london[['district', 2022]].query('district == "London"')[[2022]].sum())
df_bar_female3 = int(df_female_london[['district', 2023]].query('district == "London"')[[2023]].sum())
df_bar_female4 = int(df_female_london[['district', 2024]].query('district == "London"')[[2024]].sum())
df_bar_female5 = int(df_female_london[['district', 2025]].query('district == "London"')[[2025]].sum())
df_bar_female6 = int(df_female_london[['district', 2026]].query('district == "London"')[[2026]].sum())
df_bar_female7 = int(df_female_london[['district', 2027]].query('district == "London"')[[2027]].sum())
df_bar_female8 = int(df_female_london[['district', 2028]].query('district == "London"')[[2028]].sum())
df_bar_female9 = int(df_female_london[['district', 2029]].query('district == "London"')[[2029]].sum())
df_bar_female10 = int(df_female_london[['district', 2030]].query('district == "London"')[[2030]].sum())
df_bar_female11 = int(df_female_london[['district', 2031]].query('district == "London"')[[2031]].sum())

arr_bar_female= [
      df_bar_female,df_bar_female1, df_bar_female2, df_bar_female3,
    df_bar_female4, df_bar_female5, df_bar_female6,
    df_bar_female7, df_bar_female8, df_bar_female9, df_bar_female10,df_bar_female11
]

for i in arr_bar_female:
    print(i)


# In[11]:


#pie chart
import plotly.express as px
import plotly.graph_objects as go
df_compareAge2020_Pie_u18 = int(df_pop_london[['district', 'age',2020]].query('district == "London" and age < 18')[2020].sum())
df_compareAge2020_Pie_u60 = int(df_pop_london[['district', 'age',2020]].query('district == "London" and age < 60 and age >=18 ')[2020].sum())
df_compareAge2020_Pie_u90 = int( df_pop_london[['district', 'age',2020]].query('district == "London"and age < 90 and age >=60 ')[2020].sum())


pieType1Fig = go.Figure(data=[go.Pie(labels=['Trẻ em & vị thành niên', 'Người trưởng thành', 'người lớn tuổi'], values=[df_compareAge2020_Pie_u18, df_compareAge2020_Pie_u60,df_compareAge2020_Pie_u90])])
pieType1Fig.update_layout(
    title_text="Biểu đồ so sánh dân số 3 độ tuổi của thành phố london trong năm 2020 ",
    # Add annotations in the center of the donut pies.
    )


df_pop_westminster_2020  = int(df_pop_london[['district', 2020]].query('district == "Westminster"')[[2020]].sum())
df_pop_london_2020  = int(df_pop_london[['district', 2020]].query('district == "London"')[[2020]].sum())
df_pop_wandsworth_2020  = int(df_pop_london[['district', 2020]].query('district == "Wandsworth"')[[2020]].sum())
df_pop_towerHamlets_2020  = int(df_pop_london[['district', 2020]].query('district == "Tower Hamlets"')[[2020]].sum())
df_pop_havering_2020  = int(df_pop_london[['district', 2020]].query('district == "Havering"')[[2020]].sum())
df_pop_waltham_2020  = int(df_pop_london[['district', 2020]].query('district == "Waltham Forest"')[[2020]].sum())
df_pop_hillingdon_2020  = int(df_pop_london[['district', 2020]].query('district == "Hillingdon"')[[2020]].sum())
df_pop_harrow_2020  = int(df_pop_london[['district', 2020]].query('district == "Harrow"')[[2020]].sum())

labels = ['Westminster','London','Wandsworth','Tower Hamlets','Havering','Waltham Forest','Hillingdon','Harrow']
values = [df_pop_westminster_2020, df_pop_london_2020, df_pop_wandsworth_2020, df_pop_towerHamlets_2020,df_pop_havering_2020,
         df_pop_waltham_2020,df_pop_waltham_2020,df_pop_hillingdon_2020,df_pop_harrow_2020]
print(values)


# In[13]:


df_compareAge2020_Pie_u18 = int(df_pop_london[['district', 'age',2020]].query('district == "London" and age < 18')[2020].sum())
df_compareAge2020_Pie_u60 = int(df_pop_london[['district', 'age',2020]].query('district == "London" and age < 60 and age >=18 ')[2020].sum())
df_compareAge2020_Pie_u90 = int( df_pop_london[['district', 'age',2020]].query('district == "London"and age < 90 and age >=60 ')[2020].sum())
print(df_compareAge2020_Pie_u18)
print(df_compareAge2020_Pie_u60)
print(df_compareAge2020_Pie_u90)


# In[14]:


#scatter chart

df_scatter_citylondon = int(df_pop_london[['district', 2020]].query('district == "City of London"')[[2020]].sum())
df_scatter_BaD = int(df_pop_london[['district', 2020]].query('district == "Barking and Dagenham"')[[2020]].sum())
df_scatter_barnet = int(df_pop_london[['district', 2020]].query('district == "Barnet"')[[2020]].sum())
df_scatter_Bexley = int(df_pop_london[['district', 2020]].query('district == "Bexley"')[[2020]].sum())
df_scatter_Brent = int(df_pop_london[['district', 2020]].query('district == "Brent"')[[2020]].sum())
df_scatter_Bromley = int(df_pop_london[['district', 2020]].query('district == "Bromley"')[[2020]].sum())
df_scatter_Camden = int(df_pop_london[['district', 2020]].query('district == "Camden"')[[2020]].sum())
df_scatter_Croydon = int(df_pop_london[['district', 2020]].query('district == "Croydon"')[[2020]].sum())
df_scatter_Ealing = int(df_pop_london[['district', 2020]].query('district == "Ealing"')[[2020]].sum())
df_scatter_Enfield = int(df_pop_london[['district', 2020]].query('district == "Enfield"')[[2020]].sum())
df_scatter_Greenwich = int(df_pop_london[['district', 2020]].query('district == "Greenwich"')[[2020]].sum())
df_scatter_Hammer = int(df_pop_london[['district', 2020]].query('district == "Hammersmith and Fulham"')[[2020]].sum())
df_scatter_Haringey = int(df_pop_london[['district', 2020]].query('district == "Haringey"')[[2020]].sum())
df_scatter_Harrow = int(df_pop_london[['district', 2020]].query('district == "Harrow"')[[2020]].sum())
df_scatter_Havering = int(df_pop_london[['district', 2020]].query('district == "Havering"')[[2020]].sum())
df_scatter_Hillingdon = int(df_pop_london[['district', 2020]].query('district == "Hillingdon"')[[2020]].sum())
df_scatter_Hounslow = int(df_pop_london[['district', 2020]].query('district == "Hounslow"')[[2020]].sum())
df_scatter_Islington = int(df_pop_london[['district', 2020]].query('district == "Islington"')[[2020]].sum())
df_scatter_Kensington = int(df_pop_london[['district', 2020]].query('district == "Kensington and Chelsea"')[[2020]].sum())
df_scatter_Kingston = int(df_pop_london[['district', 2020]].query('district == "Kingston upon Thames"')[[2020]].sum())
df_scatter_Lambeth = int(df_pop_london[['district', 2020]].query('district == "Lambeth"')[[2020]].sum())
df_scatter_Lewisham = int(df_pop_london[['district', 2020]].query('district == "Lewisham"')[[2020]].sum())
df_scatter_Merton = int(df_pop_london[['district', 2020]].query('district == "Merton"')[[2020]].sum())
df_scatter_Newham = int(df_pop_london[['district', 2020]].query('district == "Newham"')[[2020]].sum())
df_scatter_Redbridge = int(df_pop_london[['district', 2020]].query('district == "Redbridge"')[[2020]].sum())
df_scatter_Richmond = int(df_pop_london[['district', 2020]].query('district == "Richmond upon Thames"')[[2020]].sum())
df_scatter_Southwark = int(df_pop_london[['district', 2020]].query('district == "Southwark"')[[2020]].sum())
df_scatter_Hamlets = int(df_pop_london[['district', 2020]].query('district == "Tower Hamlets"')[[2020]].sum())
df_scatter_Sutton = int(df_pop_london[['district', 2020]].query('district == "Sutton"')[[2020]].sum())
df_scatter_Waltham = int(df_pop_london[['district', 2020]].query('district == "Waltham Forest"')[[2020]].sum())
df_scatter_Wandsworth = int(df_pop_london[['district', 2020]].query('district == "Wandsworth"')[[2020]].sum())
df_scatter_Westminster = int(df_pop_london[['district', 2020]].query('district == "Westminster"')[[2020]].sum())
df_scatter_London = int(df_pop_london[['district', 2020]].query('district == "London"')[[2020]].sum())
yScatter_withoutLondon = [ df_scatter_citylondon, df_scatter_BaD,df_scatter_barnet,
          df_scatter_Bexley, df_scatter_Brent, df_scatter_Bromley, df_scatter_Camden, df_scatter_Croydon, 
           df_scatter_Ealing , df_scatter_Enfield, df_scatter_Greenwich, df_scatter_Hammer, df_scatter_Haringey,df_scatter_Harrow , 
            df_scatter_Havering, df_scatter_Hillingdon, df_scatter_Hounslow,df_scatter_Islington ,df_scatter_Kensington , df_scatter_Kingston,
            df_scatter_Lambeth, df_scatter_Lewisham,df_scatter_Merton ,df_scatter_Newham , df_scatter_Redbridge, df_scatter_Richmond,df_scatter_Southwark ,
           df_scatter_Hamlets , df_scatter_Sutton, df_scatter_Waltham,df_scatter_Wandsworth , df_scatter_Westminster, 
           ]
print(yScatter_withoutLondon)


# In[16]:


yScatter_HaveLondon = [ df_scatter_citylondon, df_scatter_BaD,df_scatter_barnet,
          df_scatter_Bexley, df_scatter_Brent, df_scatter_Bromley, df_scatter_Camden, df_scatter_Croydon, 
           df_scatter_Ealing , df_scatter_Enfield, df_scatter_Greenwich, df_scatter_Hammer, df_scatter_Haringey,df_scatter_Harrow , 
            df_scatter_Havering, df_scatter_Hillingdon, df_scatter_Hounslow,df_scatter_Islington ,df_scatter_Kensington , df_scatter_Kingston,
            df_scatter_Lambeth, df_scatter_Lewisham,df_scatter_Merton ,df_scatter_Newham , df_scatter_Redbridge, df_scatter_Richmond,df_scatter_Southwark ,
           df_scatter_Hamlets , df_scatter_Sutton, df_scatter_Waltham,df_scatter_Wandsworth , df_scatter_Westminster, df_scatter_London
           ]
print(yScatter_HaveLondon)


# In[18]:


u18_dot_2020 = int(df_pop_london[['district', 'age',2020]].query('district == "London" and age < 18')[2020].sum())
u18_dot_2021 = int(df_pop_london[['district', 'age',2021]].query('district == "London" and age < 18')[2021].sum())
u18_dot_2022 = int(df_pop_london[['district', 'age',2022]].query('district == "London" and age < 18')[2022].sum())
u18_dot_2023 = int(df_pop_london[['district', 'age',2023]].query('district == "London" and age < 18')[2023].sum())
u18_dot_2024 = int(df_pop_london[['district', 'age',2024]].query('district == "London" and age < 18')[2024].sum())
u18_dot_2025 = int(df_pop_london[['district', 'age',2025]].query('district == "London" and age < 18')[2025].sum())
u18_dot_2026 = int(df_pop_london[['district', 'age',2026]].query('district == "London" and age < 18')[2026].sum())
u18_dot_2027 = int(df_pop_london[['district', 'age',2027]].query('district == "London" and age < 18')[2027].sum())
u18_dot_2028 = int(df_pop_london[['district', 'age',2028]].query('district == "London" and age < 18')[2028].sum())
u18_dot_2029 = int(df_pop_london[['district', 'age',2029]].query('district == "London" and age < 18')[2029].sum())
u18_dot_2030 = int(df_pop_london[['district', 'age',2030]].query('district == "London" and age < 18')[2030].sum())
u18_dot_2031 = int(df_pop_london[['district', 'age',2031]].query('district == "London" and age < 18')[2031].sum())

u60_dot_2020 = int(df_pop_london[['district', 'age',2020]].query('district == "London" and age < 60 and age >=18 ')[2020].sum())
u60_dot_2021 = int(df_pop_london[['district', 'age',2021]].query('district == "London" and age < 60 and age >=18 ')[2021].sum())
u60_dot_2022 = int(df_pop_london[['district', 'age',2022]].query('district == "London" and age < 60 and age >=18 ')[2022].sum())
u60_dot_2023 = int(df_pop_london[['district', 'age',2023]].query('district == "London" and age < 60 and age >=18 ')[2023].sum())
u60_dot_2024 = int(df_pop_london[['district', 'age',2024]].query('district == "London" and age < 60 and age >=18 ')[2024].sum())
u60_dot_2025 = int(df_pop_london[['district', 'age',2025]].query('district == "London" and age < 60 and age >=18 ')[2025].sum())
u60_dot_2026 = int(df_pop_london[['district', 'age',2026]].query('district == "London" and age < 60 and age >=18 ')[2026].sum())
u60_dot_2027 = int(df_pop_london[['district', 'age',2027]].query('district == "London" and age < 60 and age >=18 ')[2027].sum())
u60_dot_2028 = int(df_pop_london[['district', 'age',2028]].query('district == "London" and age < 60 and age >=18 ')[2028].sum())
u60_dot_2029 = int(df_pop_london[['district', 'age',2029]].query('district == "London" and age < 60 and age >=18 ')[2029].sum())
u60_dot_2030 = int(df_pop_london[['district', 'age',2030]].query('district == "London" and age < 60 and age >=18 ')[2030].sum())
u60_dot_2031 = int(df_pop_london[['district', 'age',2031]].query('district == "London" and age < 60 and age >=18 ')[2031].sum())


u90_dot_2020 = int( df_pop_london[['district', 'age',2020]].query('district == "London"and age < 90 and age >=60 ')[2020].sum())
u90_dot_2021 = int( df_pop_london[['district', 'age',2021]].query('district == "London"and age < 90 and age >=60 ')[2021].sum())
u90_dot_2022 = int( df_pop_london[['district', 'age',2022]].query('district == "London"and age < 90 and age >=60 ')[2022].sum())
u90_dot_2023 = int( df_pop_london[['district', 'age',2023]].query('district == "London"and age < 90 and age >=60 ')[2023].sum())
u90_dot_2024 = int( df_pop_london[['district', 'age',2024]].query('district == "London"and age < 90 and age >=60 ')[2024].sum())
u90_dot_2025 = int( df_pop_london[['district', 'age',2025]].query('district == "London"and age < 90 and age >=60 ')[2025].sum())
u90_dot_2026 = int( df_pop_london[['district', 'age',2026]].query('district == "London"and age < 90 and age >=60 ')[2026].sum())
u90_dot_2027 = int( df_pop_london[['district', 'age',2027]].query('district == "London"and age < 90 and age >=60 ')[2027].sum())
u90_dot_2028 = int( df_pop_london[['district', 'age',2028]].query('district == "London"and age < 90 and age >=60 ')[2028].sum())
u90_dot_2029 = int( df_pop_london[['district', 'age',2029]].query('district == "London"and age < 90 and age >=60 ')[2029].sum())
u90_dot_2030 = int( df_pop_london[['district', 'age',2030]].query('district == "London"and age < 90 and age >=60 ')[2030].sum())
u90_dot_2031 = int( df_pop_london[['district', 'age',2031]].query('district == "London"and age < 90 and age >=60 ')[2031].sum())

u18_array_dot = [u18_dot_2020,u18_dot_2021,u18_dot_2022,
                u18_dot_2023,u18_dot_2024,u18_dot_2025,
                u18_dot_2026,u18_dot_2027,u18_dot_2028,
                u18_dot_2029,u18_dot_2030,u18_dot_2031]

u60_array_dot = [u60_dot_2020,u60_dot_2021,u60_dot_2022,
                u60_dot_2023,u60_dot_2024,u60_dot_2025,
                u60_dot_2026,u60_dot_2027,u60_dot_2028,
                u60_dot_2029,u60_dot_2030,u60_dot_2031]

u90_array_dot = [u90_dot_2020,u90_dot_2021,u90_dot_2022,
                u90_dot_2023,u90_dot_2024,u90_dot_2025,
                u90_dot_2026,u90_dot_2027,u90_dot_2028,
                u90_dot_2029,u90_dot_2030,u90_dot_2031]
print(u18_array_dot)
print(u60_array_dot)
print(u90_array_dot)


# In[ ]:




