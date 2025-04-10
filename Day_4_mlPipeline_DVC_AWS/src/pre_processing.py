import logging
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

# Download resources (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')


# made dir 
dir_logs = 'logs'
os.makedirs(dir_logs,exist_ok=True)


# ----------------------------------------logging ----------------------------------
# main logging object
logger = logging.getLogger('data_preprocessing')
logger.setLevel('DEBUG')

# for my console logging 
console_logger = logging.StreamHandler()
console_logger.setLevel('DEBUG')

# for my file logging 
log_file_Path = os.path.join(dir_logs,'data_preprocessing_logs.log')
fileHandler = logging.FileHandler(log_file_Path)
fileHandler.setLevel('DEBUG')

# for formating both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(formatter)
console_logger.setFormatter(formatter)


# adding both handlers
logger.addHandler(fileHandler)
logger.addHandler(console_logger)




# ----------------------------preprocessing Start----------------------------------

def transform_text(text):
    """
    Transform the input text by converting it in lowercase , tokenize , remove stopwords and punctuation and steam it.
    """

    ps = PorterStemmer()
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)

def preprocessing_df(df,text_columns='sentence',target_column='target'):
    """
    Preprocess DataFrame : encoding the target column , removing duplicates , transfroming text columns
    """
    try:
        logger.debug("preprocessing starts")
        encoder = LabelEncoder()
        df[target_column] = encoder.fit_transform(df[target_column])
        logger.debug("Target encoding done")

        # removing duplicates
        df = df.drop_duplicates()
        logger.debug("duplicate removed")

        #transfroming text
        df.loc[:,text_columns] = df[text_columns].apply(transform_text)
        logger.debug("sentence has been tansfromed")
        return df
    except KeyError as e:
        logger.error('missing columns in DataFrame %s',e)
        raise
    except Exception as e:
        logger.error('Unexpected error occur while preprocessing_df %s',e)
        raise


def main(text_columns='sentence',target_column='target'):
    """
    main Fuction : load train/test data , pre-process them , saving the processed data
    """
    try:
        train_data = pd.read_csv('data/raw/train.csv')
        test_data = pd.read_csv('data/raw/test.csv')

        train_preprocess = preprocessing_df(train_data,text_columns,target_column)
        test_preprocess = preprocessing_df(test_data,text_columns,target_column)

        data_path=os.path.join('./data','process_data')
        os.makedirs(data_path,exist_ok=True)

        train_preprocess.to_csv(os.path.join(data_path, "train_processed.csv"), index=False)
        test_preprocess.to_csv(os.path.join(data_path, "test_processed.csv"), index=False)    
    
    except FileNotFoundError as e:
        logger.error('File not found: %s', e)
    except pd.errors.EmptyDataError as e:
        logger.error('No data: %s', e)
    except Exception as e:
        logger.error('Failed to complete the data transformation process: %s', e)
        print(f"Error: {e}")

if __name__ == '__main__':
    main()

