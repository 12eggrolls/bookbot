def get_num_words(words: str) -> None:
    print(f"Found {len(words.split())} total words")

def get_num_char(words: str) -> dict:
    char_dict = {}
    for char in words.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_num_char_sorted(unsorted_words: dict):
    dict_list = []
    for key, value in unsorted_words.items():
        dict_list.append({"char": key, "num": value})
    
    
    dict_list.sort(reverse=True, key=lambda x: x["num"])
    return dict_list