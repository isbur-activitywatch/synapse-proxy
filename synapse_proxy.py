import time
import zmq


from Synapse import Synapse


print('Starting to listen...')
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
     
    message = socket.recv_string()
    print(message)
    Synapse.post(message)
    socket.send_string("OK")
    time.sleep(1)