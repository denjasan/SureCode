import time


# file_name = 'wow2small.txt'
file_name = 'wow.txt'
print('Длинна файла:', len(open(file_name, 'r').readline()))


def BM(what):
    t, s = what, open(file_name, 'r').readline()
    before = time.time()
    t += '~'
    d = {}
    length = len(t)
    for i in range(length - 3, -1, -1):
        d[t[i]] = d.get(t[i], length - i - 2)
    d[t[-1]] = length - 1
    d[t[-2]] = d.get(t[-2], length - 1)
    t = t[:-1]
    elem = t[-1]
    i = length - 2
    k = 0
    la = len(s)
    while i < la:
        if s[i] != elem:
            i += d.get(s[i], d['~'])
        else:
            if s[i - length + 2:i + 1] == t:
                k = i - length + 2
                break
            i += d[elem]
    after = time.time()
    return k, after - before


def find_python(what):
    p, s = what, open(file_name, 'r').readline()
    before = time.time()
    res = s.find(p)
    after = time.time()
    return res, after - before


need_long = 'PANICAMALINSUKARIBADANHDFHFHHKKRKKLGLGLLGLLGLGLGLJKJKKJFKJKFJKJKJFKJFNVNNNNNVKJKJKFJDKJFKKJKVNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKFDFKJDJKFKDFJKDJKFJKDJFKKJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFKDJFKDJFKJDKCNCKDNKNDVNLDKJKLFKLDJFKLJDFKLJDLFJFKLPANICAMALINSUKARIBADANHDFHFHHKKRKKLGLGLLGLLGLGLGLJKJKKJFKJKFJKJKJFKJFNVNNNNNVKJKJKFJDKJFKKJKVNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKFDFKJDJKFKDFJKDJKFJKDJFKKJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFKDJFKDJFKJDKCNCKDNKNDVNLDKJKLFKLDJFKLJDFKLJDLFJFKLPANICAMALINSUKARIBADANHDFHFHHKKRKKLGLGLLGLLGLGLGLJKJKKJFKJKFJKJKJFKJFNVNNNNNVKJKJKFJDKJFKKJKVNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKFDFKJDJKFKDFJKDJKFJKDJFKKJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFKDJFKDJFKJDKCNCKDNKNDVNLDKJKLFKLDJFKLJDFKLJDLFJFKLPANICAMALINSUKARIBADANHDFHFHHKKRKKLGLGLLGLLGLGLGLJKJKKJFKJKFJKJKJFKJFNVNNNNNVKJKJKFJDKJFKKJKVNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKFDFKJDJKFKDFJKDJKFJKDJFKKJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFKDJFKDJFKJDKCNCKDNKNDVNLDKJKLFKLDJFKLJDFKLJDLFJFKLPANICAMALINSUKARIBADANHDFHFHHKKRKKLGLGLLGLLGLGLGLJKJKKJFKJKFJKJKJFKJFNVNNNNNVKJKJKFJDKJFKKJKVNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKFDFKJDJKFKDFJKDJKFJKDJFKKJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFKDJFKDJFKJDKCNCKDNKNDVNLDKJKLFKLDJFKLJDFKLJDLFJFKLPANICAMALINSUKARIBADANHDFHFHHKKRKKLGLGLLGLLGLGLGLJKJKKJFKJKFJKJKJFKJFNVNNNNNVKJKJKFJDKJFKKJKVNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKFDFKJDJKFKDFJKDJKFJKDJFKKJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFKDJFKDJFKJDKCNCKDNKNDVNLDKJKLFKLDJFKLJDFKLJDLFJFKLPANICAMALINSUKARIBADANHDFHFHHKKRKKLGLGLLGLLGLGLGLJKJKKJFKJKFJKJKJFKJFNVNNNNNVKJKJKFJDKJFKKJKVNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKFDFKJDJKFKDFJKDJKFJKDJFKKJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFKDJFKDJFKJDKCNCKDNKNDVNLDKJKLFKLDJFKLJDFKLJDLFJFKLPANICAMALINSUKARIBADANHDFHFHHKKRKKLGLGLLGLLGLGLGLJKJKKJFKJKFJKJKJFKJFNVNNNNNVKJKJKFJDKJFKKJKVNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKFDFKJDJKFKDFJKDJKFJKDJFKKJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFKDJFKDJFKJDKCNCKDNKNDVNLDKJKLFKLDJFKLJDFKLJDLFJFKLPANICAMALINSUKARIBADANHDFHFHHKKRKKLGLGLLGLLGLGLGLJKJKKJFKJKFJKJKJFKJFNVNNNNNVKJKJKFJDKJFKKJKVNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKFDFKJDJKFKDFJKDJKFJKDJFKKJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFKDJFKDJFKJDKCNCKDNKNDVNLDKJKLFKLDJFKLJDFKLJDLFJFKLPANICAMALINSUKARIBADANHDFHFHHKKRKKLGLGLLGLLGLGLGLJKJKKJFKJKFJKJKJFKJFNVNNNNNVKJKJKFJDKJFKKJKVNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKFDFKJDJKFKDFJKDJKFJKDJFKKJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFKDJFKDJFKJDKCNCKDNKNDVNLDKJKLFKLDJFKLJDFKLJDLFJFKL'
print('Длинна большой подстроки:', len(need_long))
need_short = 'PANICAMALINSUKARIBADANHDFHFHHKKRKKLGLGLLGLLGLGLGLJKJKKJFKJKFJ'
print('Длинна маленькой подстроки:', len(need_short))

print("Длинная")
print('БМ:', BM(need_long))
print('Встроенная:', find_python(need_long))
print('Короткая')
print('БМ:', BM(need_long))
print('Встроенная:', find_python(need_long))
