import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    pass_test = "abc123"
    pass_hash = generate_password_hash(pass_test)
    output_string = "pass_test is: " + pass_test + " and pass_hash is: " + pass_hash
    #return output_string
    #return "hello, world"
    return render_template("template.html")