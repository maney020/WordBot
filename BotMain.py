from flask import Flask, request, jsonify
import json
import unirest


app = Flask(__name__)
port = '5000'

@app.route('/', methods=['POST'])
def index():
  print(json.loads(request.get_data()))
  response = unirest.get("https://wordsapiv1.p.mashape.com/words/modern/examples",
  headers={
    "X-Mashape-Key": "7pBaJUdsYLmshtq9gKZgC2S1WLVmp1XVyhGjsnK8AX0kZGT6mg",
    "X-Mashape-Host": "wordsapiv1.p.mashape.com"
    }
  )
  
  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'Roger that',
    }],
    conversation={
      'memory': { 'key': 'value' }
    }
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port)
