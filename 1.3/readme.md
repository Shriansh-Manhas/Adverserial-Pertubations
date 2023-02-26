
## Requirements

```
pip install -r requirements.txt
```

- [Python 3.6](https://www.python.org/downloads/)
- [Tensorflow == 1.12.0](https://github.com/tensorflow/tensorflow)
- [Keras == 2.2.4](https://github.com/keras-team/keras)
- [cleverhans >= 3.0.1](https://github.com/tensorflow/cleverhans)
- [GPy >= 1.9.6](https://github.com/SheffieldML/GPy)
- [matplotlib](https://matplotlib.org/)
- [tqdm](https://github.com/tqdm/tqdm)


<br>

## How to run
**1. Git clone**
```
$ git clone https://github.com/pod3275/GP-based-Adversarial-Detection.git
$ cd GP-based-Adversarial-Detection
```

**2. Training target model**
```
$ python train_model.py --dataset MNIST
```

- Available datasets : [MNIST](http://yann.lecun.com/exdb/mnist/), [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html)

**3. Generate adversarial examples**
```
$ python attack.py --dataset MNIST --attack JSMA
```

- Available attack methods : [FGSM](https://arxiv.org/pdf/1412.6572.pdf), [BIM](https://arxiv.org/pdf/1607.02533.pdf), [JSMA](https://arxiv.org/pdf/1511.07528.pdf), [DeepFool](https://arxiv.org/pdf/1511.04599.pdf), [CW](https://arxiv.org/pdf/1608.04644.pdf) 

**4. Detect with GP-based detector**
```
$ python gp_detector.py --dataset MNIST --attack DeepFool --num_data_in_class 30
```

- *num_data_in_class* : number of adversarial example in one class for training detector

- For FGSM and BIM, you should add epsilon at the end of the attack name (*ex. CIFAR10: "--attack FGSM_e9"*)
  - Same as the **name of directory** where the adversarial data saved

