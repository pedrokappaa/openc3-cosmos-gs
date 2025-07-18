meta:
  id: prometheus
  file-extension: prometheus
  endian: le
seq:
  - id: header
    type: header
  - id: payload
    type:
      switch-on: header.msg_type_id
      cases:
        0x00: default
        0x01: command
        0x02: beacon
        0xff: buffered
        0xfe: buffered
        0xfd: buffered
        0xfc: buffered
        0xfb: buffered
        0xfa: buffered
        0xf9: buffered
        0xf8: buffered
        0xf7: buffered
        
types:
  header:
    seq:
    - id: length
      type: u1
    - id: destination
      type: u1
    - id: node
      type: u1
    - id: identifier
      type: u1
    - id: flags
      type: u1
    - id: msg_type_id
      type: u1
  
      
  default:
    seq:
      - id: message
        type: str
        encoding: ASCII
        size-eos: true
  
  beacon:
    seq:
      - id: state_index
        type: u1
      - id: flags
        type: u1
      - id: software_error_count
        type: u2
      - id: boot_count
        type: u2
      - id: pad_byte
        type: u2
      - id: battery_voltage
        type: f4
      - id: cpu_temperature_c
        type: f4
      - id: imu_temperature_c
        type: f4
      - id: gyro_0
        type: f4
      - id: gyro_1
        type: f4
      - id: gyro_2
        type: f4
      - id: mag_0
        type: f4
      - id: mag_1
        type: f4
      - id: mag_2
        type: f4
      - id: accel_0
        type: f4
      - id: accel_1
        type: f4
      - id: accel_2
        type: f4
      - id: rssi_db
        type: f4
      - id: fei_hz
        type: f4
      - id: checksum
        type: u2
        
  buffered:
    seq:
      - id: data
        size-eos: true
  
  command:
    seq:
      - id: data
        size-eos: true