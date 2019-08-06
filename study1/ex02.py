import tensorflow as tf


s = tf.constant(100)
v = tf.constant([1,2,3,4,5])
m = tf.constant([[1,2,3],[4,5,6]])
c = tf.constant([[[1],[2],[3]],[[4],[5],[6]]])


print s._rank()
print v._rank()
print m._rank()
print c._rank()
print '\n'
print s._shape
print v._shape
print m._shape
print c._shape

with tf.Session() as sess:
    print sess.run(c)