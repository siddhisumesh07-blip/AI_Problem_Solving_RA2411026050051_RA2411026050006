import tkinter as tk
from tkinter import messagebox
import time
from collections import deque

# --- PROBLEM 1: TIC-TAC-TOE LOGIC ---
class TicTacToeAI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Problem 1: Tic-Tac-Toe AI")
        self.board = [' ' for _ in range(9)]
        self.buttons = []
        self.nodes_explored = 0
        self.setup_ui()

    def setup_ui(self):
        for i in range(9):
            btn = tk.Button(self.window, text=' ', font=('Arial', 20), width=5, height=2,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def check_winner(self, b):
        lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for line in lines:
            if b[line[0]] == b[line[1]] == b[line[2]] != ' ': return b[line[0]]
        return 'Tie' if ' ' not in b else None

    def minimax(self, b, is_max, alpha, beta, use_pruning):
        self.nodes_explored += 1
        res = self.check_winner(b)
        if res == 'O': return 10
        if res == 'X': return -10
        if res == 'Tie': return 0

        best = -float('inf') if is_max else float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O' if is_max else 'X'
                val = self.minimax(b, not is_max, alpha, beta, use_pruning)
                b[i] = ' '
                if is_max:
                    best = max(best, val)
                    if use_pruning:
                        alpha = max(alpha, val)
                        if beta <= alpha: break
                else:
                    best = min(best, val)
                    if use_pruning:
                        beta = min(beta, val)
                        if beta <= alpha: break
        return best

    def make_move(self, i):
        if self.board[i] == ' ':
            self.board[i] = 'X'
            self.buttons[i].config(text='X', state='disabled', disabledforeground="blue")
            if not self.is_over(): self.ai_turn()

    def ai_turn(self):
        # Mandatory Requirement: Compare Performance
        self.nodes_explored = 0
        start = time.time()
        self.minimax(self.board, True, -100, 100, False) 
        m_nodes = self.nodes_explored
        m_time = time.time() - start

        self.nodes_explored = 0
        start_ab = time.time()
        best_val, move = -float('inf'), -1
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                val = self.minimax(self.board, False, -float('inf'), float('inf'), True)
                self.board[i] = ' '
                if val > best_val:
                    best_val, move = val, i
        
        print(f"\n--- AI Turn Performance Comparison ---")
        print(f"Minimax (Standard): {m_nodes} nodes, {m_time:.5f}s")
        print(f"Alpha-Beta Pruning: {self.nodes_explored} nodes, {time.time()-start_ab:.5f}s")

        self.board[move] = 'O'
        self.buttons[move].config(text='O', state='disabled', disabledforeground="red")
        self.is_over()

    def is_over(self):
        res = self.check_winner(self.board)
        if res:
            messagebox.showinfo("Game Over", "Tie!" if res == 'Tie' else f"{res} wins!")
            self.window.destroy()
            return True
        return False

# --- PROBLEM 8: SMART NAVIGATION ---
def smart_navigation():
    print("\n--- Problem 8: Smart Navigation System ---")
    graph = {}
    try:
        edges = int(input("Enter number of connections: "))
        for _ in range(edges):
            u, v = input("Connection (e.g., A B): ").split()
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        start, goal = input("Enter Start and Goal Node (e.g., A D): ").split()

        def search(is_bfs):
            q = deque([(start, [start])]) if is_bfs else [(start, [start])]
            vis, count = set(), 0
            while q:
                curr, path = q.popleft() if is_bfs else q.pop()
                count += 1
                if curr == goal: return path, count
                if curr not in vis:
                    vis.add(curr)
                    for n in graph.get(curr, []):
                        if n not in vis: q.append((n, path + [n]))
            return None, count

        b_p, b_c = search(True)
        d_p, d_c = search(False)
        print(f"\nBFS Result (Optimal Path): {b_p} | Nodes Explored: {b_c}")
        print(f"DFS Result (Non-Optimal): {d_p} | Nodes Explored: {d_c}")
    except Exception as e:
        print(f"Input Error: {e}. Please try again.")

# --- MEMBER 1 MENU ---
if __name__ == "__main__":
    while True:
        print("\n===== MEMBER 1: AI PROJECTS =====")
        print("1. Problem 1: Tic-Tac-Toe AI (GUI)")
        print("2. Problem 8: Smart Navigation (BFS vs DFS)")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            print("Launching Tic-Tac-Toe GUI...")
            game = TicTacToeAI()
            game.window.mainloop()
        elif choice == '2':
            smart_navigation()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")
