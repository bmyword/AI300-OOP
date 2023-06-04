from config import TARGET_COL


class DataPreprocessor:
    '''
      Data Cleaning steps are documented in get_clean_dataset()
      Underscore prefix used for internal-access methods
    '''

    def __init__(self, df):
        self.df = df.copy(deep=True)
        self._validate_df()  # Optional: best practice to validate inputs

    def get_clean_dataset(self):
        self._encode_dependents()
        for col in ['gender', 'married', 'self_employed']:
            self.df[col].fillna('Unknown', inplace=True)
        self.df.drop(columns='loan_id', inplace=True)

        if TARGET_COL in self.df.columns:
            self._binarize_column(TARGET_COL)

        return self.df

    def _encode_dependents(self):
        # Extract numeric component (e.g. '3+' -> 3 and '-1' -> -1)
        # Adapted from: https://stackoverflow.com/a/37683738
        self.df['dependents'].fillna('-1', inplace=True)
        self.df['dependents'] = self.df['dependents'].str\
            .extract(r'(-?\d+)').astype(int)

    def _binarize_column(self, col_name):
        def binarize(value):
            if value in ['Yes', 'Y']:
                return 1
            elif value in ['No', 'N']:
                return 0
        self.df[col_name] = self.df[col_name].apply(binarize)

    def _validate_df(self):
        df_cols = self.df.columns
        check_columns = ['dependents', 'gender', 'married',
                         'self_employed', 'loan_id']

        for col in check_columns:
            assert col in df_cols, f"Required column {col} not found. "\
                f"List of Dataset Columns: {list(df_cols)}"
