from inspect import Parameter
import sqlalchemy as db
from core.database import database
from .schemas import ErrorRequest
from .models import error_logs_table

async def write_log_errors(value: ErrorRequest):
    '''writing logs to the database'''
    

    async with database.transaction():
        await database.execute(
            query=error_logs_table.insert().values(**value.dict())
        )
