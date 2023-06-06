from abc import ABC, abstractmethod
from dotenv import dotenv_values
import pandas as pd
from sqlalchemy import create_engine


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
    '''
        OOP-styled code for loading dataset from database.
        Since queries are read-only, we can use an alternative method
        to the one from Lesson 02 Notebook, which is easier to read.
    '''

    config = dotenv_values()  # Bonus: Load secrets from external .env file

    def __init__(self):
        self.database = self._get_database_engine()
        self.query = 'SELECT * FROM loans'

    def load(self, query=None):
        # If custom SQL query not provided, use default query
        if query is None:
            query = self.query
        print('Loading dataset from database...')
        return pd.read_sql(query, self.database)

    def _get_database_engine(self):
        host = self.config.get('DB_HOST')
        user = self.config.get('DB_USER')
        password = self.config.get('DB_PWD')
        db = self.config.get('DB_NAME')

        return create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}')
