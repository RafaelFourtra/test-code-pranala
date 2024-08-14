from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-bilangan-ganjil', methods=['POST'])
def generateBilanganGanjil():
    try:
        number = int(request.form['angka'])
        odd_numbers = [i for i in range(1, number + 1) if i % 2 != 0]
        return jsonify(odd_numbers=odd_numbers)
    except ValueError:
        return jsonify(error="Please enter a valid number"), 400

def is_prima(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True  

@app.route('/generate-bilangan-prima', methods=['POST'])
def generateBilanganPrima():
    try:
        number = int(request.form['angka'])
        result = is_prima(number)
        return jsonify(is_prima=result)
    except ValueError:
        return jsonify(error="Please enter a valid number"), 400

def segitiga(number):
    str_number = str(number)
    segitiga_list = []
    length = len(str_number)
    for i in range(1, length + 1):
        # Create each line of the triangle
        if i <= length:
            digit = str_number[i - 1]  # Get the digit from the input number
            line = digit * i  # Repeat the digit i times
            segitiga_list.append(line)
    return segitiga_list 

@app.route('/generate-segitiga', methods=['POST'])
def generateSegitiga():
    try:
        number = int(request.form['angka'])
        segitiga_result = segitiga(number)  
        return jsonify(segitiga=segitiga_result)  
    except ValueError:
        return jsonify(error="Please enter a valid number"), 400

if __name__ == '__main__':
    app.run(debug=True)
