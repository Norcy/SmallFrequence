# https://segmentfault.com/a/1190000010901374
import urllib.request
import urllib.parse
import requests
from pprint import pprint
import json
import shutil
import os
import time

region_url = 'https://rapi.qingting.fm/regions'

categories_url = 'https://rapi.qingting.fm/categories/{}/channels?with_total=true&pagesize=50&page={}'

root_director = "FM_List"

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

def request_regions():
    result = doRequests(region_url)
    return result["Data"]

if __name__ == "__main__":
    regions = request_regions()
    
    if os.path.exists(root_director):
        shutil.rmtree(root_director)    
    os.mkdir(root_director)

    version = int(time.time());
    finalRegions = {};
    finalRegions["version"] = version;
    finalRegions["data"] = regions;
    with open(root_director+'/regions.json', 'w') as f:
        json.dump(finalRegions, f, ensure_ascii=False)

    allChannels = [];
    for region in regions:
        regionId = region["id"]
        regionTitle = region["title"]
        channels = request_channels(regionId)
        simplifiedChannels = simplifyChannels(regionId, channels)
        allChannels += simplifiedChannels;
    
    finalChannels = {};
    finalChannels["version"] = version;
    finalChannels["data"] = allChannels;
    with open(root_director+'/all.json', 'w') as f:
        json.dump(finalChannels, f, ensure_ascii=False)