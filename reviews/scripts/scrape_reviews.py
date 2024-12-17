import requests
from bs4 import BeautifulSoup

#Scraping =>  from site web-scrapping.dev
    # دانلود صفحه اطلاعات
def scrape_reviews():
    url = "https://web-scraping.dev/reviews"
    response = requests.get(url)
    if response.status_code == 200:
        print('commande a bien été exécutée')
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup.prettify())
    else:
        print(f"Erreur lors de la requête : {response.status_code}")
        
        
def run():
    scrape_reviews()
    #python manage.py shell >  برای اجرای این دستور میتوانیم دستورات بالا را در پایتون شل اجرا کنیم با ایمپرت های مربوطه اش 
    #from reviews.scripts.scrape_reviews import run  => استفاده از این سه دستور در ترمینال میشه پنج ردیف اول رو دید
    #run()
    
    