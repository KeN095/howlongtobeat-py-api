# howlongtobeat_py_api
REST Python Flask API using howlongtobeatpy library and additional scraping. 

## Installation and Usage
Requires Python 3.X, Flask (_pip install flask_), howlongtobeatpy (_pip install howlongtobeatpy_), and BeautifulSoup (_pip install beautifulsoup4_).  

Run "app.py" (_python app.py_) in the same directory.

API Routes

```
/front-page                =>     The list of games that appear on the HowLongToBeat home page.
/find-game/"GAME_NAME"     =>     Results for search term.
/game-info/"HLTB_GAME_ID"  =>     Specific information for a game based on the ID from HowLongToBeat.

```

## Additional info
The game ID (https://howlongtobeat.com/game.php?id=XXXX) is used to extract additional information that howlongtobeatpy doesn't provide.

```
- Game description

- Developer

- List of genres

- Platforms

- Publisher

- Game rating (according to HowLongToBeat users)

- Full release dates

- Last updated on the site
```

## Example API response '/game-info/6064'
```json
{
    "description": "Minecraft is a game about placing blocks to buil anything you can imagine. At night monsters come out, make sure to build a shelter before that happens.",
    "game_id": "6064",
    "game_image_url": "https://howlongtobeat.com/game256px-Minecraft_1.1_Title.png",
    "game_name": "Minecraft",
    "game_web_link": "https://howlongtobeat.com/game.php?id=6064",
    "gameplay_completionist": "243",
    "gameplay_completionist_label": "Vs.",
    "gameplay_completionist_unit": "Hours",
    "gameplay_main": "122",
    "gameplay_main_extra": "334",
    "gameplay_main_extra_label": "Co-Op",
    "gameplay_main_extra_unit": "Hours",
    "gameplay_main_label": "Solo",
    "gameplay_main_unit": "Hours",
    "more_info": {
      "Developer": "Mojang",
      "EU": [
        " November 18",
        "2011"
      ],
      "Genres": [
        "First-Person",
        "Third-Person",
        "Virtual Reality",
        "Action",
        "Hack and Slash",
        "Open World",
        "Sandbox",
        "Survival"
      ],
      "NA": [
        " November 18",
        "2011"
      ],
      "Platforms": [
        "Mobile",
        "Nintendo 3DS",
        "Nintendo Switch",
        "PC",
        "PlayStation 3",
        "PlayStation 4",
        "PlayStation Vita",
        "Wii U",
        "Xbox 360",
        "Xbox One"
      ],
      "Publisher": "Mojang",
      "Updated": " 6 Mins Ago"
    },
    "rating": "87% Rating"
}
```

## Example API response '/find-game/blinx'
```json
{"HLTB":[
  {
    "game_alias":"",
    "game_all_styles":10.57,
    "game_completionist":12.96,
    "game_developer":"Artoon",
    "game_extra":10.43,
    "game_id":1168,
    "game_image_url":"https://howlongtobeat.com/games/Blinx_-_The_Time_Sweeper_Coverart.png",
    "game_main":10.0,"game_name":"Blinx: The Time Sweeper",
    "game_platforms":["Xbox"],
    "game_release":2002,
    "game_review_score":56,
    "game_type":"game",
    "game_web_link":"https://howlongtobeat.com/game/1168"
  },
  {
    "game_alias":"Blinx 2: Battle of Time and Space",
    "game_all_styles":7.33,
    "game_completionist":8.33,
    "game_developer":"Artoon",
    "game_extra":0.0,
    "game_id":17857,
    "game_image_url":"https://howlongtobeat.com/games/Blinx_2_-_Masters_of_Time_and_Space_Coverart.png",
    "game_main":7.24,
    "game_name":"Blinx 2: Masters of Time and Space",
    "game_platforms":["Xbox"],
    "game_release":2004,
    "game_review_score":66,
    "game_type":"game",
    "game_web_link":"https://howlongtobeat.com/game/17857"
    }
  ]
}
```

## Credit
### howlongtobeatpy

Original source by ScrappyCoco  
Python package: https://pypi.org/project/howlongtobeatpy/

Repo: https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI
