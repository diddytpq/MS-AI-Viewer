# from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QTableWidgetSelectionRange

# class MainWindow(QTableWidget):
#     def __init__(self):
#         super().__init__(5, 5)  # 5x5 table

#         # Populate the table with some items
#         # for row in range(5):
#         #     for col in range(5):
#         #         item = QTableWidgetItem(f"R{row+1}C{col+1}")
#         #         self.setItem(row, col, item)

#         # Enable drag selection and highlight of rows/columns
#         self.setSelectionMode(QTableWidget.ExtendedSelection)  # Allow multiple item selection
#         self.setSelectionBehavior(QTableWidget.SelectItems)    # Select individual cells

#         # Set up the size of the table
#         self.resize(500, 300)

#         # Select a specific range (from row 3, column 3 to row 3, column 5)
#         selection_range = QTableWidgetSelectionRange(0, 2, 4, 2)  # QTableWidgetSelectionRange(startRow, startColumn, endRow, endColumn)
#         self.setRangeSelected(selection_range, True)

#         selection_range = QTableWidgetSelectionRange(0, 1, 4, 1)  # QTableWidgetSelectionRange(startRow, startColumn, endRow, endColumn)
#         self.setRangeSelected(selection_range, True)


# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()

from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QTableWidgetSelectionRange

class TableWidgetExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTableWidget Example")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        # QTableWidget 생성
        self.table_widget = QTableWidget(5, 5)  # 5x5 테이블 생성
        layout.addWidget(self.table_widget)

        # 테이블에 데이터를 추가
        for row in range(5):
            for column in range(5):
                item = QTableWidgetItem(f"Cell {row+1},{column+1}")
                self.table_widget.setItem(row, column, item)

        # 3행 2열과 3행 4열을 선택
        self.select_multiple_cells()

    def select_multiple_cells(self):
        # 멀티 셀렉션을 활성화
        self.table_widget.setSelectionMode(QTableWidget.MultiSelection)

        # 3행 2열 선택 (행과 열은 0부터 시작하므로 2, 1)
        item_1 = self.table_widget.item(2, 1)  # 3행 2열
        item_1.setSelected(True)

        # 3행 4열 선택 (행과 열은 0부터 시작하므로 2, 3)
        item_2 = self.table_widget.item(2, 3)  # 3행 4열
        item_2.setSelected(True)

if __name__ == "__main__":
    app = QApplication([])

    window = TableWidgetExample()
    window.show()

    app.exec()
