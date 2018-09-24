

from tsa_waiver. tsa_website import login_tsa_website, create_new_waiver, create_list_input

if __name__ == "__main__":

    session = login_tsa_website()
    create_list_input(session)
    #create_new_waiver(session)
