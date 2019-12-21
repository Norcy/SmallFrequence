#!/usr/bin/env python
#encoding:utf-8
import urllib.request
import urllib.error
import re
import os
import sys
from bs4 import BeautifulSoup
import json
import time
import shutil
import http.cookiejar

RootUrl = "http://localhost:3000"
SongUrl = "https://music.163.com/song/media/outer/url?id={}"
FetchSongListUrl = "/playlist/detail?id="
FetchSongsDetailUrl = "/song/detail?ids="
UserSongLists = "/user/playlist?uid="
UserId = "341142092"
root_director = "Music_List"

fake_group_prefix = "n_"

def getHtmlData(url):
    url = (url+"&timestamp=")+str(int(time.time()))
    print(url)
    # 欺骗为 iPhone/iPad 的请求
    req = urllib.request.Request(
        url,
        data = None,
        headers = {
            'User-Agent':'AppleWebKit/537.36'
        }
    )
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e)
        return

    data = response.read()

    data = data.decode('utf-8')

    # print(data)

    return data

def getJsonHtmlData(url):
    data = getHtmlData(url)
    jsonData = json.loads(data)
    return jsonData

# 请求指定用户的所有歌单
def request_regions(userId):
    songLists = []
    data = getJsonHtmlData(RootUrl+UserSongLists+userId);
    for singleData in data["playlist"]:
        songList = {};
        songList["title"] = singleData["name"];
        songList["id"] = "{}{}".format(fake_group_prefix, singleData["id"]);
        songLists.append(songList);
    return songLists;

# 请求单个歌单信息
def request_channels(regionId):
    songIdList = getJsonHtmlData(RootUrl+FetchSongListUrl+regionId[len(fake_group_prefix):])
    songIds = [];
    if songIdList["code"] == 200:
        for trackId in songIdList["playlist"]["trackIds"]:
            songIds.append(trackId["id"])

    songList = getJsonHtmlData(RootUrl+FetchSongsDetailUrl+",".join(str(x) for x in songIds))
    ret = []
    
    if songList["code"] == 200:
        for songInfo in songList["songs"]:
            simplifiedChannel = {}
            simplifiedChannel["content_id"] = "{}{}".format(fake_group_prefix, songInfo["id"]);
            simplifiedChannel["title"] = songInfo["name"];
            simplifiedChannel["url"] = SongUrl.format(songInfo["id"]);
            simplifiedChannel["group_id"] = regionId
            simplifiedChannel["poster"] = songInfo["al"]["picUrl"];
            ret.append(simplifiedChannel)

    return ret

def main():

    absolute_root_director = os.path.split(os.path.realpath(__file__))[0]+"/"+root_director;
    
    if os.path.exists(absolute_root_director):
        shutil.rmtree(absolute_root_director)    
    os.mkdir(absolute_root_director)

    regions = request_regions(UserId);

    version = int(time.time());
    finalRegions = {};
    finalRegions["version"] = version;
    finalRegions["data"] = regions;
    with open(absolute_root_director+'/regions.json', 'w') as f:
        json.dump(finalRegions, f, ensure_ascii=False)


    allChannels = [];
    for region in regions:
        regionId = region["id"]
        regionTitle = region["title"]
        channels = request_channels(regionId)
        allChannels += channels;
    
    finalChannels = {};
    finalChannels["version"] = version;
    finalChannels["data"] = allChannels;
    with open(absolute_root_director+'/all.json', 'w') as f:
        json.dump(finalChannels, f, ensure_ascii=False, indent=4, separators=(',', ':'))

if __name__=="__main__":
    main()
