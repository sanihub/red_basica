# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flow_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 657)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.buttonBox)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.populationTab = QtWidgets.QWidget()
        self.populationTab.setObjectName("populationTab")
        self.formLayout_6 = QtWidgets.QFormLayout(self.populationTab)
        self.formLayout_6.setObjectName("formLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.populationTab)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.popWaterConsumptionStartLabel = QtWidgets.QLabel(self.groupBox)
        self.popWaterConsumptionStartLabel.setObjectName("popWaterConsumptionStartLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.popWaterConsumptionStartLabel)
        self.popWaterConsumptionStartVal = QtWidgets.QSpinBox(self.groupBox)
        self.popWaterConsumptionStartVal.setMaximum(999999999)
        self.popWaterConsumptionStartVal.setObjectName("popWaterConsumptionStartVal")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.popWaterConsumptionStartVal)
        self.popWaterConsumptionEndLabel = QtWidgets.QLabel(self.groupBox)
        self.popWaterConsumptionEndLabel.setObjectName("popWaterConsumptionEndLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.popWaterConsumptionEndLabel)
        self.popWaterConsumptionEndVal = QtWidgets.QSpinBox(self.groupBox)
        self.popWaterConsumptionEndVal.setMaximum(999999999)
        self.popWaterConsumptionEndVal.setObjectName("popWaterConsumptionEndVal")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.popWaterConsumptionEndVal)
        self.popCoefficientReturnLabel = QtWidgets.QLabel(self.groupBox)
        self.popCoefficientReturnLabel.setObjectName("popCoefficientReturnLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.popCoefficientReturnLabel)
        self.popCoefficientReturnVal = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.popCoefficientReturnVal.setMaximum(9999999999.0)
        self.popCoefficientReturnVal.setObjectName("popCoefficientReturnVal")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.popCoefficientReturnVal)
        self.formLayout_6.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.groupBox)
        self.popLayerLabel = QtWidgets.QLabel(self.populationTab)
        self.popLayerLabel.setObjectName("popLayerLabel")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.popLayerLabel)
        self.popLayerSelect = QtWidgets.QComboBox(self.populationTab)
        self.popLayerSelect.setObjectName("popLayerSelect")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.popLayerSelect)
        self.popOnlySelectedVal = QtWidgets.QCheckBox(self.populationTab)
        self.popOnlySelectedVal.setObjectName("popOnlySelectedVal")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.popOnlySelectedVal)
        self.popStartPlanLabel = QtWidgets.QLabel(self.populationTab)
        self.popStartPlanLabel.setObjectName("popStartPlanLabel")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.popStartPlanLabel)
        self.popStartPlanVal = QtWidgets.QComboBox(self.populationTab)
        self.popStartPlanVal.setObjectName("popStartPlanVal")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.popStartPlanVal)
        self.popEndPlanLabel = QtWidgets.QLabel(self.populationTab)
        self.popEndPlanLabel.setObjectName("popEndPlanLabel")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.popEndPlanLabel)
        self.popEndPlanVal = QtWidgets.QComboBox(self.populationTab)
        self.popEndPlanVal.setObjectName("popEndPlanVal")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.popEndPlanVal)
        self.tabWidget.addTab(self.populationTab, "")
        self.connectionsTab = QtWidgets.QWidget()
        self.connectionsTab.setObjectName("connectionsTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.connectionsTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.connLayerLabel = QtWidgets.QLabel(self.connectionsTab)
        self.connLayerLabel.setObjectName("connLayerLabel")
        self.verticalLayout.addWidget(self.connLayerLabel)
        self.connLayerSelect = QtWidgets.QComboBox(self.connectionsTab)
        self.connLayerSelect.setObjectName("connLayerSelect")
        self.verticalLayout.addWidget(self.connLayerSelect)
        self.connOnlySelectedVal = QtWidgets.QCheckBox(self.connectionsTab)
        self.connOnlySelectedVal.setObjectName("connOnlySelectedVal")
        self.verticalLayout.addWidget(self.connOnlySelectedVal)
        self.connNoConnectionsLabel = QtWidgets.QLabel(self.connectionsTab)
        self.connNoConnectionsLabel.setObjectName("connNoConnectionsLabel")
        self.verticalLayout.addWidget(self.connNoConnectionsLabel)
        self.connNoConnections = QtWidgets.QComboBox(self.connectionsTab)
        self.connNoConnections.setObjectName("connNoConnections")
        self.verticalLayout.addWidget(self.connNoConnections)
        self.connNoConnectionsEndPlanLabel = QtWidgets.QLabel(self.connectionsTab)
        self.connNoConnectionsEndPlanLabel.setObjectName("connNoConnectionsEndPlanLabel")
        self.verticalLayout.addWidget(self.connNoConnectionsEndPlanLabel)
        self.connNoConnectionsEndPlan = QtWidgets.QComboBox(self.connectionsTab)
        self.connNoConnectionsEndPlan.setObjectName("connNoConnectionsEndPlan")
        self.verticalLayout.addWidget(self.connNoConnectionsEndPlan)
        self.groupBox_2 = QtWidgets.QGroupBox(self.connectionsTab)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.connGrowthRateLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connGrowthRateLabel.setObjectName("connGrowthRateLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.connGrowthRateLabel)
        self.connEconomyRegionLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connEconomyRegionLabel.setObjectName("connEconomyRegionLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.connEconomyRegionLabel)
        self.connStartConsumptionLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connStartConsumptionLabel.setObjectName("connStartConsumptionLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.connStartConsumptionLabel)
        self.connEndConsumptionLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connEndConsumptionLabel.setObjectName("connEndConsumptionLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.connEndConsumptionLabel)
        self.connOcupancyRateStartLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connOcupancyRateStartLabel.setObjectName("connOcupancyRateStartLabel")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.connOcupancyRateStartLabel)
        self.connOcupancyRateEndLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connOcupancyRateEndLabel.setObjectName("connOcupancyRateEndLabel")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.connOcupancyRateEndLabel)
        self.connReturnCoefficientLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connReturnCoefficientLabel.setObjectName("connReturnCoefficientLabel")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.connReturnCoefficientLabel)
        self.connGrowthRateVal = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.connGrowthRateVal.setObjectName("connGrowthRateVal")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.connGrowthRateVal)
        self.connEconomyRegionVal = QtWidgets.QSpinBox(self.groupBox_2)
        self.connEconomyRegionVal.setObjectName("connEconomyRegionVal")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.connEconomyRegionVal)
        self.connStartConsumptionVal = QtWidgets.QSpinBox(self.groupBox_2)
        self.connStartConsumptionVal.setObjectName("connStartConsumptionVal")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.connStartConsumptionVal)
        self.connEndConsumptionVal = QtWidgets.QSpinBox(self.groupBox_2)
        self.connEndConsumptionVal.setObjectName("connEndConsumptionVal")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.connEndConsumptionVal)
        self.connOcupancyRateStartVal = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.connOcupancyRateStartVal.setObjectName("connOcupancyRateStartVal")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.connOcupancyRateStartVal)
        self.connOcupancyRateEndVal = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.connOcupancyRateEndVal.setObjectName("connOcupancyRateEndVal")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.connOcupancyRateEndVal)
        self.connReturnCoefficientVal = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.connReturnCoefficientVal.setObjectName("connReturnCoefficientVal")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.connReturnCoefficientVal)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.connectionsTab, "")
        self.flowTab = QtWidgets.QWidget()
        self.flowTab.setObjectName("flowTab")
        self.formLayout_5 = QtWidgets.QFormLayout(self.flowTab)
        self.formLayout_5.setObjectName("formLayout_5")
        self.flowLabel = QtWidgets.QLabel(self.flowTab)
        self.flowLabel.setObjectName("flowLabel")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.flowLabel)
        self.flowSelectedVal = QtWidgets.QCheckBox(self.flowTab)
        self.flowSelectedVal.setObjectName("flowSelectedVal")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.flowSelectedVal)
        self.label_22 = QtWidgets.QLabel(self.flowTab)
        self.label_22.setObjectName("label_22")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.label_22)
        self.flowCurrentStartPlan = QtWidgets.QComboBox(self.flowTab)
        self.flowCurrentStartPlan.setObjectName("flowCurrentStartPlan")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.flowCurrentStartPlan)
        self.label_23 = QtWidgets.QLabel(self.flowTab)
        self.label_23.setObjectName("label_23")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label_23)
        self.flowProjected = QtWidgets.QComboBox(self.flowTab)
        self.flowProjected.setObjectName("flowProjected")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.flowProjected)
        self.groupBox_3 = QtWidgets.QGroupBox(self.flowTab)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_4.setObjectName("formLayout_4")
        self.flowProjectionRateLabel = QtWidgets.QLabel(self.groupBox_3)
        self.flowProjectionRateLabel.setObjectName("flowProjectionRateLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.flowProjectionRateLabel)
        self.flowProjectionRateVal = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.flowProjectionRateVal.setObjectName("flowProjectionRateVal")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.flowProjectionRateVal)
        self.formLayout_5.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.groupBox_3)
        self.flowLayer = QtWidgets.QComboBox(self.flowTab)
        self.flowLayer.setObjectName("flowLayer")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.flowLayer)
        self.tabWidget.addTab(self.flowTab, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)
        self.manholeLayerLabel = QtWidgets.QLabel(Dialog)
        self.manholeLayerLabel.setObjectName("manholeLayerLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.manholeLayerLabel)
        self.influenceAreaBufferLabel = QtWidgets.QLabel(Dialog)
        self.influenceAreaBufferLabel.setObjectName("influenceAreaBufferLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.influenceAreaBufferLabel)
        self.influenceAreaBufferVal = QtWidgets.QSpinBox(Dialog)
        self.influenceAreaBufferVal.setObjectName("influenceAreaBufferVal")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.influenceAreaBufferVal)
        self.manholeOnlySelectedLabel = QtWidgets.QLabel(Dialog)
        self.manholeOnlySelectedLabel.setObjectName("manholeOnlySelectedLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.manholeOnlySelectedLabel)
        self.manholeOnlySelectedVal = QtWidgets.QCheckBox(Dialog)
        self.manholeOnlySelectedVal.setText("")
        self.manholeOnlySelectedVal.setObjectName("manholeOnlySelectedVal")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.manholeOnlySelectedVal)
        self.manholeLayerSelect = QtWidgets.QComboBox(Dialog)
        self.manholeLayerSelect.setObjectName("manholeLayerSelect")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.manholeLayerSelect)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Atribución de Caudales por Área de Influencia"))
        self.popWaterConsumptionStartLabel.setText(_translate("Dialog", "Dotación de inicio de plan (l/hab.día)"))
        self.popWaterConsumptionEndLabel.setText(_translate("Dialog", "Dotación de final de plan (l/hab.día)"))
        self.popCoefficientReturnLabel.setText(_translate("Dialog", "Coeficiente de retorno [C]"))
        self.popLayerLabel.setText(_translate("Dialog", "Seleccione la capa"))
        self.popOnlySelectedVal.setText(_translate("Dialog", "Sólo seleccionados"))
        self.popStartPlanLabel.setText(_translate("Dialog", "Población inicio de plan"))
        self.popEndPlanLabel.setText(_translate("Dialog", "Población fin de plan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.populationTab), _translate("Dialog", "Población"))
        self.connLayerLabel.setText(_translate("Dialog", "Seleccione la capa"))
        self.connOnlySelectedVal.setText(_translate("Dialog", "Sólo seleccionados"))
        self.connNoConnectionsLabel.setText(_translate("Dialog", "Cantidad de conexiones inicio de plan"))
        self.connNoConnectionsEndPlanLabel.setText(_translate("Dialog", "Cantidad de conexiones fin de plan (opcional)"))
        self.connGrowthRateLabel.setText(_translate("Dialog", "Tasa de crecimiento"))
        self.connEconomyRegionLabel.setText(_translate("Dialog", "Cantidad de economía por conexión"))
        self.connStartConsumptionLabel.setText(_translate("Dialog", "Dotación de inicio de plan (l/hab.día)"))
        self.connEndConsumptionLabel.setText(_translate("Dialog", "Dotación de final de plan (l/hab.día)"))
        self.connOcupancyRateStartLabel.setText(_translate("Dialog", "Tasa de ocupación inicio de plan (hab/vivienda)"))
        self.connOcupancyRateEndLabel.setText(_translate("Dialog", "Tasa de ocupación final de plan (hab/vivienda)"))
        self.connReturnCoefficientLabel.setText(_translate("Dialog", "Coeficiente de retorno"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.connectionsTab), _translate("Dialog", "Conexiones"))
        self.flowLabel.setText(_translate("Dialog", "Seleccione la capa"))
        self.flowSelectedVal.setText(_translate("Dialog", "Sólo seleccionados"))
        self.label_22.setText(_translate("Dialog", "Caudal actual (inicio de plan)"))
        self.label_23.setText(_translate("Dialog", "Caudal proyectado (opcional)"))
        self.flowProjectionRateLabel.setText(_translate("Dialog", "Tasa de proyección"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.flowTab), _translate("Dialog", "Caudal"))
        self.manholeLayerLabel.setText(_translate("Dialog", "Capa de caja de inspección"))
        self.influenceAreaBufferLabel.setText(_translate("Dialog", "Buffer del área de influencia (% de extensión)"))
        self.manholeOnlySelectedLabel.setText(_translate("Dialog", "Sólo seleccionados"))
