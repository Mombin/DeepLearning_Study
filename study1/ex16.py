import tensorflow as tf

sess = tf.InteractiveSession()

x_ = [[0, 0], [0, 1], [1, 0], [1, 1]]
expect = [[1, 0], [0, 1], [0, 1], [1, 0]]

x = tf.placeholder("float", [None, 2])
y_ = tf.placeholder("float", [None, 2])

number_hidden_nodes = 20

W = tf.Variable(tf.random_uniform([2, number_hidden_nodes], -.01, .01))
b = tf.Variable(tf.random_uniform([number_hidden_nodes], -.01, .01))
hidden = tf.nn.relu(tf.matmul(x, W) + b)

W2 = tf.Variable(tf.random_uniform([number_hidden_nodes, 2], -.1, .1))
b2 = tf.Variable(tf.zeros([2]))
hidden2 = tf.matmul(hidden, W2)

y = tf.nn.softmax(hidden2)

cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(cross_entropy)

tf.global_variables_initializer().run()
for step in range(1000):
    feed_dict = {x: x_, y_: expect}
    e, a = sess.run([cross_entropy, train_step], feed_dict)
    if e < 1: break
    print "step %d : entropy %s" % (step, e)

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

print "accuracy %s" % (accuracy.eval({x: x_, y_: expect}))

learned_output = tf.argmax(y, 1)
print(learned_output.eval)

sess.close()
