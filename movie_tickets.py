import os
import sys
import json
import requests
import urllib, json
#print(api.info())

def getMovieList():

    data = json.dumps({
            "recipient": {
                "id": "userTemplate.id"
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
                                        "messenger_extensions": true,
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
                     "messenger_extensions": true,
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
                     "messenger_extensions": true,
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
                     "messenger_extensions": true,
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


def init_diagnose(symptom_id,age,gender,sender_id):
	request = infermedica_api.Diagnosis(sex=gender, age=age)
	request.add_symptom(symptom_id, 'present')
	request = api.diagnosis(request)
	return request

def improve_diagnosis(request,sender_id,question_id,choice_id):
	request.add_symptom(question_id,choice_id)
	request = api.diagnosis(request)
	return request


