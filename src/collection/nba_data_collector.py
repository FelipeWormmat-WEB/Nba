import os
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog


def get_player_data(player_name, season='2022-23'):
    os.makedirs('../data/raw', exist_ok=True)
    nba_player = players.find_players_by_full_name(player_name)[0]
    player_id = nba_player['id']
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    df = game_log.get_data_frames()[0]

    print("Colunas retornadas pela API:", df.columns)
    df.to_csv(f'../data/raw/{player_name}_game_log.csv', index=False)
    print(f"Dados coletados para {player_name} e salvos em data/raw/")
    return df
