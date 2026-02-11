# MLR_PROJECT
🏠 House Price Prediction using Multiple Linear Regression
📌 Project Overview

This project implements a Multiple Linear Regression (MLR) model from scratch to predict house prices based on multiple input features such as bedrooms, bathrooms, living area, lot size, and other house-related attributes.

The model is built using Python and NumPy, without relying on machine learning libraries for training, to understand the mathematical working of multiple linear regression.

A Flask web application is developed to provide a user-friendly interface where users can enter house details and get the predicted price instantly.

🎯 Objective

To understand the mathematical implementation of Multiple Linear Regression.

To build a regression model without using built-in ML training functions.

To deploy the model using Flask.

To create an interactive frontend for prediction.

Dataset Description

The dataset contains the following features:

bedrooms

bathrooms

sqft_living

sqft_lot

floors

waterfront

view

condition

sqft_above

sqft_basement

yr_built

yr_renovated

city

country

day
month

year

Target Variable:

price
🧠 Model Description

The Multiple Linear Regression model follows the equation:

​

 → Input features

The coefficients are calculated manually using statistical formulas
⚙️ Technologies Used

Python

NumPy

Pandas

Flask

HTML & Bootstrap

Pickle (Model Serialization)
MLR_House_Price_Prediction/
│
├── app.py
├── MPP_MODEL.pkl
├── data.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── css/
        └── style.css
git clone https://github.com/your-username/MLR_House_Price_Prediction.git
pip install -r requirements.txt
python app.py
http://127.0.0.1:5000/
