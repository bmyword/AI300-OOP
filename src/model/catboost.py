from abc import ABC, abstractmethod
from config import CATBOOST_MODEL_FILEPATH, CHOSEN_CATBOOST_PARAMS
from catboost import CatBoostClassifier


class Model:
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
    def load(self):
        '''Load trained model from file'''
        pass

    @abstractmethod
    def save(self):
        '''Save trained model to file'''
        pass


class CatBoostModel(Model):

    def __init__(self):
        self.model = CatBoostClassifier(**CHOSEN_CATBOOST_PARAMS)

    def train(self, X, y):
        feature_cols = list(X.columns)

        object_col_idx = []
        for col_name in feature_cols:
            if X[col_name].dtype == 'object':
                object_col_idx.append(feature_cols.index(col_name))

        print('Training Catboost model...', end='', flush=True)
        self.model.fit(X, y, cat_features=object_col_idx, verbose=False)
        print('done.')
        return self

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)[:, 1]

    def load(self):
        self.model.load_model(CATBOOST_MODEL_FILEPATH)
        return self

    def save(self):
        self.model.save_model(CATBOOST_MODEL_FILEPATH)
        return self
