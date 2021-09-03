import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
button = 3  # GPIO 2 on PIN 3
GPIO.setup(button, GPIO.IN)

ifttt_event_name = 'pi_poubelle'
ifttt_api_key = '##REDACTED##'
ifttt_webhook_url = f'https://maker.ifttt.com/trigger/{ifttt_event_name}/with/key/{ifttt_api_key}'

try:
    state_before = 0
    while True:
        state = GPIO.input(button)
#         print(state)
        time.sleep(0.1)
        if state == 0 and state_before == 1:
            requests.post(ifttt_webhook_url)
        state_before = state
except KeyboardInterrupt:
    print("You've exited the program")
finally:
    GPIO.cleanup()
