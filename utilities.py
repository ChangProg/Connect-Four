import pygame as pg
import numpy as np


class UtilitiesMain:
    def __init__(self):
        self.COLUMN_AMOUNT = 7
        self.ROW_AMOUNT = 6
        self.background_image = pg.image.load(
            "data/images/game_screens/classic/game_screen.png"
        )
        self.chip_1 = pg.image.load("data/images/game_screens/classic/chip_1.png")
        self.chip_2 = pg.image.load("data/images/game_screens/classic/chip_2.png")

    def create_matrix(self) -> np.ndarray:
        matrix = np.zeros((self.ROW_AMOUNT, self.COLUMN_AMOUNT))
        return matrix

    def drop_piece(self, matrix: np.ndarray, row: int, column: int, piece: int) -> None:
        matrix[row][column] = piece

    def is_available(self, matrix: np.ndarray, column: int) -> bool:
        return matrix[self.ROW_AMOUNT - 1][column] == 0

    def location_X(self, click_loc: int) -> int:
        # First location (X)
        if 357 <= click_loc <= 551:
            return 1

        elif 551 <= click_loc <= 714:
            return 2

        elif 714 <= click_loc <= 879:
            return 3

        elif 879 <= click_loc <= 1038:
            return 4

        elif 1038 <= click_loc <= 1203:
            return 5

        elif 1203 <= click_loc <= 1362:
            return 6

        elif 1362 <= click_loc <= 1423:
            return 7

        else:
            return 0

    def draw_board(self, matrix: np.ndarray, screen) -> None:
        screen.blit(self.background_image, (0, 0))

        for column in range(self.COLUMN_AMOUNT):
            for row in range(self.ROW_AMOUNT):
                if matrix[row][column] != 0:
                    X_CONST = 140
                    Y_CONST = 128.5

                    x = 403 + ((X_CONST * column) + (23 * (column)))
                    y = 924 - (Y_CONST * (row) + (17 * (row)))

                    if matrix[row][column] == 1:
                        screen.blit(self.chip_1, (x, y))

                    elif matrix[row][column] == 2:
                        screen.blit(self.chip_2, (x, y))

    def get_open_row(self, matrix: np.ndarray, column: int) -> int:
        for row in range(self.ROW_AMOUNT):
            if matrix[row][column] == 0:
                return row

    def is_victory(self, matrix: np.ndarray, chip: int) -> bool:
        # Check horizontal
        for column in range(self.COLUMN_AMOUNT - 3):
            for row in range(self.ROW_AMOUNT):
                if (
                    matrix[row][column] == chip
                    and matrix[row][column + 1] == chip
                    and matrix[row][column + 2] == chip
                    and matrix[row][column + 3] == chip
                ):
                    return True

        # Check Vertical
        for column in range(self.COLUMN_AMOUNT):
            for row in range(self.ROW_AMOUNT - 3):
                if (
                    matrix[row][column] == chip
                    and matrix[row + 1][column] == chip
                    and matrix[row + 2][column] == chip
                    and matrix[row + 3][column] == chip
                ):
                    return True

        # Main diagonal
        for column in range(self.COLUMN_AMOUNT - 3):
            for row in range(self.ROW_AMOUNT - 3):
                if (
                    matrix[row][column] == chip
                    and matrix[row + 1][column + 1] == chip
                    and matrix[row + 2][column + 2] == chip
                    and matrix[row + 3][column + 3] == chip
                ):
                    return True

        # MainC diagonal
        for column in range(self.COLUMN_AMOUNT - 3):
            for row in range(3, self.ROW_AMOUNT):
                if (
                    matrix[row][column] == chip
                    and matrix[row - 1][column + 1] == chip
                    and matrix[row - 2][column + 2] == chip
                    and matrix[row - 3][column + 3] == chip
                ):
                    return True
