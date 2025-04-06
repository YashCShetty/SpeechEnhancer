import tensorflow as tf
import os

# Define the absolute path to the model file
model_path = r"C:\Users\Eyan Sequeira\Desktop\FinalSpeech\Speech-Enhancement1-main\AppModel\Model\model_unet01.keras"

# Check if the file exists
if os.path.exists(model_path):
    print(f"File found: {model_path}")
    
    # Load the model
    model = tf.keras.models.load_model(model_path)
    
    # Display the model architecture
    model.summary()
else:
    print(f"File not found: {model_path}. Please check the path and try again.")
