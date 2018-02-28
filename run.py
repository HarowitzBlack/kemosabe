
from flask import Flask,request
from .handler import Handler


app = Flask(__name__)

# for verification
@app.route('/hook',methods=['GET'])
def verify_webhook():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == verify_token:
            return request.args.get("hub.challenge")
        return "OK",200

# webhook to get
@app.route('/hook',methods=['POST'])
def handle_incomming_responses():
    if request.method == 'POST':
      	# get the response
        response_data = request.get_json()
        # create a dict with action and map them to a function.
        # Function names can be anything. But the action must
        # begin with '@'
        event_dict = {
            "@get_started":get_started,
            "@coffee":coffee,
        }
        Handler(response_data,event_dict)
        return "OK",200
