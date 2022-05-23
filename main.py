import re


def num_string_extract(string) -> int:
    """
    Takes in a string will attempt to extract a number from within
    that string
    :param string:
    :return int:
    """
    extracted_num = re.findall(r'\d', string)
    if len(extracted_num) > 1:
        extracted_num = int("".join(extracted_num))
    else:
        extracted_num = int(extracted_num[0])
    return extracted_num


def sort_string(__list) -> list:
    """
    Takes in an array of string that contains nums
    and sorts the items.
    :param __list:
    :return array:
    """
    control_count = 0
    sorted_array = []
    for _ in range(len(__list) * 1000):
        control_count += 1
        for item in __list:
            ex_num = num_string_extract(item)
            if ex_num == control_count:
                sorted_array.append(item)
    return sorted_array
