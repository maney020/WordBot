from flask import Flask, request, jsonify
import json
import unirest
import requests


app = Flask(__name__)
port = 5000

### this function gives the exact word that is to be searched for meaning
def resultword(query):
    
    import re
    text = query.lower()
    text = (text.encode('ascii','ignore')).decode('utf-8')

    text = re.sub(r"[-()\"#/@\\;.\[:\]<>{}`^&*_\`?!+=~|,]", " ", text)


    stopwords = ['of','with','word','find','me','is','know','mean','by','give','']
    querywords=text.split()

    result = [word for word in querywords if word not in stopwords]
    resultword = ''.join(result)
    #print resultword

    return resultword

### it will retrieve one example of the word from wordApi
def meaning(text):

    try:
        import unirest

        print text
        response = unirest.get("https://wordsapiv1.p.mashape.com/words/{}/examples".format(text),
        headers={
        "X-Mashape-Key": "7pBaJUdsYLmshtq9gKZgC2S1WLVmp1XVyhGjsnK8AX0kZGT6mg",
        "X-Mashape-Host": "wordsapiv1.p.mashape.com"
        }
        )
        result = response.body
        var = result['examples']
        print var[0]
        return var[0]
    except:
        return "I am unable to find the meaning of the word."



### main routing when meaning intent is triggered
@app.route('/', methods=['POST'])
def index():

  ###  extracting the word from the sentence or retrieving fro recastai JSON
  capture =json.loads(request.get_data())
  
  #to print the output in JSON format for testing purpose
  #print json.dumps(capture, indent=4, sort_keys=True)
  text = capture['conversation']['memory']['SearchWord']['raw']
  print text

  ### it calls the function to clearout out unwanted words
  text = resultword(text)
  print text


  ### it will search for the function and printout the example of the word
  meaningWord = meaning(text)

  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': '{}'.format(meaningWord),
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
