import scrapetube
import pandas as pd
ch = ["UCzzTMd1JwOAfCbLug-uiURQ"]
da=pd.DataFrame(columns=['isd'])
for i in ch:
    videos = scrapetube.get_channel(i)
    for video in videos:
        print(video['videoId'])
        df=pd.DataFrame([[video['videoId']]],columns=['isd'])
        da=pd.concat([da,df])
da.to_csv("vidid.csv")
