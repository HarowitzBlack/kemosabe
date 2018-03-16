




Demo Bot                                                                             |  echo bot
:-----------------------------------------------------------------------------------:|:-------------------------:
 <img src="https://github.com/HarowitzBlack/kemosabe/blob/master/images/demo1.gif">  |  <img src="https://github.com/HarowitzBlack/kemosabe/blob/master/images/echo_demo.gif">

### Kemosabe - Bot building framework for messenger

Kemosabe is a bot building framework for Messenger built on top of Flask.
You can create you're own interaction flow very quickly. You can add tons
of interactions just by creating functions for each of the events. Kemosabe supports
most of the Messenger API componants. So you don't have to worry about using another
external wrapper or anything.

The core idea behind Kemosabe is to build a good flow with less code.


follow me on twitter [@harowitzblack](https://twitter.com/HarowitzBlack) to get updates

See how to build different types of bots in the [examples](https://github.com/HarowitzBlack/Kemosabe-examples)

#### Installation

```
pip3 install kemosabe
```


#### Here's an example of a simple an echo bot

##### create views.py to create events.

```python
  import kemosabe

  # triggered when the get started button is tapped
  def get_started(session):
      uid = session.id
      kemosabe.send_text_message(uid,"Hello there!")

  # triggered when any text is sent. This event just sends an echo of the message
  def text(session):
      uid = session.id
      kemosabe.send_text_message(uid,session.text)

```

Wait, How do you run this? Well, to run this you have to create the main application,
views.py just contains events.

##### app.py
```python
import kemosabe,views
# map events to function
events = {
    "@get_started":views.get_started,
    "@text":views.text,
}

# set events and configs
bot = kemosabe.Kemosabe(events)
bot.set_keys(api_key="<api_key>",verify_key="<verify_key>")

if __name__ == "__main__":
    # runs the bot using Gunicorn
    bot.run(port=4999)
```

You don't have to run the bot using any external WSGI servers, Kemosabe runs Gunicorn
internally.

##### Create a configs.json file with "api_key" and "verify_key" as keys in it.
```json

  { "api_key":"<key>","verify_key":"<key>" }

```

Check out echobot example here - https://github.com/HarowitzBlack/Kemosabe-examples


### Messenger API Componants and how to use them 🖥

### Quick Reply Buttons

<img src="https://github.com/HarowitzBlack/kemosabe/blob/master/images/qk.jpeg" width="600" height="270">


```python

  # create action
  altered_carbon = kemosabe.create_action(action='tvshow',type='altered_carbon')
  # create quick reply payload
  payload = (
            ["Altered Carbon 👨‍🎤",altered_carbon,"text"],
            ...
            ...
 )
 # send the payload
 kemosabe.send_quick_reply(uid,"What's your favorite TV show? 📺",payload)

```

In the first line you create an action so that whenever a user taps the button something happens.
The action param requires an event-string which is mapped to a function in the event dict. The
event-string acts as a callback which calls the function when the user taps on the button. The next
param is defined by you. It can be anything, these additional params act as meta-data which gives info
on the action. It'll be loaded in the session object, so any data passed here could be used inside a function.

Next we create the buttons. Each button is represented as a list. You can create any number of lists,
then you pack it into a tuple. That becomes the payload. Inside the list the first value is the text you want
to show on the button, the second value is the action you created earlier, and third is the type, which is text for
all quick reply buttons. That's it! Then you send the payload to the user.

### Generic Templates / Cards

<img src="https://github.com/HarowitzBlack/kemosabe/blob/master/images/card.jpeg" width="400" height="400">

```python

cards = {"element_data":[
                          {
                                "data":["Title Button 1","image_link","Description text","link to website"],\
                                "button":["web_url","link to website","button text"]
                          },
                          {
                                "data":["Title Button 2","image_link","Description text","link to website"],\
                                "button":["payload","@action","button text"]
                          },
                          ...

]}
kemosabe.send_card_templates(uid,cards)

```

##### Method 1

There are 2 ways to send a Card. The above method is one way. You can add more cards just by adding
a dictionary to the `element_data` list. To create a card the card dictionary takes 2 key-value list pairs.
The first one is `data`, and it contains the important information to display the card (like image,card title etc).
And the second one is `button`, it contains the information required to construct the button. The button list
takes 3 parameters - Type,link/action and text on the button. Type can be of 2 types - web_url or payload.
If you set the type to web_url then the next parameter must be a link. If you set the type to payload, the 2nd parameter
must be a valid event-tag. This method is good when you have to generate buttons on the fly. Just put it through a loop
and feed in the required data (Look at the examples).

##### Method 2

The other way is to use the `send_card_templates_raw(user_id,json_payload)` method. This method lets you pass
the JSON payload/dict directly. This method is good when your content is not dynamic. Store the data in some JSON
file and feed it to this method.

```python
raw = {"payload": {
    "template_type":"generic",
    "elements":[
      <GENERIC_TEMPLATE>,
      <GENERIC_TEMPLATE>,
      ...
    ]
  }
}
# see https://developers.facebook.com/docs/messenger-platform/send-messages/template/generic

kemosabe.send_card_templates_raw(user_id,raw)

```



### Events dict

Every Interaction or event must be encupsulated within a function. Now each function must
be mapped with an event-tag. An event-tag is basically a string that corresponds to a function.
It can be created like this "@some_event". The event-tag must start with an '@'.

```python

events = {
  "@get_started":hello,
  "@text":text_function,
  "@dotask":some_task,
}

```

`@get_started` and `@text` are mandatory event tags. `@get_started` sends the greeting text when
a user taps on the get started button. And `@text` function is triggered when a user types something
into the text box and sends it.

### Session Object

Each function you create gets a session object. This object contains the
users data (user id,message,location,..) and the meta-data that you passed in when
you created an action. You can use them inside a function by accessing it's attributes.
To get the users id you do `session.uid`. To access the meta-data you do `session.whatever_variable_name_you_passed_in`.
Remember the session object only remembers everything for a single request,so don't expect it
to remember everything forever.

```python

def some_task(session):
  user_id = session.id
  msg = session.text
  print(user_id)
  print(msg)

```

### Persistent Menu

You can set the Persistent Menu using the run() methods `set_menu` parameter.
Default is None, which will use a basic menu with a start over button triggering '@get_started'.

```python
menu = {
  "persistent_menu":[
      {
        "locale":"default",
        "composer_input_disabled": false,
        "call_to_actions":[
          {
              "title":"Take me to Wonderland",
              "type":"postback",
              "payload":"@some_task"
          }
        ]
      }
  ]
}

bot.run(port=4999,set_menu=menu)

```

To trigger an event when someone clicks on a menu button, simple set the payload key to the
event tag you want to launch (Remember, the event-tag you set must be mapped with a function).

### Enabling or Disabling text input

<img src="https://github.com/HarowitzBlack/kemosabe/blob/master/images/text.jpeg" width="400" height="300">

To Enable/Disable the text input simple set the `enable_text` parameter to `True or False` in
the run() method.

```python

# enables text input when set to true. Set to false to disable it.
bot.run(port=4999,enable_text=True)

```


#### Todo  🔨📻

- [ ] Add all Messenger componants
- [ ] recieve Image, video and audio
- [ ] Trigger event when location,image,video or audio is sent.
- [ ] Integration with NLP platforms (wit.ai,dialogflow)


###### Copyright ©️ 2018 Joel Benjamin
