import sys
import gui
import record_command as rec
from PyQt5.QtWidgets import QDialog, QApplication


class DemoForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = gui.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.cur_cmd = -1

    @staticmethod
    def do_record(second=4):
        recorder = rec.Recorder()
        return recorder.record_sec(second)

    def response(self):
        self.cur_cmd = self.do_record()
        if self.cur_cmd == 0:
            self.ui.batden_phongkhach()
        elif self.cur_cmd == 2:
            self.ui.batden_phongtam()
        elif self.cur_cmd == 4:
            self.ui.tatden_phongkhach()
        elif self.cur_cmd == 6:
            self.ui.tatden_phongtam()
        elif self.cur_cmd == 30:
            self.ui.remcua_phongngu()

