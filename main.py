import qagent as model
import numpy as np


def occupancyToReward(occupancyGrid):
    return np.repeat(np.repeat((-1/(1.000 - occupancyGrid) + 1)[:, :, np.newaxis], 2, axis=2)[:, :, :, np.newaxis], 8, axis=3)


if __name__ == "__main__":
    if False:  # exampleqagent.py
        qagent = model.QAgent(0.1, 0.9, np.zeros((9,)), 1)
        route = qagent.training(0, 8, 1000000)
        print(route)
    if True:  # biggerexampleqagent.py
        occupancyGrid = np.array([[0, 0, 0.1, 0.9, 1],
                                  [0.2, 0, 0, 0, 0.8],
                                  [0.9, 0.7, 0.6, 0.1, 0.1],
                                  [0, 0.5, 0.2, 0.3, 0.1],
                                  [0, 0, 1, 0.8, 0]])
        # print(occupancyToReward(occupancyGrid))
        qagent = model.QAgent(0.1, 0.9, occupancyToReward(occupancyGrid), 0.1)
        route = qagent.training((0, 4, 0, 3), (4, 0, 0, 3), 1000)
        print(route)
