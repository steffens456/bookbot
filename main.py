from stats import (
    frank_count,
    frank_strcount,
    data_report,
    print_report
    )
import sys

def main():
    #explain what's going on
    #sys module


    try:
        book_path = sys.argv[1]
        file_contents = get_book_text(book_path)
    except IndexError:
        print("Error: Please provide a file path to your books.")
        sys.exit(1)
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

    
    #with open('books/frankenstein.txt') as f:
     #   file_contents = f.read()
        #print(file_contents)


    #from stats import frank_count
    num = frank_count(file_contents)

    print("============ BOOKBOT ============")
    print("Analyzing book input by user...")
    print(f"Found {num} total words")
    print("--------- Character Count -------")


    #from stats import frank_strcount
    dict2 = frank_strcount(file_contents)
    #print(dict2)

        
    #from stats import data_report
    frank_str2 = data_report(dict2)
    #print(frank_str2)

    #from stats import print_report
    print_report(frank_str2)

    
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


main()