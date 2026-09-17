from data_preprocessing import (
    load_invoice_data,
    apply_labels,
    split_data,
    scale_features
)
from modeling_evaluation import train_random_forest, evaluate_classifier
import joblib

features = [
    'Invoice_quantity', 'Invoice_Dollars','Freight', 'total_item_quantity', 'total_item_dollars'
]
target = "flag_invoice"

def main():

    #Load data
    df=load_invoice_data()
    df = apply_labels(df)

    #prepare data
    X_train, X_test, y_train, y_test = split_data(df, features, target)
    X_train_scaled, X_test_scaled =scale_features(
        X_train, X_test, '../models/scaler.pkl'
    )

    #train and evaluate model
    grid_search = train_random_forest(X_train_scaled, y_train)

    evaluate_classifier(
        grid_search.best_estimator_,
        X_test_scaled,
        y_test,
        "Random Forest Classifier"
    )

    #save the best model
    joblib.dump(grid_search.best_estimator_, '../models/predict_flag_invoice.pkl')

if __name__ =='__main__':
    main()