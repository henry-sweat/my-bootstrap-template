from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():

   return render_template('base.html')

@app.route('/page')
def page():

   return render_template('page.html')

@app.route('/form')
def form():

   return render_template('form.html')

if __name__ == '__main__':
    app.run()