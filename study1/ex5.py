import tensorflow as tf


input1 = tf.constant([3.])
input2 = tf.constant([2.])
input3 = tf.constant([5.])
intermed = tf.add(input2, input3)
mul = tf.multiply(input1, input2)
writer = tf.summary.FileWriter(
    '/tmp/log', graph=tf.get_default_graph()
)
with tf.Session() as sess:
    result = sess.run([mul, intermed])
    print result[0]
    print result[1]