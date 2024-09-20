from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd


def preprocess(features):
    categorical_columns=['ocean_proximity','location_cluster']
    numerical_columns=['housing_median_age','median_income','total_rooms', 'population', 'households']
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_columns),
            ('cat', OneHotEncoder(sparse_output=False), categorical_columns)
        ])
    # create pipeline
    pipeline = Pipeline(steps=[('preprocessor', preprocessor)])
    features=pipeline.transform(features)

    columns = numerical_columns + list(pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(categorical_columns))
    features = pd.DataFrame(features, columns=columns)
    features.rename(columns={'ocean_proximity_<1H OCEAN':'ocean_proximity_1H OCEAN'},inplace=True)