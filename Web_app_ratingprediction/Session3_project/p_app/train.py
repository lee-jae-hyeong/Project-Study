import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from category_encoders import OrdinalEncoder
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from p_app.models.list import List
from p_app.models.user import User
from p_app.naver_scr import movie, code

def model(username, name) :

    movie_name=movie(name) # cd 이전 할당 이름
    movie_data= [] # b 이전 할당 이름
    movie_data.append([username, code(movie_name)[0]])
    data = List.query.all()
    data1 = List.query.filter_by(username = username).all()
    feature =[] 
    label = []
    for i in data1 :
        feature.append([i.username, i.genre])
        label.append(i.rating)

    X_train = feature
    y_train = label
    
    encoder = OrdinalEncoder()
    X_train_encoder = encoder.fit_transform(X_train)

    X_test = encoder.transform(b)
    model = LinearRegression()
    model.fit(X_train_encoder, y_train)
    
    y_pred = model.predict(X_test)

    return y_pred
    

