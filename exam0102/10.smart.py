class electronics:
    def __init__(self):
        print("electronics")

class mobiledevice(electronics):
    def __init__(self):
        super().__init__()
        print("mobile device is electonic")

class smartphone(mobiledevice):
    def __init__(self):
        super().__init__()
        print("smart phone is mobile")

s=smartphone()
