from qgis.core import QgsProject, QgsWkbTypes, QgsProcessingFeedback, QgsVectorLayer
from PyQt5.QtWidgets import QDialog
import processing
from .ui.FlowDialogUi import Ui_Dialog

class FlowView(QDialog, Ui_Dialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.layers = [layer for layer in QgsProject.instance().mapLayers().values()]
        self.type = 'population'
        self.selected_layer = None

        layer_list = []
        self.popLayerSelect.addItem("")
        self.connLayerSelect.addItem("")
        self.flowLayer.addItem("")
        self.manholeLayerSelect.addItem("")
        for layer in self.layers:
            if (layer.type() == layer.VectorLayer):
                if layer.geometryType() == QgsWkbTypes.PointGeometry:
                  layer_list.append(layer.name())
        self.popLayerSelect.addItems(layer_list)
        self.connLayerSelect.addItems(layer_list)
        self.flowLayer.addItems(layer_list)
        self.manholeLayerSelect.addItems(layer_list)

        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.popLayerSelect.currentIndexChanged.connect(lambda index, tab='population': self.updateAttributes(index, tab))
        self.connLayerSelect.currentIndexChanged.connect(lambda index, tab='connection': self.updateAttributes(index, tab))
        self.flowLayer.currentIndexChanged.connect(lambda index, tab='flow': self.updateAttributes(index, tab))

        self.connNoConnectionsEndPlan.currentIndexChanged.connect(lambda index, field='connNoConnectionsEndPlan': self.blockFields(index, field))
        self.flowProjected.currentIndexChanged.connect(lambda index, field='flowProjected': self.blockFields(index, field))

        self.buttonBox.accepted.connect(self.create_voronoi)
    
    def blockFields(self, index, field):
      selected_field = self.connNoConnectionsEndPlan.itemText(index) if field == 'connNoConnectionsEndPlan' else self.flowProjected.itemText(index)
      if selected_field != "":
        if field == 'connNoConnectionsEndPlan':
          self.connGrowthRateVal.setReadOnly(True)
          self.connGrowthRateVal.setStyleSheet("background-color: rgb(238, 238, 236);")
        if field == 'flowProjected':
          self.flowProjectionRateVal.setReadOnly(True)
          self.flowProjectionRateVal.setStyleSheet("background-color: rgb(238, 238, 236);")
      else:
        if field == 'connNoConnectionsEndPlan':
          self.connGrowthRateVal.setReadOnly(False)
          self.connGrowthRateVal.setStyleSheet("")
        if field == 'flowProjected':
          self.flowProjectionRateVal.setReadOnly(False)
          self.flowProjectionRateVal.setStyleSheet("")

    def tab_changed(self, index):
        if index == 0:
           self.type = 'population'
        elif index == 1:
           self.type = 'connections'
        else:
           self.type = 'flow'

    def updateAttributes(self, index, tab):
        self.set_layer(index)

        if self.selected_layer != None:
          field_names = [field.name() for field in self.selected_layer.fields()]
          
          if tab == 'population':
            self.popStartPlanVal.clear()
            self.popEndPlanVal.clear()
            self.popStartPlanVal.addItems(field_names)
            self.popEndPlanVal.addItems(field_names)

          if tab == 'connection':
            self.connNoConnections.clear()
            self.connNoConnectionsEndPlan.clear()
            self.connNoConnections.addItems(field_names)
            self.connNoConnectionsEndPlan.addItem("")
            self.connNoConnectionsEndPlan.addItems(field_names)

          if tab == 'flow':
            self.flowCurrentStartPlan.clear()
            self.flowProjected.clear()
            self.flowCurrentStartPlan.addItems(field_names)
            self.flowProjected.addItem("")
            self.flowProjected.addItems(field_names)

        else:
          if tab == 'population':
            self.popStartPlanVal.clear()
            self.popEndPlanVal.clear()
          if tab == 'connection':
            self.connNoConnections.clear()
            self.connNoConnectionsEndPlan.clear()
          if tab == 'flow':
            self.flowCurrentStartPlan.clear()
            self.flowProjected.clear()

    def calculate_flow(self):
      if self.type == 'population':
        initial_consumption = self.popWaterConsumptionStartVal.value()
        final_consumption =  self.popWaterConsumptionEndVal.value()
        return_coeff = self.popCoefficientReturnVal.value()
        initial_selected = self.popStartPlanVal.currentText()
        final_selected = self.popEndPlanVal.currentText()
        for feature in self.selected_layer.getFeatures():
          initial_population = feature[initial_selected]
          final_population = feature[final_selected]
          initial_flow = initial_consumption * initial_population * return_coeff / 86400
          final_flow = final_consumption * final_population * return_coeff / 86400
          #TODO set to layer the initial_flow and final_flow

      elif self.type == 'connections':
        grow_rate = self.connGrowthRateVal.value()
        economy_conn =  self.connEconomyConnVal.value()
        initial_consumption = self.connStartConsumptionVal.value()
        end_consumption = self.connEndConsumptionVal.value()
        initial_occupancy_rate = self.connOcupancyRateStartVal.value()
        end_occupancy_rate = self.connOcupancyRateEndVal.value()
        return_coeff = self.connReturnCoefficientVal.value()
        no_conn_selected = self.connNoConnections.currentText()
        no_conn_end_selected = self.connNoConnectionsEndPlan.currentText()
        for feature in self.selected_layer.getFeatures():
          no_connections = feature[no_conn_selected]
          initial_flow = initial_consumption * no_connections * economy_conn * initial_occupancy_rate * return_coeff / 86400

          if no_conn_end_selected != "":
            no_end_conn = feature[no_conn_end_selected]
            final_flow = end_consumption * no_end_conn * economy_conn * end_occupancy_rate * return_coeff / 86400
          else:
            final_flow = end_consumption * (no_connections * grow_rate) * economy_conn * end_occupancy_rate * return_coeff / 86400
          #TODO set to layer the initial_flow and final_flow

      else:
        flow_start_selected = self.flowCurrentStartPlan.currentText()
        flow_projected = self.flowProjected.currentText()
        for feature in self.selected_layer.getFeatures():
          initial_flow = feature[flow_start_selected]

          if flow_projected != "":
            final_flow = feature[flow_projected]
          else:
            flow_projection_rate = self.flowProjectionRateVal.value()
            final_flow = initial_flow * flow_projection_rate
          #TODO set to layer the initial_flow and final_flow

    def set_layer(self, index):
      if self.type == 'population':
        selected_layer_name = self.popLayerSelect.itemText(index)
      elif self.type == 'connections':
        selected_layer_name = self.connLayerSelect.itemText(index)
      else:
        selected_layer_name = self.flowLayer.itemText(index)

      self.selected_layer = next((layer for layer in self.layers if layer.name() == selected_layer_name), None)

    def create_voronoi(self):
      selected_layer_name = self.manholeLayerSelect.currentText()
      selected_layer = next((layer for layer in self.layers if layer.name() == selected_layer_name), None)
      buffer = self.influenceAreaBufferVal.value()
      if selected_layer:

        input_layer = selected_layer.source()

        #TODO change output layer name
        output_layer = "TEMPORARY_OUTPUT"
        parameters = {
            'BUFFER': buffer,
            'INPUT': input_layer,
            'OUTPUT': output_layer
        }

        feedback = QgsProcessingFeedback()
        result = processing.run("qgis:voronoipolygons", parameters, feedback=feedback)

        output_layer = result['OUTPUT']
        QgsProject.instance().addMapLayer(output_layer)
      else:
          print("Error: No se pudo encontrar la capa seleccionada")

