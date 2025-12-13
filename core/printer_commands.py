BOARD_SIZE_MM = 203.2
BOARD_CELL_MM = BOARD_SIZE_MM / 8
Z_MOVEMENT_PICKUP_MM = 20
F_VALUE = "F3000"


class PrinterCommands:
    def __init__(self) -> None:
        pass

    # this assumes the move is a valid move since it will be checked before being put into this function
    # this gets the two commands to move the arm to the position of the piece
    def get_g_code_command(self, uci_move: str) -> tuple[str, str]:
        # a1a2
        start_position, end_position = uci_move[:2], uci_move[2:]
        start_g_code = self.convert_position(start_position)
        end_g_code = self.convert_position(end_position)

        return f"G0 {start_g_code} Z0 {F_VALUE}", f"G0 {end_g_code} Z0 {F_VALUE}"

    def convert_position(self, position: str) -> str:
        file, rank = position[:1], position[1:]

        match file:
            case "a":
                file_g_code = BOARD_CELL_MM * 0 + (
                    BOARD_CELL_MM / 2
                )  # added so that it is the middle of the cell not the corner
            case "b":
                file_g_code = BOARD_CELL_MM * 1 + (BOARD_CELL_MM / 2)
            case "c":
                file_g_code = BOARD_CELL_MM * 2 + (BOARD_CELL_MM / 2)
            case "d":
                file_g_code = BOARD_CELL_MM * 3 + (BOARD_CELL_MM / 2)
            case "e":
                file_g_code = BOARD_CELL_MM * 4 + (BOARD_CELL_MM / 2)
            case "f":
                file_g_code = BOARD_CELL_MM * 5 + (BOARD_CELL_MM / 2)
            case "g":
                file_g_code = BOARD_CELL_MM * 6 + (BOARD_CELL_MM / 2)
            case "h":
                file_g_code = BOARD_CELL_MM * 7 + (BOARD_CELL_MM / 2)
            case _:
                raise ValueError("Invalid value found")

        match rank:
            case "1":
                rank_g_code = BOARD_CELL_MM * 0 + (
                    BOARD_CELL_MM / 2
                )  # added so that it is the middle of the cell not the corner
            case "2":
                rank_g_code = BOARD_CELL_MM * 1 + (BOARD_CELL_MM / 2)
            case "3":
                rank_g_code = BOARD_CELL_MM * 2 + (BOARD_CELL_MM / 2)
            case "4":
                rank_g_code = BOARD_CELL_MM * 3 + (BOARD_CELL_MM / 2)
            case "5":
                rank_g_code = BOARD_CELL_MM * 4 + (BOARD_CELL_MM / 2)
            case "6":
                rank_g_code = BOARD_CELL_MM * 5 + (BOARD_CELL_MM / 2)
            case "7":
                rank_g_code = BOARD_CELL_MM * 6 + (BOARD_CELL_MM / 2)
            case "8":
                rank_g_code = BOARD_CELL_MM * 7 + (BOARD_CELL_MM / 2)
            case _:
                raise ValueError("Invalid value found")

        return f"X{rank_g_code} Y{file_g_code}"

    #this is assuming relative positioning
    # returned as a tuple down, up
    # might have to flip the sign for direction
    def get_g_code_pickup(self) -> tuple[str, str]:
        return f"G0 X0 Y0 Z{Z_MOVEMENT_PICKUP_MM} {F_VALUE}", f"G0 X0 Y0 Z{-Z_MOVEMENT_PICKUP_MM} {F_VALUE}"
