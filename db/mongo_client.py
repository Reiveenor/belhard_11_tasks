import yaml
from pymongo import MongoClient

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
client = MongoClient(host=config["host"], port=config["port"])

__all__ = (
    "client"
)
