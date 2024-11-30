import multiprocessing
from colorama import Fore, init
import time
from utils import search_keywords_in_file

def multiprocessing_search(file_paths, keywords):
    results = multiprocessing.Queue()
    processes = []

    start_time = time.time()

    for file_path in file_paths:
        process = multiprocessing.Process(target=search_keywords_in_file, args=(file_path, keywords, results))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    
    end_time = time.time()  
    print(f"{Fore.MAGENTA}Multiprocessing execution time: {end_time - start_time:.4f} seconds")
    print("")

    while not results.empty():
        file, matches = results.get()
        print(f"{Fore.BLUE}File: {Fore.YELLOW}{file}, {Fore.BLUE}Matches: {Fore.YELLOW}{matches}")

if __name__ == "__main__":
    # Ініціалізуємо colorama
    init(autoreset=True)

    file_paths = ['file1.txt', 'file2.txt', 'file3.txt']  
    keywords = ['code', 'debug', 'program']
    multiprocessing_search(file_paths, keywords)
