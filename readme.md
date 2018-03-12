

### Kemosabe - Bot building framework for messenger

Kemosabe is a bot building framework for Messenger built on top of Flask.
You can create you're own interaction flow very quickly. You can add tons
of interactions just by creating functions for each of the events. Kemosabe supports
most of the Messenger API componants. So you don't have to worry about using another
external wrapper or anything.

The core idea behind Kemosabe is to build a good flow with less code.


follow me on twitter [@harowitzblack](https://twitter.com/HarowitzBlack) to get updates

#### Installation

```
pip3 install kemosabe
```


#### Here's an example of a simple an echo bot

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
    bot.run(port=5622,debug=True)

```

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

##### Create a configs.json file with "api_key" and "verify_key" as keys in it.
```json

  { "api_key":"<key>","verify_key":"<key>" }

```


### Events

Every Interaction or event must be encupsulated within a function. Now each function must
be mapped with an event-string.(An event-tag is basically a string that corresponds to a function.
It can be created like this "@some_event". The event-tag must start with an '@'). Then the events
are passed into a function where it waits for the events to trigger.

### Session Object

Each function you create gets a session object. This object contains the
users data (user id,message,location,..) and the meta-data that you passed in when
you created an action. You can use them inside a function by accessing it's attributes.
To get the users id you do `session.uid`. To access the meta-data you do `session.whatever_variable_name_you_passed_in`.
Remember the session object only remembers everything for a single request,so don't expect it
to remember everything forever.


### Messenger API Componants and how to use them 🖥

###### Quick Demo on Quick Reply Buttons

![Quick Reply image](https://github.com/HarowitzBlack/kemosabe/blob/master/images/qk.jpeg)

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




#### Todo  🔨📻

- [ ] Add all Messenger componants
- [ ] recieve Image, video and audio
- [ ] Trigger event when location,image,video or audio is sent.


###### Copyright ©️ 2018 Joel Benjamin
