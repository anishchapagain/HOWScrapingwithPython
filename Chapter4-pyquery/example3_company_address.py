from pyquery import PyQuery as pq

sourceUrl = 'https://www.pharmaceutical-technology.com/company-a-z/'
dataSet = list()
keys = ['name','description','address','pageurl']

def read_url(url):
    """Read given Url , Returns pyquery object for page content"""
    pageSource = pq(url)
    return pq(pageSource)


def get_details(page):
    """read 'page' url and append list of queried items to dataSet"""
    response = read_url(page)
    address = response.find('.card-section:first .address:first').text().strip()
    return address

if __name__ == '__main__':
    mainPage = read_url(sourceUrl)
    if mainPage.find("[id='company-az'] > div:eq(1):has('.listing_content')"):
        print("Alphabetical Links Exist!")
        query = mainPage.find('[id="company-az"] > div:eq(1) > .listing_content:gt(0)')
        for index in query.items():
            id = index.attr('id')
            print('ID: ',id)
            if id in ['a','z']:
                for linkName in index.find('ul li').items():
                    link = linkName.find('a').attr('href')
                    if link:
                        name = linkName.find('a .companyaz_name').text()
                        linkName.find('a .companyaz_name').remove()
                        description = linkName.find('a').text()
                        address = get_details(link)
                        dataSet.append([name,description,address,link])
            else:
                print("Escaping.....",id)
    else:
        print("No Listings Found!")

    print("\nTotal Company Found (for 'a' & 'z'): ", len(dataSet))
    print(dataSet)
