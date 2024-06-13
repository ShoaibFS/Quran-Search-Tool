import re
from ner import perform_ner

def search_keywords_in_quran(df, keywords):
    keyword_verses = []
    for index, row in df.iterrows():
        surah = row['surah']
        ayah = row['ayah']
        verse = row['Verse']  # Use correct column name
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', verse, re.IGNORECASE):
                keyword_verses.append((surah, ayah, verse))
                break  # Break the loop once a match is found to avoid duplicates
    return keyword_verses

def fetch_complete_surah(df, surah_number):
    surah_verses = df[df['surah'] == surah_number]
    complete_surah = []
    for index, row in surah_verses.iterrows():
        surah = row['surah']
        ayah = row['ayah']
        verse = row['Verse']  # Use correct column name
        complete_surah.append((surah, ayah, verse))
    return complete_surah

def get_total_surahs(df):
    return df['surah'].nunique()

def get_biggest_surah(df):
    surah_sizes = df.groupby('surah').size()
    biggest_surah = surah_sizes.idxmax()
    total_verses = surah_sizes.max()
    return biggest_surah, total_verses

def get_shortest_surah(df):
    surah_sizes = df.groupby('surah').size()
    shortest_surah = surah_sizes.idxmin()
    total_verses = surah_sizes.min()
    return shortest_surah, total_verses

def get_prophets_mentions(df):
    prophets = ['Adam', 'Noah', 'Abraham', 'Moses', 'Jesus', 'Muhammad']  # Add more prophets as needed
    mentions = {prophet: [] for prophet in prophets}
    for index, row in df.iterrows():
        surah = row['surah']
        ayah = row['ayah']
        verse = row['Verse']
        for prophet in prophets:
            if re.search(r'\b' + re.escape(prophet) + r'\b', verse, re.IGNORECASE):
                mentions[prophet].append((surah, ayah))
    return mentions
