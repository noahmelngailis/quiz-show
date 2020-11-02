import pandas as pd
import numpy as np
import time

def get_data():
    
    df = pd.read_csv("JEOPARDY_CSV.csv")
    
    df.columns = df.columns.str.strip(" ")
    
    df.columns = [i.lower() for i in df.columns]
    
    df.columns = [i.replace(" ", "_") for i in df.columns]
    
    return df

df = get_data()

def question(i):
    print(df.air_date[i] + " \\ " + df.category[i] + " \\ " + df.value[i] + ":  " + df.question[i])

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