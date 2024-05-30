# Exceptions

class ValueEmptyError(Exception):
    def __init__(self, field_name):
        self.field_name = field_name

    def __str__(self):
        return f"Field {self.field_name} must not be empty!"


class ValueNotStrError(Exception):
    def __init__(self, field_name):
        self.field_name = field_name

    def __str__(self):
        return f"Field {self.field_name} must be a string!"


class ValueNotNumError(Exception):
    def __init__(self, field_name):
        self.field_name = field_name

    def __str__(self):
        return f"Field {self.field_name} must be a number!"


class ValueTooLongError(Exception):
    def __init__(self, field_name, max_length):
        self.field_name = field_name
        self.max_length = max_length

    def __str__(self):
        return f"Field {self.field_name} must not exceed the length of {self.max_length}!"


class ValueNotFourDigitNumError(Exception):
    def __init__(self, field_name):
        self.field_name = field_name

    def __str__(self):
        return f"Field {self.field_name} must be a four-digit number!"


# Main functionalities

class FileHandler:
    def __init__(self, file_path, no_connectors, max_file_size):
        self.__file_path = self.__no_connectors = self.__max_file_size = None

        self.set_file_path(file_path)
        self.set_no_connectors(no_connectors)
        self.set_max_file_size(max_file_size)

    # Validators

    @staticmethod
    def validate_file_path(file_path):
        if not isinstance(file_path, str):
            raise ValueNotStrError("file_path")

        if file_path == "":
            raise ValueEmptyError("file_path")

    @staticmethod
    def validate_no_connectors(no_connectors):
        max_length = 10

        if not isinstance(no_connectors, int):
            raise ValueNotNumError("no_connectors")

        if no_connectors > max_length:
            raise ValueTooLongError("no_connectors", max_length)

    @staticmethod
    def validate_max_file_size(max_file_size):
        required_num_digits = 4

        if not isinstance(max_file_size, int):
            raise ValueNotNumError("max_file_size")

        if len(str(max_file_size)) != required_num_digits:
            raise ValueNotFourDigitNumError("max_file_size")

    # Getters and setters

    # File path
    def get_file_path(self):
        return self.__file_path

    def set_file_path(self, file_path):
        try:
            self.validate_file_path(file_path)
        except ValueNotStrError as e:
            print(e)
        except ValueEmptyError as e:
            print(e)
        else:
            self.__file_path = file_path

    # No connectors
    def get_no_connectors(self):
        return self.__no_connectors

    def set_no_connectors(self, no_connectors):
        try:
            self.validate_no_connectors(no_connectors)
        except ValueNotNumError as e:
            print(e)
        except ValueTooLongError as e:
            print(e)
        else:
            self.__no_connectors = no_connectors

    # Max file size
    def get_max_file_size(self):
        return self.__max_file_size

    def set_max_file_size(self, max_file_size):
        try:
            self.validate_max_file_size(max_file_size)
        except ValueNotNumError as e:
            print(e)
        except ValueNotFourDigitNumError as e:
            print(e)
        else:
            self.__max_file_size = max_file_size

    # Methods

    def read_content(self):
        print("--- Poniżej znajduje się zawartość pliku ---")

        with open(self.get_file_path(), "r") as file:
            content = file.read()

            print(content)

        print("--- Koniec zawartości ---")

    def save_to_file(self, content):

        with open(self.get_file_path(), "a") as file:
            file.write(f"\n{content}")

        print("Pomyślnie dodano zawartość do pliku")


def main():
    file_handler_1 = FileHandler("test.txt", 7, 4096)
    # file_handler_1.save_to_file("hello world 4")


if __name__ == "__main__":
    main()
