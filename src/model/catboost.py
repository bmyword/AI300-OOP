from abc import ABC, abstractmethod
from config import CATBOOST_MODEL_FILEPATH, CHOSEN_CATBOOST_PARAMS
from catboost import CatBoostClassifier
import joblib


class Model(ABC):
    '''
      Interface used for CatBoostModel.
      This class serves the purposes of
      (1) Documentation, if your teammates wish to understand how to use it
      (2) Extending this interface or "template" to other models
    '''
    @abstractmethod
    def train(self, X, y):
        '''Train model with features and labels'''
        pass

    @abstractmethod
    def predict(self, X):
        '''Generate binary predictions (0/1) from trained model'''
        pass

    @abstractmethod
    def predict_proba(self, X):
        '''Generate prediction probabilities from trained model'''
        pass

    @abstractmethod
    def load(self, input_file_path):
        '''Load trained model from file'''
        return joblib.load(input_file_path)

    @abstractmethod
    def save(self, model, output_file_path):
        '''Save trained model to file'''
        joblib.dump(model, output_file_path)


class CatBoostModel(Model):

    def __init__(self):
        self.model = CatBoostClassifier(**CHOSEN_CATBOOST_PARAMS)

    def train(self, X, y):
        cat_features = list(X.select_dtypes(include='object').columns)

        print('Training Catboost model...', end='', flush=True)
        self.model.fit(X, y, cat_features=cat_features, verbose=False)
        print('done.')
        return self

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)[:, 1]

    def load(self):
        self.model = super().load(CATBOOST_MODEL_FILEPATH)
        return self

    def save(self):
        super().save(self.model, CATBOOST_MODEL_FILEPATH)
        return self
