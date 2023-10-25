from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def hellow():
  return render_template('portfolio.html')


if __name__ == "__main__":
  print("I'm inside the __name__")
  app.run(host='0.0.0.0', debug=false)