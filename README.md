# Quran Search Tool

This Python project provides functionality to search for specific keywords within the translated text of the Quran. It allows users to either search for specific keywords or fetch the complete verses of a chosen Surah (chapter) from the Quran. Additionally, it utilizes Named Entity Recognition (NER) to identify entities within the Quranic verses.

## Files

### `main.py`

This file contains the main script of the Quran search tool. It provides the following functionalities:

- **Search by Keywords**: Users can input keywords separated by spaces to search for relevant verses containing those keywords. The results are saved in a text file named `quran_keywords_<keywords>.txt`.
- **Fetch Complete Surah**: Users can input the Surah number to fetch all verses of that particular Surah. The results are saved in a text file named `quran_surah_<surah_number>.txt`.

### `search_quran.py`

This file contains functions for searching keywords within the Quranic text and fetching complete verses of a specific Surah. It includes the following functions:

- **`search_keywords_in_quran(df, keywords)`**: Searches for the specified keywords within the translated Quran text. It utilizes regular expressions to find matches and performs Named Entity Recognition (NER) to identify entities within the verses.
- **`fetch_complete_surah(df, surah_number)`**: Fetches all verses of the specified Surah from the translated Quran text.

### `ner.py`

This file contains a function for Named Entity Recognition (NER) using the spaCy library. The `perform_ner(text)` function extracts entities from a given text.

## Dependencies

- `pandas`: Used for reading the translated Quran CSV file and handling data frames.
- `pickle`: Utilized for caching search results to improve performance.
- `os`: Required for file operations and checking the existence of files.
- `spacy`: Utilized for Named Entity Recognition (NER).

## Usage

1. Ensure you have the necessary dependencies installed.
2. Place the translated Quran CSV file (`translated-quran.csv`) in the same directory as the scripts.
3. Run `main.py` and follow the prompts to either search by keywords or fetch complete Surah.
4. View the results saved in the respective text files generated in the same directory.

## Cache

The project includes a caching mechanism (`keyword_cache.pkl`) to store search results temporarily, improving performance by avoiding repeated searches for the same keywords.

## Note

- Make sure to replace the file paths or modify the script accordingly if your file locations differ.
- Ensure the translated Quran CSV file is properly formatted with columns: 'surah', 'ayah', and 'Verse'.

## Author

Muhammad Shoaib - Github: https://github.com/ShoaibFS   
                          Shoaibfaisal94@yahoo.com            

