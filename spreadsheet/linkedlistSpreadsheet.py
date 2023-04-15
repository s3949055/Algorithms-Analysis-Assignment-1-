from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, value: float):
        self.value = value
        self.next = None
        self.prev = None
# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.row_head = self.ListNode(None)  # sentinel node for the row linked list
        self.col_head = self.ListNode(None)  # sentinel node for the column linked list
        self.row_head.next = self.col_head.prev = self.ListNode(None)  # create the first node in each list
        self.row_size = self.col_size = 0  # size of the spreadsheet
        pass


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        for cell in lCells:
            self.update(cell.row, cell.col, cell.value)
        pass


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """

        new_row_node = self.ListNode(None)
        new_row_node.prev = self.row_head.prev
        new_row_node.next = self.row_head.prev.next
        new_row_node.prev.next = new_row_node.next.prev = new_row_node
        self.row_size += 1

        pass


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        new_col_node = self.ListNode(None)
        new_col_node.prev = self.col_head.prev
        new_col_node.next = self.col_head.prev.next
        new_col_node.prev.next = new_col_node.next.prev = new_col_node
        self.col_size += 1
        pass


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        if rowIndex < 0 or rowIndex > self.row_size:
            return False
        new_row_node = self.ListNode(None)
        curr_row_node = self.row_head.next
        for i in range(rowIndex):
            curr_row_node = curr_row_node.next
        new_row_node.prev = curr_row_node.prev
        new_row_node.next = curr_row_node
        new_row_node.prev.next = new_row_node.next.prev = new_row_node
        self.row_size += 1
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """

        if colIndex < -1 or colIndex >= self.col_size:
            return False
        new_col_node = self.ListNode(None)
        curr_col_node = self.col_head.next
        for i in range(colIndex):
            curr_col_node = curr_col_node.next
        new_col_node.prev = curr_col_node.prev
        new_col_node.next = curr_col_node
        new_col_node.prev.next = new_col_node


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        pass

        # TO BE IMPLEMENTED
        return 0


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        pass

        # TO BE IMPLEMENTED
        return 0



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return []



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        # TO BE IMPLEMENTED
        pass

        # TO BE IMPLEMENTED
        return []
