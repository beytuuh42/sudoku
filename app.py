from typing import List
from settings import *
from helper import *
import sys
import pygame


class PyRect:
    def __init__(self, window, colour, position, size, border=0) -> None:
        super().__init__()
        self.window = window
        self.colour = colour
        self.position = position
        self.size = size
        self.border = border

    def create_rect(self):
        self.rect = pygame.draw.rect(
            self.window, self.colour, (self.position, self.size), self.border)
        return self.rect


class Candidate(PyRect):
    def __init__(self, window, colour, position, size, border=0) -> None:
        super().__init__(window, colour, position, size, border=border)
        self.value: int = 0

    def _get_value(self):
        return self.__value

    def _set_value(self, value):
        if not isinstance(value, int):
            raise TypeError("bar must be set to an integer")
        self.__value = value
    value = property(_get_value, _set_value)


class Cell(PyRect):
    def __init__(self, window, colour, position, size, border=0) -> None:
        super().__init__(window, colour, position, size, border=border)

        self.value: int = 0
        self.is_selected = False
        self.candidates: List[Candidate] = []
        self.position_tuple = None
        self.text = None
        self.is_valid = True
        self.text_colour = BLACK
        self.block_no = None
        self.block: Block = None

    def create_candidate(self, candidate: Candidate):
        self.candidates.append(candidate)
        return candidate


class Block(PyRect):
    def __init__(self, window, colour, position, size, border=0) -> None:
        super().__init__(window, colour, position, size, border=border)

        self.cells: List[Cell] = []
        self.number = None
        self.position_tuple = None
        self.is_completed = False

    def create_cell(self, cell: Cell):
        cell.block_no = self.number
        cell.block = self
        self.cells.append(cell)
        return cell


class App:

    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        pygame.display.set_caption("Sudoku")

        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.blocks: List[Block] = []
        self.cells: List[Cell] = []
        self.candidates: List[Candidate] = []

        self.init_fields()
        self.init_board()

        self.selected_cell = None
        self.show_candidates = False
        self.show_validation = True
        self.is_running = True
        self.is_finished = False
        self.mouse_position = None

    def init_board(self):
        limit = len(BOARD)
        for x in range(limit):
            for y in range(limit):
                cell = self.cells[x*limit+y]
                cell.value = BOARD[y][x]
                cell.is_valid = True
        self.set_candidate_values()

    def set_candidate_values(self):
        can_values = [1, 4, 7,
                      2, 5, 8,
                      3, 6, 9]
        for cell in self.cells:
            for candidate, value in zip(cell.candidates, can_values):
                candidate.value = value if check_candidates(
                    cell.block, self.cells, cell, value) else 0

    def init_fields(self):
        limit = 3
        for idx, x in enumerate(range(limit)):
            for idy, y in enumerate(range(limit)):
                block = Block(self.window, BLACK, (GRID_POS[0]+(
                    BLOCK_WIDTH*x), GRID_POS[1]+(BLOCK_HEIGHT*y)), BLOCK_SIZE, 2)

                block.number = 1+idx + limit*idy
                block.position_tuple = (x, y)
                self.blocks.append(block)

        x_counter = 0

        for idx, x in enumerate(range(9)):
            y_counter = -1
            if idx % 3 == 0:
                x_counter += 1
            for idy, y in enumerate(range(9)):
                if idy % 3 == 0:
                    y_counter += 1
                block_no = x_counter + (y_counter*3)

                cell = next(b.create_cell(Cell(
                    self.window, GRAY, (GRID_POS[0]+(CELL_WIDTH*x), GRID_POS[1]+(CELL_HEIGHT*y)), CELL_SIZE, 1))
                    for b in self.blocks if b.number == block_no)

                cell.position_tuple = (x, y)
                self.cells.append(cell)

                for i in range(3):
                    for k in range(3):
                        candidate = cell.create_candidate(Candidate(self.window, WHITE, (GRID_POS[0]+(
                            CANDIDATE_WIDTH*i + CELL_WIDTH*x), GRID_POS[1]+(CANDIDATE_HEIGHT*k + CELL_HEIGHT*y)), CANDIDATE_SIZE, 1))
                        self.candidates.append(candidate)

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.is_running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

                if (is_int(event.unicode) and self.selected_cell):
                    is_valid = check_is_valid(self.selected_cell.block,
                                              self.cells, self.selected_cell, int(event.unicode))

                    self.selected_cell.is_valid = True if is_valid else False
                    self.selected_cell.text_colour = BLACK if self.selected_cell.is_valid else RED
                    self.selected_cell.value = int(event.unicode)

                    self.set_candidate_values()
                    if self.selected_cell.is_valid:
                        self.selected_cell.block.is_completed = True

                        for c in self.selected_cell.block.cells:
                            if not c.value:
                                self.selected_cell.block.is_completed = False
                                break
                        if check_is_finished(self.blocks):
                            print("You finished the game!")

                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    if self.selected_cell:
                        self.selected_cell.value = 0
                        self.set_candidate_values()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected_cell = None

                if event.button == 1:
                    if self.button_show_validation.collidepoint(self.mouse_position):
                        self.show_validation = not self.show_validation
                    elif self.button_show_candidates.collidepoint(self.mouse_position):
                        self.show_candidates = not self.show_candidates
                    elif self.button_show_hint.collidepoint(self.mouse_position):
                        show_hint_hidden_pair(self.blocks, self.cells)
                    else:
                        for c in self.cells:
                            c.is_selected = False
                            if c.rect.collidepoint(self.mouse_position):
                                self.selected_cell = c
                                self.selected_cell.is_selected = True

                        if self.show_candidates:
                            candidate = next((candidate for candidate in self.candidates if candidate.rect.collidepoint(
                                self.mouse_position)), None)

                            if candidate and candidate.value:
                                is_valid = check_is_valid(self.selected_cell.block,
                                                          self.cells, self.selected_cell, int(candidate.value))

                                self.selected_cell.is_valid = True if is_valid else False
                                self.selected_cell.text_colour = BLACK if self.selected_cell.is_valid else RED
                                self.selected_cell.value = candidate.value
                                candidate.value = 0
                                self.set_candidate_values()
                                if self.selected_cell.is_valid:
                                    self.selected_cell.block.is_completed = True

                                    for c in self.selected_cell.block.cells:
                                        if not c.value:
                                            self.selected_cell.block.is_completed = False
                                            break
                                    if check_is_finished(self.blocks):
                                        print("You finished the game!")

    def run(self):
        while self.is_running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def update(self):
        self.mouse_position = pygame.mouse.get_pos()

    def draw(self):
        self.draw_grid()
        self.draw_button()
        self.draw_numbers()
        pygame.display.flip()
        # display update einstellen dass board nur 1x geladen wird sowie bei drawbtn

    def draw_grid(self):
        self.window.fill(WHITE)
        if self.show_candidates:
            self.draw_candidates()
        self.draw_cell()
        self.draw_block()

        # pygame.display.update()

    def draw_block(self):
        [block.create_rect() for block in self.blocks]

    def draw_numbers(self):
        for cell in self.cells:
            if cell.value:
                cell.text = self.text_to_rect(
                    cell.rect, cell.value, CELL_HEIGHT*0.75, cell.text_colour, 20, 2)

    def draw_cell(self):
        for cell in self.cells:
            c = cell.create_rect()
            if c.collidepoint(pygame.mouse.get_pos()) or cell.is_selected:
                pygame.draw.rect(self.window, LIGHTBLUE,
                                 ((c.x, c.y), CELL_SIZE), 4)
            if cell.value:
                if self.show_candidates:
                    candidates = [
                        can for can in self.candidates if can.rect.colliderect(c)]
                    for can in candidates:
                        can.value = 0
                        can.colour = WHITE
            """else:
                if self.show_candidates:
                     candidates = [
                        can for can in self.candidates if can.rect.colliderect(c)]
                    test = [1, 4, 7,
                            2, 5, 8,
                            3, 6, 9]
                    for i, can in zip(test, candidates):
                        can.value = i
                        can.colour = WHITE """

    def draw_candidates(self):
        for candidate in self.candidates:
            can = candidate.create_rect()
            if candidate.value:
                self.text_to_rect(can, candidate.value,
                                  CANDIDATE_HEIGHT*.5, GRAY, 10, 2)

                if can.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(self.window, LIGHTBLUE,
                                     ((can.x, can.y), CANDIDATE_SIZE), 4)

    def draw_button(self):

        # button for candidate
        pygame.draw.rect(
            self.window, BLACK, (600, 40, 150, 30), width=5)
        self.button_show_candidates = pygame.draw.rect(
            self.window, GRAY, (600, 40, 150, 30), border_radius=1)
        self.text_to_rect(self.button_show_candidates,
                          "Toggle Candidates", 20, LIGHTBLUE)

        # button for validation
        pygame.draw.rect(
            self.window, BLACK, (600, 110, 150, 30), width=5)
        self.button_show_validation = pygame.draw.rect(
            self.window, GRAY, (600, 110, 150, 30), border_radius=1)
        self.text_to_rect(self.button_show_validation,
                          "Toggle Validation", 20, LIGHTBLUE)

        # button for hint
        pygame.draw.rect(
            self.window, BLACK, (600, 180, 150, 30), width=5)
        self.button_show_hint = pygame.draw.rect(
            self.window, GRAY, (600, 180, 150, 30), border_radius=1)
        self.text_to_rect(self.button_show_hint,
                          "Show hint", 20, LIGHTBLUE)

    def text_to_rect(self, rect, text, font_size, colour, offsetx=0, offsety=0):
        font_size = int(font_size)
        font_style = pygame.font.SysFont("arial", font_size)
        font = font_style.render(str(text), False, colour)

        self.window.blit(font, (rect.x + offsetx, rect.y + offsety))


if __name__ == "__main__":
    app = App()
    app.run()
