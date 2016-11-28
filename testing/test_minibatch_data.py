# Copyright 2016 alexggmatthews
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tensorflow as tf
import numpy as np
import unittest
from GPflow.svgp import SequenceIndexManager, MinibatchData

class TestSequentialManager(unittest.TestCase):
    def setUp(self):
        tf.reset_default_graph()
     
    def testA(self):
		minibatch_size = 3
		total_points = 5
		sequenceManager = SequenceIndexManager(minibatch_size)
		
		indecesA = sequenceManager.nextIndeces(total_points)
		self.assertTrue((indecesA==np.arange(0,minibatch_size)).all())

		indecesB = sequenceManager.nextIndeces(total_points)
		self.assertTrue((indecesB==np.array([4,0,1 ])).all())
	
    def testB(self):
		minibatch_size = 5
		total_points = 2
		sequenceManager = SequenceIndexManager(minibatch_size)
		
		indeces = sequenceManager.nextIndeces(total_points)
		targetIndeces = np.array([0,1,0,1,0])
			
		self.assertTrue((indeces==targetIndeces).all())
	
if __name__ == "__main__":
    unittest.main()