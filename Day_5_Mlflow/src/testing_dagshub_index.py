print("creating a demo model for leaning mlfloe")
from pandas.core.common import random_state
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

#importing mlflow libs
import mlflow
import mlflow.sklearn
mlflow.set_tracking_uri('http://localhost:5000') #because mlflow is expecting https but artifact receive file so we did this to change tracking url

data = load_iris()
X = data.data
y = data.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=2)

n_estimators = 25
max_depth = 5

# mentioning my own experiment 
mlflow.set_experiment('mlops-trial')

#mlflow start------------------------

with mlflow.start_run():
    rf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=2)
    rf.fit(X_train, y_train)
    yp = rf.predict(X_test)
    
    accuracy = accuracy_score(y_test, yp)
    precision = precision_score(y_test, yp, average='macro')  # or 'weighted' based on your goal

    # now mlflow initialization : log_mertic , log_params
    mlflow.log_metric('accuracy', accuracy)
    mlflow.log_metric('precision', precision)
    mlflow.log_param('n_estimators', n_estimators)
    mlflow.log_param('max_depth', max_depth)


    # intalizing confusion matrix
    conf_mat = confusion_matrix(y_test,yp)
    sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues', xticklabels=data.target_names, yticklabels=data.target_names)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Confusion Matrix')    
    plt.savefig('iris_confusion_matrix.png')

    # now log artifact with mlflow
    mlflow.log_artifact('iris_confusion_matrix.png')
    mlflow.log_artifact(__file__) #__file__ : contain the path of current file

    #tags
    mlflow.set_tags({"Author": 'ayush', "Project": "iris Classification"})

    # Log the model
    mlflow.sklearn.log_model(rf, "Random-Forest-Model")

    print(accuracy)
    print(precision)
