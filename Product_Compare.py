from builtins import print
import Product

#Will be used for parsing the files
import re



def changeInPrice(new_product, old_product):
    change = float(new_product.price) - float(old_product.price)
    #print(float(new_product.price), "MINUS", float(old_product.price))
    return change

def changeInQuantity(new_product, old_product):

    #This first creates a list containing only the numbers in the string
    old_quantity_list = (re.findall('\d+', old_product.quantity))
    print("THIS IS THE QUANTITY ATTRIBUTE", old_product.quantity)
    print("THIS IS THE LIST CREATED", old_quantity_list)

    #This variable will be used to store the new number to be created from the list entries
    old_quantity_number = ""

    #For each element within the list of numbers, the variable will receive the digits from
    for count in range(len(old_quantity_list)):
        old_quantity_number = old_quantity_number+old_quantity_list[count]

    #Turning it into an int
    old_quantity_number = int(old_quantity_number)


    #Doing the same for the other list
    new_quantity_list = (re.findall('\d+', new_product.quantity))
    new_quantity_number = ""

    for count in range(len(new_quantity_list)):
        new_quantity_number = new_quantity_number+new_quantity_list[count]

    new_quantity_number = int(new_quantity_number)


    #Finally subtracting the two numbers from each other

    change =  new_quantity_number - old_quantity_number
    print(new_quantity_number, " - ", old_quantity_number)
    print("CHANGE:", change)
    return change



def checkProducts(new_product_list, old_product_list):

    #For each element in the first list, the loop goes through the second list, finds the respective "old product" (from previous csv file)
    #The index of the product in the old list is stored in the index variable

    for element in range(len(new_product_list)-1):
        if (Product.FindProduct(new_product_list[element],old_product_list) != -1):
            index = Product.FindProduct(new_product_list[element], old_product_list)

            #Creating the new and old product objects for each iteration of the loop
            updated_product = new_product_list[element]
            #print("The new product", updated_product.quantity)
            old_product = old_product_list[index]

            price_change = changeInPrice(updated_product, old_product)



            #Checking how the price has changed within
            if (price_change<0):
                print(new_product_list[element].title,"has dropped in price by", price_change)
            elif (price_change>0):
                print(new_product_list[element].title,"has increased in price by", price_change)
            else:
                print(new_product_list[element].title, "has not changed its price")
            new_product_list[element].title = price_change
            #Checking how many more units have been sold
            #print("SENDING", updated_product.title, "AND", old_product.title)
            quantity_change = changeInQuantity(updated_product, old_product)
            #print(updated_product.title, "has sold", quantity_change, "additional units")
            new_product_list[element].quantity_change = quantity_change


#product_list_two = Product.CreateProductList("Watches 07-06-19.csv")
#product_list_one = Product.CreateProductList("Watches 25-06-19.csv")

#checkProducts(product_list_one, product_list_two)
