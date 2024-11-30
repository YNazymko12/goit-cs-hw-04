def search_keywords_in_file(file_path, keywords, results):
    """
    Шукає ключові слова у вказаному файлі з ігноруванням регістру та обробкою помилок.

    :param file_path: Шлях до файлу.
    :param keywords: Список ключових слів для пошуку.
    :param results: Черга або список для збереження результатів.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            
            text = f.read().lower()  
        # Пошук ключових слів
        matches = {keyword: text.count(keyword.lower()) for keyword in keywords if keyword.lower() in text}
        if matches:
            results.put((file_path, matches))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except UnicodeDecodeError:
        print(f"Error: File '{file_path}' could not be decoded with UTF-8 encoding.")
    except Exception as e:
        print(f"Error: An unexpected error occurred while processing '{file_path}': {e}")
