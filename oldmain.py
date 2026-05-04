from dotenv import load_dotenv
import time
from Vidhukantwebhelper import get_blog_titles
from Amazonwebhelper import get_amazon_price
from Flipkartwebhelper import get_flipkart_price
from sendmail import sendmail
from Daytabase import Product


# # Load the .env file
load_dotenv()
#
#
#
# # Step: Save to file
# # with open("titles.txt", "w", encoding="utf-8") as file:
# #     for title in blog_titles:
# #         file.write(title + "\n")
# def get_added_posts(new, old):
#     added_posts = []
#     for x in new:
#         if x not in old:
#             added_posts.append(x)
#     return added_posts
#
# def get_deleted_posts(new,old):
#     deleted_posts = []
#     for x in old:
#         if x not in new:
#             deleted_posts.append(x)
#     return deleted_posts
#
#
# old_titles = get_blog_titles()
# while True:
#     time.sleep(20)
#     new_titles = get_blog_titles()
#     print("Got new Titles")
#     if old_titles != new_titles:
#         added = get_added_posts(new_titles, old_titles)
#         deleted = get_deleted_posts(new_titles,old_titles)
#         msg = "VidhuKant.com has updated"
#         if len(added) > 0:
#             msg += "\nThe Following Post(s) were added:\n" + "\n".join(added)
#         if len(deleted) > 0:
#             msg += "\nThe Following Post(s) were deleted:\n" + "\n".join(deleted)
#         print("Sending Mail")
#         sendmail(msg)
#     old_titles = new_titles
Product.init_database()
p1 = Product("scooter", amazon_link="hello")
# p1.myntra_link = "bye guys"
p1.add()
print (Product.get_all_products())
# p1.update()
# p1.email_ids= "reachsakshichoudhary@gmail.com,vidhukant@vidhukant.com"
# p1.notify()
# p1.amazon_link = "bye kandi"
# p1.delete()
# p1.notify()
# p2 = Product("BB CC cream" , amazon_link="yuzi")
# p2.email_ids = "reachsakshichoudhary@gmail.com,vidhukant@vidhukant.com"
# p2.notify()
# price1 = get_amazon_price("https://www.amazon.in/dp/B0FQFYXCC4")
# price2 = get_flipkart_price("https://www.flipkart.com/lakm-9-5-cc-cream-foundation/p/itm49820099a5c31?pid=FNDEVYMY53JCQZU7&lid=LSTFNDEVYMY53JCQZU73AGDJF&marketplace=FLIPKART&q=lakme+cc+cream&store=g9b%2Fffi%2Fdzu%2Fgru&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=en_p8fwq7LGC_hXFVOUEAHtn7t94D-aBKe4LfF414Sh2jZJLjTHG6PmJQvpSNairdZisusPsbUaj4pICrLB1PErWfUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=sp&ppn=sp&ssid=u4r4pev7q80000001761839230506&qH=d8510c80ed04316a")
#
# print (price1)
# print (price2)