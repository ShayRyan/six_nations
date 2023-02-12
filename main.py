
def table_update_from_result(res):

    home_team, home_pts, home_tries, away_team, away_pts, away_tries = res
    home_row = {
        'team': home_team,
        'win': 0,
        'loss': 0,
        'draw': 0,
        'pts_for': home_pts,
        'pts_against': away_pts,
        'diff': home_pts - away_pts,
        'tries_for': home_tries,
        'tries_against': away_tries,
        'try_bonus': 0,
        'lose_bonus': 0,
        'points': 0}

    away_row = {
        'team': away_team,
        'win': 0,
        'loss': 0,
        'draw': 0,
        'pts_for': away_pts,
        'pts_against': home_pts,
        'diff': away_pts - home_pts,
        'tries_for': away_tries,
        'tries_against': home_tries,
        'try_bonus': 0,
        'lose_bonus': 0,
        'points': 0}

    # Win, Loss, Draw
    if home_pts > away_pts:
        home_row['win'] = 1
        home_row['points'] = 4
        away_row['loss'] = 1
    elif home_pts < away_pts:
        home_row['loss'] = 1
        away_row['win'] = 1
        away_row['points'] = 4
    else:
        home_row['draw'] = 1
        home_row['points'] = 2
        away_row['draw'] = 1
        away_row['points'] = 2

    # Try Bonus Points
    if home_tries >= 4:
        home_row['try_bonus'] = 1
        home_row['points'] += 1
    if away_tries >= 4:
        away_row['try_bonus'] = 1
        away_row['points'] += 1

    # Loss Bonus Points
    if -7 <= home_row['diff'] < 0:
        home_row['lose_bonus'] = 1
        home_row['points'] += 1
    if -7 <= away_row['diff'] < 0:
        away_row['lose_bonus'] = 1
        away_row['points'] += 1

    return home_row, away_row


def update_table(row):
    """Update championship table."""

    ...


def print_table():
    ...


def main():
    results = [
        ('Wales', 10, 1, 'Ireland', 34, 4),
        ('England', 23, 3, 'Scotland', 29, 4),
        ('Italy', 24, 1, 'France', 29, 4)]
    for result in results:
        table_rows = table_update_from_result(result)
        for row in table_rows:
            print(row)


if __name__ == '__main__':
    main()