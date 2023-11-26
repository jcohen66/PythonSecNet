import datetime
import jwt
SECRET_KEY = ''
json_data = {
    "sender": "Python JWT",d
    "message": "Testing Python JWT",
    "date": str(datetime.datetime.now()),
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
}

encoded_token = jwt.encode(json_data, SECRET_KEY, algorithm='HS256')
print("Encoded token: " + encoded_token)

try:
    decoded_token = jwt.decode(encoded_token, SECRET_KEY, algorithms=['HS256'])
    print(f"Decoded token: {decoded_token}")
except Exception as e:
    message = f"Token is invalid --> {e}"
    print({"message": message})

