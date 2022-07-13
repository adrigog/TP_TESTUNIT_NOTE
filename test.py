import model_dashboard as script
import joblib


def load_model():
    return joblib.load('regression.joblib')

model = load_model()

X = [[200,1,1]]

def test_nb_rooms():
    rooms = script.nb_rooms
    assert rooms >= 0

def test_taille():
    taille = script.taille
    assert taille >= 0

def test_garden():
    garden = script.garden
    assert garden >= 0

def test_prediction():
    prediction = model.predict(X)
    assert prediction >= 0
