def file_to_string(file):
    print(f"Analyzing book found at {file}")
    file_contents = ""
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(file_contents):
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1
    print("----------- Word Count ----------")
    return(f"Found {count} total words")


def char_count(file_contents):
    char_list = list(file_contents.lower())
    char_set = set(char_list)
    char_dict = {}
    for char in char_set:
        count = 0
        for item in char_list:
            if char == item:
                count += 1
        char_dict[char]=count
    return char_dict


def unsorted_dict(char_count):
    list_dict =[]
    for char in char_count:
        list_dict.append({"char" : char, "num" :char_count[char] }) 
    return (list_dict)


def sort_on(items):
    return items["num"]


def sorted_dict(unsorted_dict):
    unsorted_dict.sort(reverse=True, key=sort_on)
    new_dict = {}
    for item in unsorted_dict:
        new_dict[item["char"]] = item["num"]
    return(new_dict)

def pretty(sorted_dict):
    print("--------- Character Count -------")
    for item in sorted_dict:
        if item.isalpha():
            print(item + ": " + str(sorted_dict[item]))