import os
from openai import OpenAI
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()  # load env vars from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response")
def get_response():
    try:
        message = request.args.get("message")
        system = {"role": "system", "content": "You are a Journalist Recommender"}
        user = {"role":"user", "content":message}
        
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[system, user],
        )
        response = completion.choices[0].message.content
        return response
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
