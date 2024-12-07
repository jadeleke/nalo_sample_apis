import requests

# URL for the API
url = "http://email.nalosolutions.com/smsbackend/clientapi/Nal_resl/send-email/"

# Payload with email details, including HTML content in the emailBody
payload = {
    'key': 'your_key_here',  # Replace with your actual key
    'emailTo': 'hh@gmail.com',  # Replace with recipient's email
    'emailFrom': 'hello@gmail.com',  # Sender's email address
    'emailBody': """
    <html>
        <body>
            <h1>Welcome to Our Email Service</h1>
            <p>This is a test email sent via API with an attachment.</p>
            <p>Please find the attached file for your reference.</p>
        </body>
    </html>
    """,
    'senderName': 'Email API Key',
    'subject': 'Email API Test with File Attachment and HTML'
}

# File to attach
files = [
    ('attach_file', ('emailupload.pdf', open('/path/to/emailupload.pdf', 'rb'), 'application/pdf'))
]

# Empty headers (can be updated if the API requires additional headers)
headers = {}

# Make the POST request
response = requests.request("POST", url, headers=headers, data=payload, files=files)

# Print the response from the API
print(response.text)
