from twilio.rest import TwilioRestClient
import random
import time

server_number = "+17328585355"

account_sid = "ACd6f0c8c85add0a0e31a2d7e1205aaf3e"
auth_key = "0cc58ee26f28be4873d169f0d2f196f9"

server = TwilioRestClient(account_sid, auth_key)

class Game:
    def __init__(self):
        self.players = []
        self.questions = {}

    def addPlayer(self, player):
        print("ADDING: " + str(player.number))
        for p in self.players:
            if p.number == player.number:
                return
        self.players += [player]

    def addQuestion(self, question, flag):
        flag = self.formatFlag(flag)
        if not question in self.questions:
            self.questions[question] = flag

    def formatFlag(self, flag):
        if flag[0] == '{' and flag[len(flag) - 1] == '}':
            return flag
        else:
            return '{' + flag + '}'

    def answer(self, playerNumber, flag):
        for p in self.players:
            if p.number == playerNumber:
                if p.questions[len(p.questions) - 1] == flag:
                    print("CORRECT")
                    assignQuestion(self, playerNumber)
                    break
        print("DONE")

    def assignQuestion(self, playerNumber):
        for p in self.players:
            if p.number == playerNumber:
                if len(p.questions) != len(self.questions) and p.inProgress == False:
                    print("ASSIGNING")
                    print(p.inProgress)
                    time.sleep(2)
                    question = self.questions.keys()[random.randint(0, len(self.questions) - 1)]
                    while p.hasAnswered(question):
                        print(question)
                        question = self.questions.keys()[random.randint(0, len(self.questions) - 1)]
                    p.send(question, True)
                    p.inProgress = True
                    return
                else:
                    p.send("You have answered all questions currently available", False)
                    p.inProgress = False
                break
                        

    def printPlayers(self):
        print("Players:")
        for player in self.players:
            print("\t" + player.number)

    def printQuestions(self):
        print("Questions:")
        for question in self.questions.keys():
            print("\t" + question)
    

class Player:
    def __init__(self, number):
        self.number = number
        self.questions = []
        self.inProgress = False

    def send(self, question, asking):
        print("PROGRESS: " + str(self.inProgress))
        print("QUESTION: " + question)
        server.messages.create(to=self.number, from_=server_number, body=question)
        if asking:
            self.questions += [question]


    def hasAnswered(self, question):
        for i in self.questions:
            if i == question:
                return True
        return False
