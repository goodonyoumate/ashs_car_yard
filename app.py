from flask import Flask, render_template

app = Flask(__name__)

cars = [
    {'name': 'Toyota Corolla', 'price': '$15,000', 'image': 'https://via.placeholder.com/800x400?text=Toyota+Corolla'},
    {'name': 'Honda Civic', 'price': '$18,000', 'image': 'https://via.placeholder.com/800x400?text=Honda+Civic'},
    {'name': 'Ford Ranger', 'price': '$25,000', 'image': 'https://via.placeholder.com/800x400?text=Ford+Ranger'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cars')
def cars_page():
    return render_template('cars.html', cars=cars)

@app.route('/contactus')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
