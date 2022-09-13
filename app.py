#! /usr/bin/python
import requests
import re
import json
import anvil.server

anvil.server.connect("KXVF2Y6NDXKWDHHVS5M4MOM5-XEUMR6PY4G7KPZVU")

@anvil.server.callable
def getBaseUrl():
 url = 'https://bible-go-api.rkeplin.com/v1/books'
 return url

#This method will get Chapter names
@anvil.server.callable
def getBook():
 rsp = requests.get(getBaseUrl())
 rspJSON = rsp.json() 
 return rspJSON

#This method will get Verses for chapter 1
@anvil.server.callable
def getVerses(mybook):
 url = getBaseUrl()
 url = url + '/' + mybook + '/chapters/1'
 rsp = requests.get(url)
 rspJSON = rsp.json()
 return rspJSON

@anvil.server.callable
def getNextChapter(mybook, chapter):
 url = getBaseUrl()
 length = getChapterLength(mybook)
 
 if int(chapter) <= int(length):
 # chapter = str(int(chapter) + 1)
  url = url + '/' + mybook + '/chapters/' + chapter
  rsp = requests.get(url)
  rspJSON = rsp.json() 
 return rspJSON



@anvil.server.callable
def getBackChapter(mybook, chapter):
 url = getBaseUrl()
 if int(chapter) >= 1:
  url = url + '/' + mybook + '/chapters/' + chapter
  rsp = requests.get(url)
  rspJSON = rsp.json()
 return rspJSON


#This method will retreive chapter length
@anvil.server.callable
def getChapterLength(mybook):
 chapterLength = 0
 url = getBaseUrl()
 url = url + '/' + mybook + '/chapters'
 rsp = requests.get(url)
 rspJSON = rsp.json()
 for item in rspJSON:
  if "id" in item:
   chapterLength +=1
 return chapterLength


@anvil.server.callable
def getCurrentChapter(mybook, currentChapter):
 url = getBaseUrl()
 url = url + '/' + mybook + '/chapters/' + currentChapter
 rsp = requests.get(url)
 rspJSON = rsp.json()
 return  rspJSON
anvil.server.wait_forever()