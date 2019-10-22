from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1") #annotations tell which function goes with which request
def render_page1():
    
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')

@app.route("/p3")
def render_page3():
    return render_template('page3.html')

@app.route("/response")
def render_response():
    celsius_value = float(request.args['Celsius'])
    response = (celsius_value * (9/5)) + 32
    return render_template('response.html', responseFromServer = response)

@app.route("/response2")
def render_response2():
    kelvin_value = float(request.args['Kelvin'])
    response2 = kelvin_value - 273.15
    return render_template('response2.html', responseFromServer2 = response2)

@app.route("/response3")
def render_response3():
    fahrenheit = float(request.args['Fahrenheit'])
    response3 = (fahrenheit_value − 273.15) × 9/5 + 32
    return render_template('response3.html', responseFromServer3 = response3)

    
if __name__=="__main__":
    app.run(debug=False)
