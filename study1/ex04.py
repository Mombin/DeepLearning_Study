import tensorflow as tf

state = tf.Variable(0,name='counter')
one = tf.constant(1)
new_value = tf.add(state,one)
update = tf.assign(state, new_value)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print sess.run(state)
    for _ in range(3):
        sess.run(update)
        print sess.run(update)

writer = tf.summary.FileWriter(
    'tmp/log/', graph=tf.get_default_graph()
)