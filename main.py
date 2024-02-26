import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def track_website_changes(url):
    previous_content = fetch_website_content(url)
    while True:
        current_content = fetch_website_content(url)
        if current_content != previous_content:
            # Notify user about changes
            print("Website has been updated!")
            previous_content = current_content

# Example usage
url_to_track = "https://www.capitoltrades.com/trades"
track_website_changes(url_to_track)

# WIP
# Project to send email notifications and phone notifications when a website has been updated.

# import requests
# from bs4 import BeautifulSoup
# from firebase_admin import credentials, messaging, initialize_app
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Firebase initialization
# cred = credentials.Certificate("Projects/website-updater/website-notifications-2e3cc-firebase-adminsdk-2t18v-4349da3e20.json")  # Path to your service account key file
# firebase_app = initialize_app(cred)

# # Email configuration
# def send_email(receiver_email, subject, body):
#     sender_email = "kylehek123@gmail.com"  # Replace with your email
#     sender_password = "your_password"  # Replace with your email password

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))

#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.send_message(message)

# # Function to send push notification via FCM
# def send_push_notification(token, title, body):
#     message = messaging.Message(
#         notification=messaging.Notification(title=title, body=body),
#         token=token,
#     )
#     messaging.send(message)

# # Function to fetch website content
# def fetch_website_content(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return None

# # Function to track website changes
# def track_website_changes(url, email, fcm_token):
#     previous_content = fetch_website_content(url)
#     while True:
#         current_content = fetch_website_content(url)
#         if current_content != previous_content:
#             # Notify user about changes via email
#             subject = "Website Update Notification"
#             body = "Website has been updated!"
#             send_email(email, subject, body)
            
#             # Notify user about changes via FCM
#             title = "Website Update Notification"
#             body = "Website has been updated!"
#             send_push_notification(fcm_token, title, body)
            
#             previous_content = current_content

# # Example usage
# url_to_track = "https://example.com"
# receiver_email = "your_email@example.com"  # Replace with your email
# fcm_token = "your_fcm_token"  # Replace with your FCM token
# track_website_changes(url_to_track, receiver_email, fcm_token)