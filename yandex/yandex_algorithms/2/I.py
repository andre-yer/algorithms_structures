def prepare_field(rows, columns, mines):
    field = []
    for _ in range(rows):
        field.append(columns * ['-'])
    for mine in mines:
        field[mine[0] - 1][mine[1] - 1] = '*'
    return field


def count_mines(list_mines):
    return len([item for item in list_mines if item == '*'])


def count_cell(field, row, column, max_row, max_column):
    n_mines = []
    if row == 0 and column == 0:
        n_mines.append(field[0][1])
        n_mines.append(field[1][0])
        n_mines.append(field[1][1])
        return count_mines(n_mines)
    elif row == 0 and column == max_column:
        n_mines.append(field[0][max_column - 1])
        n_mines.append(field[1][max_column - 1])
        n_mines.append(field[1][max_column])
        return count_mines(n_mines)
    elif row == max_row and column == 0:
        n_mines.append(field[max_row - 1][0])
        n_mines.append(field[max_row][1])
        n_mines.append(field[max_row - 1][1])
        return count_mines(n_mines)
    elif row == max_row and column == max_column:
        n_mines.append(field[max_row - 1][max_column])
        n_mines.append(field[max_row][max_column - 1])
        n_mines.append(field[max_row - 1][max_column - 1])
        return count_mines(n_mines)
    elif row == 0:
        n_mines.append(field[0][column - 1])
        n_mines.append(field[0][column + 1])
        n_mines.append(field[1][column - 1])
        n_mines.append(field[1][column])
        n_mines.append(field[1][column + 1])
        return count_mines(n_mines)
    elif row == max_row:
        n_mines.append(field[max_row][column - 1])
        n_mines.append(field[max_row][column + 1])
        n_mines.append(field[max_row - 1][column - 1])
        n_mines.append(field[max_row - 1][column])
        n_mines.append(field[max_row - 1][column + 1])
        return count_mines(n_mines)
    elif column == 0:
        n_mines.append(field[row - 1][0])
        n_mines.append(field[row + 1][0])
        n_mines.append(field[row - 1][1])
        n_mines.append(field[row][1])
        n_mines.append(field[row + 1][1])
        return count_mines(n_mines)
    elif column == max_column:
        n_mines.append(field[row - 1][max_column])
        n_mines.append(field[row + 1][max_column])
        n_mines.append(field[row - 1][max_column - 1])
        n_mines.append(field[row][max_column - 1])
        n_mines.append(field[row + 1][max_column - 1])
        return count_mines(n_mines)
    else:
        n_mines.append(field[row][column - 1])
        n_mines.append(field[row][column + 1])
        n_mines.append(field[row - 1][column - 1])
        n_mines.append(field[row - 1][column])
        n_mines.append(field[row - 1][column + 1])
        n_mines.append(field[row + 1][column - 1])
        n_mines.append(field[row + 1][column])
        n_mines.append(field[row + 1][column + 1])
        return count_mines(n_mines)


def finish_field(field, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if field[i][j] != '*':
                field[i][j] = count_cell(field, i, j, rows - 1, columns - 1)
    return field


def draw_field(field):
    for row in field:
        print(*row)


def main():
    rows, columns, n_mines = map(int, input().split())
    mines = []
    for i in range(n_mines):
        mines.append(list(map(int, input().split())))

    field = prepare_field(rows, columns, mines)
    field = finish_field(field, rows, columns)
    draw_field(field)


if __name__ == '__main__':
    main()
