import random
import time
from collections import deque
import heapq

def generate_maze_dfs(size):
    maze = [[1] * size for _ in range(size)]
    stack = [(1, 1)]
    maze[1][1] = 0

    while stack:
        x, y = stack[-1]
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < size-1 and 0 < ny < size-1 and maze[nx][ny] == 1:
                maze[nx][ny] = 0
                maze[x + dx//2][y + dy//2] = 0
                stack.append((nx, ny))
                break
        else:
            stack.pop()

    maze[size-2][size-2] = 0
    maze[size-2][size-3] = 0

    return maze

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def explore_all_paths_a_star(maze, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    
    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            tentative_g_score = g_score[current] + 1
            
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == 0:
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return []

def main():
    size = 60
    maze = generate_maze_dfs(size)
    
    start = (1, 1)
    end = (size-2, size-2)
    
    start_time = time.time()
    path = explore_all_paths_a_star(maze, start, end)
    end_time = time.time()
    
    if path:
        print("미로찾기 성공")
    else:
        print("미로찾기 실패")
    
    elapsed_time = (end_time - start_time) * 1000
    print(f"소요 시간: {elapsed_time:.4f} ms")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(1)
