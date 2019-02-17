from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
page = 28

# Here You Put Whatever Item You Want To Search For
search = 'volkswagen golf'
searchURL = search.replace(' ','%20')

# Insert The Minimum and Maximum Values To Eliminate Outliers
priceRange = ['1000','40000']

makeAndModel = ['Skoda','Yeti']

yearRange = ['2015','2017']

listOfPrices = []
priceSlicer = []
xPlot = []


def priceFinder(page, searchURL, priceRange):
	for i in range(1, 40):
		url = 'https://www.donedeal.ie/cars/' + makeAndModel[0] + '/' + makeAndModel[1] + '?start=' + str(page) + '&price_from=' + priceRange[0] + '&price_to=' + priceRange[1] + '&year_from=' + yearRange[0] + '&year_to=' + yearRange[1]
		page = page + 28
		print(url)
		response = requests.get(url, headers=headers)
		c = response.content

		soup = BeautifulSoup(c, features='html.parser')

		prices = soup.find_all('p', 'card__price')

		pageNumber = soup.find_all('ng-class', 'icon-nav_arrow_left')

		for price in prices:
			itemPrice = price.get_text()
			itemPrice = itemPrice.replace("€","")
			itemPrice = itemPrice.replace(",","")
			if(itemPrice.isdigit()):
				itemPrice = int(itemPrice)
				if(itemPrice < int(priceRange[1])):
					listOfPrices.append(itemPrice)

		print(listOfPrices)


def xAxisMaker(listOfPrices):
	for x in range(0, len(listOfPrices)):
		xPlot.append(x)


def getAverage(listOfPrices):
	averagePrice = sum(listOfPrices) / float(len(listOfPrices))
	averagePrice = round(averagePrice)
	return averagePrice



priceFinder(page, searchURL, priceRange)
getAverage(listOfPrices)
xAxisMaker(listOfPrices)

print('The average price of a ' + search + " is €" + str(getAverage(listOfPrices)))
print(len(listOfPrices))

plt.scatter(xPlot, listOfPrices, label='skitscat', color='k')

plt.xlabel('x')
plt.ylabel('price')
plt.title(search + ' Scatter Plot')
plt.legend()
plt.show()





