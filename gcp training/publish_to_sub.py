import json
# from google.cloud import pubsub_v1


# topic_path = 'overarching_projecyt'

# publisher = pubsub_v1.PublisherClient()

record ={
  "id": 1,
  "name": "Alice",
  "online": True,
  "picture": "https://picsum.photos/48/48"
}

# data = json.dumps(record).encode("utf-8")
# future = publisher.publish(topic_path, data)
# print(f'published message id {future.result()}')

"""Publishes multiple messages to a Pub/Sub topic with an error handler."""
from concurrent import futures
from google.cloud import pubsub_v1
from typing import Callable

# TODO(developer)
project_id = "promising-lamp-400809"
topic_id = "overachingsubscription"

publisher = pubsub_v1.PublisherClient()
topic_path = "projects/promising-lamp-400809/topics/overarching_projecyt"
publish_futures = []

def get_callback(
    publish_future: pubsub_v1.publisher.futures.Future, data: str
) -> Callable[[pubsub_v1.publisher.futures.Future], None]:
    def callback(publish_future: pubsub_v1.publisher.futures.Future) -> None:
        try:
            # Wait 60 seconds for the publish call to succeed.
            print(publish_future.result(timeout=60))
        except futures.TimeoutError:
            print(f"Publishing {data} timed out.")

    return callback


data = json.dumps(record)
# When you publish a message, the client returns a future.
publish_future = publisher.publish(topic_path, data.encode("utf-8"))
# Non-blocking. Publish failures are handled in the callback function.
publish_future.add_done_callback(get_callback(publish_future, data))
publish_futures.append(publish_future)

# Wait for all the publish futures to resolve before exiting.
futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)

print(f"Published messages with error handler to {topic_path}.")