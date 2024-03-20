import numpy as np
from keras.preprocessing import image

class DogBreedIdentifier:
    def __init__(self, model):
        self.model = model

    def predict_breed(self, image_path):
        if self.model is None:
            print("Model not loaded.")
            return None
        
        try:
            # Load and preprocess the image
            img = image.load_img("C:\\Users\\gladi\\OneDrive\\Desktop\\Dog-Breed-Prediction-master\\Dog-Breed-Prediction-master\\test\\00a558277e1f03b71d8c813e03344ddf.jpg", target_size=(224, 224))
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            img /= 255.0
            
            # Make prediction using the loaded model
            prediction = self.model.predict(img)
            
            # Assuming the model predicts probabilities for each class,
            # you may want to return the class with the highest probability
            predicted_class_index = np.argmax(prediction)
            
            # Alternatively, you can return the probabilities for all classes
            # predicted_probabilities = prediction[0]
            
            return predicted_class_index  # Change this if you need probabilities
        except Exception as e:
            print(f"Error predicting breed: {e}")
            return None
