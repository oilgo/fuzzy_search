class DataBase:

    def __init__(self):
        self.host = ''
        self.port = ''
        self.password = ''
        self.port = '5432'
        self.dbname = ''
        self.conn = None
        logging.basicConfig(level=logging.INFO)