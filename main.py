def main():
    import sys
    from stats import file_to_string
    from stats import get_num_words
    from stats import char_count
    from stats import unsorted_dict
    from stats import sorted_dict
    from stats import sort_on
    from stats import pretty
  


    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    file_contents = file_to_string(sys.argv[1])    
    print(get_num_words(file_contents))
    count = char_count(file_contents)
    unsorted = unsorted_dict(count)
    ugly = sorted_dict(unsorted)
    pretty(ugly)
    print(sys.argv)




main()