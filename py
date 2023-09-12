from balebot.filters import *
from balebot.models.messages import *
from balebot.handlers import MessageHandler
from balebot.updater import Updater
updater = Updater(token="Token",loop=asyncio.get_event_loop(73352422:8wGC1cRy7uSxGkDbVhfeHCKKXZqSWraKTGKpzFUP))
dispatcher = updater.dispatcher
@dispatcher.message_handler(TextFilter())
def echo(bot, update):
    message = TextMessage('Hello')
    bot.reply(update, template_message)
