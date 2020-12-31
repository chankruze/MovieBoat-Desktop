"""
Author: chankruze (chankruze@geekofia.in)
Created: Wed Dec 30 2020 19:52:50 GMT+0530 (India Standard Time)

Copyright (c) Geekofia 2020 and beyond
"""
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import uic

# application context (fbs)
from base import app_context

# custom functions
from gql_client import query_movies

import pandas as pd
from pandas.io.json import json_normalize
import asyncio


class SearchWindow(QMainWindow):
    def __init__(self):
        super(SearchWindow, self).__init__()
        uic.loadUi(app_context.get_resource("search.ui"), self)
        # print("-------- DEBUG --------")
        # print(self.__dict__)
        # print("-------- DEBUG --------")

        # default params
        self.page = 1
        self.limit = 50

        # init movies list
        self.movies = list()

        # connect signals
        self.connect_signals()

    def get_search_query(self):
        # construct query url
        query_string = f"limit={self.limit}&page={self.page}"
        query_term = self.searchbar.text()
        quality = self.qualities.currentText()
        genre = self.genres.currentText()
        rating = self.ratings.currentText()
        sortby = self.sortby.currentText()
        orderby = self.orderby.currentText()

        if query_term != "":
            query_string += f"&query_term={query_term}"

        if quality != "All":
            query_string += f"&quality={quality}"

        if genre != "All":
            query_string += f"&genre={genre}"

        if rating != "0":
            query_string += f"&minimum_rating={rating}"

        if sortby != "date_added":
            query_string += f"&sort_by={sortby}"

        if orderby != "desc":
            query_string += f"&order_by={orderby}"

        # actual request to apollo server
        self.movies = query_movies(query_string)
        self.populate_table()

    def select_quality(self):
        print(self.qualities.currentText())

    def select_genre(self):
        print(self.genres.currentText())

    def select_rating(self):
        print(self.ratings.currentText())

    def select_sort_by(self):
        print(self.sortby.currentText())

    def select_order_by(self):
        print(self.orderby.currentText())

    def populate_table(self):
        # print(self.movies)
        table_data_frame = pd.DataFrame(self.movies)
        # print(table_data)

        table = self.resultTable
        # reset table rows
        table.setRowCount(0)

        # push data to table
        for row_index, row_data in table_data_frame.iterrows():
            # print(row_index, row_data)
            table.insertRow(row_index)

            for col_index, col_data in enumerate(row_data):
                data = ""

                if col_index == len(row_data) - 2:
                    # print(col_index)
                    data = ", ".join(col_data)
                else:
                    data = str(col_data)

                # print(col_data)
                table.setItem(row_index, col_index,
                              QTableWidgetItem(data))

    def connect_signals(self):
        # connect search button
        self.pushButton_search.clicked.connect(self.get_search_query)
        # connect quality comboBox
        self.qualities.currentIndexChanged.connect(self.select_quality)
        # connect genre comboBox
        self.genres.currentIndexChanged.connect(self.select_genre)
        # connect rating comboBox
        self.ratings.currentIndexChanged.connect(self.select_rating)
        # connect sort by comboBox
        self.sortby.currentIndexChanged.connect(self.select_sort_by)
        # connect order by comboBox
        self.orderby.currentIndexChanged.connect(self.select_order_by)
