import numpy as np
from tensorflow.keras.models import Model

def get_activations(model, x_sample):
    """
    Extract activations from all Conv2D layers given an input sample.
    """
    outputs = [layer.output for layer in model.layers if 'conv' in layer.name]
    intermediate_model = Model(inputs=model.input, outputs=outputs)
    return intermediate_model.predict(x_sample[np.newaxis, ...])

def train_model(model, x_train, y_train):
    """
    Trains the model and returns activations of the first training sample.
    """
    _ = model.predict(x_train[:1])  # 👈 Necessary to "build" the model before accessing model.input
    model.fit(x_train, y_train, epochs=5, validation_split=0.2)
    activations = get_activations(model, x_train[0])
    return model, activations

def predict(model, x_sample):
    """
    Predicts the class and returns both class and raw probabilities.
    """
    pred = model.predict(x_sample[np.newaxis, ...])
    return np.argmax(pred), pred[0]
