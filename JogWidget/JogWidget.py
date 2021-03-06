# rasPyCNCController
# Copyright 2016 Francesco Santini <francesco.santini@gmail.com>
#
# This file is part of rasPyCNCController.
#
# rasPyCNCController is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rasPyCNCController is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rasPyCNCController.  If not, see <http://www.gnu.org/licenses/>.

import os.path
import sys
import time

from PySide.QtCore import *
from PySide.QtGui import *

from Joggers.JoyJogThread import JoyJogThread
from Joggers.KeyboardJogger import KeyboardJogger
from gcode.GCodeLoader import GCodeLoader
from gcode.JogHelper import JogHelper
from jogWidget_ui import Ui_joyWidget

from string_format import config_string_format

class JogWidget(Ui_joyWidget, QWidget):

    run_event = Signal()
    load_event = Signal()
    error_event = Signal(object)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        # convert placeholders into config values for the widgets
        self.RunButton.setText(config_string_format(self.RunButton.text()))
        self.LoadButton.setText(config_string_format(self.LoadButton.text()))
        self.label.setText(config_string_format(self.label.text()))

        self.RunButton.clicked.connect(self.runEvent)
        self.LoadButton.clicked.connect(self.loadEvent)

        self.joyJog = JoyJogThread()
        self.keyJog = KeyboardJogger()
        self.grblWriter = None
        self.jogHelper = JogHelper()

        # propagate a GRBL error
        self.jogHelper.error_event.connect(lambda err: self.error_event.emit(err))
        self.setPosition([0,0,0])
        self.disableControls()
        self.isFileLoaded = False
        self.joggers = []

        self.installJogger(self.joyJog)
        self.installJogger(self.keyJog)

    def installJogger(self, jogger):
        jogger.install(self)
        jogger.exit_event.connect(self.joyExitEvent)
        jogger.relative_move_event.connect(self.relativeMove)
        jogger.absolute_move_event.connect(self.absoluteMove)
        jogger.home_update_event.connect(self.homeUpdate)
        self.joggers.append(jogger)


    def relativeMove(self, xyz, feed):
        if self.jogHelper.isBusy(): return
        if feed is not None and feed <= 0: feed = None
        self.jogHelper.relative_move(xyz, feed)

    def absoluteMove(self, xyz, feed):
        if self.jogHelper.isBusy(): return
        if feed is not None and feed <= 0: feed=None
        self.jogHelper.absolute_move(xyz, feed)

    def homeUpdate(self, xyz):
        self.jogHelper.home_update(xyz)

    def setGrbl(self, grblWriter):
        self.grblWriter = grblWriter
        self.grblWriter.position_updated.connect(self.setPosition)
        self.jogHelper.setGrbl(grblWriter)

    def fileLoaded(self):
        self.isFileLoaded = True
        self.gcode = self.loader.gcode
        self.times = self.loader.times
        self.totalTime = self.loader.totalTime
        self.bBox = self.loader.bBox
        self.setBBox(self.loader.bBox)
        self.setEstTime(self.totalTime)
        self.RunButton.setEnabled(True)
        self.BBOxGroup.setEnabled(True)
        self.estTimeGroup.setEnabled(True)
        self.fileLabel.setText(os.path.basename(self.loader.file))

    def loadError(self, err):
        self.fileLabel.setText("Error loading: %s" % err)

    def loadFile(self, filename):
        self.file = filename
        self.isFileLoaded = False
        self.disableControls()
        self.loader = GCodeLoader()
        self.loader.g0_feed = self.grblWriter.g0_feed
        self.loader.load_finished.connect(self.fileLoaded)
        self.loader.load_error.connect(self.loadError)
        self.loader.load(filename)
        self.fileLabel.setText("Loading...")

    def displayError(self, err):
        if self.isFileLoaded:
            self.fileLabel.setText("Error: %s (%s)" % (err, self.file))
        else:
            self.fileLabel.setText("Error: %s" % err)

    def disableControls(self):
        self.RunButton.setEnabled(False)
        self.BBOxGroup.setEnabled(False)
        self.estTimeGroup.setEnabled(False)
        self.setBBox(None)
        self.setEstTime(None)

    def setBBox(self, BBox):
        if BBox == None:
            self.xMaxBBoxTxt.setText("")
            self.yMaxBBoxTxt.setText("")
            self.zMaxBBoxTxt.setText("")

            self.xMinBBoxTxt.setText("")
            self.yMinBBoxTxt.setText("")
            self.zMinBBoxTxt.setText("")
            return

        self.xMinBBoxTxt.setText("%.1f" % BBox[0][0])
        self.yMinBBoxTxt.setText("%.1f" % BBox[0][1])
        self.zMinBBoxTxt.setText("%.1f" % BBox[0][2])

        self.xMaxBBoxTxt.setText("%.1f" % BBox[1][0])
        self.yMaxBBoxTxt.setText("%.1f" % BBox[1][1])
        self.zMaxBBoxTxt.setText("%.1f" % BBox[1][2])

    def setEstTime(self, timeSec):
        if timeSec == None:
            timeSec = 0
        hours = int(timeSec / 3600)
        mins = int((timeSec - hours*3600)/60)
        secs = timeSec - hours*3600 - mins*60

        self.estTimeTxt.setText("%02d:%02d:%02d" % (hours, mins, secs))

    def startJoggers(self):
        for jogger in self.joggers:
            jogger.start()

    def stopJoggers(self):
        for jogger in self.joggers:
            jogger.stop()

    def setPosition(self, posXYZ):
        self.xPosTxt.setText("%.1f" % posXYZ[0])
        self.yPosTxt.setText("%.1f" % posXYZ[1])
        self.zPosTxt.setText("%.1f" % posXYZ[2])

    def runEvent(self):
        self.stopJoggers()
        self.run_event.emit()

    def loadEvent(self):
        self.stopJoggers()
        self.load_event.emit()

    def joyExitEvent(self, exitCondition):
        # joy is stopped now!
        if exitCondition == True:
            # Run was pressed
            if self.RunButton.isEnabled():
                self.runEvent()
            else:
                #runbutton is not enabled: restart the joy
                # give sime time to the thread to exit and then restart it
                time.sleep(0.1)
                self.startJoggers()
        else:
            self.loadEvent()

class GrblWriter_debug:
    def do_command(self, cmd, wait = False):
        print(cmd)
        time.sleep(0.1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    grbl = GrblWriter_debug()
    window = JogWidget(grbl)
    window.destroyed.connect(window.stopJoggers)
    window.show()
    sys.exit(app.exec_())