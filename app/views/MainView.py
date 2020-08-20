from PyQt5.QtWidgets import QMainWindow, QDialog, QAbstractItemView
from PyQt5.QtCore import QThread, Qt, QModelIndex
from PyQt5 import uic, QtGui, QtWidgets
from qgis.utils import iface, QgsMessageLog
from .ui.MainWindowUi import Ui_MainWindow
from ..controllers.CalculationController import CalculationController
from ..models.Calculation import Calculation
from ..models.Contribution import Contribution
from ..models.WaterLevelAdj import WaterLevelAdj
from ..models.delegates.CalculationDelegate import CalculationDelegate, NumberFormatDelegate
from ..lib.ProgressThread import ProgressThread

class MainView(QMainWindow, Ui_MainWindow):
    
    def __init__(self, dialogs):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.selected = {}

        # Main window
        self._dialogs = dialogs
        self.calculationController = CalculationController()
        
        #Hide progress bar
        self.progressBar.hide()
        self.progressMsg.hide() 

        # Models
        self.calcModel = Calculation()        
        self.contribModel = Contribution()
        self.wlaModel = WaterLevelAdj()

        # Red Basica Table
        self.calcTable.setModel(self.calcModel)
        self.calcTable.setItemDelegate(CalculationDelegate(self.calcTable))
        self.calcTable.setItemDelegateForColumn(self.calcModel.fieldIndex("slopes_min_accepted_col"), NumberFormatDelegate())
        self.calcTable.model().dataChanged.connect(self.onDataChanged)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("id"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("project_id"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("layer_name"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("created_at"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("updated_at"), True)

        # Contributions Table
        self.contribTable.setModel(self.contribModel)
        self.contribTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.contribTable.setColumnHidden(self.contribModel.fieldIndex("id"), True)
        self.contribTable.setColumnHidden(self.contribModel.fieldIndex("calculation_id"), True)
        self.contribTable.setColumnHidden(self.contribModel.fieldIndex("created_at"), True)
        self.contribTable.setColumnHidden(self.contribModel.fieldIndex("updated_at"), True)
        self.contribTable.horizontalHeader().setSectionResizeMode(True)

        # WaterLevelAdj Table
        self.wlaTable.setModel(self.wlaModel)
        self.wlaTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("id"), True)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("calculation_id"), True)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("created_at"), True)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("updated_at"), True)

        # menu actions
        self.actionProject.triggered.connect(self.checkProjectAction)
        self.actionParameters.triggered.connect(self.openParametersDialog)
        self.actionCalculara_DN.triggered.connect(self.calculateDN)
        self.actionCalcular_DN_Creciente.triggered.connect(self.calculateGrowingDN)
        self.actionMin_Excav.triggered.connect(self.calculateMinExc)
        self.actionMin_Desnivel.triggered.connect(self.calculateMinSlope)
        self.actionAjuste_NA.triggered.connect(self.adjustNA)

        # triggered actions
        self._dialogs['newProject'].buttonBox.accepted.connect(self.changeMainTitle)
        self._dialogs['newProject'].buttonBox.accepted.connect(self.closeProjectDialog)
        self._dialogs['newProject'].buttonBox.accepted.connect(self.openParametersDialog)
        self._dialogs['project'].newProjectButton.clicked.connect(self.openNewProjectDialog)
        self._dialogs['project'].dialogButtonBox.accepted.connect(self.updateProject)
        self._dialogs['parameters'].buttonBox.accepted.connect(self.closeParametersDialog)
        self._dialogs['parameters'].buttonBox.accepted.connect(self.startImport)

    def newProject(self):
        self.closeProjectDialog()
        self.openNewProjectDialog()

    def updateProject(self):
        self._dialogs['project'].saveRecord()
        self.changeMainTitle()

    def checkProjectAction(self):
        if self._dialogs['project'].model.getActiveProject():
            self.openProjectDialog()
        else:
            self.openNewProjectDialog()

    def openProjectDialog(self):
        self._dialogs['project'].show()

    def closeProjectDialog(self):
        self._dialogs['project'].hide()

    def openNewProjectDialog(self):
        self.closeProjectDialog()
        self._dialogs['newProject'].addRecord()
        self._dialogs['newProject'].show()

    def changeMainTitle(self):
        name = self._dialogs['newProject'].model.getNameActiveProject()
        self.setWindowTitle('SANIBIDapp [' + name + ']')

    def closeNewProjectDialog(self):
        self._dialogs['newProject'].hide()

    def openParametersDialog(self):
        self._dialogs['parameters'].show()

    def closeParametersDialog(self):
        self._dialogs['parameters'].hide()

    def onDataChanged(self, index, index2, roles):
        #this is fired twice and index is the row after database change
        #TODO: find a better way to do this
        val = index.data()
        if type(val) in [int, float]:
            record = self.calcModel.record(val)
            colSeg = record.value('col_seg')
            controller = CalculationController()
            ProgressThread(self, controller, (lambda : controller.updateVal(colSeg)))
                   

    def refreshTables(self):
        """ Refresh table views, its called from ProgressThread instances"""
        self.calcModel.select() #TODO order by col_seg
        self.contribModel.select()
        self.wlaModel.select()

    def startImport(self):
        projectId = self._dialogs['newProject'].model.getActiveId()        
        controller = CalculationController(projectId)
        ProgressThread(self, controller, controller.importData)                       

    def calculateDN(self):
        projectId = self._dialogs['newProject'].model.getActiveId()
        controller = CalculationController()
        ProgressThread(self, controller, (lambda : controller.calculateDN(projectId)))        
    
    def calculateGrowingDN(self):
        projectId = self._dialogs['newProject'].model.getActiveId()
        controller = CalculationController()
        ProgressThread(self, controller, (lambda : controller.calculateDN(projectId, True)))
    
    def calculateMinExc(self):
        projectId = self._dialogs['newProject'].model.getActiveId()
        controller = CalculationController()
        ProgressThread(self, controller, (lambda : controller.calculateMinExc(projectId)))

    def calculateMinSlope(self):
        projectId = self._dialogs['newProject'].model.getActiveId()
        controller = CalculationController()
        ProgressThread(self, controller, (lambda : controller.calculateMinSlope(projectId)))

    def adjustNA(self):
        projectId = self._dialogs['newProject'].model.getActiveId()
        controller = CalculationController()
        ProgressThread(self, controller, (lambda : controller.adjustNA(projectId)))

    def contextMenuEvent(self, pos):
        if self.calcTable.selectionModel().selection().indexes():
            selected = {}
            for i in self.calcTable.selectionModel().selection().indexes():
                if i.column() not in selected:
                    selected[i.column()] = []
                selected[i.column()].append(i.row())
            self.menu = QtWidgets.QMenu()
            self.selected = selected
            editValuesAction = QtWidgets.QAction('Edit Values', self)
            editValuesAction.triggered.connect(lambda: self.editValuesAction(self.selected))
            deleteAction = QtWidgets.QAction('Delete Value', self)
            deleteAction.triggered.connect(lambda: self.deleteAction(self.selected))
            self.menu.addAction(editValuesAction)
            self.menu.addAction(deleteAction)
            self.menu.popup(QtGui.QCursor.pos())

    def editValuesAction(self, selected):
        editDialog = self._dialogs['editValues']
        editDialog.show()
        editDialog.accepted.connect(lambda: self.editAction(editDialog.editValueEdit.value()))
        editDialog.editValueEdit.setValue(0)

    def editAction(self, value):
        selected = self.selected
        column = next(iter(selected)) 
        calcModel = self.calcModel
        colSegs = []
        oldColNumber = None
        for item in selected.values():
            for row in item:
                index = calcModel.index(row,column)
                colName = calcModel.record(row).fieldName(column)
                id = calcModel.record(row).value('id')
                collectorNumber = calcModel.record(row).value('collector_number')
                if collectorNumber != oldColNumber:
                    colSegs.append(calcModel.record(row).value('col_seg'))
                calcModel.updateColById(value, colName, id)
                oldColNumber = collectorNumber
        self.calcModel.select()
        controller = CalculationController()
        ProgressThread(self, controller, (lambda : controller.updateValues(colSegs)))

    def deleteAction(self, selected):
        column = next(iter(selected)) 
        calcModel = self.calcModel
        colSegs = []
        oldColNumber = None
        for item in selected.values():
            for row in item:
                index = calcModel.index(row,column)
                colName = calcModel.record(row).fieldName(column)
                id = calcModel.record(row).value('id')
                collectorNumber = calcModel.record(row).value('collector_number')
                if collectorNumber != oldColNumber:
                    colSegs.append(calcModel.record(row).value('col_seg'))
                calcModel.updateColById(None, colName, id)
                oldColNumber = collectorNumber
        self.calcModel.select()
        controller = CalculationController()
        ProgressThread(self, controller, (lambda : controller.updateValues(colSegs)))