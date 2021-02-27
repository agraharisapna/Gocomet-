import requests
from bs4 import BeautifulSoup as bs_soup

var = input()

url = "https://www.flipkart.com/search?q="+var
url2 = "https://www.flipkart.com"

flpkrt = requests.get(url)
htmlContent = flpkrt.content

soup = bs_soup(htmlContent, 'html.parser')
# print(soup.prettify())

title = soup.title
print(title)

# product_count
count = soup.find_all("div", {"class": '_1AtVbE col-12-12'})  # no_of_prod
print("------------count of products--------------")
a=len(count)
print(a)
print("\n\n\n")

# product_names
prod_names = []
for names in soup.find_all('div', class_='_4rR01T'):
	prod_names.append(names.text)
print(prod_names)
print("\n\n\n")

# price_of_product
prod_price = []
for price in soup.find_all('div', {'class': '_30jeq3 _1_WHN1'}):
    prod_price.append(str(price.text).strip())
print(prod_price)
print("\n\n\n")

# product_details
prod_details = []
for desc in soup.find_all('ul', class_='_1xgFaf'):
	prod_details.append(desc.text)
print(prod_details)
print("\n\n\n")


#product_ratings
prod_ratings = []
for rates in soup.find_all('div', class_='_3LWZlK'):
	prod_ratings.append(rates.text)
print(prod_ratings)
print("\n\n\n")

# categories
prod_categories = []
for categories in soup.findAll('a', class_='_2whKao'):
	prod_categories.append(categories['href'])
print(prod_categories)
print("\n\n\n")

#links
prod_link = []
for j in soup.find_all('a', class_='_1fQZEK'):
	a = url2+j['href']
	prod_link.append(a)
print(prod_link,end=" ")
print("\n\n\n")

