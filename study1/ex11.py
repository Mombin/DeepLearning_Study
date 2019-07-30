import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


x_data = [1.,2.,3.]
y_data = [1.,2.,3.]
with tf.name_scope("GD_Grainer"):
    W= tf.Variable(tf.random_uniform([1],-1.,1.))
    b = tf.Variable(tf.random_uniform([1],-1.,1.))
    hypothesis = W*x_data +b
    cost = tf.reduce_mean(tf.square(hypothesis-y_data))
rate = 0.1
optimizer = tf.train.GradientDescentOptimizer(rate)
train = optimizer.minimize(cost)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
writer = tf.summary.FileWriter("/tmp/log",
                               graph=tf.get_default_graph())
for step in range(2001):
    sess.run(train)
    if step % 20 ==0:
        print '{:4} {:3.2f} {} {}'.format(step, sess.run(cost), sess.run(W), sess.run(b))
sess.close()
