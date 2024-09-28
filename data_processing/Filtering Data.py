
import pandas as pd
import numpy as np
import re


#list of characters to be searched for
char_regex_list = [r'\b[a-zA-Z]aido[a-zA-Z]?(?:\'s)?\b',
    r'\bbig\s*mom[a-zA-Z]?(?:\'s)?\b',
    r'\bfraud\s*mom\b',
    r'\bma\s*ma[a-zA-Z]?(?:\'s)?\b',
    r'\bbig\s*meme[a-zA-Z]?(?:\'s)?\b',
    r'\bwin\s*win\b',
    r'\bbig\s*goat\b',
    r'\blin\s*lin[a-zA-Z]?(?:\'s)?\b',
    r'\bBM[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]hank[a-zA-Z]?(?:\'s)?\b',
    r'\brat\b',
    r'\bred\s*hair[a-zA-Z]?(?:\'s)?\b',
    r'\bred\s*haired[a-zA-Z]?(?:\'s)?\b',
    r'\bkid[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]idd[a-zA-Z]?(?:\'s)?\b',
    r'\bmidd[a-zA-Z]?(?:\'s)?\b',
    r'\bjika[a-zA-Z]?(?:\'s)?\b',
    r'\bluffy[a-zA-Z]?(?:\'s)?\b',
    r'\blaw[a-zA-Z]?(?:\'s)?\b',
    r'\broger[a-zA-Z]?(?:\'s)?\b',
    r'\bfraudger[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]arp[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]ihawk[a-zA-Z]?(?:\'s)?\b',
    r'\bmihawktard[a-zA-Z]?(?:\'s)?\b',
    r'\bfraudhawk[a-zA-Z]?(?:\'s)?\b',
    r'\bmidhawk[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]ragon[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]oro[a-zA-Z]?(?:\'s)?\b',
    r'\bzorro[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]izaru[a-zA-Z]?(?:\'s)?\b',
    r'\bborsalino[a-zA-Z]?(?:\'s)?\b',
    r'\bgreen\s*bull[a-zA-Z]?(?:\'s)?\b',
    r'\bgb[a-zA-Z]?(?:\'s)?\b',
    r'\baramaki[a-zA-Z]?(?:\'s)?\b',
    r'\bryokogyu[a-zA-Z]?(?:\'s)?\b',
    r'\baokiji[a-zA-Z]?(?:\'s)?\b',
    r'\bwaokiji[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]uzan[a-zA-Z]?(?:\'s)?\b',
    r'\bblack\s*beard[a-zA-Z]?(?:\'s)?\b',
    r'\bbb[a-zA-Z]?(?:\'s)?\b',
    r'\bmarshall[a-zA-Z]?(?:\'s)?\b',
    r'\bteach[a-zA-Z]?(?:\'s)?\b',
    r'\bbum\s*beard[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]oflamingo[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]offy[a-zA-Z]?(?:\'s)?\b',
    r'\bmingo[a-zA-Z]?(?:\'s)?\b',
    r'\bcrocodile[a-zA-Z]?(?:\'s)?\b',
    r'\bcroc[a-zA-Z]?(?:\'s)?\b',
    r'\bcroco[a-zA-Z]?(?:\'s)?\b',
    r'\bcroco\s*mom[a-zA-Z]?(?:\'s)?\b',
    r'\bcroco\s*boy[a-zA-Z]?(?:\'s)?\b',
    r'\bwhite\s*beard[a-zA-Z]?(?:\'s)?\b',
    r'\bwb[a-zA-Z]?(?:\'s)?\b',
    r'\bprime\s*beard[a-zA-Z]?(?:\'s)?\b',
    r'\bold\s*beard[a-zA-Z]?(?:\'s)?\b',
    r'\bgoat\s*beard[a-zA-Z]?(?:\'s)?\b',
    r'\bking[a-zA-Z]?(?:\'s)?\b',
    r'\bling[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]ueen[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]ujitora[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]uji[a-zA-Z]?(?:\'s)?\b',
    r'\bfraudjitora[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]uggy[a-zA-Z]?(?:\'s)?\b',
    r'\bakainu[a-zA-Z]?(?:\'s)?\b',
    r'\bsakazuki[a-zA-Z]?(?:\'s)?\b',
    r'\bpapazuki[a-zA-Z]?(?:\'s)?\b',
    r'\blakazuki[a-zA-Z]?(?:\'s)?\b',
    r'\wakainu[a-zA-Z]?(?:\'s)?\b',
    r'\boar[a-zA-Z]?(?:\'s)?\b',
    r'\bbrook[a-zA-Z]?(?:\'s)?\b',
    r'\bsoul\s*king[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]hopper[a-zA-Z]?(?:\'s)?\b',
    r'\bchopperman[a-zA-Z]?(?:\'s)?\b',
    r'\bchobro[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]ami[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]anji[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]ranky[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]obin[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]inbei[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]inbe[a-zA-Z]?(?:\'s)?\b',
    r'\bjinbie[a-zA-Z]?(?:\'s)?\b',
    r'\bfraudbei[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]ayleigh[a-zA-Z]?(?:\'s)?\b',
    r'\bray[a-zA-Z]?(?:\'s)?\b',
    r'\bdark\s*king[a-zA-Z]?(?:\'s)?\b',
    r'\bwankleigh[a-zA-Z]?(?:\'s)?\b',
    r'\burouge[a-zA-Z]?(?:\'s)?\b',
    r'\bwurouge[a-zA-Z]?(?:\'s)?\b',
    r'\bdorry[a-zA-Z]?(?:\'s)?\b',
    r'\bbroggy[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]engoku[a-zA-Z]?(?:\'s)?\b',
    r'\bsengoatku[a-zA-Z]?(?:\'s)?\b',
    r'\bjack[a-zA-Z]?(?:\'s)?\b',
    r'\bwack\b',
    r'\black\b',
    r'\brocks[a-zA-Z]?(?:\'s)?\b',
    r'\bxebec[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]hiki[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]oby[a-zA-Z]?(?:\'s)?\b',
    r'\bkiller[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]eckman[a-zA-Z]?(?:\'s)?\b',
    r'\bgecko\s*moria[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]oria[a-zA-Z]?(?:\'s)?\b',
    r'\bace[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]abo[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]arco[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]ista[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]uma[a-zA-Z]?(?:\'s)?\b',
    r'\bvergo[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]racker[a-zA-Z]?(?:\'s)?\b',
    r'\boden[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]oden[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]ozu[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]ucci[a-zA-Z]?(?:\'s)?\b',
    r'\bbartolomeo[a-zA-Z]?(?:\'s)?\b',
    r'\bbarto[a-zA-Z]?(?:\'s)?\b',
    r'\bvegapunk[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]amato[a-zA-Z]?(?:\'s)?\b',
    r'\bhancock[a-zA-Z]?(?:\'s)?\b',
    r'\bboa[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]erospero[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]atakuri[a-zA-Z]?(?:\'s)?\b',
    r'\bkata[a-zA-Z]?(?:\'s)?\b',
    r'\busopp[a-zA-Z]?(?:\'s)?\b',
    r'\bbon\s*clay[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]inemon[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]awkin[a-zA-Z]?(?:\'s)?\b',
    r'\b[a-zA-Z]oothie[a-zA-Z]?(?:\'s)?\b']


#Returns true if character is in list
def char_search_regex(string, patterns):
    compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    
    return any(pattern.search(string) for pattern in compiled_patterns)


testing = pd.read_csv('frame5.csv')


testing = testing.drop(columns = ['Unnamed: 0'])


#Apply function to create new column
testing['contains_char'] = testing['comment'].apply(lambda x: char_search_regex(x, char_regex_list))

#Dropping all comments without characters
cleaned_test = testing.drop(testing[testing['contains_char'] == False].index)


cleaned_test = cleaned_test.drop(columns = ['contains_char'])


cleaned_test.to_csv('cleaned_data.csv')


