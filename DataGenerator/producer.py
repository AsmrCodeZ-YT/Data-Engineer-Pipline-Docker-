import time
import random
import json
import redis
from datetime import datetime

row_data = {
    "gender" : ["male", "female"],
    "age" : [i for i in range(18, 60)],
    "mark": [i for i in range(50, 100)],
    "diese": [True, False],

}

def generate_data():
    while True:
        user_id = random.randint(100, 999)
        producer = {
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
        }
        for index, value in row_data.items():
            producer[index] = random.choice(value)

        yield json.dumps(producer)
        time.sleep(0.1)


if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379)
    for data in generate_data():
        r.rpush("information", data)
        print(data)
