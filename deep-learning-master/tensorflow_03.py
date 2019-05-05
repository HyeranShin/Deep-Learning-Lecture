import tensorflow as tf

mat1 = tf.constant([[3., 3.]]) # 1X2 행렬
mat2 = tf.constant([[2.], [2.]]) # 2X1 행렬
# matmul: matrix multiply
mat_mul = tf.matmul(mat1, mat2)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    result = sess.run(mat_mul)
    print(result) # [[12.]]
    print(result.shape) # (1, 1)
