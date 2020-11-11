import pandas as pd
import numpy as np
import time

def get_data():
    """This function acquires data from csv and turns into df"""
    
    df = pd.read_csv("JEOPARDY_CSV.csv")

    df.columns = df.columns.str.strip(" ")

    df.columns = [i.lower() for i in df.columns]

    df.columns = [i.replace(" ", "_") for i in df.columns]
    
    # pulls out any question with a link
    df[~df.question.str.contains('href')]
    
    
    df.value = (df.value.str.replace('$', "")
                    .str.replace(',',"")
                    .str.replace('None', "10000")
                    .astype('float')
               )
    return df

df = get_data()

def question(i):
    print(df.air_date[i] + " \\ " + df.category[i] + " \\ " + df.value[i].astype(str) + ":  " + df.question[i])

def make_random_list(n):
    question_list = np.random.randint(0, len(df), n)
    return question_list

def answer(i):
    print(df.answer[i])

def quiz_round():

    question_list = make_random_list(8)

    for i in question_list:
        question(i)
        time.sleep(3)
        input()

    input()

    for i in question_list:
        answer(i) 
        

def get_all_questions_from_a_category(category):
    
    x = len(df[df.category == category].index)
    
    print(f"This round will be {x} questions long do you want to continue?")
    
    q = input()
    
    if q == 'y':
        for i in df[df.category == category].question.index:
            print(df.air_date[i] + " \\ " + df.question[i])
            time.sleep(2)
            input()
      
        for i in df[df.category == category].question.index:
            print(df.answer[i])