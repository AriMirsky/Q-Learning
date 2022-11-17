import qagent as model
import numpy as np


def occupancyToReward(occupancyGrid):
    return -1/(1.0001 - occupancyGrid) + 1


if __name__ == "__main__":
    if False:
        qagent = model.QAgent(0.1, 0.9, np.zeros((9,)), 1)
        route = qagent.training(0, 8, 1000000)
        print(route)
    if True:
        occupancyGrid = np.array([[0, 0, 0.1, 0.9, 1],
                                  [0.2, 0, 0, 0, 0.8],
                                  [0.9, 0.7, 0.6, 0.1, 0.1],
                                  [0, 0.5, 0.2, 0.3, 0.1],
                                  [0, 0, 1, 0.8, 0]])
        qagent = model.QAgent(0.1, 0.9, occupancyToReward(occupancyGrid), 0.1)
        route = qagent.training((0, 0, 0, 0), (10, 10, 0, 0), 1000)
        print(route)
