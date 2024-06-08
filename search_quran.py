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
                entities = perform_ner(verse)
                keyword_verses.append((surah, ayah, verse, entities))
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
