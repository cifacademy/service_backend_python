# external modules
import json
import redis
import pyrootutils

root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml"],
    pythonpath=True,
    dotenv=True,
)

# internal modules
import src.infra.time_infra as ABTime
from src.infra.logger_infra import ABLogger
import src.infra.text_infra as text_processing

class RedisInfraV2:

    def __init__(self) -> None:
        self.logger = ABLogger()
        self.logger.info("[RedisInfraV2] running!")

    def redis_connection(self, host: str, port:str, database:str):
        """
        redis_connection was provide us a connection to redis
        """
        try:
            self.connect = redis.Redis(host=host, port=port, db=database)
            self.pubsub = self.connect.pubsub()
            self.logger(f"Connected to redis database {host}:{port}/{database}")
        except Exception as e:
            self.logger.error(f"Redis connection catch an error: {e}")

    def publish_redis(self, channel: str, data: str):
        """
        publish_redis data to a channel.

        Args:
            channel (str): stream channel
            data (str): data to publish
        """        
        data = json.dumps(data, default=lambda o: o.__dict__)
        self.connect.publish(channel, data)
        self.logger(f"{channel} Data published")

    def subscribe_redis(self, channels: list):
        """
        Subscribe to a channel.

        Args:
            channels (list) : a collection of stream channel
                example : 

        Return:
            json data of ....
        """        
        self.logger(f"Subscribing to channel: {channels}")
        self.pubsub.subscribe(channels)
        for message in self.pubsub.listen():
            if message["type"] == "message":
                data = json.loads(message["data"].decode("utf-8"))
                self.logger(f"Subscribe data: {data}")

                return data

    def set_data_redis(self, channel: str, data: dict, ex: int = 2):
        """
        Set data to a channel.

        Args:
            channel (str): stream channel
            data (dict): data to set
            ex (int, optional): *****. Defaults to 2.
        """        
        data = json.dumps(data, default=lambda o: o.__dict__)
        self.connect.set(channel, data, ex)
        self.logger(f"Set data: {data}")

    def set_subscribe_redis(self, channel: str):
        """
        Set (save) subscribe data to redis databse.

        Args:
            channel (str): stream channel
        """
        self.pubsub.subscribe(channel)
        for message in self.pubsub.listen():
            if message["type"] == "message":
                data = json.loads(message["data"].decode("utf-8"))
                if data is not None:
                    self.set_data(channel, data, ex=60)

    def get_data_redis(self, channel: str):
        """
        Get data from a channel.

        Args:
            channel (str): stream channel
        """
        data = self.connect.get(channel)
        if data is not None:
            data = json.loads(data.decode("utf-8"))
            self.logger(f"Get data: {data}")
            return data
