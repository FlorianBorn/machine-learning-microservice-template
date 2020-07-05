### API & main ###

# List the names of the features your model expects during training and prediction
# this list is required for constructing the web service API
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

#### Logging ####
# MongoDB
enable_mongodb_logging =  True # if true, you have to provide the following env parameters
# mongo_db_name: ml-service # each service gets it's own mongodb Database, how should this db be named?
# mongo_db_url: localhost 
# mongo_db_port: 27017
# mongodb_logging_collection_name: prediction_logs
# timezone: Europe/Berlin # for possible values see: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568

# EFK-Stack
enable_fluentd_logging =  True # if you set this to true, you prob. also want to set ID_NAME, set also the following env params
# fluentd_url: localhost # where is fluentd running?
# fluentd_port: 24224
# fluentd_base_log_name: machine-learning-microservice-template 
# fluentd_log_n_best: 2 # if predict_proba, logs the n classes with highest probabilities

#### Model ####
model_path = "model_bin" # the folder where the trained model should be stored
model_name = "model.pkl" # the name the trained model will have (.pkl is mandatory)


