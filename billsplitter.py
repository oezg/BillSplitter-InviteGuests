import random


def invalid():
    print("No one is joining for the party")


try:
    num_friends = int(input("Enter the number of friends joining (including you):\n"))
    assert num_friends > 0, "No one is joining for the party"
except ValueError:
    print("No one is joining for the party")
except AssertionError as err:
    print(err)
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = [input() for _ in range(num_friends)]
    bill = int(input("Enter the total bill value:\n"))
    if "Yes" == input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n'):
        lucky = random.choice(friends)
        friends.remove(lucky)
        if friends:
            friends_share = dict.fromkeys(friends, round(bill/len(friends), 2))
            friends_share.update({lucky: 0})
        else:
            print("You do not have any friends.")
        print(lucky, "is the lucky one!")
    else:
        print("No one is going to be lucky")
        friends_share = dict.fromkeys(friends, round(bill/num_friends, 2))
    print(friends_share)
