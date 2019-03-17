import re
import requests

def read_url(url):
   #    content = open("hosting.html", "r",encoding="utf8")
    pageSource = requests.get(url).text
    return pageSource

def read_file():
    content = open("pharma.html", "r")
    pageSource = content.read()
    return pageSource

if __name__ == "__main__":

    dataSet=list()
    sourceUrl = 'https://www.pharmaceutical-technology.com/company-a-z'
    page = read_url(sourceUrl)
    # page = read_file()
    patterns = r'href="(.*?)".*companyaz_name">(.*?)\,?<'
    companies = re.findall(patterns, page)
    print("Findall found total ", len(companies))
    if len(companies)>0:
        for company in companies:
            if(re.match(r'http.*',company[0])):
                dataSet.append(company)
            else:
                print("URL not matched!")
    else:
        print("Companies not found!")

    print("Total companies in dataSet: ",len(dataSet))
    print(dataSet[0])
    print(dataSet[-1])
    print(dataSet[10:15])

