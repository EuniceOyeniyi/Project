import random

def angry():
    random_list =["Reggae","metal music"]

    list_count = len(random_list)
    random_item = random.randrange(list_count)
    return random_list[random_item]


def calm():
    calm_list =['classical music', 'country music','blues']

    list_count = len(calm_list)
    calm_item = random.randrange(list_count)
    return calm_list[calm_item]

def sad():
    sad_list = ['pop music','jazz music']
    list_count = len(sad_list)
    sad_item = random.randrange(list_count)
    return sad_list[sad_item]


def happy():
    happy_list = ['best disco dance songs']
    list_count = len(happy_list)
    happy_item = random.randrange(list_count)
    return happy_list[happy_item]


def morning_song():
    morning_list = ['classical ', 'blues','heavy metal',]
    pass
def afternoon_song():
    afternoon_list = ['hip-hop','jazz music']
    pass
def evening_song():
    pass
