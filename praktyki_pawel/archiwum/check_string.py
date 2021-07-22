a = 's'
if not '':
    print('False')


def get_height(needed_height):
    wanted_height = ''
    for ch in needed_height:
        if ch.isdigit():
            wanted_height += ch
    if wanted_height == '':
        return None

    if wanted_height[0] == '0':
        a = int(wanted_height[0])
        b = int(wanted_height[1:])
    else:
        b = int(wanted_height[2:])
        a = int(wanted_height[0:2])
    return b - a


print(get_height('18 -- 30'))
