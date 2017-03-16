import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)

with tf.Session() as sess:
    print "a = %i" % sess.run(a)
    print "b = %i" % sess.run(b)
    print "Addition with constants = %i" % sess.run(a+b)

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a, b)
mul = tf.mul(a, b)

with tf.Session() as sess:
    #feed_dict creates a dictionary that holds the number that will passed in the add function
    print "results from the add function are %i" % sess.run(add, feed_dict={a:2, b:3})
    print "results from the mul function are %i" % sess.run(mul, feed_dict={a:2, b:3})