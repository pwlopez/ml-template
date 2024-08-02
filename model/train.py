import argparse
import random

# Third Party
import numpy as np
import tensorflow.compat.v2 as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical


def train(batch_size, epoch, model):

    # Train-test split
    (X_train, y_train), (X_valid, y_valid) = cifar10.load_data()

    Y_train = to_categorical(y_train, 10)
    Y_valid = to_categorical(y_valid, 10)

    X_train = X_train.astype('float32')
    X_valid = X_valid.astype('float32')

    mean_image = np.mean(X_train, axis=0)
    X_train -= mean_image
    X_valid -= mean_image
    X_train /= 128.
    X_valid /= 128.

    # TO DO: Modify this to use a logger rather than smdebug hooks
    #hook.save_scalar("epoch", epoch)
    #hook.save_scalar("batch_size", batch_size)
    #hook.save_scalar("train_steps_per_epoch", len(X_train)/batch_size)
    #hook.save_scalar("valid_steps_per_epoch", len(X_valid)/batch_size)

    # Fit model
    model.fit(X_train, Y_train,
              batch_size=batch_size,
              epochs=epoch,
              validation_data=(X_valid, Y_valid),
              shuffle=False,
              # smdebug modification: Pass the hook as a Keras callback
              callbacks=[hook])
    
    # Save model
    model.save("/opt/ml/model/resnet50.keras")


def main():
    parser = argparse.ArgumentParser(description="Train resnet50 cifar10")
    parser.add_argument("--batch_size", type=int, default=50)
    parser.add_argument("--epoch", type=int, default=15)
    parser.add_argument("--model_dir", type=str, default="./model_keras_resnet")
    parser.add_argument("--lr", type=float, default=0.001)
    parser.add_argument("--random_seed", type=bool, default=False)

    args = parser.parse_args()

    if args.random_seed:
        tf.random.set_seed(2)
        np.random.seed(2)
        random.seed(12)


    mirrored_strategy = tf.distribute.MirroredStrategy()
    with mirrored_strategy.scope():

        model = ResNet50(weights=None, input_shape=(32,32,3), classes=10)

        opt = tf.keras.optimizers.Adam(learning_rate=args.lr)
        model.compile(loss='categorical_crossentropy',
                      optimizer=opt,
                      metrics=['accuracy'])

    # start the training.
    train(args.batch_size, args.epoch, model)

if __name__ == "__main__":
    main()

    """
    /opt/ml/model - Your algorithm should write all final model artifacts to this directory. SageMaker 
    copies this data as a single object in compressed tar format to the S3 location that you specified 
    in the CreateTrainingJob request. If multiple containers in a single training job write to this 
    directory they should ensure no file/directory names clash. SageMaker aggregates the result in a 
    TAR file and uploads to S3 at the end of the training job.

    https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-output.html
    """