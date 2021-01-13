class IntcodeComputer:
    def __init__(self, instructions):
        self.instructions = [int(x) for x in instructions]

    def run(self):
        x = 0

        while True:
            input1 = self.instructions[x + 1]
            input2 = self.instructions[x + 2]
            output = self.instructions[x + 3]

            if(self.instructions[x] == 1):                
                total = self.instructions[input1] + self.instructions[input2]
                self.instructions[output] = total
            if(self.instructions[x] == 2):
                product = self.instructions[input1] * self.instructions[input2]
                self.instructions[output] = product
            if(self.instructions[x] == 99):
                return
            x += 4