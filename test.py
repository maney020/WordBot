'''
import recastai

connect = recastai.Connect('023b08289cb13c6e96923628eccb4c45')

messages = [
  {
    'type': 'text',
    'content': 'Roger',
  }
]


connect.broadcast_message(messages)
'''
import unirest
import json
import requests


response = unirest.get("https://wordsapiv1.p.mashape.com/words/modern/examples",
  headers={
    "X-Mashape-Key": "7pBaJUdsYLmshtq9gKZgC2S1WLVmp1XVyhGjsnK8AX0kZGT6mg",
    "X-Mashape-Host": "wordsapiv1.p.mashape.com"
  }
)


result = response.body
var = result['examples']
print var[0]

