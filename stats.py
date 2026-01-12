def get_number_of_words(text):
    split_text = text.split()
    # print(f"Found {len(split_text)} total words")
    return len(split_text)


def get_char_count(text):
    my_dict = {}
    text = text.lower()
    for char in text:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict


def sort_on(d):
    return d["num"]


def get_sorted_chat_count(counts):
    sorted_list = []
    for ch in counts:
        sorted_list.append({"char": ch, "num": counts[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
