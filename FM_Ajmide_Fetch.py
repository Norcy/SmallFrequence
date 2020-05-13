# https://segmentfault.com/a/1190000010901374
import urllib.request
import urllib.parse
import requests
from pprint import pprint
import json
import shutil
import os
import time
import string

region_url = 'http://a.ajmide.com/get_city_list.php'

categories_url = 'https://rapi.qingting.fm/categories/{}/channels?with_total=true&pagesize=50&page={}'

root_director = "FM_Ajmide_List"

city_fm_list_url = "http://a.ajmide.com/v28/get_radio_station_detail.php?position={}"

channel_detail_url = "http://a.ajmide.com/v18/get_play_list.php?frequencyId={}"

all_fm_list = {}

def doRequests(url):
    print(url)
    r = requests.get(url)
    jsonResult = r.json()
    # pprint(jsonResult)
    return jsonResult
    
def request_channels_single_page(regionId, pageIndex):
    result = doRequests(categories_url.format(regionId, pageIndex))
    return result["Data"]

def request_channels(regionId):
    pageIndex = 1
    requstChannelCount = 0
    channelCount = 1
    channels = []
    while channelCount > requstChannelCount:
        result = request_channels_single_page(regionId, pageIndex)
        channelCount = result["total"]
        channels += result["items"]
        requstChannelCount += len(channels)
        pageIndex += 1

    return channels

def simplifyChannel(regionId, channel):
    simplifiedChannel = {}
    channelId = channel["content_id"]
    simplifiedChannel["content_id"] = channelId;
    simplifiedChannel["title"] = channel["title"];
    simplifiedChannel["url"] = 'http://ls.qingting.fm/live/{}/64k.m3u8'.format(channelId);
    simplifiedChannel["poster"] = channel["cover"];
    simplifiedChannel["group_id"] = regionId;
    return simplifiedChannel

def simplifyChannels(regionId, channels):
    simplifiedChannels = []
    for channel in channels:
        simplifiedChannels.append(simplifyChannel(regionId, channel))
    return simplifiedChannels

def request_citys():
    response = doRequests(region_url)
    data = response["data"]
    citys = []
    for x in string.ascii_uppercase[:]:
        if x in data:
            citys += data[x]
    return citys

def request_city_fm_list(cityName):
    response = doRequests(city_fm_list_url.format(cityName))
    data = response["data"]
    global all_fm_list
    if "province" in data:
        for item in data["province"]: 
            if item["name"] not in all_fm_list:
                if "media_data" in item and item["media_data"]:
                    all_fm_list[item["name"]] = request_fm_url(item["media_data"]["channel_id"])
                    
    if "city" in data:
        for item in data["city"]: 
            if item["name"] not in all_fm_list:
                if "media_data" in item and item["media_data"]:
                    all_fm_list[item["name"]] = request_fm_url(item["media_data"]["channel_id"])

def request_fm_url(channel_id):
    response = doRequests(channel_detail_url.format(channel_id))
    data = response["data"]
    if data and len(data) > 0:
        program = data[0]
        return program["liveUrl"]
    return None

if __name__ == "__main__":
    
    if os.path.exists(root_director):
        shutil.rmtree(root_director)    
    os.mkdir(root_director)

    citys = request_citys()

    for city in citys:
        cityName = city["city"]
        request_city_fm_list(cityName)
        

    # print(all_fm_list)

    with open(root_director+'/all.json', 'w') as f:
        json.dump(all_fm_list, f, ensure_ascii=False)

    # version = int(time.time());
    # finalRegions = {};
    # finalRegions["version"] = version;
    # finalRegions["data"] = regions;
    # with open(root_director+'/regions.json', 'w') as f:
    #     json.dump(finalRegions, f, ensure_ascii=False)

    # allChannels = [];
    # for region in regions:
    #     regionId = region["id"]
    #     regionTitle = region["title"]
    #     channels = request_channels(regionId)
    #     simplifiedChannels = simplifyChannels(regionId, channels)
    #     allChannels += simplifiedChannels;
    
    # finalChannels = {};
    # finalChannels["version"] = version;
    # finalChannels["data"] = allChannels;
    # with open(root_director+'/all.json', 'w') as f:
    #     json.dump(finalChannels, f, ensure_ascii=False)