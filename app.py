from flask import Flask, render_template
import pygal 

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('home.html')

@app.route('/index')
def graph():

    browser = pygal.Line()
    browser.title = 'Change of programming languages over the years'
    browser.x_labels = ['2011','2012','2013','2014','2015','2016']
    browser.add('Python', [15, 31, 89, 200, 350,960])
    browser.add('Java',    [15, 45, 76, 80,  91,  95])
    browser.add('C++',     [5,  51, 54, 102, 150, 201])
    browser.add('All others combined!',  [5, 15, 21, 55, 92, 105])
    line = browser.render_data_uri()
    
    

    return render_template('index.html', line=linee)

@app.route('/usage')
def usage():

   


    return render_template('usage.html')

if __name__ == "__main__":
    pass