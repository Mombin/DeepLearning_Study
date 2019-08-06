import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import numpy as np
mnist = input_data.read_data_sets("/tmp/data", one_hot=True)

learning_rate = 0.001
training_epochs = 15
batch_size = 100
display_step = 1

X = tf.placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32, [None, 10])


W1 = tf.Variable(tf.random_uniform([784, 256], -.01,.01))
W2 = tf.Variable(tf.random_uniform([256, 256],-.01,.01))
W3 = tf.Variable(tf.random_uniform([256, 10],-.01,.01))

B1 = tf.Variable(tf.random_uniform([256],-.01,.01))
B2 = tf.Variable(tf.random_uniform([256],-.01,.01))
B3 = tf.Variable(tf.random_uniform([10],-.01,.01))

L1 = tf.nn.relu(tf.add(tf.matmul(X, W1), B1))
L2 = tf.nn.relu(tf.add(tf.matmul(L1, W2), B2))
hypothesis = tf.add(tf.matmul(L2, W3), B3)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y))

optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)
init = tf.global_variables_initializer()
gpu_options = tf.GPUOptions(
    per_process_gpu_memory_fraction=0.333
)

with tf.Session() as sess:
    sess.run(init)
    for epoch in range (training_epochs):
        avg_cost=0.
        total_batch = int(mnist.train.num_examples/batch_size)
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            _, c = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y: batch_ys})
            avg_cost += c/total_batch

        if (epoch+1) % display_step == 0:
            print "Epoch:", '%04d' %(epoch+1), "cost:", "{:.9}".format(avg_cost)

    print "Optimizer"
    correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print "Accuracy: ", accuracy.eval({X: mnist.test.images, Y: mnist.test.labels})


    answer = sess.run(hypothesis, feed_dict={
        X: mnist.test.images, Y: mnist.test.labels})

fig = plt.figure()
for i in range(10):
    subplot = fig.add_subplot(2,5,i+1)
    subplot.set_xticks([])
    subplot.set_yticks([])
    subplot.set_title("%d" % np.argmax(answer[i]))
    subplot.imshow(
        mnist.test.images[i].reshape([28,28]),
        cmap = plt.cm.gray_r)
plt.show()