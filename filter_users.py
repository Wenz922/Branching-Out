import json


def filter_users_by_name(name):
    '''
    Filter users by name from a json file
    :param name: given user name
    '''
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No users found with name '{name}'.")


def filter_by_age(age):
    '''
    Filter users by age from a json file
    :param age: given age (int)
    '''
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if "age" in user and user["age"] == age]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No users found with age {age}.")


def filter_by_email(email):
    '''
    Filter users by email from a json file
    :param email: given email
    '''
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if "email" in user and user["email"].lower() == email.lower()]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No users found with email '{email}'.")


def main():
    filter_option = input("What would you like to filter by? (Currently, 'name', 'age', and 'email' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: "))
            filter_by_age(age_to_search)
        except ValueError:
            print("Invalid age entered. Please enter a number.")
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
