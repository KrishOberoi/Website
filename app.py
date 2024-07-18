from flask import Flask, render_template

app = Flask(__name__)

jobs = [
  {   
    'id': 1,
    'title': 'Data Analyst',
    'salary': 'Rs. 10,00,000'
  },
  {  
    'id': 2,
    'title': 'sofware engineer',
    'salary': 'Rs. 12,90,999'
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', name='Krish',job=jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
