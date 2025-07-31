from minio import Minio
from fastapi import FastAPI
import smtplib
from email.message import EmailMessage

app = FastAPI()

@app.get("/save-files")
async def upload_file():
    return save_file()

@app.get("/new-email")
async def new_email():
    return send_email()

def save_file():
    try:
        client = Minio('localhost:9000', access_key='username', secret_key='password', secure=False)

        client.make_bucket('newbucket')

        client.fput_object('newbucket', 'bucket_file_to_save.txt', 'LAB8/file_to_save.txt')
        client.fput_object('newbucket', 'bucket_another.txt', 'LAB8/another.txt')

        objects = client.list_objects('newbucket', recursive=True)
        for obj in objects:
            print(obj.object_name, "was successfully saved in the container!")
        return "All Good!"
    except Exception as e:
        return f"There was an error: {e}"

# The email bonces, I am not sure if it is because I am running everything in localhost
def send_email():
    msg = EmailMessage()
    msg.set_content("This is a test email from localhost")
    msg["Subject"] = "Hello World"
    msg["From"] = "test@localhost"
    msg["To"] = "localhost"

    try:
        with smtplib.SMTP("localhost", 25) as server:
            server.send_message(msg)
        return "Email was sent"
    except Exception as e:
        print(e)
        return "Error"
