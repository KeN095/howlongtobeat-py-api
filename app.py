from flask import Flask
from howlongtobeatpy import HowLongToBeat
import info_scraping

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''<p>How Long To Beat - API (beta - by JohnnyBannanis)</p>
        <p>/front-page                =>       Default Search (first page of games on HLTB)</p>
        <p>/find-game/"GAME_NAME"     =>       Results for search term</p>
        <p>/game-info/"HLTB_GAME_ID"  =>       Results for a single game based on a valid HLTB ID</p>
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
        return "<h1>500 Internal Server Error</h1>",500

    return response, 200

@app.route("/find-game/<game_name>")
def find_game(game_name):

    response = {
        "HLTB" : []
    }
    
    try:
        hltb_results = HowLongToBeat(0.1).search(game_name, similarity_case_sensitive=False)
        
        if not hltb_results:
            return  "<h1>404 Data not found</h1>", 404
        
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
        return "<h1>500 Internal Server Error</h1>",500

    if response:
        return response, 200

@app.route("/game-info/<id>")
def game_info(id):

    try:
        idInt = int(id)
    except Exception as ex:
        return "<h1>400 Invalid data</h1>", 400

    try:
        
         gameData = HowLongToBeat().search_from_id(idInt)

         if not gameData:
             return "<h1>404 Data not found</h1>", 404
         
         extra_info = info_scraping.scrape_info(gameData.game_web_link)

         game = {
                "game_id":gameData.game_id,
                "game_name":gameData.game_name,
                "game_alias":gameData.game_alias,
                "game_type":gameData.game_type,
                "game_description":extra_info["game_description"],
                "game_image_url":gameData.game_image_url,
                "game_web_link":gameData.game_web_link,
                "game_review_score":gameData.review_score,
                "game_developer":gameData.profile_dev,
                "game_publisher":extra_info["publisher"],
                "game_platforms":gameData.profile_platforms,
                "game_release":extra_info["release_dates"],
                "game_last_updated":extra_info["last_updated"],
                "game_genres":extra_info["genres"],
                "game_main":gameData.main_story,
                "game_extra":gameData.main_extra,
                "game_completionist":gameData.completionist,
                "game_all_styles":gameData.all_styles 
            }
         
    except Exception as ex:
        print(ex)
        return "<h1>500 Internal Server Error</h1>",500

    return game, 200
        

if __name__ == '__main__':
    #set host and port
    app.run(host="0.0.0.0", port=5555)