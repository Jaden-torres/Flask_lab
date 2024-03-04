import urllib.request, json
from flask import Flask, render_template, request

app = Flask(__name__)       

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name) 

@app.route("/")                
def hello():                
    url = "https://xkcd.com/info.0.json"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)    
    return render_template("index.html", datum=dict) 
if __name__ == "__main__":       
    app.run(debug=True)                    

@app.route("/<name>")   
def hello_name(name):             
    return "Hello "+ name          
