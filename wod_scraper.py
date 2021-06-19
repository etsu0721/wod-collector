#!/Users/elijahsutton/opt/anaconda3/envs/wod_collector/bin/python
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.wordnik.com/word-of-the-day' # URL which to scrape for WoD data
WoD_FNAME = '/Users/elijahsutton/Google-Drive/Professional/Portfolio/Word-of-the-Day-Collector/wod_data.txt' # file where WoD data is stored

def scrape_url(url):
    """
    This funtion takes a URL as a string to scrape for word-of-the-day data element
    and returns the data elements (word, part of speech, definiton, and example) 
    as a dictionary.

    Parameters
    ----------
    url : string which is a URL to scrape

    Returns
    -------
    res : dictionary of data elements scraped
    """
    # Send HTTP request to specified URL and save response from server
    r = requests.get(url)
    
    # Create BeautifulSoup object from raw HTML with HTML parser
    soup = BeautifulSoup(r.content, 'html.parser')                 
                           
    # Get word, part of speech, definition and example
    word = soup.find(name='h1').text
    pos = soup.find(name='abbr').text
    def_ = soup.find(name='div', attrs={'class':'guts active'}).li.contents[-1].strip()    
    eg = soup.find(name='p', attrs={'class':'text'}).text
    
    # Store scraped data elements as a dictionary
    res = {'word' : word, 
           'part_of_speech' : pos, 
           'definition' : def_,
           'example' : eg}  
    return res

def display_word_data(word_dict):
    """
    This function takes in a dictionary containing data elements of a word and 
    displays each of the key-value pairs.

    Parameters
    ----------
    word_dict : tuple which contains four data elements of a word

    Returns
    -------
    None.

    """
    for k,v in word_dict.items():
        print('{key} : {value}\n'.format(key=k.upper(), value=v))
    return

def get_wod_df():
    """
    This functions reads in the Word of the Day TXT file from the provided path,
    where previous WoD data is stored, into a DataFrame and returns it.
    
    Parameters
    ----------
    fname : string which is the filename of file where previous WoD data is stored

    Returns
    -------
    df : pandas DataFrame of word of the day data

    """
    df = pd.read_csv(WoD_FNAME, sep='\t') 
    return df

def update_wod_df(df, wod):
    """
    This function takes the WoD DataFrame (df) and the day's WoD (wod) as input
    and appends wod to df if the wod does not already exist in df.

    Parameters
    ----------
    df : pandas DataFrame containing all WoD data
    wod : dict containing today's WoD data

    Returns
    -------
    None.

    """
    # Check for presence of wod in df
    if wod['word'] in df['word'].values:
        # Print that the word has already by captured
        print('"{}" has already be captured.'.format(wod['word']))
    else:
        # Append new WoD to DataFrame
        df = df.append(wod, ignore_index=True)
        
        # Save DataFrame to file
        df.to_csv(WoD_FNAME, index=False, sep='\t')
        
        print('{} updated successfully.'.format(WoD_FNAME))
    return

def main(): 
    
    # Scrape URL
    word_dict = scrape_url(URL)
    
    # Display all elements of word_tuple
    display_word_data(word_dict)
    
    # Read in Word of the Day file to be updated as a DataFrame
    words_df = get_wod_df()
    
    # Append new word (word_dict) to DataFrame (words_df) and write back to file
    update_wod_df(words_df, word_dict)
    return

main()