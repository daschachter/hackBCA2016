from twilio.rest import TwilioRestClient
import random

server_number = "+17328585355"

account_sid = "ACd6f0c8c85add0a0e31a2d7e1205aaf3e"
auth_key = "0cc58ee26f28be4873d169f0d2f196f9"

server = TwilioRestClient(account_sid, auth_key)

people = {}
questions = {"What day is it?":"{Sunday}", "What's the score?":"{88}", "Why?":"{Twilio}"}

def getQuestion():
    return questions.keys()[random.randint(0, 2)]

def clear():
    for m in server.messages.list():
        if m.status != "queued":
            server.messages.delete_instance(m.sid)

def send(number):
    server.messages.create(to=number, from_=server_number, body=people[number])

def congratulate(number):
    server.messages.create(to=number, from_=server_number, body="congratulations!")

def printLs(ls):
    for i in ls:
        print(i.body)
        print("-" * 50)

clear()
people["+19086705435"] = getQuestion()
send("+19086705435")

while True:
    messages = server.messages.list()

    for message in messages:
        if '{' in message.body:
            congratulate("+19086705435")
            people["+19086705435"] = getQuestion()
            send("+19086705435")
    printLs(messages)
    clear()
    print("*" * 100)
    printLs(messages)
