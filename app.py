# Flask web application for Ash's Car Yard
from flask import Flask, render_template

app = Flask(__name__)

# Sample car inventory data
cars = [
    {'name': 'Toyota Corolla', 'price': '$15,000', 'image': 'https://via.placeholder.com/800x400?text=Toyota+Corolla'},
    {'name': 'Honda Civic', 'price': '$18,000', 'image': 'https://via.placeholder.com/800x400?text=Honda+Civic'},
    {'name': 'Ford Ranger', 'price': '$25,000', 'image': 'https://via.placeholder.com/800x400?text=Ford+Ranger'}
]

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Display cars with carousel
@app.route('/cars')
def cars_page():
    return render_template('cars.html', cars=cars)

# Contact page route
@app.route('/contactus')
def contact():
    return render_template('contact.html')

# Run Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
