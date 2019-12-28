from os import getenv

from dotenv import load_dotenv
from universal_analytics import HTTPRequest, Tracker

load_dotenv()


class GoogleAnalyticsClient:

    @staticmethod
    def push_command(command):
        """TODO: Test and add arguments, user and chat info"""
        with HTTPRequest() as http:
            tracker = Tracker(getenv('GOOGLE_ANALYTICS_KEY'), http, client_id=getenv('GOOGLE_ANALYTICS_CLIENT_ID'))
            tracker.send("event", "command", command.COMMAND)

    @staticmethod
    def push_button(button):
        raise NotImplementedError

    @staticmethod
    def push_search(search_inline):
        raise NotImplementedError
