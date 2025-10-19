from flask import Flask , render_template 


app = Flask(__name__)


@app.route("/")
def indexpage():
   return render_template("index.html" , value="1234")




if __name__ == "__main__":
   app.run( host='0.0.0.0' , debug=True, port=80 )



