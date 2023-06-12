import pandas as pd
import numpy as np
data = pd.read_csv("phonedata.csv");

def split_brand(data):
    brand = []
    model = []
    rows = data.shape[0]
    for i in range(0,rows):
        model_brand = data.loc[i].at["model"]
        split_arr = model_brand.split()
        brand.append(split_arr[0])
        n = len(split_arr)
        text = []
        for i in range(1,n):
            text.append(split_arr[i])
        model.append(" ".join(text))
    data['brand'] = brand
    data['model_only'] = model
    print(data[['model','brand','model_only']].head())

def replace_card(data):
    rows = data.shape[0]
    for i in range(0,rows):
        hi = "hi"
        card = data.loc[i].at["card"]
        if(type(card)==type(hi)):
            if(not card.startswith("Memory")):
                data.replace(data.loc[i].get('card'),0,inplace=True)
        else:
            continue
    return data

data = replace_card(data)
card = []
card_size = []
rows = data.shape[0]
for i in range(0,rows):
    card_data = data.loc[i].at["card"]
    if(card_data=='Memory Card (Hybrid)'  or card_data=='Memory Card Supported'):
        card.append(1)
        card_size.append(0)
        continue
    elif(card_data == 'Memory Card Not Supported' or card_data==0 or card_data==np.nan):
        card.append(0)
        card_size.append(0)
        continue
    else:
        split_data = str(card_data).split(",")
        if(len(split_data)==2):
            card.append(1)
            card_size.append(split_data[1].strip())
        else:
            card.append(0)
            card_size.append(0)
data['new_card'] = card
data['card_size'] = card_size

