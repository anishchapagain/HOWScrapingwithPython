'''
Listing Blog for first 50 or less
from 'https://blog.scrapinghub.com/tag/web-scraping'
'''

import requests
from bs4 import BeautifulSoup
import csv

sourceUrl = 'https://blog.scrapinghub.com/tag/web-scraping'
keys = ['title', 'date', 'author_name', 'author_url', 'comments', 'basic_description', 'blog_url']


def read_url(url):
    """Read given Url , Returns requests object for page content"""
    response = requests.get(url)
    return response.text


def get_details(page, dataWriter):
    # def get_details(page):
    """Read 'page' url and append list of queried items to dataSet"""
    nextPage = True
    pageNo = 1
    while (nextPage and pageNo <= 5):
        response = read_url(page + '/page/' + str(pageNo))
        soup = BeautifulSoup(response, 'lxml')

        rows = soup.find('div', 'post-listing').find_all('div', 'post-item')
        print("Total Blogs in Page : ", pageNo, " is ", len(rows))
        if (len(rows) > 0):
            for row in rows:
                if row.find('h2'):
                    # if len(title) > 0:  # Ignore Empty Titles
                    title = row.find('h2').a.text
                    blogUrl = row.find('h2').a.get('href')
                    author_name = row.find('span', 'author').a.text
                    author_url = row.find('span', 'author').a.get('href')
                    post_date = row.find('span', 'date').find('a').text
                    comments = row.find('span', 'custom_listing_comments').find('a').text
                    comments = comments.replace('Comment', '').strip()
                    basic_description = row.find('div', 'post-content').find('div', 'read-more').parent.get_text()
                    basic_description = basic_description.replace('Read More', '').strip()

                    print(title, ' : ', comments)
                    # Write a list of values in file
                    dataWriter.writerow(
                        [title, post_date, author_name, author_url, comments, basic_description, blogUrl])
                else:
                    print("Blogs Not Listed!")

            nextPage = True
            pageNo += 1
        else:
            nextPage = False

if __name__ == '__main__':
    dataSet = open('blogs.csv', 'w', newline='', encoding='utf-8')
    dataWriter = csv.writer(dataSet)
    # Write a Header or Column_names to CSV
    dataWriter.writerow(keys)
    get_details(sourceUrl, dataWriter)
    # get_details(sourceUrl)
    dataSet.close()
