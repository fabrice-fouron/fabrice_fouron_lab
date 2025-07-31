from minio import Minio
from fastapi import FastAPI

app = FastAPI()

@app.route("/save-files")
async def upload_file():
    return save_file()

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
    
