import uuid
import redis
import json
import pika


def publish_to_rabbitMQ(data):
    # Create connection
    connection = pika.BlockingConnection(
        pika.URLParameters("amqps://dlluefkd:69bRQiu8XYM5fZzKkNuXoxsFmB18iCEk@woodpecker.rmq.cloudamqp.com/dlluefkd"))
    channel = connection.channel()
    # Create queue . For now queue name is factorial_process
    channel.queue_declare(queue='factorial_process', durable=True)
    # Publish the message to the queue
    channel.basic_publish(exchange='', routing_key='factorial_process', body=json.dumps(data))
    # Close the connection
    connection.close()


pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis_instnace = redis.Redis(connection_pool=pool)


def create_request(input):
    # Generate a random ID
    random_id = str(uuid.uuid4())
    # Store the request in Redis
    redis_instnace.set(random_id, json.dumps({'input': input, 'status': 'processing', 'output': ''}))
    # Publish the request to RabbitMQ
    publish_to_rabbitMQ({'request_id': random_id, 'input': input})
    # Return the request ID
    return random_id


def get_request(request_id):
    request_data = redis_instnace.get(request_id)
    if request_data:
        return json.loads(request_data)
    return None


def update_request(request_id, status, output):
    request_details = get_request(request_id)
    redis_instnace.set(request_id, json.dumps({'input': request_details['input'], 'status': status, 'output': output}))


from flask import Flask, request

# create the Flask app
app = Flask(__name__)


# route to queue the request
@app.route('/factorial', methods=['GET'])
def factorial_handler():
    no = int(request.args.get('no'))
    id = create_request(no)
    return id


# route to get the result
@app.route('/factorial/result', methods=['GET'])
def factorial_result_handler():
    id = request.args.get('id')
    result = get_request(id)
    return result


# route to update the result
@app.route('/factorial/update', methods=['POST'])
def factorial_update_handler():
    body = request.get_json()
    id = body['id']
    status = body['status']
    output = body['output']
    update_request(id, status, output)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=False)
