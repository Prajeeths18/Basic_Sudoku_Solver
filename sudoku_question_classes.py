import pygame
from sudoku_solver import solve_board,print_board,valid
from sudoku_board_generator import random_board_generator
import math
pygame.font.init()
N=9
N_row = 9
N_col = 9
WIDTH = 540
HEIGHT = 540


class Cell:

    def __init__(self, val, i, j, w, h,n):
        self.value = val
        self.tmp = 0
        self.i = i
        self.j = j
        self.w = w
        self.h = h
        self.active = False
        self.n = n

    def draw(self, screen):
        font = pygame.font.SysFont('comicsans',40)
        step = self.w / self.n
        x, y = step * self.i, step * self.j
        if self.tmp != 0 and self.value == 0:
            txt_surf = font.render(str(self.tmp),True,(128,128,128))
            screen.blit(txt_surf,
                        (x + (step / 2 - txt_surf.get_width() / 2), y + (step / 2 - txt_surf.get_width() / 2)))
        elif self.value != 0:
            txt_surf = font.render(str(self.value),True,(0, 0, 0))
            screen.blit(txt_surf,
                        (x + (step / 2 - txt_surf.get_width() / 2), y + (step / 2 - txt_surf.get_width() / 2)))

        if self.active:
            pygame.draw.rect(screen,(255, 255, 0),(x, y, step, step), 3)


class Grid:
    board = random_board_generator(N)

    def __init__(self, rows = N_row, cols = N_col, width = WIDTH, height=HEIGHT,n = N):
        self.board = random_board_generator(n)
        self.rows = rows
        self.cols = cols
        self.w = rows*60
        self.h = cols*60
        self.cells = [[Cell(self.board[i][j],i,j,self.w,self.h,n) for j in range(cols)] for i in range(rows)]
        self.selected_pos = None
        self.n = n

    def set_board(self):
        self.board = [[self.cells[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def set_val(self,val):
        i,j = self.selected_pos
        if self.board[i][j] == 0:
            self.cells[i][j].value = val
            self.set_board()
            if valid(self.board,i,j, val) and solve_board(self.board):
                return True
            else:
                self.cells[i][j].value =  0
                self.cells[i][j].tmp = 0
                self.board = self.board
                self.set_board()
                return False

    def set_tmp(self,val):
        i, j = self.selected_pos
        self.cells[i][j].tmp = val

    def draw(self,screen):
        step = self.w / self.n
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, self.h), 1)
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (self.w, 0), 1)
        w = int(math.sqrt(self.n))
        for i in range(1,self.rows+1):
            if i % w == 0:
                width = 4
            else:
                width = 1
            pygame.draw.line(screen, (0, 0, 0), (0, i * step), (self.w, i * step), width)
            pygame.draw.line(screen, (0, 0, 0), (i * step, 0), (i * step, self.h), width)
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(screen)

    def selected(self, i, j):
        for m in range(self.rows):
            for n in range(self.cols):
                self.cells[m][n].active = False
        self.cells[i][j].active = True
        self.selected_pos = (i,j)

    def clear_cell(self):
        i, j = self.selected_pos
        if self.cells[i][j].value == 0:
            self.cells[i][j].tmp = 0

    def click_cell(self,pos):
        if pos[0] < self.w and pos[1] < self.h:
            step = self.w / self.n
            return int(pos[0]//step),int(pos[1]//step)
        else:
            return None

    def is_complete(self):
        for m in range(self.rows):
            for n in range(self.cols):
                if self.cells[m][n].value == 0:
                    return False
        return True