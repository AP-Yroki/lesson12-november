class Talking:

    def __init__(self, name):
        self.name = name
        self.number_yes = 0
        self.number_no = 0
        self.answer = True

    def to_answer(self):
        y = 'moore-moore'
        n = 'meow-meow'
        if self.answer:
            self.number_yes += 1
            self.answer = not self.answer
            return y
        else:
            self.number_no += 1
            self.answer = not self.answer
            return n


tk = Talking('Pussy')
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes} times, "no" {tk.number_no} times')
