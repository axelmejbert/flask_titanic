import joblib


# Load the machine learning model using joblib
loaded_model = joblib.load("models/titanic_log_reg.pkl")  # Replace with the actual path to your model file

class model:
    def survie(data):
        # Assuming 'log_reg' is the loaded machine learning model
        prediction = loaded_model.predict(data)
        if prediction == 1 :
            return "vous avez survécu"
        else:
            return "ne vas pas plus loin"
        return prediction

                 

    