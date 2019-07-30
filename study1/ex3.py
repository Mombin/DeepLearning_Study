import tensorflow as tf

sess = tf.InteractiveSession()
#sess = tf.Session()

x = tf.Variable([1.,2.])
a = tf.constant([3.,3.])
#sess.run(x.initializer)
x.initializer.run()
sub = tf.subtract(x,a)
print sub.eval()
sess.close()