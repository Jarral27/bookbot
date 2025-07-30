def word_count (text):
    count = len(text.split())
    count_message = f"{count} words found in the document"
    return count

def get_chars_dict(text):
    chars_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in chars_dict:
            chars_dict[lower_char] += 1
        else:
            chars_dict[lower_char] = 1
    return chars_dict

def sort_on(items):
    return items["num"]

def sort_chars_dict(num_chars_dict):
    sorted_chars_list = []
    for char, count in num_chars_dict.items():
        sorted_chars_list.append({"char": char, "num": count})
    sorted_chars_list.sort(key=sort_on, reverse=True)
    return sorted_chars_list
