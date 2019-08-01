import tensorflow as tf


input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)
with tf.Session() as sess:
    result = sess.run([output], {input1:[7.],
                                 input2:[2.]})
    print result[0]