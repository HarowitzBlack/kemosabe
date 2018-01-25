
# THIS FILE IS INDENPENDENT AND DOESN'T DEPEND ON THE BOT FRAMEWORK
# JUST FOR TESTING

from flask import Flask
from flask import request
from handler import Handler
import botutils




verify_token = "bot"
ACCESS_TOKEN = "EAAExpe5DqoQBAHrqGU2xq4atYfT216fIh58cTCpSKINOawr4lLqDKZAudzxlycaAFMsstx5HhObIrfUp8aetisdcMZApr3eYZC8RHEEmTruZC5zxeZA3RdPdByhP5vESwDahME1cFrvtpdue5pR0CEVbiMLjbBS4FDmxAz8YUHwZDZD"
app = Flask(__name__)
bot = botutils.Messenger_wrapper(ACCESS_TOKEN)


botutils.get_started_btn()


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
        }
        Handler(response_data,actions)
        return "OK",200

def get_started(entity_dict):
    user_id = entity_dict['id']
    bot.quick_reply(user_id,"Hello",[("sup","@sup","text")])

def say_hello(entity_dict):
    user_id = entity_dict['id']
    bot.send_text_message(user_id,"nothing much!")



if __name__ == '__main__':
    app.run(debug=True,port=8741,threaded=True)
