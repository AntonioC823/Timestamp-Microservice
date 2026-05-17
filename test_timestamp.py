import json
import zmq

def main():

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

   
    # valid request
    
    print("\n=== VALID REQUEST ===")

    request1 = {
        "app_name": "Task Manager",
        "user_id": "user123",
        "timestamp_format": "MM-DD-YYYY HH:MM:SS AM/PM"
    }

    socket.send_string(json.dumps(request1))
    response = socket.recv_string()
    print(json.loads(response))


   
    # missing field request
   
    print("\n=== MISSING FIELD ===")

    request2 = {
        "app_name": "Task Manager",
        "timestamp_format": "MM-DD-YYYY HH:MM:SS AM/PM"
    }

    socket.send_string(json.dumps(request2))
    response = socket.recv_string()
    print(json.loads(response))


    
    # unsupported format request
   
    print("\n=== UNSUPPORTED FORMAT ===")

    request3 = {
        "app_name": "Task Manager",
        "user_id": "user123",
        "timestamp_format": "INVALID"
    }

    socket.send_string(json.dumps(request3))
    response = socket.recv_string()
    print(json.loads(response))


if __name__ == "__main__":
    main()