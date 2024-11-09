import os
import pandas as pd


def clean_data(df):

    print("Colunas no DataFrame:", df.columns)
    # Verifique se as colunas necessárias estão presentes
    required_columns = ['MIN', 'PTS', 'AST', 'REB', 'TOV']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Coluna {col} está ausente no DataFrame.")

    # Garantir que as colunas de pontos, assistências, rebotes e turnovers
    df['PTS'] = pd.to_numeric(df['PTS'], errors='coerce')
    df['AST'] = pd.to_numeric(df['AST'], errors='coerce')
    df['REB'] = pd.to_numeric(df['REB'], errors='coerce')
    df['TOV'] = pd.to_numeric(df['TOV'], errors='coerce')

    # Exemplo de limpeza e processamento: verifica se o valor em 'MIN' contém
    df['under_pressure'] = df['MIN'].apply(
        lambda x: 1 if 'OT' in str(x) else 0
    )
    df = df[['PTS', 'AST', 'REB', 'TOV', 'under_pressure']]

    # Criar o diretório se não existir
    output_dir = '../data/processed'
    os.makedirs(output_dir, exist_ok=True)

    # Salvar o DataFrame processado
    output_path = os.path.join(output_dir, 'cleaned_data.csv')
    df.to_csv(output_path, index=False)
    print(f"Dados limpos e salvos em {output_path}")

    return df
