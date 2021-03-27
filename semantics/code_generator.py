
class CodeGenerator:
    def __init__(self):
        self.text = []

    def append(self, line):
        self.text.append(str(line))

    def generate_code(self):
        return "".join(self.text)

    def write_to(self, filename):
        with open(filename, 'w') as f:
            f.write(self.generate_code())
