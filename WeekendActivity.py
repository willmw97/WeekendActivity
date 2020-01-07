import pandas as pd
import numpy as np

weekend = { 'Deadline':['Urgent', 'Urgent', 'Near', 'None', 'None', 'None','Near','Near','Near','Urgent'],
            'IsThereEvent':['Yes','No','Yes','Yes','No','Yes','No','No','Yes','No'],
            'Lazy':['Yes','Yes','Yes','No','Yes','No','No','Yes','Yes','No'],
            'Activity':['Party','Study','Party','Party','Pub','Party','Study','TV','Party','Study']}

df = pd.DataFrame(weekend)

print(df)

def count_Party(df):
    #act = df.loc[df['Activity'].count().sum()
    total = len(df["Activity"])
    act = df["Activity"].str.count("Party").sum()

    D_count = 0
    for i,j in zip(df["Activity"],df["Deadline"]):
        if i=="Party" and j=="Near":
            D_count = D_count+1
    Is_count = 0
    for i,j in zip(df["Activity"],df["IsThereEvent"]):
        if i == "Party" and j=="No":
            Is_count = Is_count+1
    L_count = 0
    for i,j in zip(df["Activity"],df["Lazy"]):
        if i == "Party" and j=="Yes":
            L_count = L_count+1

    studyTotal = ((act/total)*(D_count/act)*(Is_count/act)*(L_count/act))

    return studyTotal

def count_Study(df):

    total = len(df["Activity"])
    act = df["Activity"].str.count("Study").sum()

    D_count = 0
    for i,j in zip(df["Activity"],df["Deadline"]):
        if i=="Study" and j=="Near":
            D_count = D_count+1
    Is_count = 0
    for i,j in zip(df["Activity"],df["IsThereEvent"]):
        if i == "Study" and j=="No":
            Is_count = Is_count+1
    L_count = 0
    for i,j in zip(df["Activity"],df["Lazy"]):
        if i == "Study" and j=="Yes":
            L_count = L_count+1

    studyTotal = ((act/total)*(D_count/act)*(Is_count/act)*(L_count/act))


    return studyTotal

def count_Pub(df):

    total = len(df["Activity"])
    act = df["Activity"].str.count("Pub").sum()

    D_count = 0
    for i,j in zip(df["Activity"],df["Deadline"]):
        if i=="Pub" and j=="Near":
            D_count = D_count+1
    Is_count = 0
    for i,j in zip(df["Activity"],df["IsThereEvent"]):
        if i == "Pub" and j=="No":
            Is_count = Is_count+1
    L_count = 0
    for i,j in zip(df["Activity"],df["Lazy"]):
        if i == "Pub" and j=="Yes":
            L_count = L_count+1

    studyTotal = ((act/total)*(D_count/act)*(Is_count/act)*(L_count/act))

    return studyTotal

def count_TV(df):

    total = len(df["Activity"])
    act = df["Activity"].str.count("TV").sum()

    D_count = 0
    for i,j in zip(df["Activity"],df["Deadline"]):
        if i=="TV" and j=="Near":
            D_count = D_count+1
    Is_count = 0
    for i,j in zip(df["Activity"],df["IsThereEvent"]):
        if i == "TV" and j=="No":
            Is_count = Is_count+1
    L_count = 0
    for i,j in zip(df["Activity"],df["Lazy"]):
        if i == "TV" and j=="Yes":
            L_count = L_count+1

    studyTotal = ((act/total)*(D_count/act)*(Is_count/act)*(L_count/act))

    return studyTotal

print("P(Party | near, no party, lazy)")
print(count_Party(df))
print("P(Study | near, no party, lazy)")
print(count_Study(df))
print("P(Pub | near, no party, lazy)")
print(count_Pub(df))
print("P(TV | near, no party, lazy)")
print(count_TV(df))