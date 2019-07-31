import requests
import json

def speak(str):
  from win32com.client import Dispatch
  speak=Dispatch("SAPI.SpVoice")
  speak.speak(str)

if __name__ == "__main__":
    url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=43165ee16c7c4f76bf77d22ab8abb3cd"
    response=requests.get(url)
    text=response.text
    my_json=json.loads(text)

    for i in range(0,11):
        speak(my_json['articles'][i]['title'])