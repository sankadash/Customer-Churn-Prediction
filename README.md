# Churning Prediction
Deadline-23rd April

App Link: https://dharmanshu1921-customer-churning-app-kg5r4p.streamlit.app/

File descriptions

train.csv - the training set. 
Contains 4250 lines with 20 columns. 3652 samples (85.93%) belong to class churn=no and 598 samples (14.07%) belong to class churn=yes

test.csv - the test set. 
Contains 750 lines with 20 columns: the index of each sample and the 19 features (missing the target variable "churn").

sampleSubmission.csv - a sample submission file in the correct format

Data fields

1.state, string. 2-letter code of the US state of customer residence

2.account_length, numerical. Number of months the customer has been with the current telco provider

3.area_code, string="area_code_AAA" where AAA = 3 digit area code.

4.international_plan, (yes/no). The customer has international plan.

5.voice_mail_plan, (yes/no). The customer has voice mail plan.

6.number_vmail_messages, numerical. Number of voice-mail messages.

7.total_day_minutes, numerical. Total minutes of day calls.

8.total_day_calls, numerical. Total number of day calls.

9.total_day_charge, numerical. Total charge of day calls.

10.total_eve_minutes, numerical. Total minutes of evening calls.

11.total_eve_calls, numerical. Total number of evening calls.

12.total_eve_charge, numerical. Total charge of evening calls.

13.total_night_minutes, numerical. Total minutes of night calls.

14.total_night_calls, numerical. Total number of night calls.

15.total_night_charge, numerical. Total charge of night calls.

16.total_intl_minutes, numerical. Total minutes of international calls.

17.total_intl_calls, numerical. Total number of international calls.

18.total_intl_charge, numerical. Total charge of international calls

19.number_customer_service_calls, numerical. Number of calls to customer service

20.churn, (yes/no). Customer churn - target variable.

Link to dataset: https://www.kaggle.com/competitions/customer-churn-prediction-2020/data

Things we have to perform

> Exploratory Data Analysis (EDA)
  https://www.kaggle.com/code/imoore/intro-to-exploratory-data-analysis-eda-in-python

> Feature Selection and Feature Engineering
  
  https://www.kaggle.com/code/willkoehrsen/introduction-to-feature-selection 
  
  https://www.kaggle.com/code/anshankul/feature-selection-feature-engineering-techniques

> Model Building
  https://www.kaggle.com/code/dansbecker/building-your-model
  
> Model Selection (comparing the performance of different models)
  https://www.kaggle.com/code/rishikhanna/model-selection
  
> Hyper-parameter Tuning
  https://www.kaggle.com/code/shreayan98c/hyperparameter-tuning-tutorial
  
> Model Deployment
  https://towardsdatascience.com/september-edition-deploying-machine-learning-models-1c79185e88b5

