# QuickDelf

Quickdelf is a food ordering web application which is similar to leading food delivery services like Grubhub and postmates. The application is designed to order food from any of our favorite restaurants available in the city. For now, I have made a simple application without any location, but my future enhancement will be to order food based on the city we reside. The main purpose of the application is to order food based on the available restaurants and available dishes. The application consists of entire flow starting from logging in, selecting restaurant, selecting food, payment and logout.  

[Demo of QuickDelf](https://youtu.be/TdWKZPwwflM)

## Django framework:

The application was built using Django framework following MVT architecture. The entire front end was built using HTML, CSS and Bootstrap. The views in the application are class-based views which are advanced in Django framework. I have followed all the standard procedures of Django such as to register the application, use of url.py file for url mappings, use of forms.py for building forms, use of templates folder for holding all template files etc. 

## SQLite database

SQLite database is the backend for the application. I have used 4 tables for the application. The database schema is automatically created when we migrate. 

Steps to create database:

Define model of database in models.py file 
Once all the model is designed run the below commands from the root folder of the application

Python manage.py makemigrations
Python manage.py migrate

Once the above commands are used the tables will be created automatically in database. For this application it is not required because I have already created the tables and I have attached the db file with the project.

### View of the application

**Login screen**
![1](https://user-images.githubusercontent.com/17997235/40793393-e843aa96-64c1-11e8-8e0e-3a155ddc59b8.png)

**Registration Page**
![2](https://user-images.githubusercontent.com/17997235/40793394-e8528868-64c1-11e8-976d-911e9ae6bf4a.png)

**Displaying list of restaurants**
![3](https://user-images.githubusercontent.com/17997235/40793395-e85fe71a-64c1-11e8-8d3e-ac5e26deeb7d.png)

**Displaying list of dishes in Capital grill**
![4](https://user-images.githubusercontent.com/17997235/40793396-e871e8d4-64c1-11e8-854f-8321068b3153.png)

**Added Lobster and Grand Plateau to cart. Select cart. It displays the dish added to cart and rate and quantity selected**
![5](https://user-images.githubusercontent.com/17997235/40793397-e8827b18-64c1-11e8-9e0a-1375b938e0e1.png)

**Payment page**
![6](https://user-images.githubusercontent.com/17997235/40793398-e8942926-64c1-11e8-9911-bd6dc985ff3b.png)

**If wrong information is given payment will not be successful.**
![7](https://user-images.githubusercontent.com/17997235/40793399-e8c7a7c4-64c1-11e8-9a69-aa1bf6de619b.png)

![8](https://user-images.githubusercontent.com/17997235/40793400-e8ddb802-64c1-11e8-80e3-90d6034a1988.png)

**Payment successful and message displayed to user**
![9](https://user-images.githubusercontent.com/17997235/40793401-e90c84fc-64c1-11e8-857a-dd9bbf143902.png)

**User will be redirected to homepage**
![10](https://user-images.githubusercontent.com/17997235/40793402-e91e99b2-64c1-11e8-8aea-b81cb959e09c.png)

## Admin Screen

**All the models will be displayed in the admin screen**
![11](https://user-images.githubusercontent.com/17997235/40793403-e93d1d42-64c1-11e8-8b73-9a9ee3587312.png)

**Click on hotels to view the hotel objects**
![12](https://user-images.githubusercontent.com/17997235/40793404-e95409e4-64c1-11e8-8679-1f0be4e525c1.png)

**Opening one of the hotel object**
![13](https://user-images.githubusercontent.com/17997235/40793405-e982d0f8-64c1-11e8-9784-8875d9311cf4.png)

**Hierarchy chart**
![14](https://user-images.githubusercontent.com/17997235/40793406-e9aa11fe-64c1-11e8-8133-510fd4795837.png)

**Project structure**
![15](https://user-images.githubusercontent.com/17997235/40793407-e9c95654-64c1-11e8-9451-165e6bbb7ae8.png)




