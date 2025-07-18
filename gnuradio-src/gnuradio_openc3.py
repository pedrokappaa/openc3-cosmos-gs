#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Interfacing with OpenC3 COSMOS
# Author: Pedro Andrade
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import gr, pdu
from gnuradio import network
from gnuradio import pdu
import gnuradio_openc3_epy_block_0 as epy_block_0  # embedded python block



from gnuradio import qtgui

class gnuradio_openc3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Interfacing with OpenC3 COSMOS", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Interfacing with OpenC3 COSMOS")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "gnuradio_openc3")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.SAMPLE_RATE = SAMPLE_RATE = 5000000000
        self.ON_SIGHT = ON_SIGHT = 0
        self.FREQ_TX = FREQ_TX = 2000000
        self.FREQ_RX = FREQ_RX = 1000000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            SAMPLE_RATE, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            SAMPLE_RATE, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.pdu_tagged_stream_to_pdu_0_0 = pdu.tagged_stream_to_pdu(gr.types.byte_t, '')
        self.pdu_pdu_to_stream_x_0 = pdu.pdu_to_stream_b(pdu.EARLY_BURST_APPEND, 64)
        self.network_socket_pdu_0 = network.socket_pdu('TCP_SERVER', '', '52001', 256, False)
        self.epy_block_0 = epy_block_0.command_parser()
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, SAMPLE_RATE,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, SAMPLE_RATE,True)
        self.blocks_selector_0_0_0 = blocks.selector(gr.sizeof_gr_complex*1,0,int(ON_SIGHT))
        self.blocks_selector_0_0_0.set_enabled(True)
        self.blocks_selector_0_0 = blocks.selector(gr.sizeof_gr_complex*1,0,int(ON_SIGHT))
        self.blocks_selector_0_0.set_enabled(True)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_msgpair_to_var_0_0_0 = blocks.msg_pair_to_var(self.set_ON_SIGHT)
        self.blocks_msgpair_to_var_0_0 = blocks.msg_pair_to_var(self.set_FREQ_RX)
        self.blocks_msgpair_to_var_0 = blocks.msg_pair_to_var(self.set_FREQ_TX)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'gnuradio-src/packet.bin', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.intern("pkt"))
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'gnuradio-src/tcp_dump.txt', True)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(SAMPLE_RATE, analog.GR_COS_WAVE, FREQ_TX, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(SAMPLE_RATE, analog.GR_COS_WAVE, FREQ_RX, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.epy_block_0, 'out_FREQ_TX'), (self.blocks_msgpair_to_var_0, 'inpair'))
        self.msg_connect((self.epy_block_0, 'out_FREQ_RX'), (self.blocks_msgpair_to_var_0_0, 'inpair'))
        self.msg_connect((self.epy_block_0, 'out_ON_SIGHT'), (self.blocks_msgpair_to_var_0_0_0, 'inpair'))
        self.msg_connect((self.network_socket_pdu_0, 'pdus'), (self.epy_block_0, 'in'))
        self.msg_connect((self.network_socket_pdu_0, 'pdus'), (self.pdu_pdu_to_stream_x_0, 'pdus'))
        self.msg_connect((self.pdu_tagged_stream_to_pdu_0_0, 'pdus'), (self.network_socket_pdu_0, 'pdus'))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.pdu_tagged_stream_to_pdu_0_0, 0))
        self.connect((self.blocks_selector_0_0, 0), (self.blocks_null_sink_0_0, 0))
        self.connect((self.blocks_selector_0_0, 1), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_selector_0_0_0, 0), (self.blocks_null_sink_0_0_0, 0))
        self.connect((self.blocks_selector_0_0_0, 1), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_selector_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_selector_0_0_0, 0))
        self.connect((self.pdu_pdu_to_stream_x_0, 0), (self.blocks_file_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "gnuradio_openc3")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_SAMPLE_RATE(self):
        return self.SAMPLE_RATE

    def set_SAMPLE_RATE(self, SAMPLE_RATE):
        self.SAMPLE_RATE = SAMPLE_RATE
        self.analog_sig_source_x_0.set_sampling_freq(self.SAMPLE_RATE)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.SAMPLE_RATE)
        self.blocks_throttle_0.set_sample_rate(self.SAMPLE_RATE)
        self.blocks_throttle_0_0.set_sample_rate(self.SAMPLE_RATE)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.SAMPLE_RATE)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.SAMPLE_RATE)

    def get_ON_SIGHT(self):
        return self.ON_SIGHT

    def set_ON_SIGHT(self, ON_SIGHT):
        self.ON_SIGHT = ON_SIGHT
        self.blocks_selector_0_0.set_output_index(int(self.ON_SIGHT))
        self.blocks_selector_0_0_0.set_output_index(int(self.ON_SIGHT))

    def get_FREQ_TX(self):
        return self.FREQ_TX

    def set_FREQ_TX(self, FREQ_TX):
        self.FREQ_TX = FREQ_TX
        self.analog_sig_source_x_0_0.set_frequency(self.FREQ_TX)

    def get_FREQ_RX(self):
        return self.FREQ_RX

    def set_FREQ_RX(self, FREQ_RX):
        self.FREQ_RX = FREQ_RX
        self.analog_sig_source_x_0.set_frequency(self.FREQ_RX)




def main(top_block_cls=gnuradio_openc3, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
