import tensorflow as tf
import numpy as np

xy = np.loadtxt('softmax.txt', unpack = True, dtype = 'float32')

x_data = np.transpose(xy[:3])
y_data = xy[3:].T
print 'x_data: ', x_data.shape
print 'y_data: ', y_data.shape

X = tf.placeholder("float", [None, 3])
Y = tf.placeholder("float", [None, 3])
W = tf.Variable(tf.zeros([3,3]))

h = tf.matmul(W, X)
hypothesis = tf.nn.softmax(tf.matmul(X,W))

cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(hypothesis), reduction_indices=1))
rate = tf.Variable(0.1)
optimizer = tf.train.GradientDescentOptimizer(rate)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(2000):
    sess.run(train, feed_dict={X: x_data, Y:y_data})
    if step % 20 ==0:
        feed = {X:x_data, Y:y_data}
        print '{:4} {:8.6}'.format(step, sess.run(cost, feed_dict=feed)), sess.run(W)
print '-'*40

a = sess.run(hypothesis, feed_dict={X: [[1,11,7]]})
print "a : ", a, sess.run(tf.argmax(a, 1))
b = sess.run(hypothesis, feed_dict={X: [[1,3,4]]})
print "b : ", b, sess.run(tf.argmax(b, 1))
c = sess.run(hypothesis, feed_dict={X: [[1,1,0]]})
print "c : ", c, sess.run(tf.argmax(c, 1))
d = sess.run(hypothesis, feed_dict={X: [[1,11,7],[1,3,4],[1,1,0]]})
print sess.run(tf.argmax(d, 1))

sess.close()