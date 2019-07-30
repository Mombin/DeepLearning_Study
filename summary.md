# deeplearning & NVIDIA TX1 comprehension


#### variable must be initialization
- eval() shoule declare InteractiveSession()
- run() also declare InteractiveSession()
- but in with statement can replace tf.Session()

```python
x= variable([1.,2.])
sess.run(x.initializer) # must type
```
```python
with tf.Session() as sess:
	x = tf.Variable([1.,2.])
	a = tf.constant([3.,3.])
	x.initializer.run()
	sub = tf. subtract(x,a)
	print sub.eval()
```
```python
with tf.Session() as sess:
	x = tf.Variable([1.,2.])
	a = tf.constant([3.,3.])
	sess.run(x.initializer())
	sess.run(sub)
```
