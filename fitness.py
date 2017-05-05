from __future__ import print_function
import tensorflow as tf

class Fitness(object):
    '''
    Fitness Function to evaluate the Phenome
    '''

    def __init__(self, data, PHENOME):
        self.data = data
        self.phenome = PHENOME

    def evaluate(self):
        X,Y = self.data
        x_,y_,weight,bias,activation = self.phenome

        init = tf.global_variables_initializer()
        sess = tf.Session()
        sess.run(init)

        result = sess.run(activation, feed_dict={x_: X, y_: Y})

        return result