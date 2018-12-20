"""
負責棋盤的邏輯處理
"""


class Chessboard:
    def __init__(self):
        self.grid_count = 19

        self.game_over = False
        self.winner = None
        self.piece = 'b'
        self.grid = []

        self.restart_game()

    def restart_game(self):
        self.game_over = False
        self.winner = None
        self.piece = 'b'

        self.grid = []
        for i in range(self.grid_count):
            self.grid.append(list("." * self.grid_count))

    def is_my_turn(self, my_piece):
        return my_piece == self.piece

    def set_piece(self, r, c):
        """
        在 (r, c)下子，並自動切換玩家
        :param r: 列
        :param c: 行
        :return: 是否成功下子
        """

        if self.can_set_piece(r, c):
            self.grid[r][c] = self.piece

            if self.piece == 'b':
                self.piece = 'w'
            else:
                self.piece = 'b'

            return True
        return False

    def can_set_piece(self, r, c):
        """檢查是否能下子"""
        if self.game_over:
            return False

        return self.grid[r][c] == '.'

    def check_win(self, r, c):
        n_count = self.get_continuous_count(r, c, -1, 0)
        s_count = self.get_continuous_count(r, c, 1, 0)

        e_count = self.get_continuous_count(r, c, 0, 1)
        w_count = self.get_continuous_count(r, c, 0, -1)

        se_count = self.get_continuous_count(r, c, 1, 1)
        nw_count = self.get_continuous_count(r, c, -1, -1)

        ne_count = self.get_continuous_count(r, c, -1, 1)
        sw_count = self.get_continuous_count(r, c, 1, -1)

        if (n_count + s_count + 1 >= 5) or (e_count + w_count + 1 >= 5) or \
                (se_count + nw_count + 1 >= 5) or (ne_count + sw_count + 1 >= 5):
            self.winner = self.grid[r][c]
            self.game_over = True

    # 取得某個方向連續的棋子數量
    def get_continuous_count(self, r, c, dr, dc):
        piece = self.grid[r][c]
        if piece == '.':
            return 0

        result = 0
        i = 1
        while True:
            new_r = r + dr * i
            new_c = c + dc * i
            if 0 <= new_r < self.grid_count and 0 <= new_c < self.grid_count:
                if self.grid[new_r][new_c] == piece:
                    result += 1
                else:
                    break
            else:
                break
            i += 1
        return result
