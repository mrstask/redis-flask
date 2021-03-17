import redis
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():

    # connect to redis
    client = redis.Redis(host='redis', port=6379)

    # set a key
    client.set('test-key', 'test-value')

    # get a value
    value = client.get('test-key')
    print(value)
    return 'Hello from Docker within PyCharm!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
