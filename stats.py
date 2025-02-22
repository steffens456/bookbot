

def frank_count(file_contents):
    frank1 = str(file_contents)
    frank_str = frank1.split()

    return len(frank_str)


def frank_strcount(file_contents):
    frank1 = str(file_contents)
    frank_str = frank1.split()

    frank_lower = frank_str.lower()

    dict1 = {}

    for c in dict1:
        if c in dict1:
            dict1 += 1
        else:
            dict1[c] = 1

    return dict1