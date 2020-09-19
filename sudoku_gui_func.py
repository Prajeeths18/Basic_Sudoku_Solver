import pygame
from sudoku_solver import solve_board,print_board
import sudoku_classes
from sudoku_classes import SubmitBox,InputBox,TextBox,TripleBox,FONT
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
start_x,start_y = 50, 50


def re_init():
    boa = []
    for i in range(9):
        z = []
        for j in range(9):
            z.append(0)
        boa.append(z)
    return boa


def input_page():
    board = []
    for i in range(9):
        z = []
        for j in range(9):
            z.append(0)
        board.append(z)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    submit_box = SubmitBox(200, 525, 100, 50)
    input_boxes = []
    border_boxes = []
    for i in range(9):
        z = []
        for j in range(9):
            z.append(InputBox(50 + 50 * i, 50 + 50 * j, 50, 50, i, j,board))
        input_boxes.append(z)
    done = False
    for i in range(3):
        w = []
        for j in range(3):
            w.append(TripleBox(50 + 150 * i, 50 + 150 * j, 150, 150))
        border_boxes.append(w)
    z=0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                z = 1
                pygame.display.quit()
                return
            for box_row in input_boxes:
                for box in box_row:
                    box.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if submit_box.rect.collidepoint(event.pos):
                    done = True
        for box_row in input_boxes:
            for box in box_row:
                box.update()

        screen.fill((30, 30, 30))
        for box_row in input_boxes:
            for box in box_row:
                box.draw(screen)
        for border_row in border_boxes:
            for border in border_row:
                border.draw(screen)

        submit_box.draw(screen)
        pygame.display.flip()
        clock.tick(30)
    for i in range(9):
        for j in range(9):
            if input_boxes[i][j].text in ['1','2','3','4','5','6','7','8','9']:
                board[i][j]=int(input_boxes[i][j].text)
            else:
                board[i][j]=0
    if z == 0:
        solve_board(board)
        pygame.display.quit()
        out_page(board)
    if z == 1:
        pygame.display.quit()
        return


def out_page(boa):
    done=False
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    revert_box = SubmitBox(150, 525, 100, 50,"Revert")
    end_box=SubmitBox(250,525,100,50,"End")
    text_boxes = []
    border_boxes = []
    for i in range(9):
        y = []
        for j in range(9):
            y.append(TextBox(50 + 50 * i, 50 + 50 * j, 50, 50))
        text_boxes.append(y)
    for i in range(3):
        w = []
        for j in range(3):
            w.append(TripleBox(50 + 150 * i, 50 + 150 * j, 150, 150))
        border_boxes.append(w)
    for i in range(9):
        for j in range(9):
            text_boxes[i][j].text = str(boa[i][j])
            text_boxes[i][j].txt_surface = FONT.render(text_boxes[i][j].text, True, text_boxes[i][j].color)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if revert_box.rect.collidepoint(event.pos):
                    pygame.display.quit()
                    input_page()
                if end_box.rect.collidepoint(event.pos):
                    pygame.quit()
                    return
        screen.fill((30, 30, 30))
        for box_row in text_boxes:
            for box in box_row:
                box.draw(screen)
        for border_row in border_boxes:
            for border in border_row:
                border.draw(screen)
        revert_box.draw(screen)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    return
