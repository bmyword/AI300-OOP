from data_loader import CSVDataLoader, DBDataLoader
from feature_builder import FeatureBuilder
from model.catboost import CatBoostModel
from model.evaluator import ModelEvaluator


def load_data():
    # Alternatively, try DBDataLoader().load()
    return CSVDataLoader().load()


def evaluate(model, dataset):
    X, y = FeatureBuilder(dataset).build_train_set()
    metrics_dict = ModelEvaluator(model, X, y)\
        .evaluate(ModelEvaluator.supported_metrics)
    for metric, value in metrics_dict.items():
        print(f"{metric} = {round(value, 4)}")


def retrain(model, dataset):
    X, y = FeatureBuilder(dataset).build_train_set()
    model.train(X, y).save()


def predict(model, dataset):
    X = FeatureBuilder(dataset).build_test_set()
    return model.predict_proba(X)


if __name__ == "__main__":
    # Step 1: Load dataset as pandas Dataframe
    dataset = load_data()
    model = CatBoostModel()

    # Step 2: Calculate offline metrics on chosen model
    print(f"\n::: Evaluate Catboost model :::")
    evaluate(model, dataset)

    # Step 3: Train model on entire dataset
    #   (Can be rerun monthly with latest historical data)
    print(f"\n::: Retrain Catboost model :::")
    retrain(model, dataset)

    # Step 4: Generate sample predictions on trained model
    #   Optional step, details covered in Lesson 6
    #   (Trained model is loaded from file when deployed)
    print(f"\n::: Make Predictions with Catboost model :::")
    model = CatBoostModel().load()
    preds = predict(model, dataset)
    print(f"First 10 predictions: {preds[:10]}")
