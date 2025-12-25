from Daytabase import Product

# Start the Database
Product.init_database()

# create new product
p1 = Product("BB CC cream", amazon_link="https://amzn.in/d/6wFUO4j")

#save product to database
p1.add()

# Delete product from database
# p1.delete(3)

products = Product.get_all_products()
for i in products:
    print (i[0],i[1])