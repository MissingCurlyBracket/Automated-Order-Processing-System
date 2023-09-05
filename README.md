# !! NOTE: source code is not included as we do not have permission to publish it !! 

# Automated Order Processing System For Real World Clients

Client: Unetiq BV

Coach: Thomas Overklift

TA: Oskar Lorek

# Description
The project aims to create an order processing system that when used by a client it will automatically read their uploaded PDFS/Excels and process them into an editable order.
This stage of the project will focus on parsing and understanding the semi-structured Excel data.
If time allows, the team will also look into the processing of the PDF type of files.
The project will be developed as a full stack application but it does not have to be a final product, rather a high fidelity prototype.
The project will be developed for Unetiq BV, which are also our client.
This project has been created as part of the CSE2000 - Software Project course provided by TU Delft.

# Running the Project

In order to run the project you need to run:
1. Install prerequisites
2. Compile the **Frontend**
3. Activate the server, Django **Backend** application

# Prerequsites
- React
- Python version 3.8 +
- pip package for python
- vitualenv package
`sudo pip3 install virtualenv`

# In order to run the application as a whole, the following steps are required.

## 1. Create a empty virtual environment and install the requirements.
**Mac OS** 

create environment
`virtualenv env`

activate the environment
`source venv/bin/activate`

install requirements
`pip install -r requirements.txt`

check if all requirements are installed
`pip freeze`

deactivate environment
`deactivate`

**Windows OS** 

create environment
`python3 -m venv envname`

cd into this env : `cd envname`

activate the created environment : `.\sample_venv\Scripts\activate`

install all the needed requirements from requirements.txt file : `pip install -r requirements.txt`

check if all requirements are installed : `pip freeze
`
deactivate environment : `deactivate`


## 2. Compile the frontend application locally
update dependencies: `cd backend/frontend` `npm install`

to run the application without server connection `npm start`

the app will be run on `localhost:3000`

**the next step is a must**

to build the static files for the server connection `npm run build`

now a build folder will apear in the repository

## 3. Run the server
from the outmost folder `cd backend`

to start the server `python manage.py runserver`

now the whole application will be available on `localhost:8000`

in order to see all available endpoints go to `localhost:8000/api`

## 4. Testing the application

to test the backend functions `./manage.py test --noinput orderprocess` from outermostFolder/backend

to test backend checkstyle `pycodestyle --statistics --ignore=E501,W503,E722,E128  backend`, ignores a few checkstyle rules

to test frontend `CI=false npm test -- --watchAll=false` from outermostFolder/backend/frontend, ignores warrnings

## 5. Database

**Note: database used for this project will be shutdown after project termination in agreement with client.**


# Usage
After running the project, users can upload Excel or PDF files by clicking the "+" 
button on the search-bar. After uploading and processing the user can view the result
and edit it if they wish. Then, the user may wish to add the products to the basket. Users can 
also manually add products by using the search functionality. The database of products 
is extracted form the Furning.com catalogue of products.
# Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

# Authors and acknowledgment
- Lucian Negru
- Kendra Sartori
- Radu Constantinescu
- Ahmed Ibrahim
- Manar Al-Robayi

# License
This project is licensed by Unetiq BV.
# Project status
Project is in development until the 19th of June 2022.
