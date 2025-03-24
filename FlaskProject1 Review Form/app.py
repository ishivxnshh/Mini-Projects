from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('temp.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    section = request.form['section']
    roll = request.form['roll']
    year = request.form['year']
    rating = request.form['rating']
    feedback = request.form['feedback']

    # Create a string with the form data
    data_str = f"Name: {name}, Section: {section}, Roll: {roll}, Year: {year}, Rating: {rating}, Feedback: {feedback}\n"

    # Write the form data to a text file
    with open('user_data.txt', 'a') as file:
        file.write(data_str)

    return "Thank you for your feedback!"

if __name__ == '__main__':
    app.run(debug=True)