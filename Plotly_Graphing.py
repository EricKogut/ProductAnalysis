import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import Product

import Product_Compare

plotly.tools.set_credentials_file(username='Eric_Kogut', api_key='zf6Wh20MnEQ6yl577x3p')

product_list_one = Product.CreateProductList("Watches 26-06-19.csv")
product_list_two = Product.CreateProductList("Watches 18-06-19.csv")
Product_Compare.checkProducts(product_list_one, product_list_two)


y_axis = []
x_axis = []
opacity = []
size = []
colour = []
counter = 0
for element in range(len(product_list_one)):
    if ((product_list_one[element].quantity_change != 0)):
        y_axis.append(product_list_one[element].quantity_change)
        x_axis.append(product_list_one[element].price)
        size.append(40)
        opacity.append(1)


    #print(size[element])
    colour.append('rgb(93, 164, 214)')

    counter= counter+1


trace0 = go.Scatter(
    x=x_axis,
    y=y_axis,
    mode='markers',
    marker=dict(
        size = size,
        opacity = opacity
    )
)

data = [trace0]
py.plot(data, filename='multiple-annotation')