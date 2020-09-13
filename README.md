## Тестовое задание на позицию Junior Backend разработчик 

#### Установка Docker
* [Подробное руководство по установке docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

#### Установка docker-compose

* [Подробное руководство по установке docker-compose](https://docs.docker.com/compose/install/)

### Запуск
Запуск производится командой `docker-compose up`
### Работа с сервисом
Сервер работает на `http://localhost`

Эндпоинты:

**Выдача обработанных данных**
1. Метод: **GET**
    
   В ответе содержится поле “response” со списком из 5 клиентов, потративших наибольшую сумму за весь период.

Каждый клиент описывается следующими полями:

   `username` - логин клиента;
   
   `spent_money` - сумма потраченных средств за весь период;

   `gems` - список из названий камней, которые купили как минимум двое из списка "5 клиентов, потративших наибольшую сумму за весь период", и данный клиент является одним из этих покупателей.

2. Метод: **POST**

   Аргументы:
 
   `deals`: файл, содержащий историю сделок.
   Описание полей deals.csv:
   
   `customer` - логин покупателя
   
   `item` - наименование товара  total - сумма сделки
   
   `quantity` - количество товара, шт
   
   `date` - дата и время регистрации сделки

Ответ:
 
  Status: OK - файл был обработан без ошибок;

  Status: Error, Desc: <Описание ошибки> - в процессе обработки файла произошла ошибка.
