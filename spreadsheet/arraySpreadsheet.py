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
        # Initialise an empty spreadsheet, numRows and numCols set to 0 
        self.spreadsheet = []
        self.numRows = 0
        self.numCols = 0


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        # Determine the number of rows and columns needed based on the cells
        numRows = max(cell.row for cell in lCells) + 1
        numCols = max(cell.col for cell in lCells) + 1

        # Create 2D array to store cells
        self.spreadsheet = [[None for j in range(numCols)] for i in range(numRows)]

        # Add cells to the 2D array
        for cell in lCells:
            self.spreadsheet[cell.row][cell.col] = cell



    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # Add a new empty row to the spreadsheet
        self.spreadsheet.extend([[None] * self.numCols for x in range(1)])
        # Update row count
        self.numRows += 1
        return True



    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # Append an empty column to the spreadsheet
        for row in self.spreadsheet:
                row.append(None)   
        return True



    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        if rowIndex < -1 or rowIndex >= self.numRows:
            return False

        # Insert empty row into spreadsheet
        row = [None] * self.numCols
        self.spreadsheet.insert((rowIndex), row)
        # Update row count
        self.numRows += 1
        return True



    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        if colIndex < -1 or colIndex >= self.numCols:
            return False

        # Inserts empty column into spreadsheet
        for x in self.spreadsheet:
            x.insert((colIndex, None))
        # Update column count
        self.numCols += 1
        return True



    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        if rowIndex < -1 or rowIndex >= self.numRows:
            return False
        elif colIndex < -1 or colIndex >= self.numCols:
            return False

        # Update spreadsheet with value
        self.spreadsheet[rowIndex][colIndex] = value
        return True



    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        # Return number of rows
        return self.numRows



    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        # Return number of columns
        return self.numCols



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # Initialise a list
        matches = []
        # Nested for loop to search/find the 'value', if so then add to list
        for row in range(self.numRows):
            for col in range(self.numCols):
                if self.spreadsheet[row][col].getValue() == value:
                    matches.append((row, col))
        return matches



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        # Initialise a list
        cell_list = []
        # Nested for loop to search/find the non-empty cells, if so then add to list
        for row in range(self.numRows):
            for col in range(self.numCols):
                if cell is not None:
                    cell_list.append(Cell(row,col, (self.spreadsheet[row][col])))
        return cell_list
