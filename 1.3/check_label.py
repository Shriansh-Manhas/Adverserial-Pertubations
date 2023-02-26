import tensorflow as tf
from utils import check_image_label

if __name__ == "__main__":
    flags = tf.app.flags
    FLAGS = flags.FLAGS
    
    flags.DEFINE_string('dataset', 'CIFAR10', 'target dataset of the trained model')
    flags.DEFINE_string('attack', 'DeepFool', 'attack to check the label')

    check_image_label(FLAGS.dataset, FLAGS.attack)