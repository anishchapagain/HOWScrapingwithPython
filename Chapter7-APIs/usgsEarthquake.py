import requests
import json
from datetime import datetime
dataSet = []
start = '2019-03-10'
end = '2019-03-17'
type = 'geojson'
apiUrl = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
url = apiUrl+'?format=geojson&starttime=start&endtime=end'

def readUrl(url):
    results = requests.get(url)
    print("Status Code: ", results.status_code)
    print("Headers: Content-Type: ", results.headers['Content-Type'])
    return results.json()

if __name__ == "__main__":
    jsonResult = readUrl(url)
    print("Found Total:",jsonResult['metadata']['count'])
    for events in jsonResult['features']:
        magnitude = events['properties']['mag']
        place = events['properties']['place']
        eventTimestamp = events['properties']['time']
        eventTime = datetime.fromtimestamp(eventTimestamp/1e3).strftime("%Y-%m-%d %H:%M:%S")
        eventUrl = events['properties']['url']
        longitude = events['geometry']['coordinates'][0]
        latitude = events['geometry']['coordinates'][1]
        dataSet.append([eventTime,place,magnitude,longitude,latitude,eventUrl])


    print(dataSet)
