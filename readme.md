

## Kemosabe - Bot building framework for messenger

Kemosabe is a bot building framework for Messenger built on top of Flask. It is simple and quite easy
to use. It scales pretty well too. It supports most of the Messenger API componants.
The core idea behind Kemosabe is to not worry about spending too much time, thinking
about how to link different interactions, or features so that the resulting outcome
is seamless.

## prerequisite

```
    virtualenv -p python3 caffbot # for python3 env
    source bin/activate           

```

## Installation

```
  pip3 install kemosabe
```


## Examples - Echo Bot

Here's an example of a simple an echo bot

app.py
```python

import kemosabe,views

events = {
    "@get_started":views.get_started,
    "@text":views.text,
}

bot = kemosabe.Kemosabe(events)
bot.set_keys(api_key="<api_key>",verify_key="<verify_key>")

if __name__ == "__main__":
    bot.run(port=5622,debug=True)

```

create views.py to create events.

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

Create a configs.json file with "api_key" and "verify_key" as keys in it.
```json

  { "api_key":"<cdcfvfv>","verify_key":"<key>" }

```
# A little bit of theory 📻

## Events

Every Interaction or event must be encupsulated within a function. And each function
can do one or more tasks. Now each function must be mapped with an event-tag.
(An event-tag is basically a string that corresponds to a function. It can be created
like this "@someevent". The event-tag must start with an '@'). Then the events are passed
into a function where it waits for the events to trigger.

## Session Object

Each function you create gets a session object. This object contains the 'important stuff'.
Here the 'important stuff' is the response sent by the user. Typically, the
response sent by the user is a massive JSON object. But the internal parser
picks the important stuff and puts them into the session object. The session object
contains the user's id, the message sent by the user, the action that the user triggered
and developer created variables, etc.

So, what's the point of this? Well, keeping track of variables that are necessery
for the future interaction is really crucial. It defines how smart your bot is.
You wouldn't want to build a dumb bot that can't remember stuff right? The other reason
for the session object is that messenger app doesn't offer space to store sessions unlike
browsers which do. The only problem with the session object is it's not permanent. It only
persists for a single future interaction, because it gets updated by the new session object.
So you better store the important stuff in a database.




copyright (c) 2018 Joel Benjamin
