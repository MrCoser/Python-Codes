from turtle import width
from Tkinter import Frame, Label, CENTER

import Logics
import Constants as c


class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<key>", self.key_down)
        self.commands = {c.KEY_UP: Logics.move_up,  c.KEY_DOWN:  Logics.move_down,
                         c.KEY_LEFT:  Logics.move_left,   c.KEY_RIGHT:  Logics.move_right}

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()


    def init_grid(self):
        background = Frame(self, bg = c.BACKGROUND_COLOR_GAME, width = c.SIZE, height = c.SIZE)
        background.grid()


        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame( background, bg = c.BACKGROUND_COLOR_CELL_EMPTY,
                              width = c.SIZE / c.GRID_LEN, height = c.SIZE / c.GRID_LEN)

                cell.grid(row = i, column = j, pad_x = c.GRID_PADDING, pad_y = c.GRID_PADDING)
                t = Label( master = cell, text = "", bg = c.BACKGROUND_COLOR_CELL_EMPTY, 
                           justify = CENTER, font = c.FONT, width = 5, height = 2) 

                t.grid()
                grid_row.append(t)

        self.grid_cells.append(grid_row)

    
    def init_matrix(self):
        self.matrix = Logics.start_game()
        Logics.add_new_2(self.matrix)
        Logics.add_new_2(self.matrix)


    def update_grid_cells(self):

        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):

                newnum = self.matrix[i][j]
                if (newnum == 0):

                    self.grid_cells[i][j].configure(
                        text = "", bg = c.BACKGROUND_COLOR_CELL_EMPTY)
                        
                else:
                    
                    self.grid_cells[i][j].configure(
                        text = str(newnum), bg = c.BACKGROUND_COLOR_DICT[newnum],  fg = c.CELL_COLOR_DICT[newnum])


        self.update_idletasks()    # Function to take time delay into account, while changing
                                   # fg, bg or text of the grid in matrix


    def key_down(self, event):
        key = repr(event.char)

        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                Logics.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False

                if Logics.current_state(self.matrix) == 'YOU WIN':
                    self.grid_cells[1][1].configure(text = "YOU", bg = c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text = "WIN!!!", bg = c.BACKGROUND_COLOR_CELL_EMPTY)

                if Logics.current_state(self.matrix) == 'YOU LOSE':
                    self.grid_cells[1][1].configure(text = "YOU", bg = c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text = "LOSE!!!", bg = c.BACKGROUND_COLOR_CELL_EMPTY)

game = Game2048()