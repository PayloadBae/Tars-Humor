from mycroft import MycroftSkill, intent_file_handler


class MovieBotQuotes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('quotes.bot.movie.intent')
    def handle_quotes_bot_movie(self, message):
        self.speak_dialog('quotes.bot.movie')


def create_skill():
    return MovieBotQuotes()

