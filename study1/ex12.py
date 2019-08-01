import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


x_data = [1.,2.,3.,4.]
y_data = [2.,4.,6.,8.]


X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

with tf.name_scope("Logit_Layer"):
    W= tf.Variable(tf.random_uniform([1],-100.,100.))
    b = tf.Variable(tf.random_uniform([1],-100.,100.))
    W2 = tf.Variable(tf.random_uniform([1], -100., 100.))

with tf.name_scope("GD_Grainer"):
    hypothesis = W*X
    cost = tf.reduce_mean(tf.square(hypothesis-Y))
    rate = tf.Variable(0.1)
    gradient = tf.reduce_mean((W*X -Y)*X)
    descent = W-rate * gradient
    update = tf.assign(W,descent)
    optimizer = tf.train.GradientDescentOptimizer(rate)
    train = optimizer.minimize(cost)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
writer = tf.summary.FileWriter("/tmp/log",
                               graph=tf.get_default_graph())
for step in range(2001):
    #sess.run(train,{X:x_data, Y:y_data})
    if step % 20 ==0:
        print '{} {} {} {}'.format(step, #sess.run(cost, {X:x_data, Y:y_data}),
                                          sess.run(update, {X:x_data, Y:y_data}),
                                          sess.run(W2), sess.run(b))

print sess.run(hypothesis, {X:5})
print sess.run(hypothesis, {X:2.5})
print sess.run(hypothesis, {X: [2.5, 5]})

# plt.ylabel('y')
# plt.xlabel('x')
# plt.show()
sess.close()
