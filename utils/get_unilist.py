def get_unilist(lis):
    result = []
    for i in lis:
        if i and i not in result:
            result.append(i)
    return result


def get_trimed_list(item, list_):
    if item in list_:
        list_.remove(item)
    return list_
