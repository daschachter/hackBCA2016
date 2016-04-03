import CTF
import time
from twilio.rest import TwilioRestClient

server_number = "+17328585355"

account_sid = "ACd6f0c8c85add0a0e31a2d7e1205aaf3e"
auth_key = "0cc58ee26f28be4873d169f0d2f196f9"

server = TwilioRestClient(account_sid, auth_key)

mainCTF = CTF.Game()


def main_loop():

    for i in server.messages.list():
        server.messages.delete_instance(i.sid)

    nextIndex = -1
    
    while True:
        if len(server.messages.list()) > nextIndex + 1:
            messages = server.messages.list()[nextIndex:]
        else:
            messages = server.messages.list()

        sid = []

        print(len(messages))

        for m in messages:
            if isValid(m.body):
                #Check if it is a request for new member
                if isRequest(m.body):
                    p = CTF.Player(parseRequest(m.body))
                    mainCTF.addPlayer(p)
                    mainCTF.assignQuestion(p.number)
                elif isPuzzle(m.body):
                    print("IT IS A PUZZLE")
                    question, flag = parsePuzzle(m.body)
                    mainCTF.addQuestion(question, flag)
                else:
                    mainCTF.answer(m.from_, m.body)
                mainCTF.printPlayers()
                mainCTF.printQuestions()
            sid += [m.sid]
            nextIndex += 1

        time.sleep(10)

            

def isValid(message):
    return not "Thanks for the message." in message

def isRequest(message):
    return message.find("**add**:") != -1

def isPuzzle(message):
    return message.find('"') != -1 and message.find(",") != -1 and message.find("{") != -1 and message.find("}") != -1

def parseRequest(message):
    return message[message.find(":") + 1:]

def parsePuzzle(message):
    question = message[message.find('"') + 1: message.find('"', message.find('"') + 1)]
    flag = message[message.find('{'):message.find('}') + 1]
    return question, flag

main_loop()
