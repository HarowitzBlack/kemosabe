

## Kemosabe - Bot building framework for messenger

Kemosabe is a bot building framework for Messenger built on top of Flask. It is simple and quite easy
to use. It scales pretty well too. It supports most of the Messenger API componants.
The core idea behind Kemosabe is to not worry about spending too much time, thinking
about how to link different interactions, or features so that the resulting outcome
is seamless.

## Installation

comming soon...


## Code - CaffineBot

app.py
```

    import kemosabe, views

    # create a bot object
    bot = kemosabe.Kemosabe()

    # set the configs. Configs must be in a json file
    bot.set_configuration(read_from="keys.json")

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
```
    import kemosabe

    # create a get started function. Triggers when the user taps on the get started button
    def get_started(session):
        # access the session obj to get the user id
        uid = session.id
        # use this to send a text message
        kemosabe.send_text_message(uid,"Hey there!")

        # this creates a payload string. It can be passed
        # into quick reply function. The action parameter
        # is the same as the key in the event dict that we created in app.py
        # the only difference is that the action doesn't have an '@' (the func automatically adds it in the
        # begining). So what basically happens is, we map the action 'coffee' to the quick reply button.
        # When someone taps on the button it launches the coffee()function.
        # the next parameter is optional, and it's developer defined. You can name it anything you want.
        # Just remember this, anything after the action parameter goes into the session object to be accessed.
        coffee = kemosabe.create(action="coffee",like_it=True)
        # same as above, you can create multiple payloads.
        nocoffee = kemosabe.create(action="coffee",like_it=False)

        # Now you create the reply payload. It is a tuple with lists as items.
        # Each list is a quick reply button. The first argument inside the list
        # is the text you want to display. The second is the payload string, we
        # stored it in a coffee variable so pass it on. The third is a type. The only
        # supported type is text. That's it
        reply = (["I like coffee",coffee,"text"],["I hate coffee",nocoffee,"text"],)
        # Now send it the the user with a text message
        kemosabe.send_quick_reply(uid,"Do you like coffee?",reply)

    def coffee(session):
        uid = session.id
        # get the variable from the last interaction
        # As I said earlier, you can access the parameters passed as a variable
        # Use it to do your thing. Make comparisons or what not!
        like_it = session.like_it
        # if the user tapped on the 'like coffee' button this is excecuted
        if like_it:
            kemosabe.send_text_message(uid,"Great! I love coffee.")
        else:
        # If the user tapped on 'hate coffee' button, this is excecuted.
            kemosabe.send_text_message(uid,"Ah! Too bad. I love coffee.")

```

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
