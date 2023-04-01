import requests

from bs4 import BeautifulSoup

class Car():
    def __init__(self,
                 name:str,
                 price:str,
                 data:str,
                 city:str,
                 info:str
                 ) -> None:

        self.name = name
        self.data = data
        self.city = city
        self.price = price
        self.info = info

    def __str__(self) -> str:
        return self.name
    
    def get_info(self):
        return f"""======================================================================================================================
        Название машины: {self.name}
        Описание: {self.info}
        Где нахрдится машина: {self.city}
        дата размещения: {self.data}
        Цена: {self.price}
        """
        
URL = 'https://kolesa.kz/cars/?page='

response = requests.get(f'{URL}3')
soup = BeautifulSoup(response.text,'html.parser')
my_list = soup.find_all(attrs={'class':'a-card__info'})
cars:list[Car] = []
for tag in my_list:
    name_car = (tag.find(class_='a-card__link').text) 
    city_car = (tag.find(class_='a-card__param').text)
    price_car = (tag.find(class_='a-card__price').text)
    data_car = (tag.find(class_='a-card__param a-card__param--date').text)
    info_car = (tag.find(class_='a-card__description').text)

    cars_info = Car(
        name = name_car,
        city = city_car,
        price= price_car,
        data = data_car,
        info = info_car
    )
    cars.append(cars_info)
  
  
for i in cars:
    print(i.get_info())

