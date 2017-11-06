import mxnet as mx
from mxnet import gluon
from mxnet import nd
from mxnet import io
DATA_PATH=""

class DataIter(object):
	def __init__(self):
		self.name='DataIter'

class PairWiseDataIter(DataIter):
	def __init__(self):
		super(PairWiseDataIter, self).__init__()
		self.name='PairwiseDataIter'
	

	

