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
        exp_arg = [(-1) * (self.loss_xz(data, k) + self.loss_z(k)) for k in range(self.K)]
        return (-1) * tf.reduce_logsumexp(exp_arg, axis=0) # Axis == 0 da ocuvamo (1000,1) jer smo vec u exp_arg sumirali po k
    

    def p_xz(self, x: TFData, k: int) -> TFData:
        raise NotImplementedError

    def p_x(self, x: TFData) -> TFData:
        raise NotImplementedError

    # 𝐿𝜽(𝑥^(𝑖)|𝑧𝑘) = 0.5 ⋅ (log(2𝜋) + log(𝜎^2) + (𝑥−𝜇)^2/𝜎^2) 
    def loss_xz(self, x: TFData, k: int):
        return self.neglog_normal_pdf(x, self.mean[k], self.logvar[k])
    
    # 𝐿𝜽(𝑧𝑘) = log∑exp(𝐥𝐨𝐠𝜋𝑗)−(log𝜋𝑘)
    def loss_z(self, k: int):
        return tf.reduce_logsumexp(self.logpi) - self.logpi[k]