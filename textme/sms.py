from twilio.rest import Client 
 
account_sid = 
auth_token = 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12253145542', 
                              body ='',       
                              to='' 
                          ) 
 
print(message.sid)