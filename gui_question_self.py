import math

import pygame
from sudoku_solver import solve_board, valid, print_board
import time
from sudoku_board_generator import random_board_generator
from sudoku_question_classes import Grid
pygame.font.init()


def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def question(n):
    win = pygame.display.set_mode((60*n,60*(n+1)))
    pygame.display.set_caption("Sudoku")
    board = Grid(n,n,50,50,n)
    txt = None
    run = True
    start = time.time()
    strikes = 0
    while run:
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if txt is None:
                        txt = "1"
                    else:
                        txt += "1"
                if event.key == pygame.K_2:
                    if txt is None:
                        txt = "2"
                    else:
                        txt += "2"
                if event.key == pygame.K_3:
                    if txt is None:
                        txt = "3"
                    else:
                        txt += "3"
                if event.key == pygame.K_4:
                    if txt is None:
                        txt = "4"
                    else:
                        txt += "4"
                if event.key == pygame.K_5:
                    if txt is None:
                        txt = "5"
                    else:
                        txt += "5"
                if event.key == pygame.K_6:
                    if txt is None:
                        txt = "6"
                    else:
                        txt += "6"
                if event.key == pygame.K_7:
                    if txt is None:
                        txt = "7"
                    else:
                        txt += "7"
                if event.key == pygame.K_8:
                    if txt is None:
                        txt = "8"
                    else:
                        txt += "8"
                if event.key == pygame.K_9:
                    if txt is None:
                        txt = "9"
                    else:
                        txt += "9"
                if event.key == pygame.K_DELETE:
                    board.clear_cell()
                    txt = None
                if event.key == pygame.K_BACKSPACE:
                    if txt is None:
                        pass
                    elif len(txt) > 1:
                        txt = txt[0:-1]
                    else:
                        board.clear_cell()
                        txt = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected_pos
                    if board.cells[i][j].tmp != 0 and board.cells[i][j].tmp <= n:
                        if board.set_val(board.cells[i][j].tmp):
                            print("Success")
                        else:
                            print("Wrong")
                            board.clear_cell()
                            strikes += 1
                        txt = None

                        if board.is_complete():
                            print("Game over")
                            run = False
                    else:
                        print("Wrong")
                        board.clear_cell()
                        strikes += 1
                        txt = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click_cell(pos)
                if clicked:
                    board.selected(clicked[0], clicked[1])
                    txt = None

        if board.selected and txt != None:
            board.set_tmp(int(txt))

        win.fill((255, 255, 255))
        fnt = pygame.font.SysFont("comicsans", 40)
        text = fnt.render("Time: " + format_time(play_time), 1, (0, 0, 0))
        win.blit(text, (60*n - 160, 60*n+20))
        text = fnt.render("X " * strikes, 1, (255, 0, 0))
        win.blit(text, (20, 60*n+20))
        board.draw(win)
        pygame.display.update()


question(16)
pygame.quit()