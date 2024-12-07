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
):
    """
    Sends an email using the Nalo Solutions Email API with key for authentication and HTML body.
    """
    endpoint = f"{BASE_URL}/send-email/"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "key": key,  # Replacing username and password with key
        "emailTo": email_to,
        "emailFrom": email_from,
        "emailBody": email_body,  # This can now include HTML content
        "senderName": sender_name,
        "subject": subject,
        "callBackUrl": callback_url
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
    email_body = """
    <html>
        <body>
            <h1>Welcome to Our Service</h1>
            <p>To get your live account enabled, please follow the instructions below:</p>
            <ol>
                <li>Download the Independent Contractor Agreement.</li>
                <li>Sign the contract.</li>
                <li>
                    Send an email to <a href="mailto:verification@myforexfunds.com">verification@myforexfunds.com</a> with the following:
                    <ul>
                        <li>Your full name</li>
                        <li>Phase 2 account number</li>
                        <li>Signed contract</li>
                        <li>Proof of identity card</li>
                        <li>Proof of address document</li>
                    </ul>
                </li>
            </ol>
            <p>Once you are done, please allow up to 48 hours for the Account Provisioning team to verify your documents and enable trading on your live account.</p>
        </body>
    </html>
    """
    sender_name = "Alex"
    subject = "Pushing the limit with Mina And Pk"
    callback_url = ""

    result = send_email(
        key,
        email_to,
        email_from,
        email_body,
        sender_name,
        subject,
        callback_url
    )
    print(result)
