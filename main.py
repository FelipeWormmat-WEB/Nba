from src.collection.nba_data_collector import get_player_data
from src.preprocessing.data_cleaning import clean_data
from src.modeling.model_trainer import train_model
import joblib


def run_pipeline(player_name):
    raw_data = get_player_data(player_name)
    processed_data = clean_data(raw_data)
    processed_data.to_csv('../data/processed/processed_data.csv', index=False)
    model = train_model()
    joblib.dump(model,
                '../models/'
                'random_forest_model.pkl')
    print("Pipeline concluído com sucesso.")


if __name__ == "__main__":
    player_name = "LeBron James"
    run_pipeline(player_name)
