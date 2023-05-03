
from flask import Flask, render_template, request
import pandas as pd
import pickle

app: object = Flask(__name__)

model= pickle.load(open(r"C:\Users\ravi2\Desktop\Meritorium\Deep Learning\Project\Project_4\LinearregressionModel.pkl", 'rb'))#loading data in LinearRegressionModel
auto_mpg = pd.read_csv(r'C:\Users\ravi2\Desktop\Meritorium\Deep Learning\Project\Project_4\Cleaned auto-mpg.csv')

@app.route('/', methods=['GET'])
def index():
     cylinders = sorted(auto_mpg['cylinders'].unique())
     origin = sorted(auto_mpg['origin'].unique())
     car_name = sorted(auto_mpg['car_name'].unique())
     return render_template('index.html', cylinders=cylinders, origin=origin, car_name=car_name)


@app.route('/predict', methods=['POST'])
def predict():
     car_name= request.form.get('car_name')
     cylinder= int(request.form.get('cylinders'))
     displacement = float(request.form.get('displacement'))
     horsepower = float(request.form.get('horsepower'))
     weight = int(request.form.get('weight'))
     acceleration = float(request.form.get('acceleration'))
     model_year = int(request.form.get('model_year'))
     origin = request.form.get('origin')

     prediction=model.predict(pd.dataFrame([[car_name, cylinders, displacement, horsepower, weight, acceleration, model_year, origin]], columns=['car_name', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin']))
     print(prediction[0])
     return str(prediction[0])



if __name__=="__main__":
    app.run(debug=True)
