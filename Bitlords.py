import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Format: age, gender (0 for male, 1 for female), weight, height, BMI, blood pressure, diabetic)
#our data has been taken from kaggle, cdc and UCI ML repository
data = np.array([
    [35,0,70,170,24.2,120,0],
    [45,1,65,165,26.9,130,1],
    [50,0,80,175,27.1,140,1],
    [42,0,70,168,24.8,118,0],
    [45,1,65,165,23.9,120,0],
    [47,1,68,160,26.6,125,0],
    [45,0,72,170,25.9,120,1],
    [48,1,70,168,24.8,128,0],
    [43,0,72,170,24.9,126,0],
    [41,1,66,162,25.1,127,0],
    [58,1,70,168,28.8,128,1],
    [44,0,85,180,25.2,128,1],
    [56,1,68,167,24.9,129,1],
    [59,1,69,169,25.2,125,1],
    [43,1,72,166,26.1,128,0],
    [41,0,79,177,25.2,130,0],
    [48,1,71,170,24.6,127,0],
    [44,0,76,174,24.1,125,0],
    [40,0,73,171,23.9,122,0],
    [43,1,68,167,24.4,123,0],
    [42,0,74,173,24.7,125,0],
    [63,1,72,166,26.1,130,1],
    [43,0,79,177,25.2,135,1],
    [46,0,73,171,24.9,128,1],
    [57,0,76,174,25.1,132,1],
    [46,0,73,171,24.9,128,1],
    [46,1,64,163,24.1,128,0],
    [15,0,62,183,18.5,118,0],
    [18,0,70,180,20.1,110,0],
    [14,0,50,163,15.5,110,0]
])

X = data[:, :-1]
Y = data[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

age=input('Enter your age: ')
gender=input('Enter your gender (0 for male, 1 for female): ')
weight=input('Enter your weight(kg): ')
height=input('Enter your height(cm): ')
blood_pressure=input('Enter your blood pressure: ')
bmi=703*((float(weight)*2.204)/((float(height)*0.397)**2))#we have taken the formula from https://www.calculator.io/bmi-calculator/

new_sample = np.array([[age,gender,weight,height,bmi,blood_pressure]])
new_sample_scaled = scaler.transform(new_sample)
prediction = model.predict(new_sample_scaled)
if prediction[0] == 1:
    print("You may have diabetes. It is highly recommended you take a fasting blood sugar test")
else:
    print("You have a low chance of having diabetes, though it is still reccomended you take a fasting blood sugar test just in case. However, we dont think it is absolutely necesary.")
