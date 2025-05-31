import math
from typing import Union, Collection

import tensorflow as tf

TFData = Union[tf.Tensor, tf.Variable, float]

class GMModel:
    def __init__(self, K):
        self.K = K
        self.mean = tf.Variable(tf.random.normal(shape=[K]))
        self.logvar = tf.Variable(tf.random.normal(shape=[K]))
        self.logpi = tf.Variable(tf.zeros(shape=[K]))

    @property
    def variables(self) -> Collection[TFData]:
        return self.mean, self.logvar, self.logpi

    @staticmethod
    def neglog_normal_pdf(x: TFData, mean: TFData, logvar: TFData):
        var = tf.exp(logvar)

        return 0.5 * (tf.math.log(2 * math.pi) + logvar + (x - mean) ** 2 / var)

    @tf.function
    def loss(self, data: TFData):

        L_x_z = tf.stack([self.neglog_normal_pdf(data, self.mean[k], self.logvar[k]) 
                          for k in range(self.K)])
        
        L_z = tf.stack([tf.reduce_logsumexp(self.logpi) - self.logpi[k] 
                        for k in range(self.K)])

        L = -tf.reduce_logsumexp(-L_x_z + L_z, axis=0)  
        return L


    def p_xz(self, x: TFData, k: int) -> TFData:
        var = tf.exp(self.logvar)
        return normal_pdf(x,self.mean[k], var[k])

    def p_x(self, x: TFData) -> TFData:
        pi = tf.nn.softmax(self.logpi)
        return tf.reduce_sum([pi[k] * self.p_xz(x, k)
                               for k in range(self.K)], axis=0)

def normal_pdf(x, mean, var):
    pi = tf.constant(3.141592653589793) 
    const = 1 / tf.sqrt((var * 2 * pi))
    exponent = - tf.square(x - mean) / (2*var)
    return const * tf.exp(exponent)