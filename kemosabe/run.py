
from flask import Flask,request
from .configs import configurations
from .events import Events
from .handler import Handler



flask_app = Flask(__name__)
cfg = configurations()
events = Events()


# for verification
@flask_app.route('/hook',methods=['GET'])
def verify_webhook():
    # gets the verification token from the config object
    # It's set in the __init__.py file
    verify_token = cfg.get()["verify_key"]
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == verify_token:
            return request.args.get("hub.challenge")
        return "OK",200

# webhook to get
@flask_app.route('/hook',methods=['POST'])
def handle_incomming_responses():
    if request.method == 'POST':
      	# get the response
        response_data = request.get_json()
        # loads the events from the Event class
        # the Kemosabe class in __init.py sets the event dict
        event_dict = events.load_events()
        Handler(response_data,event_dict)
        return "OK",200
