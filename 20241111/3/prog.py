class Maze:
    def __init__(self, N):
        self.N = N
        self.hor_passages = [[False] * (N - 1) for _ in range(N)]
        self.ver_passages = [[False] * N for _ in range(N - 1)]

    def __str__(self):
        maze_str = ""
        maze_str += "█" * (2 * self.N + 1) + "\n"

        for j in range(self.N - 1, -1, -1):
            maze_str += "█"
            for i in range(self.N):
                maze_str += "·"
                if i < self.N - 1:
                    maze_str += "·" if self.ver_passages[i][j] else "█"
            maze_str += "█\n"
            if j > 0:
                maze_str += "█"
                for i in range(self.N):
                    maze_str += "·" if self.hor_passages[i][j - 1] else "█"
                    if i < self.N - 1:
                        maze_str += "█"
                maze_str += "█\n"
        maze_str += "█" * (2 * self.N + 1)
        return "\n".join(reversed(maze_str.split("\n")))

    def __setitem__(self, key, value):
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]
        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1)):
                self.hor_passages[x0][y] = (value == "·")
        elif y0 == y1:
            for x in range(min(x0, x1), max(x0, x1)):
                self.ver_passages[x][y0] = (value == "·")

    def __getitem__(self, key):
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]
        if (x0, y0) == (x1, y1):
            return True

        visited = set()
        queue = [(x0, y0)]

        while queue:
            x, y = queue.pop(0)
            if (x, y) == (x1, y1):
                return True
            visited.add((x, y))

            if x > 0 and self.ver_passages[x - 1][y] and (x - 1, y) not in visited:
                queue.append((x - 1, y))
            if x < self.N - 1 and self.ver_passages[x][y] and (x + 1, y) not in visited:
                queue.append((x + 1, y))
            if y > 0 and self.hor_passages[x][y - 1] and (x, y - 1) not in visited:
                queue.append((x, y - 1))
            if y < self.N - 1 and self.hor_passages[x][y] and (x, y + 1) not in visited:
                queue.append((x, y + 1))

        return False


import sys

exec(sys.stdin.read())
