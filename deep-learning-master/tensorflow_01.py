import tensorflow as tf

hello = tf.constant('Hello World')

# 준비
sess = tf.Session()

# 실제 실행(런칭)
print(sess.run(hello))

# 꼭 close() 해줘야함
sess.close()