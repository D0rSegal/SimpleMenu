class InvalidMenuInput(Exception):
    """
    Raised when the user enters a wrong menu command
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"{self.message} is not a valid input, please select again"
