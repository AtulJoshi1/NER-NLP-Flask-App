from flask import render_template
from flask import Flask
from spacy import displacy
import spacy
from flask import request

nlp = spacy.load("en_core_web_sm")
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html",title="Welcome to NER App!")

@app.route('/result', methods = ['GET','POST'])
def get_entities():
    result = request.form
    text = result['inputText']
    doc = nlp(text)
    out_lst = [i.text for i in doc.ents] 
    return render_template("output.html",title="Your Output!",entities = str(out_lst))

@app.route('/display', methods = ['GET','POST'])
def display():
    result = request.form
    text = result['inputText']
    doc = nlp(text)
    return  displacy.render(doc, style="ent")

@app.route('/display_dep', methods = ['GET','POST'])
def display_dep():
    result = request.form
    text = result['inputText']
    doc = nlp(text)
    return  displacy.render(doc, style="dep")

if __name__=="__main__":
    app.run(debug="True")