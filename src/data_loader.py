from abc import ABC, abstractmethod
from dotenv import dotenv_values
import pandas as pd
import pymysql


class DataLoader(ABC):
    '''
      Provide DataLoader interface for documentation purposes.
      Used for CSVDataLoader and DBDataLoader.
    '''
    @abstractmethod
    def load(self):
        pass


class CSVDataLoader(DataLoader):
    '''
      Implements load() method with pandas read_csv functionality
    '''
    def load(self, file_path="data/loans.csv"):
        print('Loading CSV data...')
        return pd.read_csv(file_path)


class DBDataLoader(DataLoader):
    '''OOP-styled code adapted from Lesson 02 Notebook'''

    config = dotenv_values()  # Load secrets from .env file

    def __init__(self):
        self.conn = self.connect_to_database()
        self.query = 'SELECT * FROM loans'

    def load(self, query=None):
        # If custom SQL query not provided, use default query
        if query is None:
            query = self.query

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
            self.conn.commit()
            return pd.DataFrame(cursor.fetchall())
        except Exception as ex:
            print(f'Error when retrieving records: {ex}')
            raise ex

    def connect_to_database(self):
        try:
            connection = pymysql.connect(
                host=self.config.get('DB_HOST'),
                port=self.config.get('DB_PORT', 3306),
                user=self.config.get('DB_USER'),
                passwd=self.config.get('DB_PWD'),
                db=self.config.get('DB_NAME'),
                cursorclass=pymysql.cursors.DictCursor
            )
            print('[+] Database Connection Successful.')
            return connection

        except Exception as ex:
            print(f'[+] Database Connection Failed: {ex}')
            raise ex
