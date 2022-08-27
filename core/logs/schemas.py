from core.database import database
from .models import error_logs_table


class ErrorRequest:
    """ 
    """
    
    error_code: int
    error_description: str
    user_ip: str
    error_source: str

    def __init__(self, error_code, error_description, user_ip, error_source) -> None:

        self.error_code = error_code
        self.error_description = error_description
        self.user_ip = user_ip
        self.error_source = error_source

    
    async def write_log_errors(self):
        """ Error logging method in the database
        """

        async with database.transaction():
            await database.execute(
                query=error_logs_table.insert().values(
                    {
                        "error_code": self.error_code, 
                        "error_description": self.error_description, 
                        "user_ip": self.user_ip, 
                        "error_source": self.error_source
                    }))