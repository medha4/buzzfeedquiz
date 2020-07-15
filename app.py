# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import random


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/getCharacter', methods = ['GET','POST'])
def getCharacter():
    if request.method == 'GET':
        return "you are getting"
    elif request.method == 'POST':
        props = request.form
        characters = {
            'chandler':['sarcastic', 'midlife'],"joey":['funny', 'actor'],"monica":['serious','chef'],
            'rachel':['airhead','fashion'],
            'ross':['kind','professor'],
            'phoebe':['imagine','music']
        }
        char_dict = {}
        for character in characters:
            common = 0
            if props['job'] == characters[character][1]:
                common+=1
            if props['personality'] == characters[character][0]:
                common+=1
            char_dict[character] = common
        

        like_dict = {}
        for character in char_dict:
            if char_dict[character] > 0:
                like_dict[character] = char_dict[character]
        
        if len(like_dict) == 1:
            return "you are most like: " + next(iter(like_dict))
        else:
            return "you are most like: " + random.choice(list(like_dict))

        return like_dict
    

