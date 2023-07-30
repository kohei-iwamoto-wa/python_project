import pytest
from unittest.mock import patch
from dataManipulation import DataManipulation
from module.db.mysqlConnector import MysqlConnector

class TestDataManipulation:
    @pytest.fixture(scope='function')
    def test_data_create(mocker):
        data = [('taro', 22),('hanako', 23),('ichiro', 21), ('jiro', 45)]
        yield data
        data = []

    def test_fetch_rows(self, mocker, test_data_create):
        data = mocker.patch.object(DataManipulation, "fetch_rows", test_data_create)
        assert len(data) == 4
