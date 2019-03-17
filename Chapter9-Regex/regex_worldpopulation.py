import re
import requests

def read_url(url):
    pageSource = requests.get(url).text
    return pageSource

if __name__ == "__main__":

    dataSet = list()
    sourceUrl = 'http://worldpopulationreview.com/us-cities/'
    page = read_url(sourceUrl)
    patterns = r'asciiname":"(?P<city>.*?)","pop2019":(?P<population>.*?),"(.*?)"latitude":(?P<latitude>.*?),"longitude":(?P<longitude>.*?),"state":"(?P<state>.*?)",'
    cities = re.finditer(patterns, page)
    for city in cities:
        cityRows = city.groupdict()
        if(int(cityRows['population'])>0):
            dataSet.append(cityRows)

    print("Total cities found: ",len(dataSet))
    print(dataSet[0])
    print(dataSet[-1])
    print(dataSet[10:15])
