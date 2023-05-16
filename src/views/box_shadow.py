from PySide6.QtGui import QColor, QPainter, QBrush, QPen, QPalette, QStandardItemModel, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QGraphicsEffect, QGraphicsBlurEffect
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class BoxShadow:
    def __init__(self, radius=10, color=QColor(0, 0, 0, 100), offset=(5, 5)):
        self.effect = QGraphicsBlurEffect()
        self.effect.setBlurRadius(radius)
        self.effect.setColor(color)

        self.offset = offset

    def get_effect(self):
        return self.effect

    def set_radius(self, radius):
        self.effect.setBlurRadius(radius)

    def set_color(self, color):
        self.effect.setColor(color)

    def set_offset(self, offset):
        self.offset = offset

    def draw(self, painter):
        if self.offset != (0, 0):
            shadow = QPainter(self.effect.pixmap())
            shadow.setCompositionMode(QPainter.CompositionMode_Source)
            shadow.fillRect(self.effect.pixmap().rect(), QColor(0, 0, 0, 0))
            shadow.setCompositionMode(QPainter.CompositionMode_SourceOver)
            shadow.setPen(Qt.NoPen)
            shadow.setBrush(QBrush(self.effect.color()))
            shadow.drawRoundedRect(self.effect.pixmap().rect().translated(*self.offset), self.effect.blurRadius(), self.effect.blurRadius())
            shadow.end()
        self.effect.draw(painter, QStyleOptionGraphicsItem(), None)