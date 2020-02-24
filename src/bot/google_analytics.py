from os import getenv

from dotenv import load_dotenv
from universal_analytics import HTTPRequest, Tracker

from bot.commands import Command
from bot.search import SearchInline

load_dotenv()


class GoogleAnalyticsClient:

    def __init__(self, update, context):
        self.update = update
        self.context = context

    def push_command(self, command: Command):
        """Pushes a command event to the Google Analytics"""
        data = {
            'command': command.COMMAND,
            'args': self.context.args or [],
            'user_id': self.update.message.from_user.id,
            'chat_id': self.update.message.chat_id,
        }
        with HTTPRequest() as http:
            tracker = Tracker(getenv('GOOGLE_ANALYTICS_KEY'), http, client_id=self.update.message.from_user.id)
            tracker.send("event", "command", data)

    def push_button(self, button):
        """Pushes a pressed button event to the Google Analytics"""
        data = {
            'button': button.CALLBACK_NAME,
            'user_id:': self.update.message.from_user.id,
            'chat_id': self.update.message.chat_id,
        }
        with HTTPRequest() as http:
            tracker = Tracker(getenv('GOOGLE_ANALYTICS_KEY'), http, client_id=self.update.message.from_user.id)
            tracker.send("event", "button", data)

    def push_search(self, search_inline: SearchInline):
        """Pushes a search event to the Google Analytics"""
        user_input = self.update.inline_query.query
        entity_type = search_inline.get_entity_type(user_input)
        query = search_inline.get_query(user_input, entity_type)
        data = {
            'search': search_inline.INLINE,
            'search_type': entity_type,
            'query': query,
            'user_id:': self.update.message.from_user.id,
            'chat_id': self.update.message.chat_id,
        }
        with HTTPRequest() as http:
            tracker = Tracker(getenv('GOOGLE_ANALYTICS_KEY'), http, client_id=self.update.message.from_user.id)
            tracker.send("event", "search", data)
