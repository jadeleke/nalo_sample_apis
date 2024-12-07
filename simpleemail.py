import requests

BASE_URL = "https://email.nalosolutions.com/smsbackend/clientapi/Nal_resl"

def send_email(
    key: str,
    email_to: list,
    email_from: str,
    email_body: str,
    sender_name: str,
    subject: str,
    callback_url: str = ""
   # template: str = "default"
):
    """
    Sends an email using the Nalo Solutions Email API with key for authentication.
    """
    endpoint = f"{BASE_URL}/send-email/"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "key": key,  # Replacing username and password with key
        "emailTo": email_to,
        "emailFrom": email_from,
        "emailBody": email_body,
        "senderName": sender_name,
        "subject": subject,
        "callBackUrl": callback_url
     #   "template": template
    }
    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        print(f"Request Payload: {payload}")  # Debugging: Print the payload
        print(f"Response Status Code: {response.status_code}")  # Debugging: Print the response code
        print(f"Response Content: {response.text}")  # Debugging: Print the response content
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
   # Replace these with actual values
    key = "your_key_here"  # Use your valid API key
    email_to = ["alexander@gmail.com"]
    email_from = "kapper@gmail.com"
    email_body = (
        "To get your live account enabled, please follow the instructions below..."
    )
    sender_name = "Alex"
    subject = "Pushing the limit with Mina And Pk"
    callback_url = ""
   # template = "test with Alex"

    result = send_email(
        key,
        email_to,
        email_from,
        email_body,
        sender_name,
        subject,
        callback_url
      #  template
    )
    print(result)
