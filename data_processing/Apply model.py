
import pandas as pd
import numpy as np
from transformers import pipeline
from transformers import BertConfig, BertModel


import re


model = pipeline(model="Bigfoottt/autotrain-f01du-emtzm", token='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')


data = pd.read_csv('frame5.csv')


data = data.drop(columns = ['Unnamed: 0'])


data['senti'] = data['comment'].apply(lambda x: model.predict(x))


def extract_label_from_list(lst):
    if lst and isinstance(lst[0], dict):  # Check if the list is not empty and contains a dictionary
        return lst[0].get('label', None)  # Use .get() to avoid KeyError
    return None  # Return None if the list is empty or does not contain a dictionary


# Apply the function to the 'info' column
data['senti'] = data['senti'].apply(extract_label_from_list)


#Accounting for upvote from commenter
data['score'] = data['score'] + 1


#Dict to replace all variations of name
replace_dict = {
    r'\b[a-zA-Z]aido[a-zA-Z]?(?:\'s)?\b': 'Kaido',
    r'\bbig\s*mom[a-zA-Z]?(?:\'s)?\b': 'Big Mom',
    r'\bfraud\s*mom\b': 'Big Mom',
    r'\bma\s*ma[a-zA-Z]?(?:\'s)?\b': 'Big Mom',
    r'\bbig\s*meme[a-zA-Z]?(?:\'s)?\b': 'Big Mom',
    r'\bwin\s*win\b': 'Big Mom',
    r'\bbig\s*goat\b': 'Big Mom',
    r'\blin\s*lin[a-zA-Z]?(?:\'s)?\b': 'Big Mom',
    r'\bBM[a-zA-Z]?(?:\'s)?\b': 'Big Mom',
    r'\b[a-zA-Z]hank[a-zA-Z]?(?:\'s)?\b': 'Shanks',
    r'\brat\b': 'Shanks',
    r'\bred\s*hair[a-zA-Z]?(?:\'s)?\b': 'Shanks',
    r'\bred\s*haired[a-zA-Z]?(?:\'s)?\b': 'Shanks',
    r'\bkid[a-zA-Z]?(?:\'s)?\b': 'Kidd',
    r'\b[a-zA-Z]idd[a-zA-Z]?(?:\'s)?\b': 'Kidd',
    r'\bmidd[a-zA-Z]?(?:\'s)?\b': 'Kidd',
    r'\bjika[a-zA-Z]?(?:\'s)?\b': 'Kidd',
    r'\bluffy[a-zA-Z]?(?:\'s)?\b': 'Luffy',
    r'\blaw[a-zA-Z]?(?:\'s)?\b': 'Law',
    r'\broger[a-zA-Z]?(?:\'s)?\b': 'Roger',
    r'\bfraudger[a-zA-Z]?(?:\'s)?\b': 'Roger',
    r'\b[a-zA-Z]arp[a-zA-Z]?(?:\'s)?\b': 'Garp',
    r'\b[a-zA-Z]ihawk[a-zA-Z]?(?:\'s)?\b': 'Mihawk',
    r'\bmihawktard[a-zA-Z]?(?:\'s)?\b': 'Mihawk',
    r'\bfraudhawk[a-zA-Z]?(?:\'s)?\b': 'Mihawk',
    r'\bmidhawk[a-zA-Z]?(?:\'s)?\b': 'Mihawk',
    r'\b[a-zA-Z]ragon[a-zA-Z]?(?:\'s)?\b': 'Dragon',
    r'\b[a-zA-Z]oro[a-zA-Z]?(?:\'s)?\b': 'Zoro',
    r'\bzorro[a-zA-Z]?(?:\'s)?\b': 'Zoro',
    r'\b[a-zA-Z]izaru[a-zA-Z]?(?:\'s)?\b': 'Kizaru',
    r'\bborsalino[a-zA-Z]?(?:\'s)?\b': 'Kizaru',
    r'\bgreen\s*bull[a-zA-Z]?(?:\'s)?\b': 'Greenbull',
    r'\bgb[a-zA-Z]?(?:\'s)?\b': 'Greenbull',
    r'\baramaki[a-zA-Z]?(?:\'s)?\b': 'Greenbull',
    r'\bryokogyu[a-zA-Z]?(?:\'s)?\b': 'Greenbull',
    r'\baokiji[a-zA-Z]?(?:\'s)?\b': 'Aokiji',
    r'\bwaokiji[a-zA-Z]?(?:\'s)?\b': 'Aokiji',
    r'\b[a-zA-Z]uzan[a-zA-Z]?(?:\'s)?\b': 'Aokiji',
    r'\bblack\s*beard[a-zA-Z]?(?:\'s)?\b': 'Blackbeard',
    r'\bbb[a-zA-Z]?(?:\'s)?\b': 'Blackbeard',
    r'\bmarshall[a-zA-Z]?(?:\'s)?\b': 'Blackbeard',
    r'\bteach[a-zA-Z]?(?:\'s)?\b': 'Blackbeard',
    r'\bbum\s*beard[a-zA-Z]?(?:\'s)?\b': 'Blackbeard',
    r'\b[a-zA-Z]oflamingo[a-zA-Z]?(?:\'s)?\b': 'Doflamingo',
    r'\b[a-zA-Z]offy[a-zA-Z]?(?:\'s)?\b': 'Doflamingo',
    r'\bmingo[a-zA-Z]?(?:\'s)?\b': 'Doflamingo',
    r'\bcrocodile[a-zA-Z]?(?:\'s)?\b': 'Crocodile',
    r'\bcroc[a-zA-Z]?(?:\'s)?\b': 'Crocodile',
    r'\bcroco[a-zA-Z]?(?:\'s)?\b': 'Crocodile',
    r'\bcroco\s*mom[a-zA-Z]?(?:\'s)?\b': 'Crocodile',
    r'\bcroco\s*boy[a-zA-Z]?(?:\'s)?\b': 'Crocodile',
    r'\bwhite\s*beard[a-zA-Z]?(?:\'s)?\b': 'Whitebeard',
    r'\bwb[a-zA-Z]?(?:\'s)?\b': 'Whitebeard',
    r'\bprime\s*beard[a-zA-Z]?(?:\'s)?\b': 'Whitebeard',
    r'\bold\s*beard[a-zA-Z]?(?:\'s)?\b': 'Whitebeard',
    r'\bgoat\s*beard[a-zA-Z]?(?:\'s)?\b': 'Whitebeard',
    r'\bking[a-zA-Z]?(?:\'s)?\b': 'King',
    r'\bling[a-zA-Z]?(?:\'s)?\b': 'King',
    r'\b[a-zA-Z]ueen[a-zA-Z]?(?:\'s)?\b': 'Queen',
    r'\b[a-zA-Z]ujitora[a-zA-Z]?(?:\'s)?\b': 'Fujitora',
    r'\b[a-zA-Z]uji[a-zA-Z]?(?:\'s)?\b': 'Fujitora',
    r'\bfraudjitora[a-zA-Z]?(?:\'s)?\b': 'Fujitora',
    r'\b[a-zA-Z]uggy[a-zA-Z]?(?:\'s)?\b': 'Buggy',
    r'\bakainu[a-zA-Z]?(?:\'s)?\b': 'Akainu',
    r'\bsakazuki[a-zA-Z]?(?:\'s)?\b': 'Akainu',
    r'\bpapazuki[a-zA-Z]?(?:\'s)?\b': 'Akainu',
    r'\blakazuki[a-zA-Z]?(?:\'s)?\b': 'Akainu',
    r'\wakainu[a-zA-Z]?(?:\'s)?\b': 'Akainu',
    r'\boar[a-zA-Z]?(?:\'s)?\b': 'Oars',
    r'\bbrook[a-zA-Z]?(?:\'s)?\b': 'Brook',
    r'\bsoul\s*king[a-zA-Z]?(?:\'s)?\b': 'Brook',
    r'\b[a-zA-Z]hopper[a-zA-Z]?(?:\'s)?\b': 'Chopper',
    r'\bchopperman[a-zA-Z]?(?:\'s)?\b': 'Chopper',
    r'\bchobro[a-zA-Z]?(?:\'s)?\b': 'Chopper',
    r'\b[a-zA-Z]ami[a-zA-Z]?(?:\'s)?\b': 'Nami',
    r'\b[a-zA-Z]anji[a-zA-Z]?(?:\'s)?\b': 'Sanji',
    r'\b[a-zA-Z]ranky[a-zA-Z]?(?:\'s)?\b': 'Franky',
    r'\b[a-zA-Z]obin[a-zA-Z]?(?:\'s)?\b': 'Robin',
    r'\b[a-zA-Z]inbei[a-zA-Z]?(?:\'s)?\b': 'Jinbei',
    r'\b[a-zA-Z]inbe[a-zA-Z]?(?:\'s)?\b': 'Jinbei',
    r'\bjinbie[a-zA-Z]?(?:\'s)?\b': 'Jinbei',
    r'\bfraudbei[a-zA-Z]?(?:\'s)?\b': 'Jinbei',
    r'\b[a-zA-Z]ayleigh[a-zA-Z]?(?:\'s)?\b': 'Rayleigh',
    r'\bray[a-zA-Z]?(?:\'s)?\b': 'Rayleigh',
    r'\bdark\s*king[a-zA-Z]?(?:\'s)?\b': 'Rayleigh',
    r'\bwankleigh[a-zA-Z]?(?:\'s)?\b': 'Rayleigh',
    r'\burouge[a-zA-Z]?(?:\'s)?\b': 'Urouge',
    r'\bwurouge[a-zA-Z]?(?:\'s)?\b': 'Urouge',
    r'\bdorry[a-zA-Z]?(?:\'s)?\b': 'Dorry',
    r'\bbroggy[a-zA-Z]?(?:\'s)?\b': 'Broggy',
    r'\b[a-zA-Z]engoku[a-zA-Z]?(?:\'s)?\b': 'Sengoku',
    r'\bsengoatku[a-zA-Z]?(?:\'s)?\b': 'Sengoku',
    r'\bjack[a-zA-Z]?(?:\'s)?\b': 'Jack',
    r'\bwack\b': 'Jack',
    r'\black\b': 'Jack',
    r'\brocks[a-zA-Z]?(?:\'s)?\b': 'Rocks',
    r'\bxebec[a-zA-Z]?(?:\'s)?\b': 'Rocks',
    r'\b[a-zA-Z]hiki[a-zA-Z]?(?:\'s)?\b': 'Shiki',
    r'\b[a-zA-Z]oby[a-zA-Z]?(?:\'s)?\b': 'Koby',
    r'\bkiller[a-zA-Z]?(?:\'s)?\b': 'Killer',
    r'\b[a-zA-Z]eckman[a-zA-Z]?(?:\'s)?\b': 'Beckman',
    r'\bgecko\s*moria[a-zA-Z]?(?:\'s)?\b': 'Moria',
    r'\b[a-zA-Z]oria[a-zA-Z]?(?:\'s)?\b': 'Moria',
    r'\bace[a-zA-Z]?(?:\'s)?\b': 'Ace',
    r'\b[a-zA-Z]abo[a-zA-Z]?(?:\'s)?\b': 'Sabo',
    r'\b[a-zA-Z]arco[a-zA-Z]?(?:\'s)?\b': 'Marco',
    r'\b[a-zA-Z]ista[a-zA-Z]?(?:\'s)?\b': 'Vista',
    r'\b[a-zA-Z]uma[a-zA-Z]?(?:\'s)?\b': 'Kuma',
    r'\bvergo[a-zA-Z]?(?:\'s)?\b': 'Vergo',
    r'\b[a-zA-Z]racker[a-zA-Z]?(?:\'s)?\b': 'Cracker',
    r'\boden[a-zA-Z]?(?:\'s)?\b': 'Oden',
    r'\b[a-zA-Z]oden[a-zA-Z]?(?:\'s)?\b': 'Oden',
    r'\b[a-zA-Z]ozu[a-zA-Z]?(?:\'s)?\b': 'Jozu',
    r'\b[a-zA-Z]ucci[a-zA-Z]?(?:\'s)?\b': 'Lucci',
    r'\bbartolomeo[a-zA-Z]?(?:\'s)?\b': 'Bartolomeo',
    r'\bbarto[a-zA-Z]?(?:\'s)?\b': 'Bartolomeo',
    r'\bvegapunk[a-zA-Z]?(?:\'s)?\b': 'Vegapunk',
    r'\b[a-zA-Z]amato[a-zA-Z]?(?:\'s)?\b': 'Yamato',
    r'\bhancock[a-zA-Z]?(?:\'s)?\b': 'Boa',
    r'\bboa[a-zA-Z]?(?:\'s)?\b': 'Boa',
    r'\b[a-zA-Z]erospero[a-zA-Z]?(?:\'s)?\b': 'Perospero',
    r'\b[a-zA-Z]atakuri[a-zA-Z]?(?:\'s)?\b': 'Katakuri',
    r'\bkata[a-zA-Z]?(?:\'s)?\b': 'Katakuri',
    r'\busopp[a-zA-Z]?(?:\'s)?\b': 'Usopp',
    r'\bbon\s*clay[a-zA-Z]?(?:\'s)?\b': 'Bon Clay',
    r'\b[a-zA-Z]inemon[a-zA-Z]?(?:\'s)?\b': 'Kinemon',
    r'\b[a-zA-Z]awkin[a-zA-Z]?(?:\'s)?\b': 'Hawkins',
    r'\b[a-zA-Z]oothie[a-zA-Z]?(?:\'s)?\b': 'Smoothie'}


#Function to consolidiate names to one version
def replace_names_with_regex(text, replacements):
    for pattern, replacement in replacements.items():
        regex = re.compile(pattern, re.IGNORECASE)
        text = regex.sub(lambda match: replacement, text)
    return text


#Apply name consolidation
data['comment'] = data['comment'].apply(lambda x: replace_names_with_regex(x, replace_dict))


#List of valid character names to isolate
consolidation_list = ['Kaido', 'Big Mom']


#Function to extract first mentioned character in the comment
def extract_names_in_order(text, char):
    # Create a list to hold found names
    found_n = []
    
    # Create a dictionary to store the position of each name in the text
    name_positions = {}
    
    # Populate the name_positions dictionary with the starting index of each name
    for name in char:
        start = text.find(name)
        if start != -1:
            name_positions[name] = start
    
    # Sort names by their positions in the text
    sorted_names = sorted(name_positions, key=lambda k: name_positions[k])
    
    # Add the names found to the list in order
    for name in sorted_names:
        if name in text:
            found_n.append(name)
    
    return found_n


data['character'] = data['comment'].apply(lambda x: extract_names_in_order(x, consolidation_list))


#Removing empty lists
data = data.drop(data[data['character'].map(len) == 0].index)


#Resetting index
data = data.reset_index(drop = True)


#Converting to string and isolate first character mentioned
def char_first(char):
    y = []
    y.append(char[0])
    y = ''.join(y)
    return y


data['character'] = data['character'].apply(lambda x: char_first(x))


data['senti'] = data['senti'].astype(int)


data['total'] = data['senti']*data['score']





trans = data.groupby(['character'])[['total']].sum()


trans['transformed'] = trans['total'] / 30000





