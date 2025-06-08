import json
import uuid
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis_instnace = redis.Redis(connection_pool=pool)

def create_request(input):
    # Generate a random ID
    random_id = str(uuid.uuid4())
    # Store the request in Redis
    redis_instnace.set(random_id, json.dumps({'input': input, 'status': 'processing', 'output': ''}))
    # Return the request ID
    return random_id

#create_request(15)

def get_request(request_id):
    request_data = redis_instnace.get(request_id)
    if request_data:
        return json.loads(request_data)
    return None
print(get_request("56662c29-7bd6-45b3-a8f1-736b0ab53624"))
