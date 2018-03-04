
# Use as notes in tutorials

# this creates a payload string. It can be passed
# into quick reply function. The action parameter
# is the same as the key in the event dict that we created in app.py
# the only difference is that the action doesn't have an '@' (the func automatically adds it in the
# begining). So what basically happens is, we map the action 'coffee' to the quick reply button.
# When someone taps on the button it launches the coffee()function.
# the next parameter is optional, and it's developer defined. You can name it anything you want.
# Just remember this, anything after the action parameter goes into the session object to be accessed.

# Now you create the reply payload. It is a tuple with lists as items.
# Each list is a quick reply button. The first argument inside the list
# is the text you want to display. The second is the payload string, we
# stored it in a coffee variable so pass it on. The third is a type. The only
# supported type is text. That's it


# get the variable from the last interaction
# As I said earlier, you can access the parameters passed as a variable
# Use it to do your thing. Make comparisons or what not!
