class My_Dict(dict):
    def __init__(self, new_dict):
        super().__init__()
        self.dict = new_dict

    def get(self, key):
        if key not in self.dict:
            return 0
        else:
            return self.dict[key]


my_dict = My_Dict({1: 1, 2: 2})

print(my_dict.get(3))
mydict = {1: 1, 2: 2}
print(mydict.get(3))