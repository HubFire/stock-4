#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = 'cooper'

from sqlalchemy import Table
from common import beans

_sql_meta_data = beans.sql_meta_data
_sql_engine = beans.sql_engine
Stocks = Table('stocks', _sql_meta_data, autoload=True, autoload_with=_sql_engine)
StockKLineDays = Table('stock_k_line_days', _sql_meta_data, autoload=True, autoload_with=_sql_engine)
