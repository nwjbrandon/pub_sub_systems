import numpy as np
import pickle

def encode_msg(msg):
    msg = pickle.dumps(msg)
    return msg

def decode_msg(msg):
    msg = pickle.loads(msg)
    return msg
