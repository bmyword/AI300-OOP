TARGET_COL = 'loan_approval_status'


# Catboost config

CATBOOST_MODEL_FILEPATH = 'model/catboost_model.cbm'
# Params are derived from research phase in ipynb
CHOSEN_CATBOOST_PARAMS = {
    "iterations": 100,
    "depth": 8,
    "random_state": 42  # Ensure consistency across runs
}
