import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestRegressor
from collections import namedtuple
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
import joblib
import logging

logging.basicConfig(
    format="[%(asctime)s %(name)s %(levelname)s] %(message)s", level=logging.INFO
)


FILE_PATH = "filestore/data/vine_dataset.csv"
MODEL_PATH = "filestore/model/rf_regressor.pkl"


def split_data(df: pd.DataFrame):
    x, y = df.iloc[:, 1:].values, df.iloc[:, 0].values
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=0, stratify=y
    )
    Data = namedtuple("Wine", "x_train, x_test, y_train, y_test")
    logging.info("Data split successfully!")
    return Data(x_train, x_test, y_train, y_test)


def get_pipeline():
    pipeline = make_pipeline(
        StandardScaler(), RandomForestRegressor(n_estimators=100, random_state=123)
    )
    logging.info("Pipeline created!")
    return pipeline


hyper_parameters = {
    "randomforestregressor__max_features": ["auto", "sqrt", "log2"],
    "randomforestregressor__max_depth": [None, 5, 3, 1],
}


def main():
    main_df = pd.read_csv(FILE_PATH, index_col=0)
    training_data = split_data(main_df)
    pipeline = get_pipeline()
    clf = GridSearchCV(pipeline, hyper_parameters, cv=5)
    logging.info("Fitting grid search with RandomForest")
    clf.fit(training_data.x_train, training_data.y_train)
    y_pred = clf.predict(training_data.x_test)
    logging.info(f"R square: {r2_score(training_data.y_test, y_pred)}")
    logging.info(
        f"Mean square error: {mean_squared_error(training_data.y_test, y_pred)}"
    )

    joblib.dump(clf, MODEL_PATH)
    logging.info(f"Model dumped into: {MODEL_PATH}")


if __name__ == "__main__":
    main()
