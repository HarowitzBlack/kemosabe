
# THIS FILE IS INDENPENDENT AND DOESN'T DEPEND ON THE BOT FRAMEWORK
# JUST FOR TESTING

from flask import Flask,request


app = Flask(__name__)

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
        response_data = request.get_json()
        actions = {
            "@get_started":get_started,
            "@sup":say_hello,
            "@crapday":crap_day,
        }
        return "OK",200


if __name__ == '__main__':
    app.run(debug=True,port=8741,threaded=True)
