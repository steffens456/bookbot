def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        #print(file_contents)


        from stats import frank_count
        num = frank_count(file_contents)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print(f"Found {num} total words")
        print("--------- Character Count -------")


        from stats import frank_strcount
        dict2 = frank_strcount(file_contents)
        #print(dict2)

        
        from stats import data_report
        frank_str2 = data_report(dict2)
        #print(frank_str2)

        from stats import print_report
        print_report(frank_str2)




main()