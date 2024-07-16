from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterator
from enum import Enum


class Colour(Enum):
    WHITE = 0
    BLACK = 1


# Meaningfully named classes group code with a single responsibility
class Board:
    _SIZE = 8

    def __init__(self):
        self.__rows = [
            [Rook(Colour.BLACK), Knight(Colour.BLACK), Bishop(Colour.BLACK), Queen(Colour.BLACK),
             King(Colour.BLACK), Bishop(Colour.BLACK), Knight(Colour.BLACK), Rook(Colour.BLACK)],
            [Pawn(Colour.BLACK) for _ in range(8)],
            [None]*8, [None]*8, [None]*8, [None]*8,
            [Pawn(Colour.WHITE) for _ in range(8)],
            [Rook(Colour.WHITE), Knight(Colour.WHITE), Bishop(Colour.WHITE), Queen(Colour.WHITE),
             King(Colour.WHITE), Bishop(Colour.WHITE), Knight(Colour.WHITE), Rook(Colour.WHITE)]
        ]

    def __str__(self):
        result = ""
        for row in self.__rows:
            for piece in row:
                if piece is None:
                    result += "."
                else:
                    result += str(piece)
            result += "\n"
        return result[:-1]

    # Other classes interact with this class only in defined ways
    @staticmethod
    def in_bounds(y: int, x: int) -> bool:
        return 0 <= y < Board._SIZE and 0 <= x < Board._SIZE

    def get(self, y, x) -> Piece | None:
        return self.__rows[y][x]

    def move(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        self.__rows[end[0]][end[1]] = self.get(*start)
        self.__rows[start[0]][start[1]] = None


# Classes represent types of real-world object
class Piece(ABC):
    def __init__(self, colour: Colour):
        self.__colour = colour

    @property
    def colour(self) -> Colour:
        return self.__colour

    @abstractmethod
    def get_destinations(self, pos: tuple[int, int], board: Board) -> Iterator[tuple[int, int]]:
        raise NotImplementedError


class LongPiece(Piece):
    @staticmethod
    @abstractmethod
    def _directions() -> Iterator[tuple[int, int]]:
        raise NotImplementedError

    def get_destinations(self, pos: tuple[int, int], board: Board) -> Iterator[tuple[int, int]]:
        for direction in self._directions():
            yield from self.__ray_cast(direction, pos, self.colour, board)

    @staticmethod
    def __ray_cast(direction: tuple[int, int], pos: tuple[int, int], colour: Colour, board: Board
                   ) -> Iterator[tuple[int, int]]:
        dy, dx = direction
        check_y, check_x = pos[0] + dy, pos[1] + dx
        while board.in_bounds(check_y, check_x):
            if board.get(check_y, check_x) is None:
                yield check_y, check_x
            elif board.get(check_y, check_x).colour == colour:
                return
            else:
                yield check_y, check_x
                return
            check_y += dy
            check_x += dx


class Rook(LongPiece):
    def __str__(self):
        if self.colour == Colour.WHITE:
            return "R"
        else:
            return "r"

    @staticmethod
    def _directions() -> Iterator[tuple[int, int]]:
        yield from [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Bishop(LongPiece):
    def __str__(self):
        if self.colour == Colour.WHITE:
            return "B"
        else:
            return "b"

    @staticmethod
    def _directions() -> Iterator[tuple[int, int]]:
        yield from [(1, 1), (1, -1), (-1, 1), (-1, -1)]


class Queen(LongPiece):
    def __str__(self):
        if self.colour == Colour.WHITE:
            return "Q"
        else:
            return "q"

    @staticmethod
    def _directions() -> Iterator[tuple[int, int]]:
        yield from [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


class ShortPiece(Piece):
    @staticmethod
    @abstractmethod
    def _directions() -> Iterator[tuple[int, int]]:
        raise NotImplementedError

    def get_destinations(self, pos: tuple[int, int], board: Board) -> Iterator[tuple[int, int]]:
        y, x = pos
        for (dy, dx) in self._directions():
            if not board.in_bounds(y + dy, x + dx):
                continue
            check = board.get(y + dy, x + dx)
            if check is None or check.colour != self.colour:
                yield y + dy, x + dx


class Knight(ShortPiece):
    def __str__(self):
        if self.colour == Colour.WHITE:
            return "N"
        else:
            return "n"

    @staticmethod
    def _directions() -> Iterator[tuple[int, int]]:
        yield from [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]


class King(ShortPiece):
    def __str__(self):
        if self.colour == Colour.WHITE:
            return "K"
        else:
            return "k"

    @staticmethod
    def _directions() -> Iterator[tuple[int, int]]:
        yield from [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]


class Pawn(Piece):
    def __str__(self):
        if self.colour == Colour.WHITE:
            return "P"
        else:
            return "p"

    def get_destinations(self, pos: tuple[int, int], board: Board) -> Iterator[tuple[int, int]]:
        y, x = pos
        if self.colour == Colour.WHITE:
            dy = -1
        else:
            dy = 1
        if board.in_bounds(y + dy, x) and board.get(y + dy, x) is None:
            yield y + dy, x
            if self.colour == Colour.WHITE and y == 6 or self.colour == Colour.BLACK and y == 1:
                if board.in_bounds(y + 2 * dy, x) and board.get(y + 2 * dy, x) is None:
                    yield y + 2 * dy, x
        for dx in (1, -1):
            if board.in_bounds(y + dy, x + dx):
                check = board.get(y + dy, x + dx)
                if check is not None and check.colour != self.colour:
                    yield y + dy, x + dx


def main():
    board = Board()
    while True:
        print(board)
        start = tuple(map(int, input("Enter coordinates of square to move from as two indices 0-7 within the board, "
                                     "separated by a space (eg \"0 7 for h8\") ").split()))
        moves = list(board.get(*start).get_destinations(start, board))
        if moves:
            print("Piece can move to:")
            print(", ".join(map(str, moves)))
        else:
            print("No moves for that piece")
            continue
        end = tuple(map(int, input("Enter coordinates of square to move from as two indices 0-7 within the board, "
                                   "separated by a space (eg \"0 7 for h8\") ").split()))
        board.move(start, end)


main()
