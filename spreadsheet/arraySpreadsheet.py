from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED

        self._grid = []
        # pass

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        # TO BE IMPLEMENTED

        nRows = max(cell.row for cell in lCells) + 1
        nCols = max(cell.col for cell in lCells) + 1
    
        # Create a 2D array with size nRows x nCols
        self._spreadsheet = [[None] * nCols for _ in range(nRows)]
    
        # Fill in the 2D array with the corresponding cell values
        for cell in lCells:
            self._spreadsheet[cell.row][cell.col] = cell.value
        # pass


    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED

        # Add a new empty row to the spreadsheet
        self._cells.append([None] * self.colNum())

        # Update row count
        self._rowCount += 1

        # Return True to indicate successful operation
        return True
        #pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        # return True


    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED

        if not self._spreadsheet:
        # If spreadsheet is empty, create a new row and add a cell to it.
            self._spreadsheet = [[Cell()]]
            
        else:
        # Otherwise, append a new cell to each existing row.
            for row in self._spreadsheet:
                row.append(Cell())

        return True

        #pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        #return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # TO BE IMPLEMENTED

        # Check if rowIndex is valid
        if rowIndex < 0 or rowIndex >= self.rowNum():
            return False

        # Shift all rows after rowIndex down by one
        for i in range(self.rowNum()-1, rowIndex-1, -1):
            for j in range(self.colNum()):
                self._spreadsheet[i+1][j] = self._spreadsheet[i][j]

        # Insert an empty row at rowIndex
        self._spreadsheet[rowIndex] = [None] * self.colNum()

        return True
        #pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        #return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # TO BE IMPLEMENTED
        if colIndex < 0 or colIndex > self.colNum():
            return False

        for i in range(self.rowNum()):
            self._sheet[i].insert(colIndex, None)

        return True
        #pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        #return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        return len(self._spreadsheet)
        #pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        #return 0


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        # TO BE IMPLEMENTED

        if not self.cells:
        # Spreadsheet is empty
            return 0
        else:
        # Get the number of columns in the first row
            return len(self.cells[0])
        #pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        #return 0



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED

        matches = []
        for row in range(self.rowNum()):
            for col in range(self.colNum()):
                if self._spreadsheet[row][col].getValue() == value:
                    matches.append((row, col))
        return matches
        #pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        #return []



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        # TO BE IMPLEMENTED
        cell_list = []
        for row in range(self.rowNum()):
            for col in range(self.colNum()):
                cell = self._spreadsheet[row][col]
                if cell is not None:
                    cell_list.append(cell)
        return cell_list
        #pass

        # TO BE IMPLEMENTED
        #return []