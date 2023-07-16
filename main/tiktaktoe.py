import tkinter as tk
from tkinter import messagebox

def check_win(b):
    for r in b:
        if len(set(r)) == 1 and r[0] != " ":
            return r[0]

    for c in range(3):
        if len(set([b[r][c] for r in range(3)])) == 1 and b[0][c] != " ":
            return b[0][c]

    if len(set([b[i][i] for i in range(3)])) == 1 and b[0][0] != " ":
        return b[0][0]
    if len(set([b[i][2-i] for i in range(3)])) == 1 and b[0][2] != " ":
        return b[0][2]

    return None

def check_tie(b):
    for r in b:
        if " " in r:
            return False
    return True

def minimax(b, d, m):
    w = check_win(b)
    if w:
        return -1 if w == "X" else 1
    elif check_tie(b):
        return 0

    if m:
        max_e = float("-inf")
        for r in range(3):
            for c in range(3):
                if b[r][c] == " ":
                    b[r][c] = "O"
                    e = minimax(b, d + 1, False)
                    b[r][c] = " "
                    max_e = max(max_e, e)
        return max_e
    else:
        min_e = float("inf")
        for r in range(3):
            for c in range(3):
                if b[r][c] == " ":
                    b[r][c] = "X"
                    e = minimax(b, d + 1, True)
                    b[r][c] = " "
                    min_e = min(min_e, e)
        return min_e

def ai_move(b):
    best_s = float("-inf")
    best_m = None

    for r in range(3):
        for c in range(3):
            if b[r][c] == " ":
                b[r][c] = "O"
                s = minimax(b, 0, False)
                b[r][c] = " "
                if s > best_s:
                    best_s = s
                    best_m = (r, c)

    r, c = best_m
    b[r][c] = "O"
    buttons[r][c].config(text="O", state="disabled")
    
    w = check_win(b)
    if w:
        messagebox.showinfo("", f"Player {w} wins!")
        reset_game()
    elif check_tie(b):
        messagebox.showinfo("", "It's a tie!")
        reset_game()

def button_click(r, c):
    if board[r][c] == " ":
        buttons[r][c].config(text="X", state="disabled")
        board[r][c] = "X"
        
        w = check_win(board)
        if w:
            messagebox.showinfo("", f"Player {w} wins!")
            reset_game()
        elif check_tie(board):
            messagebox.showinfo("", "It's a tie!")
            reset_game()
        else:
            ai_move(board)

def reset_game():
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text=" ", state="normal")
            board[r][c] = " "

window = tk.Tk()
window.title("Tic Tac Toe")

board = [[" " for _ in range(3)] for _ in range(3)]
buttons = []

for r in range(3):
    button_row = []
    for c in range(3):
        button = tk.Button(window, text=" ", font=("Arial", 24), width=5, height=2,
                           command=lambda r=r, c=c: button_click(r, c))
        button.grid(row=r, column=c, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

window.mainloop()
