from sendmail import sendmail

class Product:
    def __init__(self, title, amazon_link="", flipkart_link="", email=""):
        self.id = 0
        self.title = title
        self.amazon_link = amazon_link
        self.flipkart_link = flipkart_link
        self.email = email

    def notify_addition(self):
        msg = "Hello! New product '" + self.title + "' has been added to SmartPrice.\nCurrent Amazon price = " + str(self.amazon_current_price) + "Rs." 
        sendmail(msg,self.email)

    def notify_change(self):
        msg = "'" + self.title + "' Price has decreased. New Amazon price = " + str(self.amazon_current_price) + "Rs." 
        sendmail(msg,self.email)
