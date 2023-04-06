from fastapi import FastAPI, Response, status
from pydantic import BaseModel, parse_file_as
import datetime
import os
import json
import glob
app = FastAPI()

# @app.get('/')

# def get_hello_world():
#     return{"answer":"Hello World!"}

# @app.get('/items/{item_id}')
# def get_item(item_id:int):
#     return{"item_id":item_id}

activities_folder = "activities"

class Activity(BaseModel):
    id: int
    name: str
    date: datetime.datetime

def find_activity(activity_id=0):
    return glob.glob(os.path.join(activities_folder, f'*{activity_id}.json'))


@app.post('/activity/get/all')
def get_activity():
    res = []
    files = find_activity()
    if files:
        for file in files:
            res.append(parse_file_as(Activity, file))
    return res

@app.post('/activity/get/{activity_id}')
def get_activity(activity_id:int, response:Response):
    file = find_activity(activity_id)
    if file:
        return parse_file_as(Activity, file[0])


@app.post('/activity/add/{activity_id}')

def add_activity(activity_id:int, activity:Activity, response:Response):

    file = find_activity(activity_id)
    if file:
        response.status_code = status.HTTP_302_FOUND
        return False
    else:
         with open(os.path.join(activities_folder,f'activity_{activity_id}.json'),'w') as f:
            f.write(activity.json())
    return True    


@app.post('/activity/add/{activity_id}')
def update_activity(activity_id:int, activity:Activity, response:Response):
        file = find_activity(activity_id)
        if file:
            pass
        response.status_code = status.HTTP_302_FOUND