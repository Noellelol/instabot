# install Instabot 'pip install instabot'

# now lets go and import Instabot in our project
from instabot import Bot
bot = Bot() #we declared a variable with name bot you can name it whatever you want

# now time for us to login
bot.login(username="your insta username",password="your insta password")

# alright so We logged in with our Instagram account! But now we have to upload an image on Instagram 

bot.upload_photo("your image.jpg",caption="Instagram Bot tutorial")

# and that's it!! Yay! 

# ⚠️ Important - Make sure to delete config file before running it!
