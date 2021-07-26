import requests
import bs4

import os


############################## Function File For NLP Acquire ###########################

def process_articles(article_list):
    '''
    This function is designed to return a dictionary after taking in a webpage.
    
    Then the function will use a beatiful soup object to scrape the webpage
    for the webpage's title and article content    
    '''
    
    ## making my empty website list
    website_list = []
    
    # make the http request and turn the response into a beautiful soup object
    for article in article_list:
        headers = headers = {'User-Agent': 'Codeup Data Science'}
    
        response = requests.get(article, headers = headers)
        
        html = response.text
        soup = bs4.BeautifulSoup(html, 'html.parser')
        
        ## getting article title and article content using soup.find and turning the
        ## variables into .text's
        title = soup.find('h1', class_= 'jupiterx-post-title').text
        article = soup.find('div', class_ = 'jupiterx-post-content').text
        
        ## creating my dictionary inside the for loop
        my_dict = {"Title": title, 'Content': article}
        
        ## appending my website list inside the dictionary for each iteration
        website_list.append(my_dict)
    
    ## returning the full website list
    return website_list



def get_blog_articles(category_list):
    '''
    This function is designed to take in category list for a specific blog 
    (https://inshorts.com/en/read/) and scrape all the articles from each category for 
    the blog.
    
    Then the function will divide each categorized article and split them into article
    titles, article bodies, and their respective category
    '''
    
    base_url = 'https://inshorts.com/en/read/'
    
    article_list = []
    # make the http request and turn the response into a beautiful soup object
    for category in category_list:
        response = requests.get(f'{base_url}{category}')
        html = response.text
        soup = bs4.BeautifulSoup(html, 'html.parser')
        
        ## getting our title into the title variable
        titles = soup.findAll('div', class_= 'news-card-title')
        
        content = soup.findAll('div', itemprop = 'articleBody') ## getting the article content
        ## for all the articles
        for title in range(len(titles)):
            ## creating the dictionary
            my_dict = {"Title": titles[title].text, 'Content': content[title].text, 
                       'Category': category}
            
            ## appending the dictionary for each iteration
            article_list.append(my_dict)
        
    ## returning the full article list
    return article_list
