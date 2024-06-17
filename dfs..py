import random
import time

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

def explore_all_paths(maze, start, end, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
        visited.add(start)

    if start == end:
        return [path]

    paths = []
    x, y = start
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) not in visited:
            new_path = path + [(nx, ny)]
            visited.add((nx, ny))
            paths.extend(explore_all_paths(maze, (nx, ny), end, new_path, visited))
            visited.remove((nx, ny))
    
    return paths

def main():
    size = 60
    maze = generate_maze_dfs(size)
    
    start = (1, 1)
    end = (size-2, size-2)
    
    start_time = time.time()
    all_paths = explore_all_paths(maze, start, end)
    end_time = time.time()
    
    if all_paths:
        print("미로찾기 성공")
    else:
        print("미로찾기 실패")
    
    elapsed_time = (end_time - start_time) * 1000
    print(f"소요 시간: {elapsed_time:.4f} ms")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(1)
