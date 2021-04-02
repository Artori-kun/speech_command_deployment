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
        if self.cur_cmd == 0 or self.cur_cmd == 13:
            self.ui.batden_phongkhach(None)
        elif self.cur_cmd == 2 or self.cur_cmd == 15:
            self.ui.batden_phongtam(None)
        elif self.cur_cmd == 4 or self.cur_cmd == 17:
            self.ui.tatden_phongkhach(None)
        elif self.cur_cmd == 6 or self.cur_cmd == 19:
            self.ui.tatden_phongtam(None)
        elif self.cur_cmd == 30 or self.cur_cmd == 37:
            self.ui.remcua_dong(None)
        elif self.cur_cmd == 33 or self.cur_cmd == 39:
            self.ui.remcua_mo(None)
        elif self.cur_cmd == 8:
            self.ui.den_phongtam_sanghon(None)
        elif self.cur_cmd == 9:
            self.ui.den_phongkhach_toihon(None)
        elif self.cur_cmd == 21:
            self.ui.tangdosang_denphongkhach(None)
        elif self.cur_cmd == 24:
            self.ui.tangdosang_denphongtam(None)
        elif self.cur_cmd == 25:
            self.ui.giamdosang_denphongkhach(None)
        elif self.cur_cmd == 28:
            self.ui.giamdosang_denphongtam(None)
        elif self.cur_cmd == 54:
            self.ui.denphongkhach_chuyenmaudo(None)
        elif self.cur_cmd == 55:
            self.ui.denphongkhach_chuyenmauxanh(None)
        elif self.cur_cmd == 56:
            self.ui.denphongkhach_chuyenmautim(None)
        elif self.cur_cmd == 57:
            self.ui.denphongkhach_chuyenmautrang(None)
        elif self.cur_cmd == 66:
            self.ui.cuaphongbep_dong(None)
        elif self.cur_cmd == 70:
            self.ui.cuaphongbep_mo(None)
        else:
            print("Nothing happened")


app = QApplication(sys.argv)
f = DemoForm()
f.show()
sys.exit(app.exec_())
