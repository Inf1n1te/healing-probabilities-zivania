from discreteMarkovChain import markovChain

from chances import chances


class healing_probability(markovChain):
    def __init__(self, hp=0, successes=0, failures=0, painkiller_one=0, painkiller_two=(0, 0), fever_reducing=0,
                 max_hp=5, healer=(4, 2, 2), assistant_one=None, assistant_two=None, sterile=True,
                 probabilities=chances):
        super(healing_probability, self).__init__()
        self.max_hp = max_hp
        self.probabilities = probabilities
        self.sterile = sterile
        self.initialState = [hp, successes, failures, painkiller_one, painkiller_two, fever_reducing]
        self.assistant_two = assistant_two
        self.assistant_one = assistant_one
        self.healer = healer
        self.chances = chances(healer, assistant_one, assistant_two)

    def transition(self, state):
        probabilities = {}
        possible_states = [
            state,                                                                              #0
            [-self.max_hp, state[1], state[2], state[3], state[4], state[5]],                   #1
            [state[0] - 1, 0, 0, state[3], state[4], state[5]],                                 #2
            [state[0] - 1, 0, 0, state[3], state[4], state[5] - 1],                             #3

            [state[0] + 1, 0, state[2], state[3], state[4], state[5]],                          #4
            [state[0] + 1, 0, state[2], state[3] - 1, state[4], state[5]],                      #5
            [state[0] + 1, 0, state[2], state[3], state[4], state[5] - 1],                      #6
            [state[0] + 1, 0, state[2], state[3], (state[4][0] - 1, 2), state[5]],              #7

            [state[0], state[1] + 1, state[2], state[3], state[4], state[5]],                   #8
            [state[0], state[1] + 1, state[2], state[3], state[4], state[5] - 1],               #9
            [state[0], state[1] + 1, state[2], state[3], (state[4][0] - 1, 2), state[5]],       #10

            [state[0], state[1], state[2] + 1, state[3], state[4], state[5]],                   #11
            [state[0], state[1], state[2] + 1, state[3], state[4], state[5] - 1],               #12

            [state[0], state[1], state[2], state[3], (state[4][0], state[4][1] - 1), state[5]], #13
        ]
        for s in possible_states:
            probabilities[s] = 0
        if abs(state[0]) == self.max_hp: #todo almost everything
            probabilities[possible_states[0]] = 1
        elif self.sterile:
            if state[1] == 1:
                probabilities[possible_states[4]] += self.chances['white'] + self.chances['red']
            else:
        else:


mc = healing_probability()
mc.computePi()
mc.printPi()
