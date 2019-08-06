#Required to write to a csv file
import csv

#Needed in order to compare titles
from difflib import SequenceMatcher



#This function create the Product Object
class Product:
    def __init__(self, title, price, currency, quantity):
        self.title = title
        self.price = price
        self.currency = currency
        self.quantity = quantity
        self.quantity_change = 0
        self.price_change = 0

#This function will return the details of the inputted product
def Details(product_input):
    print("Product title", product_input.title)
    print("Product currency", product_input.currency)
    print("Product price",product_input.price)
    print("Product quantity",product_input.quantity)

#This function creates a list of products based on the name of the csv file provided
def CreateProductList(data_name):
    with open(data_name, newline='') as csv_file:
        product_list = []

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for column in csv_reader:
            new_product = Product(column[0], column[1][1:], column[2], column[3])
            Details(new_product)
            product_list.append(new_product)
        #print(len(product_list))
    return product_list


#This function will return the ratio of how similar two products are two each other based on their title
def ProductSimilarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

#This function will help find itself within another csv file based on its name,
#It will use the similarity package to find itself
def FindProduct(product, other_product_list):
    product_position=-1

    for element in range(len(other_product_list)-1):
        if(ProductSimilarity(product.title,other_product_list[element].title) > 0.9):
            product_position = element
            #print("Found", product.title, "in list 2. It's title is", other_product_list[element].title)
            #print("They are", 100*ProductSimilarity(product.title,other_product_list[element].title),"% similar")
            #print("The product you are looking for in the list is found in position", element)



    return product_position

