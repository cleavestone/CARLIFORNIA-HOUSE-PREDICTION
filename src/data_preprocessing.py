from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib

KMODEL_PATH=r'C:\Users\Hp\Desktop\HOUSE_PREDICTION_APP\models\kmeans.joblib'
clustering_model=joblib.load(KMODEL_PATH)

def preprocess(features):
    # Create a DataFrame from the input dictionary
    df = pd.DataFrame([features])

    # Convert the relevant columns to float
    for col in ['longitude', 'latitude', 'housing_median_age', 
                'total_rooms', 'total_bedrooms', 
                'population', 'households', 'median_income']:
        df[col] = df[col].astype(float)

    # Create cluster for longitude and latitude
    long_lat_df = df[['longitude', 'latitude']]
    long_lat_scaled = StandardScaler().fit_transform(long_lat_df)
    df['location_cluster'] = clustering_model.predict(long_lat_scaled)  # Use predict instead of fit_predict

    categorical_columns=['ocean_proximity','location_cluster']
    numerical_columns=['housing_median_age','median_income','total_rooms', 'population', 'households']
    # Define categorical and numerical columns
    pipeline=joblib.load(r'C:\Users\Hp\Desktop\HOUSE_PREDICTION_APP\models\trained_pipeline.joblib')

    # Fit the pipeline on training data and transform the input DataFrame
    # Note: You should fit this pipeline on your training data in production
    df_transformed = pipeline.transform(df)

    # Combine transformed features
    columns = numerical_columns + list(pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(categorical_columns))
    features_df = pd.DataFrame(df_transformed, columns=columns)

    # Rename specific columns if necessary
    features_df.rename(columns={'ocean_proximity_<1H OCEAN': 'ocean_proximity_1H OCEAN'}, inplace=True)
    print(features_df.columns)
    return features_df