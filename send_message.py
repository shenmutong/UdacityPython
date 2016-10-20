from twilio.rest import TwilioRestClient

account_sid = "ACe712e8a527f10f9800e4f6c8239ca11a" # Your Account SID from www.twilio.com/console
auth_token  = "c38a99b967eb6ea8dca705f5c2b353a3"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+8613625298662",    # Replace with your phone number
    from_="+12052363497") # Replace with your Twilio number

print(message.sid)