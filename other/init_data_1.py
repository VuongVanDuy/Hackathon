import json
import ijson
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QTableView

class DatabaseManager:
    def __init__(self, database_name):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(database_name)

        if not self.db.open():
            print("Unable to open database")
            raise Exception("Unable to open database")
    
    def create_table(self):
        query = QSqlQuery()
        query.exec_("""
        CREATE TABLE IF NOT EXISTS stops (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            lat REAL,
            lon REAL
        )
        """)
    
    def create_coords_table(self):
        query = QSqlQuery()
        query.exec_("""
        CREATE TABLE IF NOT EXISTS coords (
            lat REAL,
            lon REAL
        )
        """)
    
    def import_data_from_json(self, json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        for stop in data['result']:
            self.add_stop(stop['id'], stop['name'], stop['lat'], stop['lon'])
    
    def import_coords_from_json(self, json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        print(data['result'][0]['path'])
        for coord in data['result'][0]['path']:
            self.add_coords(coord['lat'], coord['lon'])
    
    def add_coords(self, lat, lon):
        query = QSqlQuery()
        query.prepare("INSERT INTO coords (lat, lon) VALUES ( ?, ?)")
        query.addBindValue(lat)
        query.addBindValue(lon)
        if not query.exec_():
            print(f"Error adding coord: {query.lastError().text()}")
    
    def add_stop(self, stop_id, name, lat, lon):
        query = QSqlQuery()
        query.prepare("INSERT INTO stops (id, name, lat, lon) VALUES (?, ?, ?, ?)")
        query.addBindValue(stop_id)
        query.addBindValue(name)
        query.addBindValue(lat)
        query.addBindValue(lon)
        if not query.exec_():
            print(f"Error adding stop: {query.lastError().text()}")
    
    def create_model(self, table):
        self.model = QSqlTableModel()
        self.model.setTable(table)
        self.model.select()
        return self.model

class EmployeeTableView(QTableView):
    def __init__(self, model):
        super().__init__()
        self.setModel(model)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    db_manager = DatabaseManager("stops.db")
    # db_manager.create_table()
    # db_manager.import_data_from_json('./data/stops.json')
    db_manager.create_coords_table()
    db_manager.import_coords_from_json('./data/1065_coords.json')

    print("Data imported successfully!")
    model = db_manager.create_model("coords")
    view = EmployeeTableView(model)
    view.setWindowTitle("Employee Table")
    view.resize(400, 300)
    view.show()
    sys.exit(app.exec_())
