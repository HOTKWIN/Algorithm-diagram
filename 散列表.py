# 检查投票人是否投过票
voted = {}

def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")


if __name__ == '__main__':
    check_voter('hwh')
    check_voter('abc')
    check_voter('hwh')


#检查散列表中是否存储了该页面
cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data

