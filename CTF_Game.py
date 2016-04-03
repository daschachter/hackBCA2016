from twilio.rest import TwilioRestClient

server_number = "+17328585355"

account_sid = "ACd6f0c8c85add0a0e31a2d7e1205aaf3e"
auth_key = "0cc58ee26f28be4873d169f0d2f196f9"

server = TwilioRestClient(account_sid, auth_key)

class Users:
    def __init__(self):
        self.players = []

    def addPlayer(self, player):
        self.players += [player]

class Player:
    def __init__(self, number):
        self.number = number
        self.questions = []

    def askQuestion(self, question):
        server.messages.create(to=self.number, from_=server_number, body=question.text)
        self.questions += [question]

    def hasAnswered(self, question):
        for i in questions:
            if i == question:
                return True
        return False

class Question:
    def __init__(self, text, flag):
        self.text = text
        self.flag = flag
