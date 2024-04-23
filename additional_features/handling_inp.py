def user_inp_opt(prompt, options):
    user_input = input(prompt)
    while user_input not in options:
        print("Invalid Input!")
        user_input = input(prompt)
    return user_input

def user_inp_data(prompt, datatype):
    while True:
        try:
            user_input = datatype(input(prompt).isdigit())
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    return user_input

