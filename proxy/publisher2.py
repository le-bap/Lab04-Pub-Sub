import zmq
from time import time, sleep
import random

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

topico = "aleatorio"

while True:
    number = random.randint(1, 6)
    message = f"{topico} {number}"
    print(message, flush=True)
    pub.send_string(message)
    sleep(1)

pub.close()
context.close()
