from fastapi import APIRouter, HTTPException, status

from tasks.models import Task
from tasks.service import TaskService

task_service = TaskService()
router = APIRouter()


@router.get("/tasks")
def get_all():
    return task_service.get_all()


@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create(item: Task):
    return task_service.create(item)


@router.get("/tasks/{item_id}")
def get_one(item_id: int):
    task = task_service.get_one(item_id)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Item not found")


@router.put("/tasks/{item_id}")
def update(item_id: int, updated: Task):
    result = task_service.update(item_id, updated)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/tasks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int):
    if task_service.delete(item_id):
        return None
    raise HTTPException(status_code=404, detail="Item not found")
