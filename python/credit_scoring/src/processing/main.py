"""
Credit Data Preprocessor
"""

import pandas as pd
from typing import Tuple
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class CreditDataPreprocessor:
    """
    Preprocessor for German Credit Risk dataset
    Handles categorical encoding, numerical scaling, and feature engineering
    """

    def __init__(self):
        self.numerical_features = ["Age", "Job", "Credit amount", "Duration"]
        self.categorical_features = [
            "Sex",
            "Housing",
            "Saving accounts",
            "Checking account",
            "Purpose",
        ]
        self.target_feature = "Risk"

    def fit_preprocessor(self, df: pd.DataFrame) -> ColumnTransformer:
        """
        Builds a pipeline for preprocessing the data
        1. Scale numerical features (StandardScaler)
        2. Codify categorical features (OneHotEncoder)
        """
        # features transformers
        numeric_tf = Pipeline(steps=[("scaler", StandardScaler())])
        categorical_tf = Pipeline(
            steps=[("onehot", OneHotEncoder(handle_unknown="ignore"))]
        )

        # column transformer
        preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_tf, self.numerical_features),
                ("cat", categorical_tf, self.categorical_features),
            ],
            remainder="passthrough",
        )

        # Adjust column names
        x_train = df.drop(self.target_feature, axis=1)
        preprocessor.fit(x_train)

        return preprocessor

    def process_data(
        self, df: pd.DataFrame, preprocessor: ColumnTransformer
    ) -> Tuple[pd.DataFrame, pd.Series]:
        """
        Process the data using the preprocessor

        Args:
        - df: Input DataFrame
        - preprocessor: Preprocessor pipeline

        Returns:
        - Tuple of processed features and target
        """
        df_copy = df.copy()
        df_copy[self.target_feature] = df_copy[self.target_feature].map(
            {"good": 1, "bad": 0}
        )
        x = df_copy.drop(self.target_feature, axis=1)
        y = df_copy[self.target_feature]
        return preprocessor.transform(x), y
