"""
Main program integer all the other file
"""
import webbrowser
from api_call import get_categorie, get_quote
from user_input import user_option

url_categorie = "https://api.chucknorris.io/jokes/categories"
url_random = "https://api.chucknorris.io/jokes/random"

# Call the API to get a list of valid category
cat_list = get_categorie(url_categorie)

while True:
    #get user best category
    choise = user_option(cat_list)

    if choise == len(cat_list):
        # in case the user choose Random
        quote = get_quote(url_random)
    else:
        # pass the category to the API request
        quote = get_quote(url_random, cat_list[choise])

    print(quote["value"])
    print(quote)
    webbrowser.open_new_tab(quote["url"])# open in a new tab, if possible
    input("Press a key to start over")
    print()