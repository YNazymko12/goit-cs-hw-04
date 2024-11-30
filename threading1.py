import threading
from queue import Queue
from colorama import Fore, init
import time
from utils import search_keywords_in_file

def threaded_search(file_paths, keywords):
    results = Queue()
    threads = []

    start_time = time.time()

    for file_path in file_paths:
        thread = threading.Thread(target=search_keywords_in_file, args=(file_path, keywords, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    end_time = time.time() 
    print(f"{Fore.MAGENTA}Threading execution time: {end_time - start_time:.4f} seconds")
    print("")

    while not results.empty():
        file, matches = results.get()
        print(f"{Fore.BLUE}File: {Fore.YELLOW}{file}, {Fore.BLUE}Matches: {Fore.YELLOW}{matches}")

if __name__ == "__main__":
    # Ініціалізуємо colorama
    init(autoreset=True)

    file_paths = ['file1.txt', 'file2.txt', 'file3.txt']  
    keywords = ['code', 'debug', 'program']
    threaded_search(file_paths, keywords)
