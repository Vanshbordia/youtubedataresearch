import json
import pandas as pd
from csv import writer
import time
from urllib.request import urlopen
vid = pd.read_csv("vidid.csv")
api="youryoutubeapihere"
def yttimeconvert(duration):
   day_time = duration.split('T')
   day_duration = day_time[0].replace('P', '')
   day_list = day_duration.split('D')
   if len(day_list) == 2:
      day = int(day_list[0]) * 60 * 60 * 24
      day_list = day_list[1]
   else:
      day = 0
      day_list = day_list[0]
   hour_list = day_time[1].split('H')
   if len(hour_list) == 2:
      hour = int(hour_list[0]) * 60 * 60
      hour_list = hour_list[1]
   else:
      hour = 0
      hour_list = hour_list[0]
   minute_list = hour_list.split('M')
   if len(minute_list) == 2:
      minute = int(minute_list[0]) * 60
      minute_list = minute_list[1]
   else:
      minute = 0
      minute_list = minute_list[0]
   second_list = minute_list.split('S')
   if len(second_list) == 2:
      second = int(second_list[0])
   else:
      second = 0
   return day + hour + minute + second
def main(urs):
   url = "https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id="+urs+"&key="+api
   response = urlopen(url)
   json_load = json.loads(response.read())

   try:
      vidtitle=json_load['items'][0]['snippet']['title']
   except:
      vidtitle=""
   try:
      chanid=json_load['items'][0]['snippet']['channelId']
   except:
      chanid=""
   try:
      viddesc=json_load['items'][0]['snippet']['description']
   except:
      viddesc=""
   try:
      vidpub=json_load['items'][0]['snippet']['publishedAt']
   except:
      vidpub=""
   try:
      channame=json_load['items'][0]['snippet']['channelTitle']
   except:
      channame=""
   try:
      vidtags=json_load['items'][0]['snippet']['tags']
   except:
      vidtags=""
   try:
      vidcat=json_load['items'][0]['snippet']['categoryId']
   except:
      vidcat=""
   try:
      vidlive=json_load['items'][0]['snippet']['liveBroadcastContent']
   except:
      vidlive=""
   try:
      vidlang=json_load['items'][0]['snippet']['defaultAudioLanguage']
   except:
      vidlang=" "
   try:
      viddu=time.strftime("%H:%M:%S",time.gmtime(yttimeconvert(json_load['items'][0]['contentDetails']['duration'])))
   except:
      viddu=""
   try:
      vidview=json_load['items'][0]['statistics']['viewCount']
   except:
      vidview=""
   try:
      vidlikes=json_load['items'][0]['statistics']['likeCount']
   except:
      vidlikes=""
   try:
      vidcom=json_load['items'][0]['statistics']['commentCount']
   except:
      vidcom=""
   try:
      vidthumb=json_load['items'][0]['snippet']['thumbnails']['maxres']['url']
   except:
      vidthumb=json_load['items'][0]['snippet']['thumbnails']['default']['url']
   try:
      vidid=json_load['items'][0]['id']
   except:
      vidid=""
   df2 = pd.DataFrame([[vidtitle,chanid,viddesc,vidpub,channame,vidtags,vidcat,vidlive,vidlang,viddu,vidview,vidlikes,vidcom,vidthumb,vidid]],columns=['vidtitle','chanid','viddesc','vidpub','channame','vidtags','vidcat','vidlive','vidlang','viddu','vidview','vidlikes','vidcom','vidthumb','vidid'])
   return df2
    

for i in range(0,len(vid.index+1)):

   data = main(str(vid.iloc[i,1]))
   print (i)
   print(data)
   data.to_csv("exdata.csv", mode='a', header=False, index=False)
   time.sleep(1)
