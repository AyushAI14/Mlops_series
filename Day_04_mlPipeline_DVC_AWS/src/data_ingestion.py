import pandas as pd
from sklearn.model_selection import train_test_split
import os
import logging
import yaml

# made dir 
dir_logs = 'logs'
os.makedirs(dir_logs,exist_ok=True)


# ----------------------------------------logging ----------------------------------
# main logging object
logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')

# for my console logging 
console_logger = logging.StreamHandler()
console_logger.setLevel('DEBUG')

# for my file logging 
log_file_Path = os.path.join(dir_logs,'Data_ingestion_logs.log')
fileHandler = logging.FileHandler(log_file_Path)
fileHandler.setLevel('DEBUG')

# for formating both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(formatter)
console_logger.setFormatter(formatter)


# adding both handlers
logger.addHandler(fileHandler)
logger.addHandler(console_logger)

# --------------------------------params----------------------------
def params_load(param_path:str)->dict:
    """load params from yaml file"""
    try:
        with open(param_path,'r') as f:
            params=yaml.safe_load(f)
        logger.debug("params.yaml loaded successfully")

        return params
    except FileNotFoundError:
        logger.error('File not found: %s', param_path)
        raise
    except yaml.YAMLError as e:
        logger.error('YAML error: %s', e)
        raise
    except Exception as e:
        logger.error('Unexpected error: %s', e)
        raise    



# ----------------------------------------Ingestion Start ----------------------------------

# writing a function that take url and load data 
def load_data(data_url:str) -> pd.DataFrame:
    try:
        df = pd.read_csv(data_url)
        logger.debug('Data loaded from %s',data_url)
        return df
    except pd.errors.ParserError as e:
        logger.error('Failed to parse the CSV file : %s',e)
        raise
    except Exception as e:
        logger.error('Unexpected error occur file loading the file')
        raise

#writing a function to preprocess the df
def preprocessing_data(df:pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1)
        df = df.rename(columns={'v1':'target','v2':'sentence'})
        logger.debug("Data preprocessing complete")
        return df
    except KeyError as e:
        logger.error('missing columns in DataFrame %s',e)
        raise
    except Exception as e:
        logger.error('Unexpected error occur while preprocessing %s',e)
        raise

#writing a function to save train and test data

def save_data(train_data:pd.DataFrame,test_data:pd.DataFrame,data_path:str) ->None:
    try:
        raw_data_file = os.path.join(data_path,'raw')
        os.makedirs(raw_data_file,exist_ok=True)
        train_data.to_csv(os.path.join(raw_data_file,'train.csv'),index=False)
        test_data.to_csv(os.path.join(raw_data_file,'test.csv'),index=False)
        logger.debug('train and test data made successfully')

    except Exception as e :
        logger.error('unexpected error occur while saving the data %s',e)
        raise

def main():
    try:
        params = params_load(param_path='params.yaml')
        test_size = params['data_ingestion']['test_size']
        # test_size = 0.2
        data_url = 'https://raw.githubusercontent.com/AyushAI14/Test-dataset/refs/heads/main/spam.csv'
        df = load_data(data_url=data_url)
        final_df = preprocessing_data(df)
        train_data,test_data = train_test_split(final_df,test_size=test_size,random_state=2)
        save_data(train_data,test_data,data_path='./data')
    except Exception as e:
        logger.error('unexpected error occur while data ingestion  %s',e)
        print(e)
        

if __name__ == '__main__':
    main()









