import zmq
from time import sleep
from datetime import datetime

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

topico = "horas"

while True:
    message = f"{topico} {datetime.now().strftime('%H:%M:%S')}"
    print(message, flush=True)
    pub.send_string(message)
    sleep(1)

pub.close()
context.close()