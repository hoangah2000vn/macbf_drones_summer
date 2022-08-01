import numpy as np
def init_obstacles(obstacles):
        """
        construct the array self.obstacle_points containing the coordinate of the obstacles
        array dimension (num_obstacles, 2)
        """
        obstacle_points = []
        for x1, y1, x2, y2 in obstacles:
            xrnd = np.linspace(x1, x2, int(abs(x1-x2) * 3))[:, np.newaxis] #xrnd.shape shape= (6,1)
            for r in np.linspace(0, 1, int(abs(y1-y2) * 3)): # r = 0, 0.2, 0.4, 0.6, 0.8, 1
                yrnd = np.ones_like(xrnd) * (r * y1 + (1-r) * y2)
                obstacle_points.append(np.concatenate([xrnd, yrnd], axis=1))
            
            yrnd = np.linspace(y1, y2, int(abs(y1-y2) * 3))[:, np.newaxis]
            for r in np.linspace(0, 1, int(abs(x1-x2) * 3)):
                xrnd = np.ones_like(yrnd) * (r * x1 + (1-r) * x2) # r = 0, 0.2, 0.4, 0.6, 0.8, 1
                obstacle_points.append(np.concatenate([xrnd, yrnd], axis=1))
        obstacle_points = np.concatenate(obstacle_points, axis=0)
        print(obstacle_points)

OBSTACLES = [[0, 4,  2, 6], # x1, y1, x2, y2
                 [4, 4,  6, 6],
                 [8, 4, 10, 6],
                                ]


def init_broadlines(area_size = 10):
        """
        not really sure what this does???
        """
        area_size = 10
        bx, by = [], []
        bx.append(np.linspace(-1, area_size + 1, int(area_size * 2)))
        by.append(-np.ones(int(area_size * 2)))
        bx.append(np.linspace(-1, area_size + 1, int(area_size * 2)))
        by.append(np.ones(int(area_size * 2)) + area_size)
        by.append(np.linspace(-1, area_size + 1, int(area_size * 2)))
        bx.append(-np.ones(int(area_size * 2)))
        by.append(np.linspace(-1, area_size + 1, int(area_size * 2)))
        bx.append(np.ones(int(area_size * 2)) + area_size)
        bx = np.concatenate(bx, axis=0)[:, np.newaxis]
        by = np.concatenate(by, axis=0)[:, np.newaxis]
        broadline_points = np.concatenate([bx, by], axis=1)
        print(broadline_points)
                                
if __name__ == '__main__':
    #init_obstacles(OBSTACLES)
    init_broadlines()