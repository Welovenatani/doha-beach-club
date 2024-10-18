from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the booking page (GET for form, POST for submission)
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        # Capture form data
        name = request.form['name']
        email = request.form['email']
        event = request.form['event']
        # Handle the booking (e.g., save to database or process)
        return render_template('booking_success.html', name=name, event=event)
    return render_template('book.html')

# Route for the events page
@app.route('/events')
def events():
    return render_template('events.html')

# Route for the rewards page
@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

# Route for the booking success page
@app.route('/booking_success')
def booking_success():
    return render_template('booking_success.html')

if __name__ == '__main__':
    app.run(debug=True)
