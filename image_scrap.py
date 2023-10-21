import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os 

save_dir = "images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

query = "sudhanshu kumar ineuron"
response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")
