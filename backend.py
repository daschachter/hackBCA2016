from flask import Flask, render_template, request, redirect
import jinja2
import os
from twilio.rest import TwilioRestClient

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html")
	
	
@app.route('/sms', methods=["POST"])
def sms():
	Number = request.form['Number']
	Answer = request.form['Answer']
	client = TwilioRestClient("ACd5e1907fbd1bc4c99d0c26fe4cbd2efc", "164ef73f252586d49da5de900a08b131")
	message = client.messages.create(to=Number, from_="+17328585355", body="Welcome to CTS (Capture The Swag)!")
    
    toAdd = "**add**: " + Number
    
    client.messages.create(to="+17328585355", from_="+17328585355", body=toAdd)
	return message.sid
	
@app.route('/change')
def chance():
	return redirect('/')

@app.route('/post', methods=['GET','POST'])
def post():
	if request.method == 'POST':
		return render_template('post.html')
	return render_template('get.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)