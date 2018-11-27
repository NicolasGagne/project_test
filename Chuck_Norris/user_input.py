"""
File to handel all user interaction
"""

def user_option(list):
    """

    :param list:
        list = list of choise for the user.
    :return: x 'choise  index the user make'
    """
    option = str()
    for x, cat in enumerate(list):
        option = option + str(x + 1) + "-" +  cat + "; "

    option = option + str(len(list) + 1) + "- Random"
    print(option)

    while True:
        x = input('Select form choise above...')

        try:
            int(x)
            if int(x) > 0 & int(x) < len(list) + 1:
                break

        except ValueError:
            pass

    return int(x) - 1