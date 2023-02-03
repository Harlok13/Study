from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    indx = get_offset(game_stamps, offset)

    return game_stamps[indx]['score']['home'], game_stamps[indx]['score']['away']


def get_offset(game_stamps, target):
    first = 0
    last = len(game_stamps) - 1
    indx = -1
    while (first <= last) and (indx == -1):
        mid = (first + last) // 2
        if game_stamps[mid]['offset'] == target:
            indx = mid
        else:
            if target < game_stamps[mid]['offset']:
                last = mid - 1
            else:
                first = mid + 1
    else:
        if first > last:
            return last
    return indx


game_stamps = generate_game()

if __name__ == '__main__':
    pprint(game_stamps)
    print(get_score(game_stamps, 54898), 'score'.rjust(14))
    print(get_offset(game_stamps, 54898), 'indx'.rjust(15))
    print(game_stamps[get_offset(game_stamps, 54898)]['offset'], 'offset'.rjust(15))
