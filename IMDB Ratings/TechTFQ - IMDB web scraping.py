#!/usr/bin/env python
# coding: utf-8

# In[5]:


# !pip install requests


# In[6]:


# !pip install bs4


# In[9]:


from bs4 import BeautifulSoup


# In[11]:


import requests


# In[65]:


url = requests.get('https://www.imdb.com/chart/top/')
# To track error if website incorrect
url.raise_for_status()


# In[66]:


soup = BeautifulSoup(url.text,"html.parser")


# In[67]:


# Look for thead of the table from inspect
movies = soup.find('tbody',class_="lister-list").find_all('tr')


# In[22]:


#Double check if all 250 tr are located
len(movies)


# In[68]:


for movie in movies:
    with open("imdb.html")
    name = movie.find('td',class_="titleColumn").a.text
    rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
    year = movie.find('td',class_="titleColumn").span.text.strip("()")
    rating = movie.find('td',class_="ratingColumn").strong.text


# In[76]:


import requests, openpyxl


# In[85]:


excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Rated Movies'
sheet.append(['Movie_Rank','Movie_Name','Year_of_Release','IMDB_rating'])

for movie in movies:
    name = movie.find('td',class_="titleColumn").a.text
    rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
    year = movie.find('td',class_="titleColumn").span.text.strip("()")
    rating = movie.find('td',class_="ratingColumn").strong.text
    sheet.append([rank,name,year,rating])


# In[86]:


excel.save('IMDB Movie Ratings.xlsx')

