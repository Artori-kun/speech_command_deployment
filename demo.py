import sys
import gui
import record_command as rec
from PyQt5.QtWidgets import QDialog, QApplication


class DemoForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = gui.Ui_Dialog()
        self.ui.setupUi(self)
        self.cur_cmd = -1
        self.recorder = rec.Recorder()
        self.ui.btn_ghiam.clicked.connect(lambda: self.response())
        # self.show()

    # @staticmethod
    # def do_record(second=4):
    #     recorder = rec.Recorder()
    #     return recorder.record_sec(second)

    def response(self):
        self.cur_cmd = self.recorder.record_sec()
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
        else:
            print("Nothing happened")


app = QApplication(sys.argv)
f = DemoForm()
f.show()
sys.exit(app.exec_())
