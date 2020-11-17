generator_text = """
import os
tests_path = os.path.join(os.path.split(__file__)[0], "tests")
existing_tests = []
test_names = list(map(lambda x: x[:x.find('.')], filter(lambda x: x[x.find('.') + 1:] == 'dat', os.listdir(tests_path))))

class Test:
    def __init__(self, data, ans, new=1):
        self.data = str(data)
        self.ans = str(ans)
        if new:
            self.save_test()
        else:
            existing_tests.append(self)

    def __eq__(self, other):
        if isinstance(other, Test):
            return self.data == other.data and self.ans == other.ans
        return False

    def save_test(self):
        if self not in existing_tests:
            existing_tests.append(self)
            for l in range(3, 10):
                for i in range(1, 1000):
                    name = (f"%{l}d" % i).replace(" ", "0")
                    if name not in test_names:
                        with open(tests_path + f"/{name}.dat", "w") as file:
                            file.write(self.data)
                        with open(tests_path + f"/{name}.ans", "w") as file:
                            file.write(self.ans)
                        test_names.append(name)
                        return 0


def read_tests():
    for input in test_names:
        with open(tests_path + f"/{input}.dat", "r") as file:
            data = file.read()
        with open(tests_path + f"/{input}.ans", "r") as file:
            ans = file.read()
        Test(data, ans, 0)
read_tests()

from random import randint
def generate_tests():
    #your code here


    Test(data, ans)

generate_tests()
"""
