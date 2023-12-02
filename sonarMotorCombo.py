import RPi.GPIO as GPIO
import time

Lin1 = 24
Lin2 = 23
Len = 25

Rin1 = 9
Rin2 = 10
Ren = 11

speed = 0
toggle = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(Lin1,GPIO.OUT)
GPIO.setup(Lin2,GPIO.OUT)
GPIO.setup(Len,GPIO.OUT)
GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.LOW)
p=GPIO.PWM(Len,1000)

GPIO.setup(Rin1,GPIO.OUT)
GPIO.setup(Rin2,GPIO.OUT)
GPIO.setup(Ren,GPIO.OUT)
GPIO.output(Rin1,GPIO.LOW)
GPIO.output(Rin2,GPIO.LOW)
w=GPIO.PWM(Ren,1000)


p.start(50)
w.start(50)
print("\n\tw-forward a-left s-backward d-right\n")
print("\tr-run c-stop Hold Shift to go faster\n")
print("\tPress e to cleanup before and after running\n")

while(1):

    x=input()
    
    if x=='r':
        print("run")
        toggle = 1
    
    elif x=='t':
        try:
            GPIO.setmode(GPIO.BCM)

            TRIG = 20  
            ECHO = 21
            pmwVal = 20
            gainVal = 5
            timeCount = 0

            # Set up the GPIO pins as output 
            GPIO.setup(TRIG, GPIO.OUT)
            GPIO.setup(ECHO, GPIO.IN)

            # Initialize the trigger pin to a low state
            GPIO.output(TRIG, False)

            print("Waiting for Sensor")
            time.sleep(2)

            # Send a short pulse
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

            # Measure pulse return time
            while GPIO.input(ECHO) == 0:
                pulse_start = time.time()

            while GPIO.input(ECHO) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            # Calculate Distance
            distance = pulse_duration * 17150
            prevDist = round(distance, 2)

            time.sleep(0.5)
            
            while(timeCount < 200):
                # 20 second timer
                timeCount += 1

                # Send a short pulse
                GPIO.output(TRIG, True)
                time.sleep(0.00001)
                GPIO.output(TRIG, False)

                # Measure pulse return time
                while GPIO.input(ECHO) == 0:
                    pulse_start = time.time()

                while GPIO.input(ECHO) == 1:
                    pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start

                # Calaulate Distance
                distance = pulse_duration * 17150
                distance = round(distance, 2)

                error = prevDist - distance

                # When distance changes by over +0.25 cm
                if(error > 0.5 and pmwVal>0):
                    pmwVal -= gainVal

                elif(error < -0.5 and pmwVal<100):
                    pmwVal += gainVal

                else:
                    pmwVal = pmwVal

                p.ChangeDutyCycle(pmwVal)
                w.ChangeDutyCycle(pmwVal)

                GPIO.output(Lin1,GPIO.HIGH)
                GPIO.output(Lin2,GPIO.LOW)
                GPIO.output(Rin1,GPIO.LOW)
                GPIO.output(Rin2,GPIO.HIGH)

                print("\rPMW: " + str(pmwVal) + " %\tTimer: " + str(timeCount*0.1) + " sec\tDistance: " + str(distance) + " cm\tPrevious Distance: " + str(prevDist) + " cm", end = "     ")
            
                prevDist = distance

                time.sleep(.1)
            
            p.ChangeDutyCycle(0)
            w.ChangeDutyCycle(0)

            GPIO.output(Lin1,GPIO.HIGH)
            GPIO.output(Lin2,GPIO.LOW)
            GPIO.output(Rin1,GPIO.LOW)
            GPIO.output(Rin2,GPIO.HIGH)
            print("\n")
            timeCount = 0
            x = 'r'
        finally:
            x = 'r'

    elif x=='c':
        print("stop")
        toggle = 0

        GPIO.output(Lin1,GPIO.LOW)
        GPIO.output(Lin2,GPIO.LOW)
        GPIO.output(Rin1,GPIO.LOW)
        GPIO.output(Rin2,GPIO.LOW)
        x='z'

    elif (x=='w' and toggle==1):
        print("forward")


        if (speed==0):
            p.ChangeDutyCycle(50)
            w.ChangeDutyCycle(50)
        else:
            p.ChangeDutyCycle(100)
            w.ChangeDutyCycle(100)

        GPIO.output(Lin1,GPIO.HIGH)
        GPIO.output(Lin2,GPIO.LOW)
        GPIO.output(Rin1,GPIO.LOW)
        GPIO.output(Rin2,GPIO.HIGH)
        x='z'

    elif (x=='s' and toggle==1):
        print("backward")


        if (speed==0):
            p.ChangeDutyCycle(50)
            w.ChangeDutyCycle(50)
        else:
            p.ChangeDutyCycle(100)
            w.ChangeDutyCycle(100)

        GPIO.output(Lin1,GPIO.LOW)
        GPIO.output(Lin2,GPIO.HIGH)
        GPIO.output(Rin1,GPIO.HIGH)
        GPIO.output(Rin2,GPIO.LOW)
        x='z'

    elif (x=='a' and toggle==1):
        print("left")

        p.ChangeDutyCycle(30)
        w.ChangeDutyCycle(30)

        GPIO.output(Lin1,GPIO.LOW)
        GPIO.output(Lin2,GPIO.HIGH)
        GPIO.output(Rin1,GPIO.LOW)
        GPIO.output(Rin2,GPIO.HIGH)
        x='z'

    elif (x=='d' and toggle==1):
        print("right")

        p.ChangeDutyCycle(30)
        w.ChangeDutyCycle(30)

        GPIO.output(Lin1,GPIO.HIGH)
        GPIO.output(Lin2,GPIO.LOW)
        GPIO.output(Rin1,GPIO.HIGH)
        GPIO.output(Rin2,GPIO.LOW)
        x='z'

    elif x=='h': #Change to shift key
             
        if (speed==0):
            print("Toggled Speed to Fast Mode")
            speed = 1

            p.ChangeDutyCycle(100)
            w.ChangeDutyCycle(100)
        else:
            print("Toggled Speed to Normal Mode")
            speed = 0
            
            p.ChangeDutyCycle(50)
            w.ChangeDutyCycle(50)
        x='z'
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

