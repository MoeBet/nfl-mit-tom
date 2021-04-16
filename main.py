from Data import Data

test = Data()

gameday_items = test.get_gameday()

for item in gameday_items:
    print(item.away_team)