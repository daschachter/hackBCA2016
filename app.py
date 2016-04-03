from twilio.rest import TwilioRestClient

# account_sid = "ACe79ec9f6f876dba8d755f4ef2030944e"
account_sid = "ACd6f0c8c85add0a0e31a2d7e1205aaf3e"

# auth_token = "ea57cc52800bba1495b9f3142aa830c7"
auth_token = "0cc58ee26f28be4873d169f0d2f196f9"

client = TwilioRestClient(account_sid, auth_token)

messsages = client.messages.list()

print (messages[0].body)
