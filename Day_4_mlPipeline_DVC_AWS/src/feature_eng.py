from sklearn.feature_extraction.text import  TfidfVectorizer
import logging
import os
import pandas as pd


# made dir 
dir_logs = 'logs'
os.makedirs(dir_logs,exist_ok=True)


# ----------------------------------------logging ----------------------------------
# main logging object
logger = logging.getLogger('Feature_engineer')
logger.setLevel('DEBUG')

# for my console logging 
console_logger = logging.StreamHandler()
console_logger.setLevel('DEBUG')

# for my file logging 
log_file_Path = os.path.join(dir_logs,'Feature_engineer_logs.log')
fileHandler = logging.FileHandler(log_file_Path)
fileHandler.setLevel('DEBUG')

# for formating both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(formatter)
console_logger.setFormatter(formatter)


# adding both handlers
logger.addHandler(fileHandler)
logger.addHandler(console_logger)


# -------------------------------Feature_engineer------------------------------
# making function for loading the processing data

def load_data(file_path:str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        df.fillna('',inplace=True)
        logger.debug('Data loaded successfully')
        return df
    except pd.errors.ParserError as e:
        logger.error('Failed to parse the CSV file : %s',e)
        raise
    except Exception as e:
        logger.error('Unexpected error occur file loading the file')
        raise

# making function for feature extraction

def apply_tfid(train_data:pd.DataFrame,test_data:pd.DataFrame,max_feature:int) -> tuple:
    try:
        vectorizer = TfidfVectorizer(max_features=max_feature)
        X_train = train_data['sentence'].values
        y_train = train_data['target'].values
        X_test = test_data['sentence'].values
        y_test = test_data['target'].values

        X_train_bow = vectorizer.fit_transform(X_train)
        X_test_bow = vectorizer.transform(X_test)

        train_df = pd.DataFrame(X_train_bow.toarray())
        train_df['label'] = y_train

        test_df = pd.DataFrame(X_test_bow.toarray())
        test_df['label'] = y_test

        logger.debug('tfidf applied and data transformed')
        return train_df, test_df
    except Exception as e:
        logger.error('Error during Bag of Words transformation: %s', e)
        raise      

def save_data(df: pd.DataFrame, file_path: str) -> None:
    """Save the dataframe to a CSV file."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_csv(file_path, index=False)
        logger.debug('Data saved to %s', file_path)
    except Exception as e:
        logger.error('Unexpected error occurred while saving the data: %s', e)
        raise

def main():
    try:
        max_feature=50
        train_data = load_data('data/process_data/train_processed.csv')
        test_data = load_data('data/process_data/test_processed.csv')

        train_df,test_df = apply_tfid(train_data,test_data,max_feature)

        save_data(train_df,os.path.join('./data','featureData','traindf_tfid.csv'))
        save_data(test_df,os.path.join('./data','featureData','testdf_tfid.csv'))

    except Exception as e:
        logger.error("Failed to complete feature engg process %s",e)
        print(e)

if __name__ == "__main__":
    main() 
