import os

import joblib


def model_fn(model_dir: str):  # type: ignore[no-untyped-def]
    print("loading model.joblib from: {}".format(model_dir))
    loaded_model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return loaded_model
