from flask import Flask,render_template
app=Flask(__name__)
@app.route('/fetch')
def fetch():
  import requests
  import json
  url="https://dashboard.nbshare.io/api/v1/apps/reddit"
  resp=requests.get(url)
  resp=resp.json()
  result=""
  for i in resp:
    result=result+str(i["ticker"])+": "+str(i["sentiment"])+"\n"
    text=result.split('\n')
  return render_template("index.html",text=text)
if __name__=="__main__":
  app.run()
