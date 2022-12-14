import numpy as np
#from HardToWriteFunctions import getPlayableActions, getStateMatrix
from exampleqagent import getPlayableActions, getStateMatrix


class QAgent():
    def getRandomState(self):
        result = []
        for i in range(len(self.q.shape)):
            result.append(np.random.randint(0, high=self.q.shape[i]))
        return tuple(result)

    def set_up_rewards(self, end_state):
        rewards_new = np.copy(self.rewards)

        # Set goal to be very high reward
        rewards_new[end_state] = 999

        return rewards_new

    def qlearning(self, rewards_new, iterations, end_state):
        for _ in range(iterations):
            current_state = self.getRandomState()
            if current_state == end_state:
                continue
            playable_actions = getPlayableActions(
                current_state, self.differentials, self.dt)
            temporal_difference = rewards_new[current_state] + self.gamma * \
                np.amax(self.q[playable_actions]) - \
                self.q[current_state]
            self.q[current_state] += self.alpha * \
                temporal_difference

    def get_optimal_route(self, start_state, end_state):
        route = [start_state]
        next_state = start_state
        while next_state != end_state:
            playable_actions = getPlayableActions(
                next_state, self.differentials, self.dt)
            t1 = self.q[playable_actions]
            t2 = np.argmax(self.q[playable_actions])
            t3 = playable_actions[0]
            next_state = playable_actions[0][np.argmax(
                self.q[playable_actions])]
            route.append(next_state)

        return route

    def training(self, start_state, end_state, iterations):
        rewards_new = self.set_up_rewards(end_state)
        self.qlearning(rewards_new, iterations, end_state)
        print(self.q.reshape((3, 3)))
        route = self.get_optimal_route(start_state, end_state)
        return route

    def __init__(self, alpha, gamma, rewards, dt):
        self.gamma = gamma
        self.alpha = alpha
        self.rewards = rewards
        self.q, self.differentials = getStateMatrix()
        self.dt = dt
