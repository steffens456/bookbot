def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        #print(file_contents)


        from stats import frank_count
        num = frank_count(file_contents)

        print(f"{num} words found in the document")

        from stats import frank_strcount

        dict2 = frank_strcount(file_contents)
        print(dict2)



main()