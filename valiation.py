class Validator:
    def is_integer(input_string):
        try:
            int(input_string)
            return True
        except ValueError:
            return False
        
    def input_integer(message):
        while True:
            user_input = input(message)
            if Validator.is_integer(user_input):
                return int(user_input)
            else: print("Enter a number")

    def validate_range(number, min_value, max_value):
        if number < min_value or number > max_value:
            raise ValueError("Число повинно бути в діапазоні від {} до {}".format(min_value, max_value))