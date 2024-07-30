import tablib
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QTableWidgetItem


class Table(QtWidgets.QTableWidget):
    def __init__(self, data: list = None, headers: list = None, isEdit: bool = False):
        """
        Data table with style
        Args:
            data (list): Two-dimensional array data
            headers (list): Table header
            isEdit (bool): Whether to allow editing
        """
        super().__init__(len(data), header_length := len(headers))
        self.setObjectName('main-table')
        self.__data = data
        self.isEdit = isEdit
        self.__headers = headers
        self.setHorizontalHeaderLabels(headers)
        self.setShowGrid(False)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.horizontalHeader().setHighlightSections(False)
        self.verticalHeader().setVisible(False)
        for column_index in range(header_length - 1):
            self.horizontalHeader().setSectionResizeMode(column_index, QtWidgets.QHeaderView.ResizeMode.Interactive)

        for row_index, item_data in enumerate(data):
            for column_index in range(header_length):
                item = QTableWidgetItem(str(item_data[column_index]))
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                if not isEdit:
                    item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable)
                self.setItem(row_index, column_index, item)
                item.setSizeHint(self.sizeHint())
        self.resizeColumnsToContents()

    def addColumn(self, header: str, data: list):
        """
        Add a column at the end
        Args:
            header (str): Column heading
            data (list): Column data

        Returns:

        """
        if len(data) != self.rowCount(): raise ValueError("Data length error")
        if header in set(self.__headers): raise ValueError("The column header already exists")
        self.__headers.append(header)
        self.setColumnCount(self.columnCount() + 1)
        self.setHorizontalHeaderLabels(self.__headers)
        for column_index, column_data in enumerate(data):
            item = QTableWidgetItem(str(column_data))
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            if not self.isEdit:
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable)
            self.setItem(column_index, self.rowCount(), item)
            # TODO: 添加不上
            item.setSizeHint(self.sizeHint())

    def addLine(self, data: list):
        """
        Add a row of data at the end
        Args:
            data (list): data

        Returns:

        """
        row_count = self.rowCount()
        if len(data) != row_count: raise ValueError("Data length error")
        self.setRowCount(row_count + 1)
        for column_index, column_data in enumerate(data):
            item = QTableWidgetItem(str(column_data))
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            if not self.isEdit:
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable)
            self.setItem(row_count, column_index, item)
            item.setSizeHint(self.sizeHint())

    def delColumn(self, index: int):
        """
        Delete column data
        Args:
            index (int): Column index

        Returns:

        """
        self.removeColumn(index)

    def delLine(self, index: int):
        """
        Delete row data
        Args:
            index (int): Row index

        Returns:

        """
        self.removeRow(index)

    @property
    def shape(self):
        return self.rowCount(), self.columnCount()

    def export(self):
        csv_table = tablib.Dataset(
            headers=[self.horizontalHeaderItem(i).text() for i in range(self.columnCount())]
        )
        for row in range(self.rowCount()):
            csv_table.append(
                [item.text() if (item := self.item(row, column)) else '' for column in range(self.columnCount())]
            )
        return csv_table

    def toCSV(self):
        """
        Save the table data to a csv file
        Returns:
            isOK (bool): Whether the storage is successful
            msg (str): Error message
        """
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            parent=self,
            caption="Table To CSV",
            filter=".csv;;.CSV",
            dir="NTable_export.csv"
        )
        if not path: return
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(self.export().export('csv', lineterminator='\n'))
            return True, ''
        except IOError or OSError as e:
            return False, e

    def toExcel(self):
        """
       Save the table data to a xlsx file
       Returns:
           isOK (bool): Whether the storage is successful
           msg (str): Error message
       """
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            parent=self,
            caption="Table To CSV",
            filter=".xlsx;;.XLSX",
            dir="NTable_export.xlsx"
        )
        if not path: return
        try:
            with open(path, 'wb') as f:
                f.write(self.export().export('xlsx'))
            return True, ''
        except IOError or OSError as e:
            return False, e
