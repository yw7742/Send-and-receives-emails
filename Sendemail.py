# mars_emails.py
import requests
from random import choice

rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

def get_mars_photo(sol, api_key='DEMO_KEY'):
    params = {'sol': sol, 'api_key': api_key}
    response = requests.get(rover_url, params).json()
    photos = response['photos']
    return choice(photos)['img_src']

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

sg = SendGridAPIClient(os.environ.get('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'))

def send_mars_email(from_email, to_email, img_url):
    message = Mail(
        from_email=from_email,
        to_emails=yw7742@nyu.edu,
        subject='Here is your Mars Rover picture',
        html_content=f'<strong>Check out this Mars pic</strong><br><img src="{img_url}"></img>'
    )
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)

# app.py
from flask import Flask, request
from mars_emails import send_mars_email, get_mars_photo

app = Flask(__name__)

@app.route('/email', methods=['POST'])
def email_response():
    from_email = request.form['from']
    to_email = request.form['to']
    body = request.form.get('text', '1000')

    if body.isdigit():
        img_url = get_mars_photo(body)
    else:
        img_url = get_mars_photo('1000')

    send_mars_email(to_email, from_email, img_url)
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)

