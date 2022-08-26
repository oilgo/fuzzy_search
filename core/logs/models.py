from core.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func

class ErrorLogs(Base):
    '''logs of services errors'''

    __tablename__ = 'error_logs'
    error_logs_id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    error_code = Column(Integer)
    error_description = Column(String(500))
    user_ip = Column(String(15))
    error_date = Column(DateTime(timezone=True), server_default=func.now())
    error_source = Column(String(100))


error_logs_table = ErrorLogs.__table__