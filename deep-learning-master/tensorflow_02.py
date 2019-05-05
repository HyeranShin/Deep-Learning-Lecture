x = 1
y = x + 9
print(y) # 10

import tensorflow as tf

# python 소스 코드 내의 x와 뒤의 string x는 다르다.
# 첫번째 x는 python 변수
# 두번째 x는 TensorFlow(그래프) 상의 이름
x = tf.constant(1, name = 'x')
y = tf.Variable(x + 9, name = 'y')
print(y) # <tf.Variable 'y:0' shape=() dtype=int32_ref>

print(y.value()) # Tensor("y/read:0", shape=(), dtype=int32)

model = tf.global_variables_initializer()

# with 구문 사용 시 close() 생략 가능
with tf.Session() as sess:
    sess.run(model) # 한꺼번에 초기화
    print(sess.run(y)) # 10 => 그래프를 그린 결과 값
