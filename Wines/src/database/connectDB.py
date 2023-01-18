import sqlite3

from ..core.directorymanager import directory, dbase_folder, dbase_name


class ConnectDB:
    def __init__(self) -> None:
        with directory(dbase_folder):
            self.connection = sqlite3.connect(dbase_name)
            self.cursor = self.connection.cursor()

    def execute(self, sql, param=None) -> list:
        with self.connection:
            if param != None:
                self.cursor.execute(sql, param)
            else:
                self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def executemany(self, sql, param=None) -> list:
        with self.connection:
            if param != None:
                self.cursor.executemany(sql, param)
            else:
                self.cursor.executemany(sql)
        return self.cursor.fetchall()

    def __close(self) -> None:
        if self.connection:
            self.connection.close()
            self.connection = None

    def __del__(self) -> None:
        self.__close()
