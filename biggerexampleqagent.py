
import numpy as np


def mod(n, k):
    return ((n % k) + k) % k


def getPlayableActions(currentState, differentials, timestep):
    if currentState[2] == 0:
        x, y, s, a = currentState
        states = np.array([[(x, y, si, ai) for si in [0, 1]]
                          for ai in [mod(a - 1, 8), a, mod(a + 1, 8)]]).reshape((-1, 4))
        return states
    if currentState[2] == 1:
        x, y, s, a = currentState
        states = np.array([[(xi, yi, si, ai) for si in [0, 1]] for xi, yi, ai in [(x-1, y-1, 5), (x, y-1, 4), (x+1, y-1, 3),
                          (x-1, y, 6), (x+1, y, 2), (x-1, y+1, 7), (x, y+1, 0), (x+1, y+1, 1)]]).reshape((-1, 4))
        finalstates = np.empty((states.size(),), dtype=tuple)
        i = 0
        for st in states:
            x, y, s, a = st
            if x < 0 or x >= 5 or y < 0 or y >= 5 or (a != mod(currentState[3] - 1, 8) and a != currentState[3] and a != mod(currentState[3] + 1, 8)):
                continue
            finalstates[i] = st
            i += 1
        return finalstates


def getStateMatrix():
    return np.zeros((5, 5, 1, 8)), (1, 1, 1, 45)


if __name__ == "__main__":
    #print(getPlayableActions((1, 1, 0, 0), None, None))
    print(getPlayableActions((1, 1, 1, 1), None, None))
