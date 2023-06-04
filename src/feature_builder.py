from data_preprocessor import DataPreprocessor
from config import TARGET_COL


class FeatureBuilder:
    '''
      This class uses DataPreprocessor to clean data during __init__.
      Underscore prefix used for internal-access methods.
      Feature Engineering steps are documented in:
      build_train_set() and build_test_set().
    '''

    def __init__(self, df):
        self.df = DataPreprocessor(df).get_clean_dataset()
        self._validate_df()  # Optional: best practice to validate inputs

    def build_train_set(self):
        '''
          Returns model_input (X) and labels (y) for training.
          Requires target column to be present
        '''
        self._add_income_features()

        X = self.df.drop(columns=TARGET_COL)
        y = self.df[TARGET_COL]
        return X, y

    def build_test_set(self):
        '''Returns model_input (X) for predictions.'''
        self._add_income_features()

        # Drop target column if it exists
        X = self.df.drop(columns=TARGET_COL, errors='ignore')
        return X

    def _validate_df(self):
        df_cols = self.df.columns
        check_columns = ['applicant_income', 'coapplicant_income',
                         'loan_amount']
        for col in check_columns:
            assert col in df_cols, f"Required column {col} not found. "\
                f"List of Dataset Columns: {list(df_cols)}"

    def _add_income_features(self):
        self.df['total_income'] = self.df['applicant_income']\
            + self.df['coapplicant_income']
        self.df['loan_amt_income_ratio'] = self.df['loan_amount']\
            / self.df['total_income']
        return self.df
