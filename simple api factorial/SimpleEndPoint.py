import time

from flask import Flask, request


# Function to calculate the factorial of a number
def calculate_factorial(n):
    result = 1
    if n > 1:
        for i in range(1, n + 1):
            result = result * i
    return result


# create the Flask app
app = Flask(__name__)


# route to queue the request
@app.route('/factorial', methods=['GET'])
def factorial_handler():
    no = int(request.args.get('no'))
    start = time.time()
    result = calculate_factorial(no)
    end = time.time()
    print(end - start)

    return str(result)


if __name__ == '__main__':
    app.run(debug=False)
