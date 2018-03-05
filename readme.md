

## Kemosabe - Bot building framework for messenger

Kemosabe is a bot building framework for Messenger built on top of Flask. It is simple and quite easy
to use. It scales pretty well too. It supports most of the Messenger API componants.
The core idea behind Kemosabe is to not worry about spending too much time, thinking
about how to link different interactions, or features so that the resulting outcome
is seamless.

## Installation

``` 
  pip3 install kemosabe
```


## Examples - CaffineBot

Here's an example of a simple bot that asks you if you like coffee or not.

app.py
```python

    import kemosabe, views

    # create a bot object
    bot = kemosabe.Kemosabe()

    bot.set_configuration(api_key="<key>",verify_key="<key>")

    # create an event dict and map the functions to event-tags
    events = {
      "@get_started":views.get_started,
      "@coffee":views.coffee,
    }

    # pass in the events to the bot
    bot.set_events(events)

    if __name__ == "__main__":
      # run the bot
      bot.run(port=8011,debug=True)

```

views.py
```python
    import kemosabe

    # create a get started function. Triggers when the user taps on the get started button
    def get_started(session):
        # access the session obj to get the user id
        uid = session.id
        # use this to send a text message
        kemosabe.send_text_message(uid,"Hey there!")
        coffee = kemosabe.create(action="coffee",like_it=True)
        # same as above, you can create multiple payloads.
        nocoffee = kemosabe.create(action="coffee",like_it=False
        reply = (["I like coffee",coffee,"text"],["I hate coffee",nocoffee,"text"],)
        # Now send it the the user with a text message
        kemosabe.send_quick_reply(uid,"Do you like coffee?",reply)

    def coffee(session):
        uid = session.id
        like_it = session.like_it
        # if the user tapped on the 'like coffee' button this is excecuted
        if like_it:
            kemosabe.send_text_message(uid,"Great! I love coffee.")
        else:
        # If the user tapped on 'hate coffee' button, this is excecuted.
            kemosabe.send_text_message(uid,"Ah! Too bad. I love coffee.")

```


# How it works?

## Inner workings

Every Interaction or event must be encupsulated within a function. And each function
must only do one task. It can do many tasks(more on this later) nothings stopping you
from doing it. The only problem is that the resultant will be messy. Now each function
must be mapped with an event-tag. (An event-tag is basically a string that corresponds
to a function. It can be created like this "@someevent". The event-tag must start with
an '@'). Then the events are passed into a function where it waits for the events to
trigger.

## Session variables

Every function gets a session object. This object contains the 'important stuff'.
Here the 'important stuff' is the response sent by the user. Typically, the
response sent by the user is a massive JSON object. But the internal extractor
picks the important stuff and puts them into the session object. The session object
contains the user's id, the message sent by the user, the action that the user triggered
and developer created variables. Yeah, you can put anything into it.

So, what's the point of this? Well, keeping track of variables that are necessery
for the future interaction is really crucial. It defines how smart your bot is.
You wouldn't want to build a dumb bot that can't remember stuff right? The other reason
for the session object is that messenger app doesn't offer space to store sessions unlike
browsers which do. The only problem with the session object is it's not permanent. It only
persists for a single future interaction, because it gets updated by the new session object.
So you better store the important stuff in a database.


copyright (c) 2018 Joel Benjamin
