A. Timestamp-Microservice
The microservice generates formatted timestamps for applications and returns them as JSON responses.

B. To grammatically REQUEST data from the microservice: A program connects to it using ZeroMQ. It sends a message in JSON format that includes the required information: app_name, user_id, and timestamp_format. The microservice uses this information to generate a timestamp or return an error message.

import json
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = {
    "app_name": "Task Manager",
    "user_id": "user123",
    "timestamp_format": "MM-DD-YYYY HH:MM:SS AM/PM"
}

socket.send_string(json.dumps(request))


C. To programmatically RECEIVE data from the microservice: After sending a request, the program waits for a response from the microservice. The response comes back as a JSON string. The program then converts it into a Python dictionary so it can be used or printed. 

response = socket.recv_string()
data = json.loads(response)

print(data)


D. UML sequence diagram