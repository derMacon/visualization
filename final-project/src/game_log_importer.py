import numpy as np
from datetime import datetime
import pandas as pd

GAME_LOGS_DATA_WORLD = '../datasets/retrosheets/game-logs_combined/game_logs_data-world.csv'

_dtypeDict = {
    'date': str,
    'number_of_game': np.uint32,
    'day_of_week': str,
    'v_name': str,
    'v_league': str,
    'v_game_number': np.int32,
    'h_name': str,
    'h_league': str,
    'h_game_number': np.int32,
    'v_score': np.int32,
    'h_score': np.int32,
    'length_outs': np.int32,
    'day_night': str,
    'completion': str,
    'forefeit': str,
    'protest': str,
    'park_id': str,
    'attendance': np.int32,
    'length_minutes': np.int32,
    'v_line_score': str,
    'h_line_score': str,
    'v_at_bats': np.int32,
    'v_hits': np.int32,
    'v_doubles': np.int32,
    'v_triples': np.int32,
    'v_homeruns': np.int32,
    'v_rbi': np.int32,
    'v_sacrifice_hits': np.int32,
    'v_sacrifice_flies': np.int32,
    'v_hit_by_pitch': np.int32,
    'v_walks': np.int32,
    'v_intentional walks': np.int32,
    'v_strikeouts': np.int32,
    'v_stolen_bases': np.int32,
    'v_caught_stealing': np.int32,
    'v_grounded_into_double': np.int32,
    'v_first_catcher_interference': np.int32,
    'v_left_on_base': np.int32,
    'v_pitchers_used': np.int32,
    'v_individual_earned_runs': np.int32,
    'v_team_earned_runs': np.int32,
    'v_wild_pitches': np.int32,
    'v_balks': np.int32,
    'v_putouts': np.int32,
    'v_assists': np.int32,
    'v_errors': np.int32,
    'v_passed_balls': np.int32,
    'v_double_plays': np.int32,
    'v_triple_plays': np.int32,
    'h_at_bats': np.int32,
    'h_hits': np.int32,
    'h_doubles': np.int32,
    'h_triples': np.int32,
    'h_homeruns': np.int32,
    'h_rbi': np.int32,
    'h_sacrifice_hits': np.int32,
    'h_sacrifice_flies': np.int32,
    'h_hit_by_pitch': np.int32,
    'h_walks': np.int32,
    'h_intentional walks': np.int32,
    'h_strikeouts': np.int32,
    'h_stolen_bases': np.int32,
    'h_caught_stealing': np.int32,
    'h_grounded_into_double': np.int32,
    'h_first_catcher_interference': np.int32,
    'h_left_on_base': np.int32,
    'h_pitchers_used': np.int32,
    'h_individual_earned_runs': np.int32,
    'h_team_earned_runs': np.int32,
    'h_wild_pitches': np.int32,
    'h_balks': np.int32,
    'h_putouts': np.int32,
    'h_assists': np.int32,
    'h_errors': np.int32,
    'h_passed_balls': np.int32,
    'h_double_plays': np.int32,
    'h_triple_plays': np.int32,
    'hp_umpire_id': str,
    'hp_umpire_name': str,
    '1b_umpire_id': str,
    '1b_umpire_name': str,
    '2b_umpire_id': str,
    '2b_umpire_name': str,
    '3b_umpire_id': str,
    '3b_umpire_name': str,
    'lf_umpire_id': str,
    'lf_umpire_name': str,
    'rf_umpire_id': str,
    'rf_umpire_name': str,
    'v_manager_id': str,
    'v_manager_name': str,
    'h_manager_id': str,
    'h_manager_name': str,
    'winning_pitcher_id': str,
    'winning_pitcher_name': str,
    'losing_pitcher_id': str,
    'losing_pitcher_name': str,
    'saving_pitcher_id': str,
    'saving_pitcher_name': str,
    'winning_rbi_batter_id': str,
    'winning_rbi_batter_id_name': str,
    'v_starting_pitcher_id': str,
    'v_starting_pitcher_name': str,
    'h_starting_pitcher_id': str,
    'h_starting_pitcher_name': str,
    'v_player_1_id': str,
    'v_player_1_name': str,
    'v_player_1_def_pos': np.int32,
    'v_player_2_id': str,
    'v_player_2_name': str,
    'v_player_2_def_pos': np.int32,
    'v_player_3_id': str,
    'v_player_3_name': str,
    'v_player_3_def_pos': np.int32,
    'v_player_4_id': str,
    'v_player_4_name': str,
    'v_player_4_def_pos': np.int32,
    'v_player_5_id': str,
    'v_player_5_name': str,
    'v_player_5_def_pos': np.int32,
    'v_player_6_id': str,
    'v_player_6_name': str,
    'v_player_6_def_pos': np.int32,
    'v_player_7_id': str,
    'v_player_7_name': str,
    'v_player_7_def_pos': np.int32,
    'v_player_8_id': str,
    'v_player_8_name': str,
    'v_player_8_def_pos': np.int32,
    'v_player_9_id': str,
    'v_player_9_name': str,
    'v_player_9_def_pos': np.int32,
    'h_player_1_id': str,
    'h_player_1_name': str,
    'h_player_1_def_pos': np.int32,
    'h_player_2_id': str,
    'h_player_2_name': str,
    'h_player_2_def_pos': np.int32,
    'h_player_3_id': str,
    'h_player_3_name': str,
    'h_player_3_def_pos': np.int32,
    'h_player_4_id': str,
    'h_player_4_name': str,
    'h_player_4_def_pos': np.int32,
    'h_player_5_id': str,
    'h_player_5_name': str,
    'h_player_5_def_pos': np.int32,
    'h_player_6_id': str,
    'h_player_6_name': str,
    'h_player_6_def_pos': np.int32,
    'h_player_7_id': str,
    'h_player_7_name': str,
    'h_player_7_def_pos': np.int32,
    'h_player_8_id': str,
    'h_player_8_name': str,
    'h_player_8_def_pos': np.int32,
    'h_player_9_id': str,
    'h_player_9_name': str,
    'h_player_9_def_pos': np.int32,
    'additional_info': str,
    'acquisition_info': str
}


def _process_value(value):
    if value == '':
        return
    else:
        return value


def _convert_to_datetime64(date_string):
    datetime_obj = datetime.strptime(date_string, '%Y%m%d')
    return np.datetime64(datetime_obj, 'D')


def _sanitize_df(df):
    placeholder = '-12345'
    # fill empty cells with placeholder
    df = df.fillna(placeholder)
    # necessary to cast with type dictionary
    df = df.astype(_dtypeDict)
    # after cast insert nan value, for an early fail in later processing if list
    # is not properly sanitized
    df = df.replace(placeholder, np.nan)

    # create a new column containing just the year - easier for later processing
    df['date'] = pd.to_datetime(df['date'])
    df = pd.concat([df, df['date'].apply(lambda x: x.year).rename('date_year')], axis=1)

    # TODO sanitize all other fields

    return df


def _clean_partial_games(df):
    return df.drop(df[df.acquisition_info != 'Y'].index)


def read_game_logs():
    df = pd.read_csv(GAME_LOGS_DATA_WORLD, converters={col: _process_value for col in _dtypeDict.keys()}, nrows=5000)
    return _sanitize_df(df)
