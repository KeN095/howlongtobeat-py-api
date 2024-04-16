from flask import Flask
from howlongtobeatpy import HowLongToBeat
import info_scraping

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''<p>How Long To Beat - API (beta - by JohnnyBannanis)</p>
        <p>/front-page                =>       Default Search (first page of games on HLTB)</p>
        <p>/find-game/"GAME_NAME"     =>       Results for search term</p>
        <p>/game_info/"HLTB_GAME_ID"  =>       Results for a single game based on a valid HLTB ID</p>
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
        return 500

    return response, 200

@app.route("/find-game/<game_name>")
def find_game(game_name):

    response = {
        "HLTB" : []
    }
    
    try:
        hltb_results = HowLongToBeat(0.1).search(game_name, similarity_case_sensitive=False)
        
        if not hltb_results:
            return [], 404
        
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
        return 500

    if response:
        return response, 200

@app.route("/game_info/<id>")
def find_by_id(id):

    if not id.isnumeric():
        return [],404

    try:
        
         gameData = HowLongToBeat().search_from_id(id)
         #extraInfo = info_scraping(gameData.game_web_link)

         if not gameData:
             return [], 404

         game = {
                "game_id":gameData.game_id,
                "game_name":gameData.game_name,
                "game_alias":gameData.game_alias,
                "game_type":gameData.game_type,
                "game_image_url":gameData.game_image_url,
                "game_web_link":gameData.game_web_link,
                "game_review_score":gameData.review_score,
                "game_developer":gameData.profile_dev,
                "game_platforms":gameData.profile_platforms,
                "game_release":gameData.release_world,
                "game_main":gameData.main_story,
                "game_extra":gameData.main_extra,
                "game_completionist":gameData.completionist,
                "game_all_styles":gameData.all_styles 
            }
         
    except Exception as ex:
        print(ex)
        return 500

    return game, 200
        

if __name__ == '__main__':
    #set host and port
    app.run(host="0.0.0.0", port=5555)