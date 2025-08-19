from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Task
from .schemas import TaskCreate, TaskUpdate

async def create_task(db:AsyncSession, task: TaskCreate):
    db_task = Task(**task.model_dump())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def get_task(db: AsyncSession, taskid: int):
    stmt = select(Task).where(Task.id == taskid)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Task).offset(skip).limit(limit))
    return result.scalars().all()


async def update_task(db: AsyncSession, task_id: int, task: TaskUpdate):
    stmt = update(Task).where(Task.id == task_id).values(**task.model_dump(exclude_unset=True))
    await db.execute(stmt)
    await db.commit()
    return await get_task(db, task_id)


async def delete_task(db: AsyncSession, task_id: int):
    task = await get_task(db, task_id)
    if task:
        await db.delete(task)
        await db.commit()
    return task