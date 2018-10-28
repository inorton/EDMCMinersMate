"""
The "Miners Mate" Plugin
"""
import Tkinter as tk
import sys

this = sys.modules[__name__]  # For holding module globals


class MinersMate(object):
    def __init__(self):
        self.mined = 0

    def reset(self):
        self.mined = 0

    def collect(self):
        self.mined += 1
        self.update_window()

    def update_window(self):
        msg = "{}".format(self.mined)
        self.count_widget.after(0, self.count_widget.config, {"text": msg})


def plugin_start():
    mate = MinersMate()
    this.mate = mate


def plugin_app(parent):
    """
    Create a pair of TK widgets for the EDMC main window
    """
    mate = this.mate

    frame = tk.Frame(parent)

    mate.count_widget = tk.Label(
        frame,
        text="...",
        justify=tk.RIGHT)
    count_label = tk.Label(frame, text="Mined Cargo:", justify=tk.LEFT)
    count_label.grid(row=0, column=0, sticky=tk.W)
    mate.count_widget.grid(row=0, column=2, sticky=tk.E)

    reset_btn = tk.Button(frame, text="Reset", command=mate.reset)
    reset_btn.grid(row=0, column=1, sticky=tk.W)

    frame.columnconfigure(1, weight=1)

    mate.update_window()
    return frame


def journal_entry(cmdr, system, station, entry, state):
    """
    Process a journal event
    :param cmdr:
    :param system:
    :param station:
    :param entry:
    :param state:
    :return:
    """
    if "event" in entry:
        if "MiningRefined" in entry["event"]:
            this.mate.collect()

