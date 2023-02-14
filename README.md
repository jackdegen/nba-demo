# nba-demo

+ Overview

This repository will use NBA stats to demonstrate various data science examples, including but not limited to: 
- Cleaning and organizing data,
- General exploratory data analysis,
- Preprocessing datasets for models.

I use this data and these various techniques to help me compete in Daily Fantasy Sports (DFS), mostly on FanDuel--therefore, "fantasy points" throughout this repository refers to FanDuel scoring, which differs slightly from DraftKings and some other fantasy sites.

The entire dataset is compiled by scraping the boxscores from every NBA basektball game in the 2022-2023 season. The source of this data is www.basketballreference.com.

I have written a separate package that uses the BeautifulSoup library to extensively scrape all applicable data (basic/advanced stats, starters, injuries, etc.) into .csv files for each team, for each game.
- The parameters for this algorithm can be easily customized for various time frames, teams, games dating all the way back to the 1970s if one wished.
- However, I have decided to keep this package private as I consider it to be valuable. I don't want to allow everyone access to it since it is a competitive advantage for me in DFS.
- That being said:
  * The 2022-2023 dataset will be posted publicly here, updated somewhat regularly, so individuals will have access to this data, just not the mechanisms to add more data.
  * If any possible employers would like to see this package, I would be more than pleased to provide access.
  * If anyone else would like to access this, feel free to contact me at jackbdegen@gmail.com and I will be happy to consider your request.


+ What is not in this repository:

In addition to the above mentioned webscraper, I will also not provide my projections which take into account further information such as lineups/injuries, my optimizer to create possible lineups, various correlation checkers, and my lineup analyzer to determine leverage points based on most likely ownership combinations.

Similarly to the webscraper, I am open to request--I just do not want my code to be accessed by anyone without my knowledge.
