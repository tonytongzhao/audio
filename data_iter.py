import mxnet as mx
import numpy as np
import mxnet as mx
import mxnet.gluon as gluon
from mxnet import nd

from utils import *


class AudioDataIter(mx.io.NDArrayIter):
	def __init__(self, data_path, raw=False):
		self.data_path=data_path
		if raw:
			continue
		
	def 


