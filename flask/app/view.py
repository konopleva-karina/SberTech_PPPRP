from flask import Flask
import os
import requests

app = Flask(__name__)


@app.route('/numberinfo/<number>', methods=['GET'])
def get_info_about_number(number):
    import logging
    logging.basicConfig(filename='error.log', level=logging.DEBUG)

    if not str(number).isdecimal():
        return f'<p1>{number} is not a decimal number</p1>'
    return requests.get(f"http://numbersapi.com/{number}").content


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
