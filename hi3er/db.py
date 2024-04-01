import sqlite3

from model import Signet, Valk

class db_helper:
    ACRONYM = []

    def __init__(self):
        self.db_file = 'db.sqlite3'
        self.conn = None
        if not self.conn:
            self.connect()
        valks = self.get_all_valks()
        self.ACRONYM = []
        for valk in valks:
            self.ACRONYM.append(valk.acronym)

    def connect(self):
        """ Establishes a connection to the SQLite database. """
        try:
            self.conn = sqlite3.connect(self.db_file)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        """ Closes the connection to the database. """
        if self.conn:
            self.conn.close()

    def get_all_valks(self):
        """ Fetches all Valk objects from the database. """
        if not self.conn:
            self.connect()

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM bot_valk")
        
        valks = [Valk(*row) for row in cursor.fetchall()]


        return valks

    def get_valk_by_acronym(self, acronym:str):
        """ Fetches a single Valk object by ID, along with its Build name and linked Signet details (name and category). """
        if not self.conn:
            self.connect()

        cursor = self.conn.cursor()
        sql = f"""
            SELECT v.*, b.name AS build_name, s.name AS signet_name, sc.name AS category_name
            FROM bot_valk v
            INNER JOIN bot_build b ON v.id = b.valk_id
            INNER JOIN bot_build_signets sb ON b.id = sb.build_id
            INNER JOIN bot_signet s ON sb.signet_id = s.id
            INNER JOIN bot_signetcategory sc ON s.category_id = sc.id
            WHERE v.acronym = '{acronym.strip()}'
        """
        cursor.execute(sql)

        response = cursor.fetchall()
 
        signets = []
        for data in response:
            signets.append(Signet(data[-2],data[-1]))
        valk = Valk(*response[0][:-3])
        valk.build = signets
        return valk
        
