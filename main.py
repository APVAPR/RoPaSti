class game():

    def __init__(self, *args):
        self.steps = args

    def available_moves(self):
        for n, step in enumerate(self.steps, 1):
            print(n, step)
        print(0, 'exit')
        print('?', 'help')

    def start_round(self):
        m = int(input('Enter your move'))

a = game('rock', 'paper', 'scissors')
a.available_moves()