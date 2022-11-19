from flask import Flask, render_template, request
from gpiozero import LED
from time import sleep
#Copy and paste imports

led = LED(17)
led_on = False
app = Flask(__name__)
#/ means home page of the host/

@app.route('/')

#app captured request and gives the template index.html

#Decorator receives request
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/animate', methods=['POST'])
def animate():
    animate = request.form['dropdown']
    led.off()
    if animate == 'on':
        print('light on')
        #led_on == True
        led.on()
    elif animate == 'off':
        print('light off')
        #led_on == False
        led.off()
    else:
        print('light blinking')
        led_on = True
        while led_on:
            led.on()
            sleep(1)
            led.off()
            sleep(1)

    return render_template('on.html')

#app captured request and gives the template index.html
def about():
    return render_template('about.html')


    

    #display = f'{message}  Love, {name}'
    #sense.show_message(display, text_colour=[0, 0, 255])
    
    
    
    #returing received.html
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#hosting it from your computer
