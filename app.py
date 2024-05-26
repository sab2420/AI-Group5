from flask import Flask, render_template, request
import google.generativeai as palm
import os
from flask import url_for

flag = 1
name = ""

makersuite_api = os.getenv("MAKERSUITE_API_TOKEN")
palm.configure(api_key=makersuite_api)

model = {"model" : "models/chat-bison-001"}
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    r = request.form.get("q")
    return(render_template("main.html",r=r))

@app.route("/open_account",methods = ["GET","POST"])
def open_account():
    return(render_template("open_account.html"))

@app.route("/thank_you",methods = ["GET","POST"])
def thank_you():
    return(render_template("thank_you.html"))

@app.route("/generate_text",methods = ["GET","POST"])
def generate_text():
    return(render_template("generate_text.html"))

@app.route("/text_result_makersuite",methods = ["GET","POST"])
def text_result_makersuite():
    q = request.form.get("q")
    r = palm.chat(**model, messages=q)
    return(render_template("text_result_makersuite.html",r=r.last))

@app.route("/end",methods = ["GET","POST"])
def end():
    global flag
    flag = 1
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()
