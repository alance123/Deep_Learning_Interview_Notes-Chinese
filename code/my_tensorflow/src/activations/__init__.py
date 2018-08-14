"""激活函数"""

from .relu import *
from .selu import *
from .softmax import *


def linear(x):
    """"""
    return x


def identity(x):
    """"""
    return tf.identity(x)


def sigmoid(x):
    """"""
    return tf.nn.sigmoid(x)


def hard_sigmoid(x):
    """
    x = 0.                  x < -2.5
      = 1.                  x > 2.5
      = 0.2 * x + 0.5       otherwise
    """
    x = (0.2 * x) + 0.5
    x = tf.clip_by_value(x, 0., 1.)
    return x


def tanh(x):
    return tf.nn.tanh(x)


def softplus(x):
    return tf.nn.softplus(x)


def softsign(x):
    """
    o = x / (1 + abs(x))
    """
    return tf.nn.softsign(x)


def softmax(x, axis=-1):
    """"""
    return tf.nn.softmax(x, axis=axis)
