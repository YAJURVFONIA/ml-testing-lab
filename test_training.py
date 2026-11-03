from train import run_pipeline
 
 
def test_pipeline_runs():
    model, X_test, y_test, accuracy = run_pipeline()
    assert hasattr(model, "predict")
 
 
def test_accuracy_is_good_enough():
    model, X_test, y_test, accuracy = run_pipeline()
    assert accuracy >= 0.85
 
 
def test_same_result_every_time():
    first = run_pipeline()[3]
    second = run_pipeline()[3]
    assert first == second
