import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'User-Agent': ua.random
    }

def scrape_info(url):
    #Code depends on existing HTML tree, so it's likely to break
    
    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")

        release_dates={}
        description = publisher = genres = last_updated = None
        readMore = "...Read More"

        # Get description by determining if the string "...Read More" is present
        if soup.find('div', class_= "GameSummary_profile_info__HZFQu GameSummary_large__TIGhL").text.find(readMore) >= 1:
            #Get the index of when that string first appears
            desc = soup.find('div', class_= "GameSummary_profile_info__HZFQu GameSummary_large__TIGhL").text
            readMorePosition = soup.find('div', class_= "GameSummary_profile_info__HZFQu GameSummary_large__TIGhL").text.find(readMore)
            #Take the substring from index 0 all the way up to the first occurence of "...Read More"
            beforeReadMore = desc[:readMorePosition].strip()
            #Combine the index at readMorePosition with the length of the readMore string to retrieve the starting index and obtain the rest of the string after "...Read More" 
            afterReadMore = desc[readMorePosition + len(readMore):].strip()
            #Concatenate/Combine the strings
            description = beforeReadMore + afterReadMore
        elif soup.find('div', class_= "GameSummary_profile_info__HZFQu GameSummary_large__TIGhL").text:
             #if "...Read more" is not present, just extract the description text
             description = soup.find('div', class_= "GameSummary_profile_info__HZFQu GameSummary_large__TIGhL").text
        
        #Get publisher and genres
        if soup.find_all('div', class_="GameSummary_profile_info__HZFQu GameSummary_medium___r_ia"):
                publisher_genres_info = soup.find_all('div', class_="GameSummary_profile_info__HZFQu GameSummary_medium___r_ia")

                if publisher_genres_info:
                    start_index_publisher = publisher_genres_info[3].text.find(": ") + 2
                    publisher = publisher_genres_info[3].text[start_index_publisher:]

                    start_index_genres = publisher_genres_info[1].text.find(": ") + 2
                    genres = publisher_genres_info[1].text[start_index_genres:]

        
        #Get release dates and last updated info
        dates_last_updated_info = soup.find_all('div', class_="GameSummary_profile_info__HZFQu")

        if dates_last_updated_info:
            start_index_release = dates_last_updated_info[6].text.find(": ") + 2

            na_release = dates_last_updated_info[6].text[start_index_release:]
            eu_release = dates_last_updated_info[7].text[start_index_release:]

            start_index_updated = dates_last_updated_info[8].text.find(": ") + 2
            last_updated = dates_last_updated_info[8].text[start_index_updated:]

            release_dates["NA"] = na_release
            release_dates["EU"] = eu_release

        extra_info = {
            "game_description": description,
            "publisher":publisher,
            "genres": genres,
            "release_dates": release_dates,
            "last_updated":last_updated
        }

        return extra_info
    except Exception as ex:
         print(ex)
         return {}
