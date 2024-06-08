import pandas as pd
from googletrans import Translator
import time


def translate_verse(verse, translator):
    try:
        translation = translator.translate(verse, src='ar', dest='en').text
        return translation
    except Exception as e:
        print(f"Error translating verse: {e}")
        return verse


def translate_quran_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv, delimiter='|', names=['surah', 'ayah', 'verse'])
    translator = Translator()

    translated_verses = []
    for index, row in df.iterrows():
        surah = row['surah']
        ayah = row['ayah']
        verse = row['verse']
        print(f"Translating Surah {surah}, Ayah {ayah}")
        translated_verse = translate_verse(verse, translator)
        translated_verses.append([surah, ayah, translated_verse])

        # Sleep to avoid hitting the translation API rate limit
        time.sleep(0.5)  # Reduced sleep time to 0.5 seconds

    translated_df = pd.DataFrame(translated_verses, columns=['surah', 'ayah', 'verse'])
    translated_df.to_csv(output_csv, index=False, sep='|')


if __name__ == "__main__":
    input_csv_path = 'arabic-original.csv'
    output_csv_path = 'translated-quran.csv'
    translate_quran_csv(input_csv_path, output_csv_path)
    print(f"Translated Quran saved to {output_csv_path}")
