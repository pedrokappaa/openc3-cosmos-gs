# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Prometheus(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = Prometheus.Header(self._io, self, self._root)
        _on = self.header.msg_type_id
        if _on == 0:
            self.payload = Prometheus.Default(self._io, self, self._root)
        elif _on == 249:
            self.payload = Prometheus.Buffered(self._io, self, self._root)
        elif _on == 251:
            self.payload = Prometheus.Buffered(self._io, self, self._root)
        elif _on == 1:
            self.payload = Prometheus.Command(self._io, self, self._root)
        elif _on == 252:
            self.payload = Prometheus.Buffered(self._io, self, self._root)
        elif _on == 253:
            self.payload = Prometheus.Buffered(self._io, self, self._root)
        elif _on == 248:
            self.payload = Prometheus.Buffered(self._io, self, self._root)
        elif _on == 2:
            self.payload = Prometheus.Beacon(self._io, self, self._root)
        elif _on == 255:
            self.payload = Prometheus.Buffered(self._io, self, self._root)
        elif _on == 250:
            self.payload = Prometheus.Buffered(self._io, self, self._root)
        elif _on == 247:
            self.payload = Prometheus.Buffered(self._io, self, self._root)
        elif _on == 254:
            self.payload = Prometheus.Buffered(self._io, self, self._root)

    class Command(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = self._io.read_bytes_full()


    class Beacon(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.state_index = self._io.read_u1()
            self.flags = self._io.read_u1()
            self.software_error_count = self._io.read_u2le()
            self.boot_count = self._io.read_u2le()
            self.pad_byte = self._io.read_u2le()
            self.battery_voltage = self._io.read_f4le()
            self.cpu_temperature_c = self._io.read_f4le()
            self.imu_temperature_c = self._io.read_f4le()
            self.gyro_0 = self._io.read_f4le()
            self.gyro_1 = self._io.read_f4le()
            self.gyro_2 = self._io.read_f4le()
            self.mag_0 = self._io.read_f4le()
            self.mag_1 = self._io.read_f4le()
            self.mag_2 = self._io.read_f4le()
            self.accel_0 = self._io.read_f4le()
            self.accel_1 = self._io.read_f4le()
            self.accel_2 = self._io.read_f4le()
            self.rssi_db = self._io.read_f4le()
            self.fei_hz = self._io.read_f4le()
            self.checksum = self._io.read_u2le()


    class Buffered(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = self._io.read_bytes_full()


    class Default(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.message = (self._io.read_bytes_full()).decode(u"ASCII")


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u1()
            self.destination = self._io.read_u1()
            self.node = self._io.read_u1()
            self.identifier = self._io.read_u1()
            self.flags = self._io.read_u1()
            self.msg_type_id = self._io.read_u1()