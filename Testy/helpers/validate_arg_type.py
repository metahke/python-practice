def validate_arg_type(arg_type):
    def check(func):
        def validate_args(arg):
            if not isinstance(arg, arg_type) or type(arg) is not arg_type:
                return "Invalid argument passed to the function."

            return func(arg)

        return validate_args

    return check
