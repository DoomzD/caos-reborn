import os
import sys
from clint.textui import puts, colored

tests_path = os.path.join(os.path.split(os.path.realpath(sys.argv[0]))[0], "tests")
if not(os.path.exists(tests_path)):
    puts(colored.red(f"Path {tests_path} doesn't exist."))
    exit(0)

existing_tests = []
test_names = list(map(lambda x: x[:x.find('.')], filter(lambda x: x[x.find('.') + 1:] == 'dat', os.listdir(tests_path))))

class save_test:
    def __init__(self, data, ans, new=1):
        self.data = str(data)
        self.ans = str(ans)
        if new:
            self.do_it()
        else:
            existing_tests.append(self)

    def __eq__(self, other):
        if isinstance(other, save_test):
            return self.data == other.data and self.ans == other.ans
        return False

    def do_it(self):
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
        save_test(data, ans, 0)
read_tests()
