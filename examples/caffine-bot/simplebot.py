
import kemosabe, views

bot = kemosabe.Kemosabe()
bot.set_keys(api_key="<key>",
             verify_key="bot")

events = {
    "@get_started":views.get_started,
    "@coffee":views.coffee,
    "@fallback":views.fallback,
}

bot.set_events(events)

if __name__ == "__main__":
    bot.run(port=5002,debug=True)
