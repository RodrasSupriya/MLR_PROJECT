# MLR_PROJECT
📌 Project Overview

The House Price Prediction project aims to estimate house prices based on various input features using Machine Learning techniques. The system analyzes housing parameters such as area, number of bedrooms, bathrooms, and other relevant attributes to predict the expected price of a house.

This project demonstrates the complete machine learning workflow including data preprocessing, model training, evaluation, and deployment using a Flask web application.

🎯 Problem Statement

Determining accurate house prices manually is difficult due to multiple influencing factors. This project provides an automated solution that predicts house prices efficiently using machine learning, helping buyers, sellers, and real estate analysts make informed decisions.

🚀 Features

Data preprocessing and cleaning

Multiple Linear Regression model implementation

Model training and evaluation

Accuracy evaluation using performance metrics

Model serialization using Pickle

Flask-based web interface for prediction

User-friendly input form for real-time predictions

🛠️ Technologies Used

Programming Language: Python

Libraries: NumPy, Pandas, Scikit-learn

Web Framework: Flask

Frontend: HTML, CSS

Model Storage: Pickle

📂 Project Structure
House-Price-Prediction/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── model/
│   └── house_price_model.pkl
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction


2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv


Activate environment:

venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Application

Start the Flask server:

python app.py


Open your browser and navigate to:

http://127.0.0.1:5000/


Enter the house details and get the predicted price instantly.

🤖 Machine Learning Model

Algorithm Used: Multiple Linear Regression

Model trained using housing dataset

Features include:

Area

Number of Bedrooms

Number of Bathrooms

Additional housing parameters

The trained model is saved using Pickle and loaded during application runtime.

📊 Model Evaluation

The model performance is evaluated using:

R² Score

Mean Squared Error (MSE)

Prediction accuracy comparison

🔮 Future Enhancements

Improve prediction accuracy using advanced regression models

Add more housing features

Deploy application on cloud platforms

Add graphical data visualization

User authentication for saving predictions
