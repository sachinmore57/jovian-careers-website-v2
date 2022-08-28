from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location': 'Mumbai, India',
    'salary': 'RS. 10,00,000'
  },

  {
    'id':2,
    'title':'Data Scientist',
    'location': 'Mumbai, India',
    'salary': 'RS. 15,00,000'
  },

  {
      'id':3,
      'title': 'Backend Engineer',
      'location': 'Mumbai, India'
    },
  
  {
      'id':4,
      'title':'Data Engineer',
      'location': 'Mumbai, India',
      'salary': 'RS. 18,00,000'
    }
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name = 'Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)