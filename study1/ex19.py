import tensorflow as tf
import numpy as np

unique = 'helo'
y_data = [1,2,2,3]
x_data = np.array([[1,0,0,0], [0,1,0,0],[0,0,1,0], [0,0,1,0]], dtype='f')

cells = tf.nn.rnn_cell.BasicRNNCell(4)
state = tf.zeros([1, cells.state_size])
x_data = tf.split(x_data, 4)

outputs, state = tf.nn.static_rnn(cells, x_data, state)
logits = tf.reshape(outputs, [-1, 4])
targets= tf.reshape(y_data, [-1])
weights = tf.ones([4])
loss = tf.contrib.legacy_seq2seq.sequence_loss_by_example([logits], [targets], [weights])

cost = tf.reduce_sum(loss)
train_op = tf.train.RMSPropOptimizer(.01, .9).minimize(cost)
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for i in range(100):
        sess.run(train_op)
        r0, r1, r2, r3 = sess.run(tf.argmax(logits, 1))
        print r0, r1, r2, r3, ':', unique[r0],\
            unique[r1], unique[r2], unique[r3]
        if (r0,r1,r2,r3) == (1,2,2,3):
            break