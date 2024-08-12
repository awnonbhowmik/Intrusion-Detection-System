from twilio.rest import Client

def send_sms_alert(message, to_number):
    account_sid = "your_account_sid"  # Replace with your Twilio account SID
    auth_token = "your_auth_token"    # Replace with your Twilio auth token
    from_number = "your_twilio_number"  # Replace with your Twilio phone number
    
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(f"SMS sent to {to_number}: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS to {to_number}: {e}")
