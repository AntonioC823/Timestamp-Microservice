import json
from datetime import datetime
import zmq

def generate_timestamp(timestamp_format):
    """
    Generates the current timestamp using the requested format.
    """

    if timestamp_format == "MM/DD/YYYY HH:MM:SS AM/PM" or timestamp_format == "":
        return datetime.now().strftime("%m/%d/%Y %I:%M:%S %p") # Use %I for 12-hour clock

    if timestamp_format == "MM-DD-YYYY HH:MM:SS AM/PM":
        return datetime.now().strftime("%m-%d-%Y %I:%M:%S %p") # Use %I for 12-hour clock

    if timestamp_format == "MM/DD/YYYY HH:MM:SS":
        return datetime.now().strftime("%m/%d/%Y %H:%M:%S") # Use %H for 24-hour clock

    if timestamp_format == "MM-DD-YYYY HH:MM:SS":
        return datetime.now().strftime("%m-%d-%Y %H:%M:%S") # Use %H for 24-hour clock

    if timestamp_format == "DD/MM/YYYY HH:MM:SS AM/PM":
        return datetime.now().strftime("%d/%m/%Y %I:%M:%S %p") # Use %I for 12-hour clock

    if timestamp_format == "DD-MM-YYYY HH:MM:SS AM/PM":
        return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") # Use %I for 12-hour clock

    if timestamp_format == "DD/MM/YYYY HH:MM:SS":
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Use %H for 24-hour clock

    if timestamp_format == "DD-MM-YYYY HH:MM:SS":
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S") # Use %H for 24-hour clock

    # Return None if client requested a timestamp in the wrong format
    return None



def main():
    """
    Starts the Timestamp service that utilizes ZeroMQ request/reply communication.
    """

    context = zmq.Context()

    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Timestamp service is running on tcp://localhost:5555")

    while True:

        # Receive request from client
        request = socket.recv_string()

        # Convert JSON string to Python dictionary
        data = json.loads(request)

        app_name = data.get("app_name")
        user_id = data.get("user_id")
        timestamp_format = data.get("timestamp_format")

        # validate fields
        if not app_name:
            response = {
                "message": "Missing required field: app_name"
            }

        elif not user_id:
            response = {
                "message": "Missing required field: user_id"
            }

        elif timestamp_format is None:
            response = {
                "message": "Missing required field: timestamp_format"
            }

        else:

            # Generate timestamp
            timestamp = generate_timestamp(timestamp_format)

            # Response
            if timestamp is None:
                response = {
                    "message": "Unsupported timestamp format"
                }
            else:
                response = {
                    "app_name": app_name,
                    "user_id": user_id,
                    "timestamp_format": timestamp_format,
                    "timestamp": timestamp
                }

        # Send response
        socket.send_string(json.dumps(response))


if __name__ == "__main__":
    main()