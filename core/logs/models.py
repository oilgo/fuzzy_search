from core.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func


class ErrorLogs(Base):
    """ Logs of services errors model
    """

    __tablename__ = "error_logs"

    error_logs_id = Column(
        Integer, 
        primary_key = True, 
        index = True, 
        unique = True, 
        autoincrement = True)

    error_code = Column(
        Integer,
        nullable = False,
        comment = "HTTP code error")

    error_description = Column(
        String(500),
        nullable = False,
        comment = "Error text")

    user_ip = Column(
        String(15),
        server_default = "127.0.0.1")

    error_date = Column(
        DateTime(timezone = True), 
        server_default = func.now())

    error_source = Column(
        String(100),
        nullable = False,
        comment = "Path to the file where the error occurred")

error_logs_table = ErrorLogs.__table__