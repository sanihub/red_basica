from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Project(QSqlRelationalTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(Project, self).__init__(*args, **kwargs)
        self.setTable("projects")
        self.select()

    def refresh(self):
        self.dataChanged.emit(QModelIndex(), QModelIndex())
        self.select()

    def getDisplayColumn(self):
        return self.nameFieldIndex        

    def getActiveProject(self):
        currentProjectId = None
        query = QSqlQuery("SELECT id FROM projects WHERE active")
        while query.next():
            currentProjectId = query.value(0)
        return self.record(currentProjectId) if currentProjectId else currentProjectId

    def getNameActiveProject(self):
        currentProjectName = None
        query = QSqlQuery("SELECT name FROM projects WHERE active")
        while query.next():
            currentProjectName = query.value(0)
        return str(currentProjectName)

    def setActive(self, id):        
        # current = self.getActiveProject()
        # if current:
        #     current.setValue('active', 0)
        # newActive = self.record(id)
        # newActive.setValue('active', 1)       
        # self.submitAll()                    
        query = QSqlQuery("UPDATE projects SET active = 0")
        queryUpdate = QSqlQuery()
        queryUpdate.prepare("UPDATE projects SET active = 1 WHERE id = :id ")
        queryUpdate.bindValue(":id", id)
        queryUpdate.exec_()
         