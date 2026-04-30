# Flask web application for Ashs Cars
from flask import Flask, render_template

app = Flask(__name__)

# Sample car inventory data
cars = [
            {
                'name': 'Toyota Corolla',
                'price': '$15,000',
                'image': '/static/images/car1.jpg'
            },
            {
                'name': 'Honda Civic',
                'price': '$18,000',
                'image': '/static/images/car2.jpg'
            },
            {
                'name': 'Ford Ranger',
                'price': '$25,000',
                'image': '/static/images/car3.jpg'
            }
        ]

# Home page route


# Display cars with carousel


# Contact page route


# Run Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
