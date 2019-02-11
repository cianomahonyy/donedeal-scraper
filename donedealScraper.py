from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
page = 28

# Here You Put Whatever Item You Want To Search For
search = 'iphone 7'
searchURL = search.replace(' ','%20')

# Insert The Minimum and Maximum Values To Eliminate Outliers
priceRange = ['100','800']

listOfPrices = []
xPlot = []


def priceFinder(page, searchURL, priceRange):
	for i in range(1, 26):
		url = 'https://www.donedeal.ie/all?words=' + searchURL + '&area=&campaign=14' + '&start=' + str(page) + '&price_from=' + priceRange[0] + '&price_to=' + priceRange[1]
		page = page + 28
		print(url)
		response = requests.get(url, headers=headers)
		c = response.content

		soup = BeautifulSoup(c, features='html.parser')

		prices = soup.find_all('p', 'card__price')

		for price in prices:
			itemPrice = price.get_text()
			itemPrice = itemPrice[1:7]
			itemPrice = itemPrice.replace(",","")
			if(itemPrice.isdigit()):
				itemPrice = int(itemPrice)
				listOfPrices.append(itemPrice)
				print(itemPrice)

		print(listOfPrices)


def xAxisMaker(xListOfPrices):
	for x in range(0, len(xListOfPrices)):
		xPlot.append(x)


def getAverage(listOfPrices):
	averagePrice = sum(listOfPrices) / float(len(listOfPrices))
	averagePrice = round(averagePrice)
	print('The average price of a ' + search + " is €" + str(averagePrice))
	return averagePrice


priceFinder(page, searchURL, priceRange)
getAverage(listOfPrices)
xAxisMaker(listOfPrices)

plt.scatter(xPlot, listOfPrices, label='skitscat', color='k')

plt.xlabel('x')
plt.ylabel('price')
plt.title(search + ' Scatter Plot')
plt.legend()
plt.show()





