def get_wordcount(file_contents):
    return len(file_contents.split())

def get_charcount(file_contents):
        chars = {}
        for c in file_contents:
                lowered = c.lower()
                if lowered in chars:
                        chars[lowered] +=1
                else:
                        chars[lowered] = 1
        return chars

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(charcount):
    sorted_list = []
    for ch in charcount:
        sorted_list.append({"char": ch, "num": charcount[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        