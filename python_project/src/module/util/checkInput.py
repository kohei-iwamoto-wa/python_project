
class CheckInput:
     
    def __init__(self, value, check_type):
        self.value = value
        self.check_type = check_type

    def check_input_type(self):
        print(self.value, type(self.check_type))
        if isinstance(self.value, self.check_type):
            return True
        return False
