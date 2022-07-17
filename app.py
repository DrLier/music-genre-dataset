from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model_dt.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    like, provokasi, komentar, emosi = [x for x in request.form.values()]

    data = []

    data.append(int(like))
    data.append(int(provokasi))
    data.append(int(komentar))
    data.append(int(emosi))


    prediction = model.predict([data])
    if prediction==1 :
        output = "Hoax"
    else:
        output = "Bukan Hoax"

    return render_template('index.html', prediction=output, like=like, provokasi=provokasi, komentar=komentar, emosi=emosi)


if __name__ == '__main__':
    app.run(debug=True)
