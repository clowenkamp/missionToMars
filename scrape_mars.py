#!/usr/bin/env python
# coding: utf-8

# In[1]:


# dependencies
from bs4 import BeautifulSoup as bs

import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd


# In[2]:


# declare browser path and browser
executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

url = "https://mars.nasa.gov/news/"
browser.visit(url)

html = browser.html
soup = bs(html, "html.parser")


# In[3]:


response = requests.get(url)
print(response)


# In[4]:


print(soup.prettify())


# In[5]:


headline = soup.body.find('div', class_='content_title').get_text()


# In[6]:


print(headline)


# In[7]:


text = soup.find('div', class_='article_teaser_body').get_text()


# In[8]:


print(text)


# In[9]:


url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)

html = browser.html
soup = bs(html, "html.parser")


# In[10]:


featured_img = soup.find('div', class_='carousel_items')


# In[11]:


print(featured_img)


# In[12]:


featured_img = soup.find('a', class_='button fancybox')['data-fancybox-href']


# In[13]:


print(featured_img)


# In[14]:


featured_image_url = "https://www.jpl.nasa.gov" + featured_img
print(featured_image_url)


# In[15]:


url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)

html = browser.html
soup = bs(html, "html.parser")


# In[16]:


tweets = soup.find_all("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")


# In[17]:


for tweet in tweets:
    tweet_parent = tweet.find_parent("div", class_="content")
    tweet_id = tweet_parent.find("a", class_="account-group js-account-group js-action-profile js-user-profile-link js-nav")["href"]
    
    if tweet_id == '/MarsWxReport':
        mars_weather = tweet_parent.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()
        break


# In[18]:


mars_weather


# In[19]:


url = 'https://space-facts.com/mars/'


# In[20]:


table_facts = pd.read_html(url)


# In[21]:


table_facts


# In[22]:


type(table_facts)


# In[23]:


df = table_facts[0]
df.columns = ["Description", "Value"]
df.set_index(df["Description"], inplace=True)


# In[24]:


df = df[['Value']]


# In[25]:


table_facts = df.to_html()
table_facts = table_facts.replace('\n', '')
table_facts


# In[ ]:


##Can't complete homework as the website below is not available.  

url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


# In[ ]:




