def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        #print(file_contents)
        num = frank_count(file_contents)
        print(f"{num} words found in the document")


def frank_count(file_contents):
    frank1 = str(file_contents)
    frank_str = frank1.split()

    return len(frank_str)


main()