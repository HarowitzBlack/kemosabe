
import kemosabe

def get_started(session):
    uid = session.id
    kemosabe.send_text_message(uid,"Hey there😉!")
    coffee = kemosabe.create(action="coffee",like_it=True)
    nocoffee = kemosabe.create(action="coffee",like_it=False)
    reply = (["I like coffee ☕️",coffee,"text"],["I hate coffee 🤢",nocoffee,"text"],)
    kemosabe.send_quick_reply(uid,"Do you like coffee?",reply)

def coffee(session):
    uid = session.id
    like_it = session.like_it
    if like_it:
        kemosabe.send_text_message(uid,"Great! I ❤️ coffee too.")
    else:
        kemosabe.send_text_message(uid,"Oh, Too bad☹️. I love coffee.")

def fallback(session):
    uid = session.id
    kemosabe.send_text_message(uid,"Sorry this feature is not implemented yet")
