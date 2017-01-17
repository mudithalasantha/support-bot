import os
import sys
import json
import requests
import urllib, json
import psql
#print(api.info())

class MyMovie:
    
    def __init__(self):
        #        self.data = []
        self.fbid = None
        self.movie = 'empty'
        self.theater = 'empty'
        self.date = 'empty'
        self.time = 'empty'
        self.status = 'empty'
        self.id = None
        self.last_edit = 'empty'


def CheckMyMovie(userID):
    row_count = psql.is_purchase_movie_tickets_available(userID)
    if row_count == 1:
        return True
    else:
        return False

def GetMyMovie(userID):
    return psql.get_purchase_movie_tickets(userID)

def CreateMyMovie(userID):
    newMyMovie = MyMovie()
    newMyMovie.fbid = userID
    newMyMovie.movie = 'NoMovie'
    newMyMovie.theater = 'NoTheater'
    newMyMovie.date = 'NoDate'
    newMyMovie.time = 'NoTime'
    newMyMovie.status = 'JustCreated'
    
    psql.insert_purchase_movie_tickets(newMyMovie)
    
    return psql.get_user(newMyMovie.id)

def UpdateMyMovie(userID, mMovie):
    if psql.update_purchase_movie_tickets(userID,mMovie) == 0:
        log("Error : MyMovie not found for update id. : " + str(userID))
    else:
        log("Success : MyMovie updated. id : " + str(userID))

def getMovieList(userTemplate):

    data = json.dumps({
            "recipient": {
                "id": userTemplate.id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "list",
                        "top_element_style": "compact",
                        "elements": [
                                     {
                                     "title": "MOANA",
                                     "image_url": "http://www.eapmovies.com/components/com_eapmovies/includes/images/movies/movies_366/movies_366_5811f1cbafcc8_02.jpg",
                                     "subtitle": "American 3D computer-animated musical fantasy comedy adventure",
                                     "default_action": {
                                        "type": "web_url",
                                        "url": "https://m.youtube.com/watch?v=LKFuXETZUsI",
                                        "messenger_extensions": "true",
                                        "webview_height_ratio": "tall",
                                        "fallback_url": "https://m.youtube.com/watch?v=LKFuXETZUsI"
                                     },
                                     "buttons": [
                                        {
                                            "title": "Select",
                                            "type": "postback",
                                            "payload": "MovieTickets:SelectTheater%MOANA%NoTheater%NoDate%NoTime:Please select theater from below list."
                                        }
                                        ]
                                     },
                     {
                     "title": "64 Mayam",
                     "image_url": "http://www.eapmovies.com/components/com_eapmovies/includes/images/movies/movies_372/movies_372_5821bfb7d22ed_03.jpg",
                     "subtitle": "Comedy",
                     "default_action": {
                     "type": "web_url",
                     "url": "https://m.youtube.com/watch?v=6rfkwSQ1dQ4",
                     "messenger_extensions": "true",
                     "webview_height_ratio": "tall",
                     "fallback_url": "https://m.youtube.com/watch?v=6rfkwSQ1dQ4"
                     },
                     "buttons": [
                                 {
                                 "title": "Select",
                                 "type": "postback",
                                 "payload": "MovieTickets:SelectTheater%64 Mayam%NoTheater%NoDate%NoTime:Please select theater from below list."
                                 }
                                 ]
                     },
                     {
                     "title": "Assassin'S Creed",
                     "image_url": "http://www.eapmovies.com/components/com_eapmovies/includes/images/movies/movies_382/movies_382_583d4c083d919_003.jpg",
                     "subtitle": "Action adventure",
                     "default_action": {
                     "type": "web_url",
                     "url": "https://m.youtube.com/watch?v=gfJVoF5ko1Y",
                     "messenger_extensions": "true",
                     "webview_height_ratio": "tall",
                     "fallback_url": "https://m.youtube.com/watch?v=gfJVoF5ko1Y"
                     },
                     "buttons": [
                                 {
                                 "title": "Select",
                                 "type": "postback",
                                 "payload": "MovieTickets:SelectTheater%Assassin'S Creed%NoTheater%NoDate%NoTime:Please select theater from below list."
                                 }
                                 ]
                     },
                     {
                     "title": "Zoom",
                     "image_url": "http://www.eapmovies.com/components/com_eapmovies/includes/images/movies/movies_390/movies_390_5853dbac7b507_j0koa070.jpg",
                     "subtitle": "Horror",
                     "default_action": {
                     "type": "web_url",
                     "url": "https://m.youtube.com/watch?v=QINtUD6muF8",
                     "messenger_extensions": "true",
                     "webview_height_ratio": "tall",
                     "fallback_url": "https://m.youtube.com/watch?v=QINtUD6muF8"
                     },
                     "buttons": [
                                 {
                                 "title": "Select",
                                 "type": "postback",
                                 "payload": "MovieTickets:SelectTheater%Zoom%NoTheater%NoDate%NoTime:Please select theater from below list."
                                 }
                                 ]
                     }
                     ],
                     "buttons": [
                                 {
                                 "title": "View More",
                                 "type": "postback",
                                 "payload": "payload"
                                 }
                                 ]
                     }
                }
            }
        })
    return data

def getTheaterList(userTemplate):
    data = json.dumps({
                      "recipient": {
                      "id": userTemplate.id
                      },
                      "message": {
                      "attachment": {
                      "type": "template",
                      "payload": {
                      "template_type": "list",
                      "top_element_style": "compact",
                      "elements": [
                                   {
                                   "title": "Liberty",
                                   "image_url": "http://www.eapmovies.com/components/com_eapmovies/includes/images/theaters/theater_6/theater_6_51add7a324282_1.JPG",
                                   "subtitle": "Colombo 3",
#                                   "default_action": {
#                                   "type": "web_url",
#                                   "url": "",
#                                   "messenger_extensions": "true",
#                                   "webview_height_ratio": "tall",
#                                   "fallback_url": ""
#                                   },
                                   "buttons": [
                                               {
                                               "title": "Select",
                                               "type": "postback",
                                               "payload": "MovieTickets:SelectDate%NoMovie%Liberty%NoDate%NoTime:Please enter date."
                                               }
                                               ]
                                   },
                                   {
                                   "title": "Cinemax 3D",
                                   "image_url": "http://www.eapmovies.com/components/com_eapmovies/includes/images/theaters/theater_8/theater_8_5121ef42cb837_3.JPG",
                                   "subtitle": "Jaela",
#                                   "default_action": {
#                                   "type": "web_url",
#                                   "url": "",
#                                   "messenger_extensions": "true",
#                                   "webview_height_ratio": "tall",
#                                   "fallback_url": ""
#                                   },
                                   "buttons": [
                                               {
                                               "title": "Select",
                                               "type": "postback",
                                               "payload": "MovieTickets:SelectDate%NoMovie%Cinemax 3D%NoDate%NoTime:Please enter date."
                                               }
                                               ]
                                   },
                                   {
                                   "title": "Savoy 2",
                                   "image_url": "http://www.eapmovies.com/components/com_eapmovies/includes/images/theaters/theater_2/theater_2_4ffd4f2ae2703_1400.jpg",
                                   "subtitle": "Wellawatte",
#                                   "default_action": {
#                                   "type": "web_url",
#                                   "url": "",
#                                   "messenger_extensions": "true",
#                                   "webview_height_ratio": "tall",
#                                   "fallback_url": ""
#                                   },
                                   "buttons": [
                                               {
                                               "title": "Select",
                                               "type": "postback",
                                               "payload": "MovieTickets:SelectDate%NoMovie%Savoy 2%NoDate%NoTime:Please enter date."
                                               }
                                               ]
                                   },
                                   {
                                   "title": "Willmax 3D",
                                   "image_url": "http://www.eapmovies.com/components/com_eapmovies/includes/images/theaters/theater_10/theater_10_502b6e093c971_Willmax%201.JPG",
                                   "subtitle": "Anuradhapura",
#                                   "default_action": {
#                                   "type": "web_url",
#                                   "url": "",
#                                   "messenger_extensions": "true",
#                                   "webview_height_ratio": "tall",
#                                   "fallback_url": ""
#                                   },
                                   "buttons": [
                                               {
                                               "title": "Select",
                                               "type": "postback",
                                               "payload": "MovieTickets:SelectDate%NoMovie%Willmax 3D%NoDate%NoTime:Please enter date."
                                               }
                                               ]
                                   }
                                   ]
                    }
                }
            }
        })
    return data

