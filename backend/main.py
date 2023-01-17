
from fastapi import FastAPI
from src.schemas import Task
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/tasks/')
async def alls():
    return [format(pk) for pk in Task.all_pks()]


@app.post('/create_tasks/')
async def gettask(task: Task):
    return task.save()


def format(pk: str):
    task = Task.get(pk)
    
    return {
        'id': task.pk,
        'name': task.name,
        'complete': task.complete
    }


@app.put('/tasks_update/{pk}')
async def update(pk: str, request: Request):
    task = Task.get(pk)
    body = await request.json()
    task.comlpete = body['complete']
    return task.save()
    
    
@app.delete('/tasks_delete/{id}')
async def delete(pk: str):
    task = Task.get(pk)
    return task.delete(pk)