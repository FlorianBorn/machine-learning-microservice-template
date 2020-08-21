from pathlib import Path

### API & main ###

# List the names of the features your model expects during training and prediction
# this list is required for constructing the web service API
target_label = "species"
input_features = [
    # Example:
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
    # End Example:
] 
ID_NAME = "ID" # if set, an additional ID Parameter, which is used for logging, can be passed during requests, can be empty

#### Data ####
# ...



#### Model ####
task = "classification"  # one of [classification, regression]

