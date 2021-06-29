
class DLXNode:
    '''
    Class for nodes of Algorithm X.
    These are based on the observation that in a circular doubly linked
    list of nodes you can remove a node from a list and restore it easily.
    This is an implementation of a sparse matrix where only 1's are stored.
    Each row and column in a matrix consists of a circular doubly-linked
    list of nodes.
    '''

    def __init__(self, value=0):
        '''
        Initialise node with all directions as self and value as value.
        '''
        self.L = self.R = self.U = self.D = self.C = self
        self.value = value

    def insertRow(self):
        # Insert node into row
        self.L.R = self.R.L = self

    def insertCol(self):
        # Insert node into the column
        self.U.D = self.D.U = self
        self.C.value += 1

    def removeRow(self):
        # Opposite of insertRow
        self.L.R = self.R
        self.R.L = self.L

    def removeCol(self):
        # Opposite of insertCol
        self.U.D = self.D
        self.D.U = self.U
        self.C.value -= 1

    def insertAbove(self, node):
        # Insert node above given node
        self.C = node.C
        self.U = node.U
        self.D = node
        self.insertCol()

    def insertRight(self, node):
        # Insert node to the right of a given node
        self.R = node.R
        self.L = node
        self.insertRow()
        
    def loopCol(self):
        # Loop through column of nodes
        node = self.D
        while node != self:
            yield node
            node = node.D

    def loopRow(self):
        # Loop through row of nodes
        node = self.R
        while node != self:
            yield node
            node = node.R

    def cover(self):
        # Remove header from graph, and rows with same constraint 
        self.C.removeRow()
        for row in self.C.loopCol():
            for node in row.loopRow():
                node.removeCol()

    def uncover(self):
        # Restore header and subsequent nodes to graph 
        self.C.insertRow()
        for row in self.C.loopCol():
            for node in row.loopRow():
                node.insertCol()

class DLX:
    '''
    Implement Donald Knuth's Algorithm X with Dancing Links to represent 
    and solve n-queens as an Exact Cover problem.

    See https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X and
    ref arXiv:cs/0011047v for Knuth's paper on the topic
    '''

    def __init__(self, n):
        '''Initialise matrix of nodes for Algorithm X'''
        self.solution = np.array([[0]*n]*n)
        
        # Initialise empty header nodes
        columnObject = []
        for _ in range((6*n)-6):
            columnObject.append(DLXNode())

        def constraints(r, c, x):
            # Map each cell value to its constraints
            cell = (9*r) + c # Cell full constraint
            row = 81 + (9*r) + x # Row constraint
            col = (81*2) + (9*c) + x # Column constraint
            box = (81*3) + (9*((3*(r//3)) + (c//3))) + x # Square constraint

            return [cell, row, col, box]

        def add_to_matrix(c_row, r, c, x):
            first = None
            for con in constraints(r,c,x):
                # The cell-number information is stored as the nodes value 
                node = DLXNode(c_row + x)
                node.insertAbove(columnObject[con])
                if first == None:
                    first = node
                else:
                    node.insertRight(first)

        c_row = 0
        for r in range(9):
            for c in range(9):
                if sudoku[r][c] == 0:
                    for x in range(9):
                        add_to_matrix(c_row, r, c, x)
                else:
                    x = sudoku[r][c] - 1
                    add_to_matrix(c_row, r, c, x)
                c_row += 9

        self.root = DLXNode()
        last = self.root
        for header in columnObject:
            header.insertRight(last)
            last = header


    def addToSolution(self, val):
        '''The cell-number information is recovered from the value'''
        r = val // 81
        val %= 81
        c = val // 9
        val %= 9
        self.solution[r][c] = val + 1

    def solve(self):
        '''
        Solve sudoku using DLX
        '''
        # If header row is empty, A is empty, problem solved
        if self.root.R == self.root:
            return True

        # Choose column c with lowest amount of constraints
        colHead = min(self.root.loopRow(), key=attrgetter('value'))
        if colHead.value == 0:
            return False
        colHead.cover()
        for row in colHead.loopCol():
            for node in row.loopRow():
                node.cover()
            if self.solve():
                self.addToSolution(row.value)
                return True
            for node in row.loopRow():
                node.uncover()
        colHead.uncover()
        return False