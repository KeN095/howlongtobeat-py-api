from flask import Flask
from howlongtobeatpy import HowLongToBeat
import info_scraping

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''<p>How Long To Beat - API (beta - by JohnnyBannanis)</p>
        <p>/front-page                =>       Default Search (first page of games on HLTB)</p>
        <p>/find-game/"GAME_NAME"     =>       Results for search term</p>
        <p>/game_info/"HLTB_GAME_ID"  =>       Spacific game full info</p>
        '''

@app.route("/front-page")
def front_page():
    
    response = {
        "HLTB" : []
    }

    try:
        hltb_results = HowLongToBeat(0.1).search(" ", similarity_case_sensitive=False)
        for i in hltb_results:
            game = {
                "game_id":i.game_id,
                "game_name":i.game_name,
                "game_alias":i.game_alias,
                "game_type":i.game_type,
                "game_image_url":i.game_image_url,
                "game_web_link":i.game_web_link,
                "game_review_score":i.review_score,
                "game_developer":i.profile_dev,
                "game_platforms":i.profile_platforms,
                "game_release":i.release_world,
                "game_main":i.main_story,
                "game_extra":i.main_extra,
                "game_completionist":i.completionist,
                "game_all_styles":i.all_styles
            }

            response["HLTB"].append(game)
            
    except Exception as ex:
        print(ex)

    return response

@app.route("/find-game/<game_name>")
def find_game(game_name):

    response = {
        "HLTB" : []
    }
    
    try:
        hltb_results = HowLongToBeat(0.1).search(game_name, similarity_case_sensitive=False)
        for i in hltb_results:
            game = {
                "game_id":i.game_id,
                "game_name":i.game_name,
                "game_alias":i.game_alias,
                "game_type":i.game_type,
                "game_image_url":i.game_image_url,
                "game_web_link":i.game_web_link,
                "game_review_score":i.review_score,
                "game_developer":i.profile_dev,
                "game_platforms":i.profile_platforms,
                "game_release":i.release_world,
                "game_main":i.main_story,
                "game_extra":i.main_extra,
                "game_completionist":i.completionist,
                "game_all_styles":i.all_styles
            }

            response["HLTB"].append(game)
            
    except Exception as ex:
        print(ex)
    return response

@app.route("/game_info/<id>")
def Game(id):
    game_url = "https://howlongtobeat.com/game.php?id=" + str(id)
    response = {
    }
    try:
        i = HowLongToBeat().search_from_id(id)
        extra_info = info_scraping.scraping(game_url)
        game = {
            "game_id":i.game_id,
            "game_name":i.game_name,
            "game_image_url": "https://howlongtobeat.com" + i.game_image_url,
            "game_web_link":i.game_web_link,
            "description": extra_info["description"],
            "rating": extra_info["rating"],
            "more_info": extra_info["game_info"],
            "gameplay_main" : i.gameplay_main,
            "gameplay_main_unit" : i.gameplay_main_unit,
            "gameplay_main_label" : i.gameplay_main_label,
            "gameplay_main_extra" : i.gameplay_main_extra,
            "gameplay_main_extra_unit" : i.gameplay_main_extra_unit,
            "gameplay_main_extra_label" : i.gameplay_main_extra_label,
            "gameplay_completionist" : i.gameplay_completionist,
            "gameplay_completionist_unit" : i.gameplay_completionist_unit,
            "gameplay_completionist_label" : i .gameplay_completionist_label
        }
        response = game
    except Exception as ex:
        print(ex)
    return response

if __name__ == '__main__':
    #set host and port
    app.run(host="0.0.0.0", port=5555)