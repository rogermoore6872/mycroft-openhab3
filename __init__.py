from mycroft import MycroftSkill, intent_file_handler


class Openhab(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('openhab.intent')
    def handle_openhab(self, message):
        self.speak_dialog('openhab')


def create_skill():
    return Openhab()

