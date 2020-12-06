from textwrap import dedent


apps = {
    'wings': 0,
    'cookies': 0,
    'spring rolls': 0,
    'salmon': 0,
    'steak': 0,
    'meat tornado': 0,
    'a literal garden': 0,
    'ice cream': 0,
    'cake': 0,
    'pie': 0,
    'coffee': 0,
    'tea': 0,
    'unicorn tears': 0,
}


def snakes():



    appstring = """
    **************************************
    **  Welcome to the Snakes Cafe! **
    **  Please see our menu below.  **
    **
    **To quit at any time, type "quit"**
    **************************************
    

    Appetizers
    ----------
    Wings
    Cookies
    SpringRolls

    Entrees
    ----------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden 

    Desserts
    ----------
    Ice Cream
    Cake
    Pie

    Drinks
    ----------
    Coffee
    Tea
    Unicorn Tears
    """


    print(appstring)



    message = """
    ***********************************
    **  What would you like to order? ** 
    ***********************************
    """

    userorder(message)


def userorder(message=''):


    dedent(message)


    user_input = input(message).lower()

    if user_input == 'quit':
        pass
    else:
      while user_input not in apps.keys():
        message = dedent("""
        Thats not on the menu please choose an item on the menu!!!
        """)
        user_input = input(message).lower()
      apps[user_input] += 1

      print(f"{apps[user_input]} order of %s has been added to your meal" % user_input)

      userorder()


if __name__ == '__main__':
    snakes()