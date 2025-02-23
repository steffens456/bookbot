

def frank_count(file_contents):
    frank1 = str(file_contents)
    frank_str = frank1.split()

    return len(frank_str)


def frank_strcount(file_contents):
    dict1 = {}

    for c in file_contents.lower():
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1

    return dict1


    #helper function
def sort_on(dict2):
    dog1 = list(dict2.values())[0]
    return dog1

def data_report(dict2):
    

    #create a list of dictionaries
    sorted_counts = [{char: count} for char, count in dict2.items() if char.isalpha()]

    #sort the list in place by descending order
    sorted_counts.sort(reverse= True, key= sort_on)

    return sorted_counts

def print_report(frank_str2):
    #it's a list of dictionaries

    for i in range(0, len(frank_str2)):
        dict3 = frank_str2[i]
        str3 = str(dict3)
        str4 = str3[2] + ": " + str3[6:-1]
        print(str4)

    return