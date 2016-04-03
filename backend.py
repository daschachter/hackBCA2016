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
        print("IN")
	Number = request.form['Number1']
	print("IN2")
	#Answer = request.form['Answer']
	print("IN3")
	client = TwilioRestClient("ACd6f0c8c85add0a0e31a2d7e1205aaf3e", "0cc58ee26f28be4873d169f0d2f196f9")
        print("IN4")
	message = client.messages.create(to="+1" + str(Number), from_="+17328585355", body="Welcome to CTS (Capture The Swag)!")
        print("IN5")
        toAdd = "**add**:" + Number
        print("IN6")
        client.messages.create(to="+17328585355", from_="+17328585355", body=toAdd)
	return "OK"
	
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
