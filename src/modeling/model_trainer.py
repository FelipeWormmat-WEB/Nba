import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os  # Importando a biblioteca para manipulação de diretórios


def train_model():
    # Carregando os dados
    df = pd.read_csv('../data/processed/cleaned_data.csv')
    X = df.drop('under_pressure', axis=1)
    y = df['under_pressure']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Inicializando o modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Realizando previsões e avaliando o modelo
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Garantir que o diretório para salvar o modelo exista
    model_dir = '../models'
    os.makedirs(model_dir, exist_ok=True)  # Cria o diretório caso não exista

    # Salvando o modelo treinado
    model_path = os.path.join(model_dir, 'random_forest_model.pkl')
    model = joblib.load(model_path)
    print(f"Modelo salvo em {model_path}")

    return model
