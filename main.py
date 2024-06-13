import pandas as pd
import pickle
import os
from search_quran import (
    search_keywords_in_quran,
    fetch_complete_surah,
    get_total_surahs,
    get_biggest_surah,
    get_shortest_surah,
)

CACHE_FILE = 'keyword_cache.pkl'

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'rb') as f:
            return pickle.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(cache, f)

def main():
    # Load the translated Quran CSV
    try:
        quran_df = pd.read_csv('translated-quran.csv', delimiter='|')
        print("Column names in the DataFrame:", quran_df.columns)  # Print column names to verify
    except Exception as e:
        print(f"Error reading translated Quran CSV file: {e}")
        return

    print("Successfully loaded translated Quran.")

    # Load cache
    cache = load_cache()

    # Choose option
    option = input("Choose an option:\n1. Search by keywords\n2. Fetch complete surah\n3. Get total number of surahs\n4. Get the biggest surah\n5. Get the shortest surah\n").strip()

    if option == '1':
        # Get keywords from user
        keywords = input("Enter the keyword(s) separated by spaces: ").strip().lower().split()
        if not keywords:
            print("No keyword provided.")
            return

        keyword_str = ' '.join(keywords)

        if keyword_str in cache:
            print("Found in cache:")
            results = cache[keyword_str]
        else:
            # Search for the specified keywords in the Quran text
            keyword_verses = search_keywords_in_quran(quran_df, keywords)
            if keyword_verses:
                results = [f"Surah {surah}, Ayah {ayah}: {verse}" for surah, ayah, verse in keyword_verses]
                cache[keyword_str] = results
                save_cache(cache)
            else:
                results = ["No verses found containing the specified keyword(s)."]
                cache[keyword_str] = results
                save_cache(cache)

        keyword_file = f"quran_keywords_{'_'.join(keywords)}.txt"
        with open(keyword_file, "w") as f:
            for result in results:
                print(result)
                f.write(result + "\n")

    elif option == '2':
        # Get surah number from user
        surah_number = input("Enter the Surah number: ").strip()
        if not surah_number.isdigit():
            print("Invalid Surah number.")
            return

        surah_number = int(surah_number)
        complete_surah = fetch_complete_surah(quran_df, surah_number)

        if complete_surah:
            results = [f" Ayah {ayah}: {verse}" for surah, ayah, verse in complete_surah]
        else:
            results = [f"No verses found for Surah {surah_number}."]

        surah_file = f"quran_surah_{surah_number}.txt"
        with open(surah_file, "w") as f:
            for result in results:
                print(result)
                f.write(result + "\n")

    elif option == '3':
        # Get total number of surahs
        total_surahs = get_total_surahs(quran_df)
        print(f"Total number of Surahs in Quran are: {total_surahs}")

    elif option == '4':
        # Get the biggest surah
        biggest_surah, total_verses = get_biggest_surah(quran_df)
        print(f"The biggest surah is Surah of Quran is: {biggest_surah} with {total_verses} verses.")

    elif option == '5':
        # Get the shortest surah
        shortest_surah, total_verses = get_shortest_surah(quran_df)
        print(f"The shortest surah is Surah of Quran is: {shortest_surah} with {total_verses} verses.")


    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
