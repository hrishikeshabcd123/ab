from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

    
