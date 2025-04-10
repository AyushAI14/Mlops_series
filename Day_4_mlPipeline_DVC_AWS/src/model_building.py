import logging
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np 
import pickle
import yaml



# made dir 
dir_logs = 'logs'
os.makedirs(dir_logs,exist_ok=True)


# ----------------------------------------logging ----------------------------------
# main logging object
logger = logging.getLogger('model_building')
logger.setLevel('DEBUG')

# for my console logging 
console_logger = logging.StreamHandler()
console_logger.setLevel('DEBUG')

# for my file logging 
log_file_Path = os.path.join(dir_logs,'model_building_logs.log')
fileHandler = logging.FileHandler(log_file_Path)
fileHandler.setLevel('DEBUG')

# for formating both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(formatter)
console_logger.setFormatter(formatter)


# adding both handlers
logger.addHandler(fileHandler)
logger.addHandler(console_logger)

# ---------------------model_building-------------------------

# making function for loading the processing data

def load_data(file_path:str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        logger.debug('Data loaded from %s  successfully with %s shape',file_path,df.shape)
        return df
    except pd.errors.ParserError as e:
        logger.error('Failed to parse the CSV file : %s',e)
        raise
    except Exception as e:
        logger.error('Unexpected error occur file loading the file')
        raise


def model_training(X_train:np.ndarray,y_train:np.ndarray,param:dict)->RandomForestClassifier:
    try:
        if X_train.shape[0] != y_train.shape[0]:
            raise ValueError("The noumber of  sample of X_train and y_train are not same")
        
        logger.debug("random forest intializing")
        cls = RandomForestClassifier(n_estimators=param['n_estimator'],random_state=param['ramdom_state'])
        cls.fit(X_train,y_train)
        logger.debug("model training is completed")
        return cls
    except ValueError as e:
        logger.error("value error during model training %s",e)
        raise
    except Exception as e:
        logger.error("unable to train the model %s",e)
        raise

def save_model(model,file_path:str):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        
        with open(file_path,'wb') as f:
            pickle.dump(model,f)
        logger.debug("model convertf to pkl and saved in %s",file_path)
    except FileNotFoundError as e:
        logger.error('File path not found: %s', e)
        raise
    except Exception as e:
        logger.error('Error occurred while saving the model: %s', e)
        raise

def main():
    try:
        param = {'n_estimator':25,'ramdom_state':2}
        train_data = load_data('data/featureData/traindf_tfid.csv')
        X_train = train_data.iloc[:, :-1].values
        y_train = train_data.iloc[:, -1].values

        clf = model_training(X_train,y_train,param)
        modelPath = 'models/model.pkl'
        save_model(clf,modelPath)
    except Exception as e:
        logger("Unable to complete model training process")
        print(e)

if __name__ == "__main__":
    main()
