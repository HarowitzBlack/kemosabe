
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
        Handler(response_data,actions)
        return "OK",200

def get_started(entity_dict):
    user_id = entity_dict['id']
    p_str = p.create_payload(action="sup",custom_text="what up dawg!",coffee="capachino")
    p_str1 = p.create_payload(action="crapday",custom_text="that's sad!",coffee="espresso")
    bot.quick_reply(user_id,"Hello",[
                    ("sup",p_str,"text"),
                    ("had a crap day",p_str1,"text")
    ])

def say_hello(entity_dict):
    user_id = entity_dict['id']
    cust_msg = entity_dict['custom_text']
    cust_msg += "Do ya like {0}?".format(entity_dict['coffee'])
    bot.send_text_message(user_id,cust_msg)

def crap_day(entity_dict):
    user_id = entity_dict['id']
    cust_msg = entity_dict['custom_text'] + "An {0} should take the pressure down.".format(entity_dict['coffee'])
    bot.send_text_message(user_id,cust_msg)




if __name__ == '__main__':
    app.run(debug=True,port=8741,threaded=True)
