from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def square():
    return render_template("index.html", my_color = 'blue', times = 3)

@app.route('/play/<string:color>')
def square1(color):
    return render_template("index.html", my_color= color, times = 3)

@app.route('/play/<string:color>/int:num')
def square2(color,num):
    return render_template("index.html", my_color= color, times = num)



if __name__=="__main__":
    app.run(debug=True, port = 5001)

