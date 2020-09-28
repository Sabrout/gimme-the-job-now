import time
import json
from random import randrange, random

def receive_model_input():
  return json.dumps([{'fileId': 1}, { 'fileId': 2}, {'fileId': 3}, {'fileId': 4}]) 

class MyModel:
  def __init__(self):
    pass

  def warmup_model(self):
    time.sleep(randrange(1, 10))

  def pre_process(self, inputs):
    time.sleep(randrange(1, 4))
    return ['s3://test/image-1', 's3://test/image-2', 's3://test/image-3', 's3://test/image-4']

  def predict(self, inputs):
    if random() <= 1/10000:
      raise RuntimeError()
    time.sleep(randrange(1, 2))
    return ['barley', 'barley', 'barley', 'barley']

  def post_process(self, raw_output):
    time.sleep(randrange(1, 4))
    return [{ 'label': 'barley' },{ 'label': 'barley' },{ 'label': 'barley' },{ 'label': 'barley' }]
