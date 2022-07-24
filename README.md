# Supportiv Empathy Creation/Classification

This app creates an empathic summary segment based on User/Client input as well as the supportive statement provided by the Caregiver. The app uses a fine-tuned GPT3 model and a fine-tuned distilbert transformer.
It should be noted that exceptionally long emphatic segments were excluded as they seemed to skew the results. 

All of the work done in this project can be found in /Notebooks
Although, one of the notebooks may also be found on Google Colab as well: https://colab.research.google.com/drive/1UAZrqCEVq4S1FixqaYuDIrpMhk2cv32t?usp=sharing

The training results from the segment creation model can be found in gpt3_results.csv

The classification model results are as follows:

              precision    recall  f1-score   support

           1       0.58      0.74      0.65        50
           2       0.83      0.71      0.77        28
           3       0.00      0.00      0.00        13
           4       0.74      0.93      0.82        42
           5       0.00      0.00      0.00        15
           6       0.70      0.79      0.74        38

    accuracy                           0.68       186
    macro avg      0.47      0.53      0.50       186
    weighted avg   0.59      0.68      0.63       186

And the accompanying confusion matrix:

    [37,  4,  0,  2,  1,  6]
    [ 7, 20,  0,  0,  0,  1]
    [ 1,  0,  0, 12,  0,  0]
    [ 3,  0,  0, 39,  0,  0]
    [ 9,  0,  0,  0,  0,  6]
    [ 7,  0,  0,  0,  1, 30]

While the accuracy for the model is less than perfect, it does provide a good foundation to start from. More context surrounding the nature of each classification label will be helpful going forward as well. For instance the content of categories 3 and 4 appeared to be very similar with both containing a lot of questions as responses. Additionally, it is unclear if the categories have any ordinal implication. 


One last edit. I have made several attempts to try to load the classificaiton model from both Google and OneDrive. However, there seems to be some issues in creating the authentication. Still the model weights can be found through the following link: https://drive.google.com/drive/folders/1I7A6WF__AbvaMf2hCYC2Wjj8Vxyj_jjM?usp=sharing

