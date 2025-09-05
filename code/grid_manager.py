import pygame
from node import Node
from constants import WHITE, GREY

class GridManager:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.gap = width // rows
        self.grid = self.make_grid()

    def make_grid(self):
        """Create a grid of nodes"""
        grid = []
        for i in range(self.rows):
            grid.append([])
            for j in range(self.rows):
                node = Node(i, j, self.gap, self.rows)
                grid[i].append(node)
        return grid

    def draw_grid_lines(self, win):
        """Draw grid lines on the window"""
        for i in range(self.rows):
            pygame.draw.line(win, GREY, (0, i * self.gap), (self.width, i * self.gap))
        for j in range(self.rows):
            pygame.draw.line(win, GREY, (j * self.gap, 0), (j * self.gap, self.width))

    def draw(self, win):
        """Draw the entire grid"""
        win.fill(WHITE)
        
        for row in self.grid:
            for node in row:
                node.draw(win)
        
        self.draw_grid_lines(win)
        pygame.display.update()

    def get_clicked_position(self, pos):
        """Convert mouse position to grid coords"""
        x, y = pos
        row = y // self.gap
        col = x // self.gap
        return row, col

    def get_node(self, row, col):
        """Get node at a specific position"""
        if 0 <= row < self.rows and 0 <= col < self.rows:
            return self.grid[row][col]
        return None

    def reset_grid(self):
        """Reset the grid to initial state"""
        self.grid = self.make_grid()

    def update_all_neighbours(self):
        """Update the neighbors for all nodes"""
        for row in self.grid:
            for node in row:
                node.update_neighbours(self.grid)