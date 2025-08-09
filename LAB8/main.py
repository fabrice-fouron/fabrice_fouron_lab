from minio import Minio
from fastapi import FastAPI
import smtplib
from email.message import EmailMessage
from redis import Redis
from pydantic import BaseModel

app = FastAPI()

students = {
    '1': {
        'first_name': 'Fabrice',
        'last_name': 'Fouron',
        'grad_year': 2025
    },
    '2': {
        'first_name': 'John',
        'last_name': 'Doe',
        'grad_year': 2024
    }
}

class StudentInfo(BaseModel):
    id: str
    first_name: str
    last_name: str
    grad_year: int

@app.get("/save-files")
async def upload_file():
    return save_file()

@app.get("/new-email")
async def new_email():
    return send_email()

@app.post("/set-user-info")
async def set_info(student_info: StudentInfo):
    return set_student_info(student_info)

@app.get("/get-user-info")
async def get_info(student_id: str):
    return get_student_info(student_id)

def save_file():
    try:
        client = Minio('localhost:9000', access_key='username', secret_key='password', secure=False)

        try:
            client.make_bucket('newbucket')
        except Exception:
            print("The buck already exists")

        client.fput_object('newbucket', 'bucket_file_to_save.txt', 'file_to_save.txt')
        client.fput_object('newbucket', 'bucket_another.txt', 'another.txt')

        objects = client.list_objects('newbucket', recursive=True)
        for obj in objects:
            print(obj.object_name, "was successfully saved in the container!")
        return "All Good!"
    except Exception as e:
        return f"There was an error: {e}"

# The email bounces, I am not sure why
def send_email():
    msg = EmailMessage()
    msg.set_content("This is a test email from localhost")
    msg["Subject"] = "Hello World"
    msg["From"] = "test@localhost"
    msg["To"] = "fouronf@wit.edu"

    try:
        with smtplib.SMTP("localhost", 25) as server:
            server.send_message(msg)
        return "Email was sent"
    except Exception as e:
        print(e)
        return "Error"

red = Redis(host='localhost', port=6379, decode_responses=True, password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81')

def set_student_info(student_info):
    try:
        red.hset(f'{student_info.id}', mapping={
            "first_name": student_info.first_name,
            "last_name": student_info.last_name,
            "grad_year": student_info.grad_year
        })
        return "Successful"
    except Exception as e:
        print("There was an error trying to access run the redis server")
        print(e)
        return "Failed"

def get_student_info(id):
    try:
        temp = red.hgetall(id)
        print(temp)
        return temp
    except Exception:
        print("There was a problem getting the user info.")
