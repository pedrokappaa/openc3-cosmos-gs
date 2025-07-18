import numpy as np
from gnuradio import gr
import pmt

class command_parser(gr.basic_block):
    def __init__(self):
        gr.basic_block.__init__(self,
            name="Command parser",
            in_sig=[],
            out_sig=[])
        self.message_port_register_in(pmt.intern("in"))
        self.message_port_register_out(pmt.intern("out_ON_SIGHT"))
        self.message_port_register_out(pmt.intern("out_FREQ_RX"))
        self.message_port_register_out(pmt.intern("out_FREQ_TX"))
        self.set_msg_handler(pmt.intern("in"), self.handle_msg)

    def handle_msg(self, msg_pdu):
        data = pmt.cdr(msg_pdu)

        if pmt.is_u8vector(data):
            msg = bytes(pmt.u8vector_elements(data)).decode("utf-8").strip()

            if msg == "aos":
                self.publish_var("ON_SIGHT", 1)

            elif msg == "los":
                self.publish_var("ON_SIGHT", 0)

            elif msg.startswith("freq_rx"):
                try:
                    _, value = msg.split()
                    freq = int(value)
                    self.publish_var("FREQ_RX", freq)
                except Exception as e:
                    print("Error parsing freq_rx:", e)

            elif msg.startswith("freq_tx"):
                try:
                    _, value = msg.split()
                    freq = int(value)
                    self.publish_var("FREQ_TX", freq)
                except Exception as e:
                    print("Error parsing freq_tx:", e)

    def publish_var(self, key_str, val_int):
        key = pmt.intern(key_str)
        val = pmt.from_long(val_int)
        pair = pmt.cons(key, val)
        self.message_port_pub(pmt.intern(f"out_{key_str}"), pair)
        print(f"{key_str} : {val_int}")
