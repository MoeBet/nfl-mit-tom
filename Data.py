import requests
from bs4 import BeautifulSoup
from Gameday import Gameday

class Data:
    def __init__(self):

        response = requests.get("https://www.pro-football-reference.com/years/2020/week_1.htm")
        data = response.text
        self.soup = BeautifulSoup(data, "html.parser")

    def get_gameday(self):
        """Elemente im HTML parsing noch nicht richtig"""
        list_index = self.soup.find_all(name="div", class_="game_summary expanded nohover")
        raw_data = self.soup.find(name="div", class_="game_summary expanded nohover")
        actual_element = raw_data

        gamedays = []

        for n in range(len(list_index)):
            date = actual_element.find_next(name="td").getText()
            actual_element = actual_element.find_next(name="td")
            away_team = actual_element.getText()
            actual_element = actual_element.find_next(name="td")
            away_team_score = actual_element.getText()
            actual_element = actual_element.find_next(name="tr")
            actual_element = actual_element.find_next(name="td")
            home_team = actual_element.getText()
            actual_element = actual_element.find_next(name="td")
            home_team_score = actual_element.getText()
            gameday = Gameday(date=date,
                              away_team=away_team,
                              away_team_score=away_team_score,
                              home_team=home_team,
                              home_team_score=home_team_score)
            gamedays.append(gameday)

        return gamedays




