
# THIS FILE IS INDENPENDENT AND DOESN'T DEPEND ON THE BOT FRAMEWORK
# JUST FOR TESTING

from flask import Flask
from flask import request
from handler import Handler


verify_token = "bot"
ACCESS_TOKEN = "EAAExpe5DqoQBAHrqGU2xq4atYfT216fIh58cTCpSKINOawr4lLqDKZAudzxlycaAFMsstx5HhObIrfUp8aetisdcMZApr3eYZC8RHEEmTruZC5zxeZA3RdPdByhP5vESwDahME1cFrvtpdue5pR0CEVbiMLjbBS4FDmxAz8YUHwZDZD"
app = Flask(__name__)

@app.route('/hook',methods=['GET'])
def verify_webhook():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == verify_token:
            return request.args.get("hub.challenge")
        return "OK",200


# recieve messages and pass it to some function which parses it further
@app.route('/hook',methods=['POST'])
def handle_incomming_responses():
    if request.method == 'POST':
        response_data = request.get_json()
        Handler(response_data)
        return "OK",200



if __name__ == '__main__':
    app.run(debug=True,port=8741,threaded=True)
