import requests

from bs4 import BeautifulSoup

class Home():
    def __init__(self,
                 name:str,
                 price:str,
                 info:str,
                 location:str
                 ) -> None:

        self.name = name
        self.location = location
        self.info = info
        self.price = price

    def __str__(self) -> str:
        return self.name
    
    def get_info(self):
        return f"""======================================================================================================================
        Название: {self.name}
        Местоположение: {self.location}
        Описание: {self.info}
        Цена: {self.price}
        """
        
URL = 'https://krisha.kz/prodazha/kvartiry/karaganda/?page='

response = requests.get(f'{URL}2')
soup = BeautifulSoup(response.text,'html.parser')
my_list = soup.find_all(attrs={'class':'a-card__inc'})
homes:list[Home] = []
for tag in my_list:
    name_home = (tag.find(class_='a-card__title').text)
    location_home = (tag.find(class_='a-card__subtitle').string)
    info_home = (tag.find(class_='a-card__text-preview').text)
    price_home = (tag.find(class_='a-card__price').text)

    hotels = Home(
        name= name_home,
        location = location_home,
        price= price_home,
        info = info_home
    )
    homes.append(hotels)
  
for i in homes:
    print(i.get_info())





