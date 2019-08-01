import tensorflow as tf

state1 = tf.Variable(0, name="state1")
state2 = tf.Variable(10, name="state2")

init_op = tf.global_variables_initializer()

saver = tf.train.Saver({"mys2":state2})

with tf.Session() as sess:
    sess.run(init_op)

    save_path = saver.save(sess, "/tmp/model/model.ckpt")
    print "Model saved in file: ", save_path