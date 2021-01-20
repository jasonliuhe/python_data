# d = {'key1': 'value', 'key2': 123}
# print(d['key1'])
# print(d['key2'])
# d = {'k1': [1, 2, 3]}
# print(d['k1'])
# print(d['k1'][0])
# d = {'k1': {'innerkey': [1, 2, 3]}}
# print(d['k1'])
# print(d['k1']['innerkey'][1])

# my_list = [1, 2, 3]
# print(my_list[0])
# t = (1, 2, 3)
# print(t[0])
# my_list[0] = 'NEW'
# print(my_list[0])
# t[0] = 'NEW'
# print(t[0])

# if 1 < 2:
#     print(1)

# seq = [1, 2, 3, 4, 5]
# for item in seq:
#     print(item)
#
# def times2(var):
#     return var * 2
#
#
# seq = [1, 2, 3, 4, 5]
# print(list(map(lambda var: var * 3, seq)))
#
# print(list(filter(lambda num: num % 2 == 0, seq)))
#
# s = 'hello my name is Sam'
# print(s.lower())
# tweet = 'Go Sports! #Sports'
# print(tweet.split('#'))
#
# d = {'k1': 1, 'k2': 2}
# print(d.keys())
# print(d.values())
# lst = [1, 2, 3]
# print(lst.pop())
# print(lst.pop())
# print('x' in [1, 2, 'x'])
# x = [(1, 2), (3, 4), (5, 6)]
# print(x[0][0])
# for (a, b) in x:
#     print(b)


# s = "Hi there Sam!"
# print(s.split(" "))
planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet, diameter))


def domainGet(var):
    return list(var.split("@"))[1]


print(domainGet('saldfj@user.com'))


def findDog(var):
    if "dog" in var.lower():
        return True
    else:
        return False


print(findDog("saldfjdo"))


def coundDog(var):
    return len(var.split('dog')) - 1


print(coundDog('This dog runs faster than the other dog dude!'))


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed - 5
    if speed <= 60:
        return 'No Ticket'
    elif speed <= 80:
        return 'Small Ticket'
    else:
        return 'Big Ticket'


print(caught_speeding(81, True))
print(caught_speeding(81, False))
