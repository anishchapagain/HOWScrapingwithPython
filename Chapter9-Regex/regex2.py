import re
import requests

def read_url(url):
    pageSource = requests.get(url).text
    return pageSource

if __name__ == "__main__":
    dataSet=dict()
    sourceUrl = 'https://hostadvice.com/hosting-services/wordpress/'
    page=1
    totalPages=5
    while page <= totalPages:
        source = read_url(sourceUrl+'page/'+str(page))   # page = read_file()
        titleReviews = re.findall(r'class="user-reviews-link.*title="(.*?)">\s*.*\s*\(\s*(.*?)\s*\)\s*</a>', source)
        print("Findall found total ", len(titleReviews))
        if len(titleReviews)>0:
            for titleReview in titleReviews:
                if re.search(r'[0-9,]+',titleReview[1]):
                    dataSet[titleReview[0].strip()]=titleReview[1]
        else:
            print("NO Data Found!")
        page+=1
    else:
        print("Completed!\nTotal Found: ",len(dataSet))
    print(dataSet)
