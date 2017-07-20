from flask import Flask, render_template,request, redirect, url_for
import serial

ser = serial.Serial("COM4")
app = Flask(__name__)
# we are able to make 2 different requests on our webpage
# GET = we just type in the url
# POST = some sort of form submission like a button
@app.route('/', methods = ['POST','GET'])
def hello_world():
    # if we make a post request on the webpage aka press button then do stuff
    text=request.form["text1"]
    print text
    b = str(text.encode('utf-8').decode('ascii', 'ignore'))
    ser.write(b)
    if request.method == 'POST':
        # if we press the turn on button
        if request.form['submit'] == 'Turn On':
            ser.write("0")
            print 'TURN ON'
            
        # if we press the turn off button
        elif request.form['submit'] == 'Turn Off': 
            print 'TURN OFF'
            ser.write("1")
        #for lcd control
        elif request.form["submit"]=="Clear LCD":
            print "clear lcd"
            ser.write("2")
        else:
            pass
        
    # the default page to display will be our template with our template variables
    return render_template('index.html')

@app.errorhandler(400)      #to handel the 400(bad request error)
def page_not_found(e):
    return render_template('index.html')
if __name__ == "__main__":

    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    app.run(host='0.0.0.0')
