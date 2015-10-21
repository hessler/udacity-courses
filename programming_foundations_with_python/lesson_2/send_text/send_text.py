# Note: This script will NOT work in its current state, since the Account Sid,
# Auth Token, and phone numbers are placeholders. They need to be replaced with
# legitimate values in order to properly execute.

from twilio.rest import TwilioRestClient

# Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token  = "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="Hello from Python Send Text script!",
    to="+18005551234",    # My mobile phone number
    from_="+18005550000") # My Twilio number

print message.sid
