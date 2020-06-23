"""
Feedback paramaters:
Illegal move = -99
Mated in x = -40/x
Normal moves = positional advantage/disadvantage change from chess.com
Mate in x = +40/x
Take king = +99

Test 1, this would probably be better as a reinforcement learning algorithm, but just testing to
relearn the basics.
"""
import tensorflow as tf
n_nodes_hl1 = 25
n_nodes_hl2 = 25
classes = 224
x = tf.placeholder('float', [None, 768])
y = tf.placeholder('float')
def neural_network_model(data):
    hidden_1_layer = {
        'weights': tf.Variable(tf.random_normal([768, n_nodes_hl1])),
        'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))
    }
    hidden_2_layer = {
        'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
        'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))
    }
    hidden_1_layer = {
        'weights': tf.Variable(tf.random_normal([n_nodes_hl2, classes])),
        'biases': tf.Variable(tf.random_normal([classes]))
    }
    l1 = td.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.sigmoid(l1)
    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.sigmoid(l2)
    output = (tf.matmul(l2, output_l['weights']) + output_l['biases'])
    return output