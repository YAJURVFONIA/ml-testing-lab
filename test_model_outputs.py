from train import run_pipeline
 
# Train once here, then check the model's answers below
model, X_test, y_test, accuracy = run_pipeline()
 
 
def test_one_prediction_per_row():
    assert len(model.predict(X_test)) == len(X_test)
 
 
def test_predictions_are_valid_classes():
    for label in model.predict(X_test):
        assert label in [0, 1, 2]
 
 
def test_probabilities_are_between_0_and_1():
    probabilities = model.predict_proba(X_test)
    assert probabilities.min() >= 0.0
    assert probabilities.max() <= 1.0
 
 
def test_each_row_of_probabilities_adds_up_to_1():
    for row in model.predict_proba(X_test):
        assert abs(row.sum() - 1.0) < 0.0001
