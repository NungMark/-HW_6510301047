import os
import keyboard
import time

class pos:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

class maze:
    def __init__(self) -> None:
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", " ", " ", "X"],
            ["X", "X", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", " ", " ", "X", "X", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X"],
        ]
        self.ply = pos(6, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"

    def isInBound(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

    def print_maze(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col, " ", end="")
            print("")
        print("\n\n\n")

    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congratulation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")

    def move(self, next_move):
        self.maze[self.ply.y][self.ply.x] = " "
        self.maze[next_move.y][next_move.x] = "P"
        self.ply = next_move
        time.sleep(0.25)

    def move_up(self):
        next_move = pos(self.ply.y - 1, self.ply.x)
        if self.isInBound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] in [" ", "E"]:
            self.move(next_move)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_down(self):
        next_move = pos(self.ply.y + 1, self.ply.x)
        if self.isInBound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] in [" ", "E"]:
            self.move(next_move)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x - 1)
        if self.isInBound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] in [" ", "E"]:
            self.move(next_move)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x + 1)
        if self.isInBound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] in [" ", "E"]:
            self.move(next_move)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def find_shortest_path(self):
        start = (self.ply.y, self.ply.x)
        end = (self.end.y, self.end.x)
        queue = deque([(start, [])])
        visited = set([start])

        while queue:
            current, path = queue.popleft()

            if current == end:
                return path

            for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_pos = (current[0] + move[0], current[1] + move[1])

                if self.isInBound(*next_pos) and self.maze[next_pos[0]][next_pos[1]] in [" ", "E"] and next_pos not in visited:
                    queue.append((next_pos, path + [move]))
                    visited.add(next_pos)

    def auto_move(self, moves):
        for move in moves:
            if move == "up":
                if not self.move_up():
                    break
            elif move == "down":
                if not self.move_down():
                    break
            elif move == "left":
                if not self.move_left():
                    break
            elif move == "right":
                if not self.move_right():
                    break
            self.print_maze()

if __name__ == '__main__':
    m = maze()
    m.print_maze()

    # Automatic movement steps
    moves = ["up", "up", "right", "right", "up", "up", "up", "right", "right", "down", "right"]
    
    for move in moves:
        m.auto_move([move])
        time.sleep(0.5)

    while True:
        m.printEND()
        break
